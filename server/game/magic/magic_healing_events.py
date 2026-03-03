"""
Healing event notification for spellcasting.

Mixin that sends player_dp_updated events when spells apply healing
(heal_self, heal_other). Used by MagicService.
"""

import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy.exc import SQLAlchemyError

from server.models.spell import Spell
from server.schemas.shared import TargetType
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.player_service import PlayerService


logger = get_logger(__name__)


class MagicServiceHealingMixin:
    """Mixin for MagicService: send DP update events when spells apply healing."""

    # Provided by MagicService concrete implementation
    player_service: "PlayerService"

    def _is_heal_other_target(
        self,
        effect_result: dict[str, Any],
        spell: Spell,
        target: Any,
        player_id: uuid.UUID,
    ) -> bool:
        """True when healing was applied to another player (heal-other, not steal-life or self)."""
        return (
            bool(effect_result.get("effect_applied"))
            and bool(effect_result.get("heal_amount"))
            and spell.spell_id != "steal_life"
            and target is not None
            and getattr(target, "target_type", None) == TargetType.PLAYER
            and str(getattr(target, "target_id", None)) != str(player_id)
        )

    @staticmethod
    def _effect_result_has_healing(effect_result: dict[str, Any]) -> bool:
        """True if effect result indicates healing was applied (success, effect_applied, heal_amount)."""
        return (
            bool(effect_result.get("success"))
            and bool(effect_result.get("effect_applied"))
            and bool(effect_result.get("heal_amount"))
        )

    async def _send_healing_update_event(
        self,
        player_id: uuid.UUID,
        effect_result: dict[str, Any],
        spell_id: str,
        room_id: str,
        healed_player_id: uuid.UUID | None = None,
    ) -> None:
        """Send player_dp_updated event for the healed player (target for heal other, caster for heal self)."""
        if not self._effect_result_has_healing(effect_result):
            return

        event_player_id = healed_player_id if healed_player_id is not None else player_id

        try:
            await self._publish_or_send_dp_update(event_player_id, effect_result, spell_id, room_id)
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as dp_error:
            logger.warning(
                "Failed to publish PlayerDPUpdated event after spell",
                player_id=event_player_id,
                spell_id=spell_id,
                error=str(dp_error),
            )

    async def _publish_or_send_dp_update(
        self,
        event_player_id: uuid.UUID,
        effect_result: dict[str, Any],
        spell_id: str,
        room_id: str,
    ) -> None:
        """Load player stats and delegate DP event publishing."""
        updated_player = await self.player_service.persistence.get_player_by_id(event_player_id)
        if not updated_player:
            return

        stats = updated_player.get_stats()
        current_dp = stats.get("current_dp", 0)
        max_dp = stats.get("max_dp", 0)
        heal_amount = effect_result.get("heal_amount", 0)
        old_dp = max(0, current_dp - heal_amount)

        await self._publish_dp_event(
            event_player_id=event_player_id,
            old_dp=old_dp,
            current_dp=current_dp,
            max_dp=max_dp,
            heal_amount=heal_amount,
            spell_id=spell_id,
            room_id=room_id,
        )

    async def _publish_dp_event(
        self,
        event_player_id: uuid.UUID,
        old_dp: int,
        current_dp: int,
        max_dp: int,
        heal_amount: int,
        spell_id: str,
        room_id: str,
    ) -> None:
        """Publish DP update via event bus, or send fallback game event."""
        from server.container import ApplicationContainer
        from server.events.event_types import PlayerDPUpdated

        container = ApplicationContainer.get_instance()
        if container and container.event_bus:
            dp_event = PlayerDPUpdated(
                player_id=event_player_id,
                old_dp=old_dp,
                new_dp=current_dp,
                max_dp=max_dp,
                damage_taken=-heal_amount,
                source_id=spell_id,
                room_id=room_id,
            )
            container.event_bus.publish(dp_event)
            return

        from server.realtime.connection_manager_api import send_game_event

        await send_game_event(
            event_player_id,
            "player_dp_updated",
            {
                "old_dp": old_dp,
                "new_dp": current_dp,
                "max_dp": max_dp,
                "damage_taken": -heal_amount,
                "player": {
                    "stats": {
                        "current_dp": current_dp,
                        "max_dp": max_dp,
                    },
                },
            },
        )
        logger.warning(
            "Event bus not available for DP update after spell",
            player_id=event_player_id,
            spell_id=spell_id,
        )

    async def _send_instant_heal_event_if_applied(
        self, player_id: uuid.UUID, spell: Any, target: Any, result: dict[str, Any]
    ) -> None:
        """If instant cast applied healing, send DP update event to the healed player."""
        effect_result = result.get("effect_result", result)
        if not (
            effect_result.get("success") and effect_result.get("effect_applied") and effect_result.get("heal_amount")
        ):
            return
        room_id = getattr(target, "room_id", None) or ""
        tid = getattr(target, "target_id", None) if target is not None else None
        healed_player_id = uuid.UUID(tid) if spell.spell_id == "heal_other" and tid else None
        await self._send_healing_update_event(
            player_id, effect_result, spell.spell_id, room_id, healed_player_id=healed_player_id
        )
