"""
Combat turn processing logic.

Handles turn advancement, NPC turn processing, and player turn processing
for automatic combat progression.
"""

from server.config import get_config
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services.nats_exceptions import NATSError
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CombatTurnProcessor:
    """Handles combat turn processing and auto-progression."""

    def __init__(self, combat_service):
        """
        Initialize the turn processor.

        Args:
            combat_service: Reference to the parent CombatService for attack processing
        """
        self._combat_service = combat_service

    async def process_game_tick(self, current_tick: int, active_combats: dict, auto_progression_enabled: bool) -> None:
        """
        Process game tick for combat auto-progression.

        Args:
            current_tick: Current game tick number
            active_combats: Dictionary of active combat instances
            auto_progression_enabled: Whether auto-progression is enabled
        """
        logger.info(
            "Combat tick processing",
            tick=current_tick,
            auto_progression_enabled=auto_progression_enabled,
            active_combats_count=len(active_combats),
        )
        if not auto_progression_enabled:
            logger.info("[COMBAT TICK] Auto-progression is disabled, returning early")
            return

        # Check all active combats for auto-progression
        for combat_id, combat in list(active_combats.items()):
            if combat.status != CombatStatus.ACTIVE:
                continue

            if not combat.auto_progression_enabled:
                continue

            logger.debug(
                "Combat auto-progression check",
                combat_id=combat_id,
                current_tick=current_tick,
                next_turn_tick=combat.next_turn_tick,
                auto_progression_enabled=combat.auto_progression_enabled,
            )

            # Check if it's time for the next turn
            if current_tick >= combat.next_turn_tick:
                logger.debug("Auto-progression triggered", combat_id=combat_id, tick=current_tick)
                await self._advance_turn_automatically(combat, current_tick)

    async def _advance_turn_automatically(self, combat: CombatInstance, current_tick: int) -> None:
        """
        Automatically advance combat turn and process NPC actions.

        Args:
            combat: Combat instance to advance
            current_tick: Current game tick
        """
        # Update activity
        combat.update_activity(current_tick)

        # Advance turn
        combat.advance_turn(current_tick)

        # Get current participant
        current_participant = combat.get_current_turn_participant()
        if not current_participant:
            logger.warning("No current participant for combat", combat_id=combat.combat_id)
            logger.debug(
                "Combat state debug",
                turn_order=combat.turn_order,
                current_turn=combat.current_turn,
                participants=list(combat.participants.keys()),
            )
            # Check if the participant ID exists in turn_order but not in participants
            if combat.turn_order and combat.current_turn < len(combat.turn_order):
                expected_participant_id = combat.turn_order[combat.current_turn]
                logger.debug(
                    "Expected participant lookup",
                    expected_participant_id=expected_participant_id,
                    exists_in_participants=expected_participant_id in combat.participants,
                )

                # If participant is missing, try to fix the combat state
                if expected_participant_id not in combat.participants:
                    logger.error(
                        "Participant not found in participants dictionary - combat state corrupted",
                        participant_id=expected_participant_id,
                    )
                    # Remove the corrupted combat using public method
                    await self._combat_service.end_combat(
                        combat.combat_id, "Combat state corrupted - participant missing"
                    )
                    return

                # Try to find the participant by matching UUID values
                found_participant = None
                for participant_id, participant in combat.participants.items():
                    if str(participant_id) == str(expected_participant_id):
                        found_participant = participant
                        logger.debug("Found participant by UUID string match", participant=participant)
                        break

                if found_participant:
                    current_participant = found_participant
                else:
                    logger.error(
                        "Could not find participant even by UUID string match",
                        participant_id=expected_participant_id,
                    )
                    return
            else:
                return

        # Debug logging to understand participant type
        debug_participant_id = getattr(current_participant, "participant_id", None)
        logger.debug(
            "Current participant type",
            participant_type=type(current_participant).__name__,
            participant_id=str(debug_participant_id) if debug_participant_id else "NO_PARTICIPANT_ID",
        )

        # Additional debugging for the combat state
        logger.debug(
            "Combat state debug",
            turn_order=combat.turn_order,
            current_turn=combat.current_turn,
            participants=list(combat.participants.keys()),
        )

        # Debug the specific participant lookup
        if combat.turn_order and combat.current_turn < len(combat.turn_order):
            current_participant_id = combat.turn_order[combat.current_turn]
            logger.debug(
                "Participant lookup",
                looking_for=current_participant_id,
                available_participants=list(combat.participants.keys()),
            )
            found_participant = combat.participants.get(current_participant_id)
            logger.debug("Participant found", participant=found_participant)
            logger.debug("current_participant (from get_current_turn_participant)", participant=current_participant)
            logger.debug("Participant comparison", same=found_participant == current_participant)

        # If it's an NPC's turn, process their action
        if current_participant.participant_type == CombatParticipantType.NPC:
            await self._process_npc_turn(combat, current_participant, current_tick)
        else:
            # Player's turn - perform automatic basic attack
            await self._process_player_turn(combat, current_participant, current_tick)

    async def _process_npc_turn(self, combat: CombatInstance, npc: CombatParticipant, current_tick: int) -> None:
        """
        Process NPC turn with actual combat attack.

        Args:
            combat: Combat instance
            npc: NPC participant
            current_tick: Current game tick
        """
        try:
            # Debug logging to understand what we're receiving
            logger.debug("_process_npc_turn called", npc_type=type(npc).__name__, npc=npc)
            if hasattr(npc, "participant_id"):
                logger.debug(
                    "NPC participant_id", participant_id=npc.participant_id, id_type=type(npc.participant_id).__name__
                )
            else:
                logger.error("NPC object missing participant_id attribute", npc=npc)
                return

            # BUGFIX: Check if NPC is alive (DP > 0) before allowing actions
            # NPCs die immediately at DP <= 0, unlike players who enter mortally wounded state
            # As documented in "Non-Euclidean Biology and Combat Mechanics" - Dr. Armitage, 1929
            if npc.current_dp <= 0:
                logger.info(
                    "NPC is dead and cannot act",
                    npc_name=npc.name,
                    current_dp=npc.current_dp,
                    combat_id=combat.combat_id,
                )
                # Skip turn but don't end combat (combat ends when is_alive() returns False)
                npc.last_action_tick = current_tick
                return

            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != npc.participant_id:
                    target = participant
                    break
            if not target:
                logger.warning("No target found for NPC", npc_name=npc.name, combat_id=combat.combat_id)
                return

            # Perform automatic basic attack
            logger.debug("NPC performing automatic attack", npc_name=npc.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage
            # Process the attack
            combat_result = await self._combat_service.process_attack(
                attacker_id=npc.participant_id, target_id=target.participant_id, damage=damage
            )
            if combat_result.success:
                logger.info("NPC automatically attacked", npc_name=npc.name, target_name=target.name, damage=damage)
            else:
                logger.warning("NPC automatic attack failed", npc_name=npc.name, message=combat_result.message)

            # Update NPC's last action tick
            npc.last_action_tick = current_tick

        except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
            logger.error("Error processing NPC turn", npc_name=npc.name, error=str(e), exc_info=True)

    async def _process_player_turn(self, combat: CombatInstance, player: CombatParticipant, current_tick: int) -> None:
        """
        Process player turn with automatic basic attack.

        Args:
            combat: Combat instance
            player: Player participant
            current_tick: Current game tick
        """
        try:
            # Debug logging to understand what we're receiving
            logger.debug("_process_player_turn called", player_type=type(player), player=player)
            if hasattr(player, "participant_id"):
                logger.debug(
                    "Player participant_id",
                    participant_id=player.participant_id,
                    participant_id_type=type(player.participant_id),
                )
            else:
                logger.error("Player object missing participant_id attribute", player=player)
                return

            # BUGFIX #243: Check if player is conscious (DP > 0) before allowing actions
            # As documented in "Consciousness and Corporeal Agency in Combat" - Dr. Armitage, 1929
            # Unconscious entities (DP <= 0) cannot perform voluntary actions
            if player.current_dp <= 0:
                logger.info(
                    "Player is unconscious and cannot act",
                    player_name=player.name,
                    current_dp=player.current_dp,
                    combat_id=combat.combat_id,
                )
                # Skip turn but don't end combat (player may be unconscious but not dead)
                player.last_action_tick = current_tick
                return

            # Find the target (other participant in combat)
            target = None
            for participant in combat.participants.values():
                if participant.participant_id != player.participant_id:
                    target = participant
                    break

            if not target:
                logger.warning("No target found for player", player_name=player.name, combat_id=combat.combat_id)
                return

            # Check if player is casting a spell - if so, skip autoattack
            # Casting spells takes priority over autoattacks
            try:
                # Access magic_service through combat_service
                magic_service = getattr(self._combat_service, "magic_service", None)
                if magic_service and magic_service.casting_state_manager.is_casting(player.participant_id):
                    casting_state = magic_service.casting_state_manager.get_casting_state(player.participant_id)
                    logger.debug(
                        "Player is casting, skipping autoattack",
                        player_name=player.name,
                        spell_name=casting_state.spell_name if casting_state else "unknown",
                    )
                    # Update player's last action tick but don't attack
                    player.last_action_tick = current_tick
                    return
            except (AttributeError, TypeError, KeyError) as e:
                # If we can't check casting state, allow autoattack to proceed
                logger.debug("Could not check casting state for autoattack", player_name=player.name, error=str(e))

            # Perform automatic basic attack
            logger.debug("Player performing automatic attack", player_name=player.name, target_name=target.name)

            # Use configured damage for automatic attacks
            config = get_config()
            damage = config.game.basic_unarmed_damage

            # Process the attack
            combat_result = await self._combat_service.process_attack(
                attacker_id=player.participant_id, target_id=target.participant_id, damage=damage
            )

            if combat_result.success:
                logger.info(
                    "Player automatically attacked", player_name=player.name, target_name=target.name, damage=damage
                )
            else:
                logger.warning("Player automatic attack failed", player_name=player.name, message=combat_result.message)

            # Update player's last action tick
            player.last_action_tick = current_tick

        except (AttributeError, ValueError, TypeError, RuntimeError, NATSError, ConnectionError, KeyError) as e:
            # Handle case where player might not be a CombatParticipant
            player_type = type(player)
            player_name = getattr(player, "name", f"Unknown Player (type: {player_type})")
            logger.error("Error processing player turn", player_name=player_name, error=str(e), exc_info=True)
