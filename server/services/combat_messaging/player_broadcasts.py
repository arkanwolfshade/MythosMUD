"""Player lifecycle broadcasts (mortally wounded, death, respawn, dp decay)."""

from typing import Any, cast

from server.realtime.envelope import build_event
from server.services.combat_messaging.base import HasConnectionManager
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerBroadcastMixin(HasConnectionManager):
    """Mixin for player lifecycle broadcast methods. Requires connection_manager on self."""

    def _build_mortally_wounded_messages(self, player_name: str, attacker_name: str | None) -> tuple[str, str]:
        """Build personal and room messages for mortally wounded broadcast."""
        if attacker_name:
            personal = f"{attacker_name}'s attack causes you to collapse as darkness begins closing in on your vision"
            room = f"{player_name} collapses from {attacker_name}'s attack and is on the verge of death!"
        else:
            personal = "You collapse as darkness begins closing in on your vision"
            room = f"{player_name} collapses and is on the verge of death!"
        return personal, room

    async def _send_mortally_wounded_personal_message(self, player_id: str, personal_event: dict[str, Any]) -> None:
        """Send mortally wounded personal message. Logs warning on failure."""
        try:
            await self.connection_manager.send_personal_message(player_id, personal_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning("Failed to send mortally wounded message to player", player_id=player_id, error=str(e))

    async def broadcast_player_mortally_wounded(
        self,
        player_id: str,
        player_name: str,
        attacker_name: str | None,
        room_id: str,
    ) -> dict[str, Any]:
        """Broadcast player mortally wounded to room. Sends personal message to wounded player."""
        logger.info(
            "Broadcasting player mortally wounded",
            player_id=player_id,
            player_name=player_name,
            attacker_name=attacker_name,
            room_id=room_id,
        )
        personal_message, room_message = self._build_mortally_wounded_messages(player_name, attacker_name)
        personal_event = build_event(
            "player_mortally_wounded",
            {
                "player_id": player_id,
                "player_name": player_name,
                "attacker_name": attacker_name,
                "message": personal_message,
            },
            room_id=room_id,
            player_id=player_id,
        )
        room_event = build_event(
            "player_mortally_wounded_room",
            {
                "player_id": player_id,
                "player_name": player_name,
                "attacker_name": attacker_name,
                "message": room_message,
            },
            room_id=room_id,
        )
        await self._send_mortally_wounded_personal_message(player_id, personal_event)
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)
        logger.debug("Player mortally wounded broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)
        return cast(dict[str, Any], broadcast_stats)

    async def broadcast_player_death(
        self,
        player_id: str,
        player_name: str,
        room_id: str,
        death_location: str,
        current_dp: int = -10,
    ) -> dict[str, Any]:
        """Broadcast player death message to all players in the room."""
        logger.info(
            "Broadcasting player death",
            player_id=player_id,
            player_name=player_name,
            room_id=room_id,
            death_location=death_location,
        )
        personal_message = "You exhale your last breath."
        room_message = f"{player_name} exhales their last breath."
        personal_event = build_event(
            "player_died",
            {
                "player_id": player_id,
                "player_name": player_name,
                "death_location": death_location,
                "current_dp": current_dp,
                "message": personal_message,
            },
            room_id=room_id,
            player_id=player_id,
        )
        room_event = build_event(
            "player_died_room",
            {"player_id": player_id, "player_name": player_name, "message": room_message},
            room_id=room_id,
        )
        try:
            await self.connection_manager.send_personal_message(player_id, personal_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning("Failed to send death message to player", player_id=player_id, error=str(e))
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)
        logger.debug("Player death broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)
        return cast(dict[str, Any], broadcast_stats)

    async def broadcast_player_respawn(self, player_id: str, player_name: str, room_id: str) -> dict[str, Any]:
        """Broadcast player respawn message to all players in the room."""
        logger.info("Broadcasting player respawn", player_id=player_id, player_name=player_name, room_id=room_id)
        personal_message = "You open your eyes and awaken from your coma."
        room_message = f"Patient {player_name} opens their eyes and awakens from their coma."
        personal_event = build_event(
            "player_respawned",
            {"player_id": player_id, "player_name": player_name, "message": personal_message},
            room_id=room_id,
            player_id=player_id,
        )
        room_event = build_event(
            "player_respawned_room",
            {"player_id": player_id, "player_name": player_name, "message": room_message},
            room_id=room_id,
        )
        try:
            await self.connection_manager.send_personal_message(player_id, personal_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning("Failed to send respawn message to player", player_id=player_id, error=str(e))
        broadcast_stats = await self.connection_manager.broadcast_to_room(room_id, room_event, exclude_player=player_id)
        logger.debug("Player respawn broadcast completed", room_id=room_id, broadcast_stats=broadcast_stats)
        return cast(dict[str, Any], broadcast_stats)

    async def send_dp_decay_message(self, player_id: str, current_dp: int) -> dict[str, Any]:
        """Send DP decay message to a specific mortally wounded player."""
        logger.debug("Sending DP decay message", player_id=player_id, current_dp=current_dp)
        message = f"Your lifeforce ebbs away... (DP: {current_dp})"
        decay_event = build_event(
            "player_dp_decay",
            {"player_id": player_id, "current_dp": current_dp, "message": message},
            player_id=player_id,
        )
        try:
            delivery_status = await self.connection_manager.send_personal_message(player_id, decay_event)
        except (ConnectionError, OSError, RuntimeError, ValueError) as e:
            logger.warning("Failed to send DP decay message to player", player_id=player_id, error=str(e))
            delivery_status = {"success": False, "error": str(e)}
        logger.debug("DP decay message sent", player_id=player_id, delivery_status=delivery_status)
        return cast(dict[str, Any], delivery_status)
