"""
Read command handler for reading spellbooks and other readable items.

This module handles the /read command for learning spells from spellbooks.
"""

from typing import Any

from server.alias_storage import AliasStorage
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.command_parser import get_username_from_user

logger = get_logger(__name__)


async def handle_read_command(
    command_data: dict,
    current_user: dict,
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

    # Get services from app state
    app = request.app if request else None
    if not app:
        return {"result": "System error: application not available."}

    persistence = getattr(app.state, "persistence", None)
    spell_learning_service = getattr(app.state, "spell_learning_service", None)

    if not persistence:
        return {"result": "System error: persistence layer not available."}

    if not spell_learning_service:
        return {"result": "Spell learning system not initialized."}

    # Get player
    player = await persistence.get_player_by_name(get_username_from_user(current_user))
    if not player:
        return {"result": "You are not recognized by the cosmic forces."}

    # Extract item name and optional spell name
    args = command_data.get("args", [])
    if not args:
        return {"result": "Usage: /read <item_name> [spell_name]"}

    item_name = args[0]
    spell_name = args[1] if len(args) > 1 else None

    # TODO: Integrate with item system to find spellbook  # pylint: disable=fixme  # Reason: Feature placeholder for item system integration
    # For now, check if item is in inventory or room
    # This is a placeholder - full integration requires item system lookup

    # Check inventory
    try:
        import json

        inventory = json.loads(player.inventory) if isinstance(player.inventory, str) else player.inventory
        item_found = None
        for item in inventory:
            if isinstance(item, dict) and item.get("name", "").lower() == item_name.lower():
                item_found = item
                break

        if not item_found:
            # Check room drops
            # TODO: Check room drops via room manager  # pylint: disable=fixme  # Reason: Feature placeholder for room drop system
            return {"result": f"'{item_name}' not found in your inventory or the room."}

        # Check if item is a spellbook (has spellbook metadata)
        item_metadata = item_found.get("metadata", {}) if isinstance(item_found, dict) else {}
        if not item_metadata.get("spellbook"):
            return {"result": f"'{item_name}' is not a spellbook."}

        # Get spells from spellbook
        spells_in_book = item_metadata.get("spells", [])
        if not spells_in_book:
            return {"result": f"'{item_name}' appears to be empty or corrupted."}

        # If spell_name specified, learn that spell
        if spell_name:
            # Find spell ID from name
            spell_registry = getattr(app.state, "spell_registry", None)
            if not spell_registry:
                return {"result": "Spell registry not available."}

            spell = spell_registry.get_spell_by_name(spell_name)
            if not spell:
                return {"result": f"Spell '{spell_name}' not found in the spellbook."}

            if spell.spell_id not in spells_in_book:
                return {"result": f"'{spell_name}' is not in this spellbook."}

            # Learn the spell
            result = await spell_learning_service.learn_spell(
                player.player_id, spell.spell_id, source=f"spellbook:{item_found.get('id', 'unknown')}"
            )

            if not result.get("success"):
                return {"result": result.get("message", "Failed to learn spell.")}

            message = result.get("message", f"Learned {spell_name}!")
            if result.get("corruption_applied", 0) > 0:
                message += (
                    f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."
                )

            return {"result": message}

        # If no spell specified and only one spell in book, learn it
        if len(spells_in_book) == 1:
            spell_id = spells_in_book[0]
            result = await spell_learning_service.learn_spell(
                player.player_id, spell_id, source=f"spellbook:{item_found.get('id', 'unknown')}"
            )

            if not result.get("success"):
                return {"result": result.get("message", "Failed to learn spell.")}

            spell_registry = getattr(app.state, "spell_registry", None)
            spell_name_display = spell_id
            if spell_registry:
                spell = spell_registry.get_spell(spell_id)
                if spell:
                    spell_name_display = spell.name

            message = result.get("message", f"Learned {spell_name_display}!")
            if result.get("corruption_applied", 0) > 0:
                message += (
                    f" The forbidden knowledge has tainted your mind (+{result['corruption_applied']} corruption)."
                )

            return {"result": message}

        # Multiple spells - list them
        spell_registry = getattr(app.state, "spell_registry", None)
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

    except (ValueError, KeyError, TypeError) as e:
        logger.error("Error reading spellbook", player_name=player_name, item_name=item_name, error=str(e))
        return {"result": f"An error occurred while reading '{item_name}': {str(e)}"}
