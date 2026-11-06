"""
Combat attack processing logic.

Handles attack validation, damage application, and attack event publishing.
"""

from typing import TYPE_CHECKING, Protocol, cast
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from server.config import get_config
from server.exceptions import DatabaseError
from server.game.player_registry import PlayerNotFoundError
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.models.player_dp import dp_of, set_to
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.services.player_health_service import PlayerHealthService
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.player_registry import PlayerRegistry

logger = get_logger(__name__)

# RuntimeError: a commit can surface as one, and a LockOrderError (a unit that didn't take this player) is one.
_PLAYER_DP_ERRORS: tuple[type[Exception], ...] = (SQLAlchemyError, DatabaseError, OSError, RuntimeError)


class _AppStateWithConnectionManager(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """FastAPI app.state surface used to resolve ConnectionManager."""

    connection_manager: object | None


class _AppWithState(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal FastAPI app surface attached to AppConfig._app_instance."""

    state: _AppStateWithConnectionManager


class _CombatAttackService(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """CombatService surface required by CombatAttackHandler."""

    async def get_combat_by_participant(self, participant_id: UUID) -> CombatInstance | None: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


def _connection_manager_for_grace_check() -> object | None:
    """Resolve connection_manager from config app instance for login grace checks."""
    config = get_config()
    app = cast(_AppWithState | None, getattr(config, "_app_instance", None))
    if app is None:
        return None
    return app.state.connection_manager


def _player_damage_blocked_by_grace(target: CombatParticipant, damage: int) -> bool:
    """Return True when login grace period blocks damage to a player target."""
    if target.participant_type != CombatParticipantType.PLAYER:
        return False
    try:
        connection_manager = _connection_manager_for_grace_check()
        if connection_manager and is_player_in_login_grace_period(target.participant_id, connection_manager):
            logger.info(
                "Damage blocked - target in login grace period",
                target_id=target.participant_id,
                target_name=target.name,
                damage=damage,
            )
            return True
    except (AttributeError, ImportError, TypeError, ValueError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Fail-open behavior requires catching all exceptions
        logger.debug("Could not check login grace period for damage", target_id=target.participant_id, error=str(e))
    return False


class CombatAttackHandler:
    """Handles combat attack processing and damage application."""

    def __init__(self, combat_service: _CombatAttackService) -> None:
        """
        Initialize the attack handler.

        Args:
            combat_service: Reference to the parent CombatService
        """
        self._combat_service: _CombatAttackService = combat_service

    def _validate_attack(self, combat: CombatInstance, _is_initial_attack: bool) -> None:
        """Validate that attack is allowed."""
        if combat.status != CombatStatus.ACTIVE:
            raise ValueError("Combat is not active")

        # In round-based combat, all participants act each round, so turn validation
        # is not needed. Attacks can happen anytime during a round.
        # Note: _is_initial_attack is kept for backward compatibility but not used for validation

    def _cap_damage_for_no_death_room(
        self, target: CombatParticipant, damage: int, combat: CombatInstance | None
    ) -> tuple[int, bool]:
        """Cap damage in no_death rooms; return (damage, skip_apply_when_zero_cap).

        Floors DP at 1, not 0: at 0 DP the player is mortally wounded and the bleed-out tick
        would still kill them at -10, so "no_death" must never leave them there.
        """
        if not (
            combat
            and target.participant_type == CombatParticipantType.PLAYER
            and self._room_has_no_death(combat.room_id)
        ):
            return damage, False
        cap_damage = max(0, target.current_dp - 1)
        damage = min(damage, cap_damage)
        return damage, damage <= 0

    def _apply_damage(
        self, target: CombatParticipant, damage: int, combat: CombatInstance | None = None
    ) -> tuple[int, bool, bool]:
        """
        Apply damage to target and check death states.

        Delegates domain logic to CombatParticipant.apply_damage; handles
        infrastructure concerns (login grace period, no_death rooms) here.

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        damage, skip_apply = self._cap_damage_for_no_death_room(target, damage, combat)
        if skip_apply:
            return target.current_dp, False, False

        if _player_damage_blocked_by_grace(target, damage):
            return target.current_dp, False, False

        return target.apply_damage(damage)

    def _room_has_no_death(self, room_id: str) -> bool:
        """Check if room has no_death attribute (tutorial/safe zones)."""
        try:
            from ..container.async_persistence_access import get_container_async_persistence

            persistence = get_container_async_persistence()
            room = persistence.get_room_by_id(room_id)
            return bool(room and getattr(room, "attributes", {}) and room.attributes.get("no_death"))
        except (AttributeError, ImportError, TypeError) as _:
            return False

    async def apply_attack_damage(
        self, combat: CombatInstance, target: CombatParticipant, damage: int
    ) -> tuple[int, bool, bool]:
        """
        Apply damage to target and update combat state.

        Args:
            combat: Combat instance
            target: Target participant
            damage: Damage amount

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        old_dp, target_died, target_mortally_wounded = self._apply_damage(target, damage, combat)

        combat.update_activity(0)
        return old_dp, target_died, target_mortally_wounded

    async def apply_player_hit(
        self, registry: "PlayerRegistry", combat: CombatInstance, target: CombatParticipant, damage: int
    ) -> tuple[int, bool, bool]:
        """
        Land a hit on a player's live DP as one registry unit (ADR-029 step 6c).

        Combat's own rules (armor, no_death rooms, the login ward) run on the participant, but it starts from the
        registry's DP and the result commits before this returns: every other DP writer changes only the registry, so
        a hit that trusted the participant's copy would overwrite them. A failed commit lands no damage at all.

        Returns:
            Tuple of (old_dp, target_died, target_mortally_wounded)
        """
        before = target.current_dp
        try:
            async with registry.mutate(target.participant_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                target.current_dp = dp_of(player.row.stats)
                live_dp = target.current_dp
                result = await self.apply_attack_damage(combat, target, damage)
                if target.current_dp != live_dp:
                    _ = PlayerHealthService.apply_in(player, set_to(player.row.stats, target.current_dp))
            return result
        except PlayerNotFoundError:
            # The character was deleted mid-fight: there is nothing to write, but the fight can still finish.
            logger.warning("Player not found for a combat hit", player_id=target.participant_id)
            return await self.apply_attack_damage(combat, target, damage)
        except _PLAYER_DP_ERRORS as e:
            logger.error(
                "Combat hit could not be committed; no damage landed",
                player_id=target.participant_id,
                combat_id=combat.combat_id,
                error=str(e),
                exc_info=True,
            )
            target.current_dp = before
            return before, False, False

    async def refresh_player_participants(self, registry: "PlayerRegistry", combat: CombatInstance) -> None:
        """Bring each player participant's DP up to date, so who can act and who is targeted follow heals and damage."""
        for participant in combat.participants.values():
            if participant.participant_type != CombatParticipantType.PLAYER:
                continue
            try:
                player = await registry.get(participant.participant_id)
            except _PLAYER_DP_ERRORS as e:
                logger.warning(
                    "Could not refresh a combat participant's DP", player_id=participant.participant_id, error=str(e)
                )
                continue
            if player is not None:
                participant.current_dp = dp_of(player.row.stats)

    def _find_combat_target(self, combat: CombatInstance, target_id: UUID) -> CombatParticipant:
        target = combat.participants.get(target_id)
        if target:
            return target
        target_id_str = str(target_id)
        target = next(
            (p for p in combat.participants.values() if str(p.participant_id) == target_id_str),
            None,
        )
        if target:
            return target
        participant_ids = [str(pid) for pid in combat.participants.keys()]
        participant_names = {str(pid): getattr(p, "name", "?") for pid, p in combat.participants.items()}
        logger.error(
            "Target not found in combat participants (stale target or wrong combat)",
            combat_id=str(combat.combat_id),
            target_id=str(target_id),
            participant_ids=participant_ids,
            participant_names=participant_names,
        )
        raise ValueError("Target is not in this combat")

    def _validate_target_can_be_attacked(self, target: CombatParticipant) -> None:
        if target.is_alive():
            return
        if target.participant_type == CombatParticipantType.PLAYER and -10 < target.current_dp <= 0:
            logger.debug(
                "Allowing attack on mortally wounded player",
                target_id=target.participant_id,
                target_name=target.name,
                current_dp=target.current_dp,
                is_active=target.is_active,
            )
            return
        raise ValueError("Target is already dead")

    async def validate_and_get_combat_participants(
        self, attacker_id: UUID, target_id: UUID, is_initial_attack: bool
    ) -> tuple[CombatInstance, CombatParticipant, CombatParticipant]:
        """
        Validate attack and retrieve combat participants.

        Args:
            attacker_id: ID of the attacker
            target_id: ID of the target
            is_initial_attack: Whether this is the initial attack

        Returns:
            Tuple of (combat, attacker, target)

        Raises:
            ValueError: If attack is invalid
        """
        combat = await self._combat_service.get_combat_by_participant(attacker_id)
        if not combat:
            raise ValueError("Attacker is not in combat")

        self._validate_attack(combat, is_initial_attack)

        target = self._find_combat_target(combat, target_id)
        self._validate_target_can_be_attacked(target)

        current_participant = combat.participants.get(attacker_id)
        if not current_participant:
            raise ValueError("Attacker not found in combat")

        return combat, current_participant, target
