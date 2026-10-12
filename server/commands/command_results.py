"""Shared builders for command-handler result dicts."""

from ..constants.message_category import MessageCategory


def command_error(message: str) -> dict[str, str]:
    """Result for a usage/permission/system failure; the client renders it as ``system.error``."""
    return {"result": message, "category": MessageCategory.SYSTEM_ERROR}
