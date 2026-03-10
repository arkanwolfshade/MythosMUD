"""NPC monitoring commands (population, zone, status)."""

from typing import Any

from ...alias_storage import AliasStorage
from ...services.npc_instance_service import get_npc_instance_service
from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def handle_npc_population_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC population stats command."""
    logger.debug("Processing NPC population command", player_name=player_name)

    try:
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_population_stats()

        result_lines = ["NPC Population Statistics:"]
        result_lines.append(f"  Total NPCs: {stats.get('total_npcs', 0)}")

        if stats.get("by_type"):
            result_lines.append("  By Type:")
            for npc_type, count in stats["by_type"].items():
                result_lines.append(f"    {npc_type}: {count}")

        if stats.get("by_zone"):
            result_lines.append("  By Zone:")
            for zone, count in stats["by_zone"].items():
                result_lines.append(f"    {zone}: {count}")

        logger.info("NPC population stats retrieved", admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error getting NPC population stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC population stats: {str(e)}"}


async def handle_npc_zone_command(
    command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC zone stats command."""
    logger.debug("Processing NPC zone command", player_name=player_name)

    args = command_data.get("args", [])
    zone_key = args[1] if len(args) > 1 else None

    try:
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_zone_stats()

        result_lines = ["NPC Zone Statistics:"]
        result_lines.append(f"  Total Zones: {stats.get('total_zones', 0)}")
        result_lines.append(f"  Total NPCs: {stats.get('total_npcs', 0)}")

        if stats.get("zones"):
            result_lines.append("  Zone Details:")
            for zone in stats["zones"]:
                zone_key_display = zone.get("zone_key", "unknown")
                npc_count = zone.get("npc_count", 0)
                result_lines.append(f"    {zone_key_display}: {npc_count} NPCs")

                if zone_key and zone_key_display == zone_key and zone.get("active_npcs"):
                    result_lines.append(f"      Active NPCs: {', '.join(zone['active_npcs'])}")

        logger.info("NPC zone stats retrieved", admin_name=player_name, zone_key=zone_key)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error getting NPC zone stats", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC zone stats: {str(e)}"}


async def handle_npc_status_command(
    _command_data: dict[str, Any],
    _current_user: dict[str, Any],
    _request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Handle NPC system status command."""
    logger.debug("Processing NPC status command", player_name=player_name)

    try:
        instance_service = get_npc_instance_service()
        stats = await instance_service.get_system_stats()

        result_lines = ["NPC System Status:"]
        result_lines.append(f"  Status: {stats.get('system_status', 'unknown')}")
        result_lines.append(f"  Active NPCs: {stats.get('active_npcs', 0)}")
        result_lines.append(f"  Lifecycle Manager: {stats.get('lifecycle_manager_status', 'unknown')}")
        result_lines.append(f"  Population Controller: {stats.get('population_controller_status', 'unknown')}")
        result_lines.append(f"  Spawn Queue Size: {stats.get('spawn_queue_size', 0)}")

        logger.info("NPC system status retrieved", admin_name=player_name)
        return {"result": "\n".join(result_lines)}

    except Exception as e:  # noqa: B904,BLE001  # pylint: disable=broad-exception-caught
        logger.error("Error getting NPC system status", admin_name=player_name, error=str(e))
        return {"result": f"Error getting NPC system status: {str(e)}"}
