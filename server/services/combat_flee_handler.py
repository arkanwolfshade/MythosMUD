"""
Combat flee handler for involuntary flee logic.

Handles checking if players should involuntarily flee due to lucidity effects.
"""

# pylint: disable=too-many-return-statements  # Reason: Flee handler requires multiple return statements for different flee condition checks and state evaluations

from datetime import UTC, datetime, timedelta

from server.database import get_async_session
from server.models.combat import CombatParticipant
from server.services.lucidity_command_disruption import should_involuntary_flee
from server.services.lucidity_service import LucidityService
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def check_involuntary_flee(target: CombatParticipant, damage: int) -> bool:
    """
    Check if player should involuntarily flee due to lucidity effects.

    Deranged tier players have a 20% chance to auto-flee when taking >15% max HP damage
    in one hit, with a 2-minute cooldown.

    Args:
        target: The player participant who took damage
        damage: Amount of damage taken

    Returns:
        True if player should flee, False otherwise
    """
    try:
        # Calculate damage percentage
        if target.max_dp <= 0:
            return False  # Avoid division by zero
        damage_percent = damage / target.max_dp

        # Get lucidity tier from database
        async for session in get_async_session():
            try:
                lucidity_service = LucidityService(session)
                lucidity_record = await lucidity_service.get_player_lucidity(target.participant_id)
                tier = lucidity_record.current_tier if lucidity_record else "lucid"

                # Check if should flee based on tier and damage
                if not should_involuntary_flee(tier, damage_percent):
                    return False

                # Check cooldown (2 minutes)
                cooldown_code = "involuntary_flee"
                cooldown = await lucidity_service.get_cooldown(target.participant_id, cooldown_code)
                if cooldown and cooldown.cooldown_expires_at:
                    # Cooldown still active
                    if cooldown.cooldown_expires_at.tzinfo is None:
                        expires_at = cooldown.cooldown_expires_at.replace(tzinfo=UTC)
                    else:
                        expires_at = cooldown.cooldown_expires_at
                    if datetime.now(UTC) < expires_at:
                        logger.debug(
                            "Involuntary flee on cooldown",
                            player_id=target.participant_id,
                            expires_at=expires_at.isoformat(),
                        )
                        return False

                # Set cooldown (2 minutes from now)
                cooldown_expires = datetime.now(UTC) + timedelta(minutes=2)
                # Remove timezone for database storage (PostgreSQL TIMESTAMP WITHOUT TIME ZONE)
                cooldown_expires_naive = cooldown_expires.replace(tzinfo=None)
                await lucidity_service.set_cooldown(target.participant_id, cooldown_code, cooldown_expires_naive)
                await session.commit()

                logger.info(
                    "Involuntary flee conditions met",
                    player_id=target.participant_id,
                    tier=tier,
                    damage=damage,
                    damage_percent=damage_percent,
                    max_dp=target.max_dp,
                )
                return True

            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Flee check errors unpredictable, must not fail combat
                logger.warning(
                    "Error checking involuntary flee",
                    player_id=target.participant_id,
                    error=str(e),
                    error_type=type(e).__name__,
                )
                await session.rollback()
                return False
        # If async for loop doesn't yield any sessions (shouldn't happen, but mypy needs this)
        return False

    except Exception as e:  # pylint: disable=broad-except  # Reason: Flee check errors unpredictable, must catch all exceptions to handle various failure modes during flee validation
        logger.warning(
            "Error in involuntary flee check (session creation)",
            player_id=target.participant_id,
            error=str(e),
            error_type=type(e).__name__,
        )
        return False
