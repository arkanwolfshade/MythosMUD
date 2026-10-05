"""
Inventory command factory methods.

This module contains factory methods for inventory and item management commands:
pickup, drop, put, get, equip, unequip, use, inventory.
"""

from ..exceptions import ValidationError as MythosValidationError
from ..models.command import (
    DropCommand,
    EquipCommand,
    GetCommand,
    InventoryCommand,
    PickupCommand,
    PutCommand,
    ReadCommand,
    UnequipCommand,
    UseCommand,
)
from ..structured_logging.enhanced_logging_config import get_logger
from .enhanced_error_logging import log_and_raise_enhanced

logger = get_logger(__name__)

_KNOWN_EQUIP_SLOTS = frozenset(
    {
        "head",
        "torso",
        "legs",
        "feet",
        "hands",
        "left_hand",
        "right_hand",
        "main_hand",
        "off_hand",
        "accessory",
        "ring",
        "amulet",
        "belt",
        "backpack",
        "waist",
        "neck",
    }
)

_MULTI_WORD_EQUIP_SLOTS = {
    "main hand": "main_hand",
    "off hand": "off_hand",
    "left hand": "left_hand",
    "right hand": "right_hand",
}


def _normalize_equip_slot_tokens(tokens: list[str]) -> list[str]:
    """Normalize multi-word slot tokens (e.g. 'main hand' -> 'main_hand'); reduces create_equip_command complexity."""
    if len(tokens) < 2:
        return tokens
    phrase = f"{tokens[-2].strip().lower()} {tokens[-1].strip().lower()}"
    if phrase in _MULTI_WORD_EQUIP_SLOTS:
        return tokens[:-2] + [_MULTI_WORD_EQUIP_SLOTS[phrase]]
    return tokens


def _maybe_extract_equip_slot(tokens: list[str]) -> tuple[list[str], str | None]:
    """If last token is a known slot, return (remaining tokens, slot); else (tokens, None)."""
    if not tokens:
        return tokens, None
    normalized = tokens[-1].strip().lower()
    if normalized in _KNOWN_EQUIP_SLOTS:
        return tokens[:-1], normalized
    return tokens, None


def _parse_equip_selector(selector_tokens: list[str], args: list[str]) -> tuple[int | None, str | None, str | None]:
    """Parse selector tokens into (index, search_term, target_slot); may raise MythosValidationError."""
    index: int | None = None
    search_term: str | None = None
    target_slot: str | None = None
    try:
        index_candidate = int(selector_tokens[0])
    except ValueError:
        index_candidate = None
    if index_candidate is not None:
        if index_candidate <= 0:
            log_and_raise_enhanced(
                MythosValidationError,
                "Inventory index must be a positive integer.",
                args=args,
                index=index_candidate,
                logger_name=__name__,
            )
        index = index_candidate
        if len(selector_tokens) > 1:
            target_slot = selector_tokens[1].strip().lower()
    else:
        trimmed_tokens, inferred_slot = _maybe_extract_equip_slot(selector_tokens)
        search_term = " ".join(trimmed_tokens or selector_tokens).strip()
        if not search_term:
            log_and_raise_enhanced(
                MythosValidationError,
                "Equip item name cannot be empty.",
                args=args,
                logger_name=__name__,
            )
        target_slot = inferred_slot
    return index, search_term, target_slot


_GET_USAGE = "Usage: get <item> [from <container>] [quantity]"
_PUT_USAGE = "Usage: put <item> [in|into] <container> [quantity]"


def _split_item_container(
    args: list[str], separators: frozenset[str], usage: str
) -> tuple[str, str | None, int | None]:
    """
    Split get/put args into (item, container, quantity); container is None when no separator is present.

    The separator word is the only thing that can tell where a multi-word item name ends (#982), so it
    is kept through parsing. Splitting on its LAST occurrence lets item names contain the word
    ("letter from arkham from chest"). A trailing integer is a quantity unless it is the only token,
    which stays an index selector.
    """
    tokens = [arg for arg in args if arg.strip()]
    quantity: int | None = None
    if len(tokens) > 1:
        try:
            quantity = int(tokens[-1])
        except ValueError:
            quantity = None
        else:
            if quantity <= 0:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Quantity must be a positive integer",
                    quantity=quantity,
                    logger_name=__name__,
                )
            tokens = tokens[:-1]

    separator_at = max((i for i, token in enumerate(tokens) if token.lower() in separators), default=None)
    if separator_at is None:
        if not tokens:
            log_and_raise_enhanced(MythosValidationError, usage, logger_name=__name__)
        return " ".join(tokens), None, quantity

    item_tokens, container_tokens = tokens[:separator_at], tokens[separator_at + 1 :]
    if not item_tokens or not container_tokens:
        log_and_raise_enhanced(MythosValidationError, usage, args=args, logger_name=__name__)
    return " ".join(item_tokens), " ".join(container_tokens), quantity


class InventoryCommandFactory:
    """Factory class for creating inventory and item management command objects."""

    @staticmethod
    def create_inventory_command(args: list[str]) -> InventoryCommand:
        """Create InventoryCommand from arguments."""
        if args:
            log_and_raise_enhanced(
                MythosValidationError, "Inventory command takes no arguments", args=args, logger_name=__name__
            )
        return InventoryCommand()

    @staticmethod
    def _parse_quantity_from_args(args: list[str], selector_tokens: list[str]) -> tuple[int | None, list[str]]:
        """
        Parse quantity from args if present.

        Args:
            args: Original args list
            selector_tokens: Current selector tokens

        Returns:
            Tuple of (quantity, remaining_selector_tokens)
        """
        quantity: int | None = None

        if len(selector_tokens) > 1:
            potential_quantity = selector_tokens[-1]
            try:
                quantity_candidate = int(potential_quantity)
            except ValueError:
                quantity_candidate = None

            if quantity_candidate is not None:
                if quantity_candidate <= 0:
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer.",
                        args=args,
                        quantity=quantity_candidate,
                        logger_name=__name__,
                    )
                quantity = quantity_candidate
                selector_tokens = selector_tokens[:-1]

        return quantity, selector_tokens

    @staticmethod
    def _parse_index_or_search_term(args: list[str], selector_tokens: list[str]) -> tuple[int | None, str | None]:
        """
        Parse index or search term from selector tokens.

        Args:
            args: Original args list
            selector_tokens: Selector tokens (after quantity extraction)

        Returns:
            Tuple of (index, search_term)
        """
        if not selector_tokens:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                args=args,
                logger_name=__name__,
            )

        primary_token = selector_tokens[0]
        index: int | None = None
        search_term: str | None = None

        try:
            index_candidate = int(primary_token)
        except ValueError:
            index_candidate = None

        if index_candidate is not None:
            if index_candidate <= 0:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Item number must be a positive integer.",
                    args=args,
                    index=index_candidate,
                    logger_name=__name__,
                )

            if len(selector_tokens) > 1:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Usage: pickup <item-number|item-name> [quantity]",
                    args=args,
                    logger_name=__name__,
                )

            index = index_candidate
        else:
            search_term = " ".join(selector_tokens).strip()
            if not search_term:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Pickup item name cannot be empty.",
                    args=args,
                    logger_name=__name__,
                )

        return index, search_term

    @staticmethod
    def create_read_command(args: list[str]) -> ReadCommand:
        """Create ReadCommand from arguments.

        Item name/spell name parsing and the "usage" message for missing args
        are handled by handle_read_command itself, so this takes any args
        (including none) and builds a bare command.
        """
        del args  # Reason: handle_read_command parses args from command_data directly
        return ReadCommand()

    @staticmethod
    def create_pickup_command(args: list[str]) -> PickupCommand:
        """Create pickup command supporting numeric indices or fuzzy names."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                logger_name=__name__,
            )

        selector_tokens = list(args)
        quantity, selector_tokens = InventoryCommandFactory._parse_quantity_from_args(args, selector_tokens)
        index, search_term = InventoryCommandFactory._parse_index_or_search_term(args, selector_tokens)

        return PickupCommand(index=index, search_term=search_term, quantity=quantity)

    @staticmethod
    def create_drop_command(args: list[str]) -> DropCommand:
        """Create drop command."""

        if not args:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: drop <inventory-number> [quantity]",
                logger_name=__name__,
            )

        try:
            index = int(args[0])
        except ValueError:
            log_and_raise_enhanced(
                MythosValidationError, "Inventory index must be an integer", args=args, logger_name=__name__
            )

        quantity = None
        if len(args) > 1:
            try:
                quantity = int(args[1])
            except ValueError:
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Quantity must be an integer",
                    args=args,
                    logger_name=__name__,
                )

        return DropCommand(index=index, quantity=quantity)

    @staticmethod
    def create_put_command(args: list[str]) -> PutCommand:
        """
        Create put command.

        Supports: put <item> [in|into] <container> [quantity]
        "in"/"into" is required for a multi-word item; without it the first word is the item.
        """
        item, container, quantity = _split_item_container(args, frozenset({"in", "into"}), _PUT_USAGE)
        if container is None:
            item, _, container = item.partition(" ")
            if not container:
                log_and_raise_enhanced(MythosValidationError, _PUT_USAGE, args=args, logger_name=__name__)
        return PutCommand(item=item, container=container, quantity=quantity)

    @staticmethod
    def create_get_command(args: list[str]) -> GetCommand:
        """
        Create get command.

        Supports: get <item> [from <container>] [quantity]
        Without "from" the whole phrase is an item taken from the room ("room" is the floor sentinel).
        """
        item, container, quantity = _split_item_container(args, frozenset({"from"}), _GET_USAGE)
        return GetCommand(item=item, container=container or "room", quantity=quantity)

    @staticmethod
    def create_equip_command(args: list[str]) -> EquipCommand:
        """Create equip command."""
        if not args:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: equip <inventory-number|item-name> [slot]",
                logger_name=__name__,
            )
        selector_tokens = _normalize_equip_slot_tokens(list(args))
        index, search_term, target_slot = _parse_equip_selector(selector_tokens, args)
        return EquipCommand(index=index, search_term=search_term, target_slot=target_slot)

    @staticmethod
    def create_use_command(args: list[str]) -> UseCommand:
        """Create use command (``use``/``drink``/``quaff``): a 1-based inventory number or an item name."""
        candidate = " ".join(args).strip()
        if not candidate or (candidate.isdecimal() and int(candidate) < 1):
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: use <inventory-number|item-name>",
                logger_name=__name__,
            )
        if candidate.isdecimal():
            return UseCommand(index=int(candidate))
        return UseCommand(search_term=candidate)

    @staticmethod
    def create_unequip_command(args: list[str]) -> UnequipCommand:
        """Create unequip command."""

        if not args:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                logger_name=__name__,
            )

        candidate = " ".join(args).strip()
        if not candidate:
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                args=args,
                logger_name=__name__,
            )

        normalized = candidate.lower()
        known_slots = {
            "head",
            "torso",
            "legs",
            "feet",
            "hands",
            "left_hand",
            "right_hand",
            "main_hand",
            "off_hand",
            "accessory",
            "ring",
            "amulet",
            "belt",
            "backpack",
            "waist",
            "neck",
        }

        if normalized in known_slots:
            return UnequipCommand(slot=candidate)

        return UnequipCommand(search_term=candidate)
