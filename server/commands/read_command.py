"""
Read command handler for reading spellbooks and other readable items.

This module handles the /read command for learning spells from spellbooks.
"""

# pylint: disable=too-many-arguments,too-many-locals,too-many-return-statements  # Reason: Read commands require many parameters and intermediate variables for complex item reading logic and multiple return statements for early validation returns

import json
from typing import Any, cast

from server.alias_storage import AliasStorage
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)


def _find_item_in_inventory(player: Any, item_name: str) -> dict[str, Any] | None:
    """Find an item in player's inventory by name."""
    inventory = json.loads(player.inventory) if isinstance(player.inventory, str) else player.inventory
    for item in inventory:
        if isinstance(item, dict) and item.get("name", "").lower() == item_name.lower():
            return item
    return None


def _validate_spellbook(
    item_found: dict[str, Any] | None, item_name: str
) -> tuple[list[str] | None, dict[str, str] | None]:
    """Validate item is a spellbook and return spells list."""
    if not item_found:
        return None, {"result": f"'{item_name}' not found in your inventory or the room."}

    item_metadata = item_found.get("metadata", {}) if isinstance(item_found, dict) else {}
    if not item_metadata.get("spellbook"):
        return None, {"result": f"'{item_name}' is not a spellbook."}

    spells_in_book = item_metadata.get("spells", [])
    if not spells_in_book:
        return None, {"result": f"'{item_name}' appears to be empty or corrupted."}

    return spells_in_book, None


def _format_learn_spell_message(result: dict[str, Any], spell_name: str) -> str:
    """Format message after learning a spell, including corruption if applicable."""
    message = result.get("message", f"Learned {spell_name}!")
    if result.get("corruption_applied", 0) > 0:
        message += f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."
    return cast(str, message)


async def _learn_specific_spell(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Spell learning requires many parameters for context and validation
    spell_learning_service: Any,
    spell_registry: Any,
    player: Any,
    item_found: dict[str, Any],
    spell_name: str,
    spells_in_book: list[str],
) -> dict[str, str]:
    """Learn a specific spell from the spellbook."""
    if not spell_registry:
        return {"result": "Spell registry not available."}

    spell = spell_registry.get_spell_by_name(spell_name)
    if not spell:
        return {"result": f"Spell '{spell_name}' not found in the spellbook."}

    if spell.spell_id not in spells_in_book:
        return {"result": f"'{spell_name}' is not in this spellbook."}

    result = await spell_learning_service.learn_spell(
        player.player_id, spell.spell_id, source=f"spellbook:{item_found.get('id', 'unknown')}"
    )

    if not result.get("success"):
        return {"result": result.get("message", "Failed to learn spell.")}

    message = _format_learn_spell_message(result, spell_name)
    return {"result": message}


async def _learn_single_spell(
    spell_learning_service: Any,
    spell_registry: Any,
    player: Any,
    item_found: dict[str, Any],
    spell_id: str,
) -> dict[str, str]:
    """Learn the only spell in a spellbook."""
    result = await spell_learning_service.learn_spell(
        player.player_id, spell_id, source=f"spellbook:{item_found.get('id', 'unknown')}"
    )

    if not result.get("success"):
        return {"result": result.get("message", "Failed to learn spell.")}

    spell_name_display = spell_id
    if spell_registry:
        spell = spell_registry.get_spell(spell_id)
        if spell:
            spell_name_display = spell.name

    message = _format_learn_spell_message(result, spell_name_display)
    return {"result": message}


def _list_spells_in_book(spell_registry: Any, spells_in_book: list[str], item_name: str) -> dict[str, str]:
    """List all spells in a spellbook."""
    spell_list = []
    for spell_id in spells_in_book:
        if spell_registry:
            spell = spell_registry.get_spell(spell_id)
            if spell:
                spell_list.append(spell.name)
            else:
                spell_list.append(spell_id)
        else:
            spell_list.append(spell_id)

    return {
        "result": (
            f"'{item_name}' contains the following spells:\n"
            + "\n".join(f"  - {spell}" for spell in spell_list)
            + f"\n\nUse '/read {item_name} <spell_name>' to learn a specific spell."
        )
    }


async def handle_read_command(  # pylint: disable=too-many-arguments,too-many-locals  # Reason: Read command requires many parameters and intermediate variables for complex item reading logic
    command_data: dict[str, Any],
    current_user: dict[str, Any],
    request: Any,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """
    Handle /read command for reading spellbooks.

    Usage: /read <item_name> [spell_name]
    If spell_name is omitted and item contains only one spell, learn that spell.

    Args:
        command_data: Command data dictionary
        current_user: Current user information
        request: FastAPI request object
        alias_storage: Alias storage instance
        player_name: Player name

    Returns:
        dict: Command result
    """
    logger.debug("Handling read command", player_name=player_name, command_data=command_data)

    app = request.app if request else None
    if not app:
        return {"result": "System error: application not available."}

    persistence = getattr(app.state, "persistence", None)
    spell_learning_service = getattr(app.state, "spell_learning_service", None)

    if not persistence:
        return {"result": "System error: persistence layer not available."}

    if not spell_learning_service:
        return {"result": "Spell learning system not initialized."}

    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    args = command_data.get("args", [])
    if not args:
        return {"result": "Usage: /read <item_name> [spell_name]"}

    item_name = args[0]
    spell_name = args[1] if len(args) > 1 else None

    try:
        item_found = _find_item_in_inventory(player, item_name)
        spells_in_book, error = _validate_spellbook(item_found, item_name)
        if error:
            return error

        if item_found is None or spells_in_book is None:
            return {"result": f"'{item_name}' not found or invalid."}

        spell_registry = getattr(app.state, "spell_registry", None)

        if spell_name:
            return await _learn_specific_spell(
                spell_learning_service, spell_registry, player, item_found, spell_name, spells_in_book
            )

        if len(spells_in_book) == 1:
            return await _learn_single_spell(
                spell_learning_service, spell_registry, player, item_found, spells_in_book[0]
            )

        return _list_spells_in_book(spell_registry, spells_in_book, item_name)

    except (ValueError, KeyError, TypeError) as e:
        logger.error("Error reading spellbook", player_name=player_name, item_name=item_name, error=str(e))
        return {"result": f"An error occurred while reading '{item_name}': {str(e)}"}
