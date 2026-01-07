"""
Time command handlers for MythosMUD.

This module contains handlers for the time command.
"""

from typing import Any

from ..alias_storage import AliasStorage
from ..structured_logging.enhanced_logging_config import get_logger
from ..time.time_service import get_mythos_chronicle

logger = get_logger(__name__)


async def handle_time_command(
    _command_data: dict, _current_user: dict, request: Any, _alias_storage: AliasStorage | None, player_name: str
) -> dict[str, str]:
    """Handle the time command, exposing the current Mythos time and active holidays."""

    logger.debug("Processing time command", player=player_name)

    chronicle = get_mythos_chronicle()
    mythos_dt = chronicle.get_current_mythos_datetime()
    components = chronicle.get_calendar_components(mythos_dt)

    active_holidays: list[str] = []
    app = request.app if request else None
    state = getattr(app, "state", None) if app else None
    holiday_service = getattr(state, "holiday_service", None) if state else None
    if holiday_service:
        try:
            holiday_service.refresh_active(mythos_dt)
            active_holidays = holiday_service.get_active_holiday_names()
        except Exception as exc:  # pragma: no cover - defensive logging  # pylint: disable=broad-exception-caught  # Reason: Holiday service errors unpredictable, optional metadata
            logger.warning("Time command could not refresh holiday data", error=str(exc))

    clock_line = chronicle.format_clock(mythos_dt)
    date_line = f"{components.day_name}, {components.month_name} {components.day_of_month}, {components.year}"
    week_line = f"Week {components.week_of_month} of {components.month_name}"
    holiday_line = f"Active Holidays: {', '.join(active_holidays)}" if active_holidays else "Active Holidays: None"

    lines = [
        "--- MYTHOS TIME ---",
        f"{clock_line} ({components.daypart}, {components.season})",
        date_line,
        week_line,
        holiday_line,
    ]

    return {"result": "\n".join(lines)}
