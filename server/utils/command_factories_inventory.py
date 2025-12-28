"""
Inventory command factory methods.

This module contains factory methods for inventory and item management commands:
pickup, drop, put, get, equip, unequip, inventory.
"""

from ..exceptions import ValidationError as MythosValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..models.command import (
    DropCommand,
    EquipCommand,
    GetCommand,
    InventoryCommand,
    PickupCommand,
    PutCommand,
    UnequipCommand,
)
from .enhanced_error_logging import create_error_context, log_and_raise_enhanced

logger = get_logger(__name__)


class InventoryCommandFactory:
    """Factory class for creating inventory and item management command objects."""

    @staticmethod
    def create_inventory_command(args: list[str]) -> InventoryCommand:
        """Create InventoryCommand from arguments."""
        if args:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Inventory command takes no arguments", context=context, logger_name=__name__
            )
        return InventoryCommand()

    @staticmethod
    def create_pickup_command(args: list[str]) -> PickupCommand:
        """Create pickup command supporting numeric indices or fuzzy names."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                context=context,
                logger_name=__name__,
            )

        quantity: int | None = None
        selector_tokens = list(args)

        if len(selector_tokens) > 1:
            potential_quantity = selector_tokens[-1]
            try:
                quantity_candidate = int(potential_quantity)
            except ValueError:
                quantity_candidate = None

            if quantity_candidate is not None:
                if quantity_candidate <= 0:
                    context = create_error_context()
                    context.metadata = {"args": args, "quantity": quantity_candidate}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer.",
                        context=context,
                        logger_name=__name__,
                    )
                quantity = quantity_candidate
                selector_tokens = selector_tokens[:-1]

        if not selector_tokens:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: pickup <item-number|item-name> [quantity]",
                context=context,
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
                context = create_error_context()
                context.metadata = {"args": args, "index": index_candidate}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Item number must be a positive integer.",
                    context=context,
                    logger_name=__name__,
                )

            if len(selector_tokens) > 1:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Usage: pickup <item-number|item-name> [quantity]",
                    context=context,
                    logger_name=__name__,
                )

            index = index_candidate
        else:
            search_term = " ".join(selector_tokens).strip()
            if not search_term:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Pickup item name cannot be empty.",
                    context=context,
                    logger_name=__name__,
                )

        return PickupCommand(index=index, search_term=search_term, quantity=quantity)

    @staticmethod
    def create_drop_command(args: list[str]) -> DropCommand:
        """Create drop command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: drop <inventory-number> [quantity]",
                context=context,
                logger_name=__name__,
            )

        try:
            index = int(args[0])
        except ValueError:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError, "Inventory index must be an integer", context=context, logger_name=__name__
            )

        quantity = None
        if len(args) > 1:
            try:
                quantity = int(args[1])
            except ValueError:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Quantity must be an integer",
                    context=context,
                    logger_name=__name__,
                )

        return DropCommand(index=index, quantity=quantity)

    @staticmethod
    def create_put_command(args: list[str]) -> PutCommand:
        """
        Create put command.

        Supports: put <item> [in] <container> [quantity]
        The "in" keyword is optional.
        """
        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: put <item> [in] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        # Remove optional "in" keyword
        args_clean = [arg for arg in args if arg.lower() != "in"]

        if len(args_clean) < 2:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: put <item> [in] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        item = args_clean[0]
        container = args_clean[1]
        quantity = None

        # Check if last argument is a quantity
        if len(args_clean) > 2:
            try:
                quantity = int(args_clean[-1])
                if quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"quantity": quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer",
                        context=context,
                        logger_name=__name__,
                    )
                # If quantity was parsed, container might be multi-word
                if len(args_clean) > 3:
                    container = " ".join(args_clean[1:-1])
            except ValueError:
                # Last arg is not a number, container might be multi-word
                container = " ".join(args_clean[1:])

        return PutCommand(item=item, container=container, quantity=quantity)

    @staticmethod
    def create_get_command(args: list[str]) -> GetCommand:
        """
        Create get command.

        Supports: get <item> [from] <container> [quantity]
        The "from" keyword is optional.
        """
        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: get <item> [from] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        # Remove optional "from" keyword
        args_clean = [arg for arg in args if arg.lower() != "from"]

        if len(args_clean) < 2:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: get <item> [from] <container> [quantity]",
                context=context,
                logger_name=__name__,
            )

        item = args_clean[0]
        container = args_clean[1]
        quantity = None

        # Check if last argument is a quantity
        if len(args_clean) > 2:
            try:
                quantity = int(args_clean[-1])
                if quantity <= 0:
                    context = create_error_context()
                    context.metadata = {"quantity": quantity}
                    log_and_raise_enhanced(
                        MythosValidationError,
                        "Quantity must be a positive integer",
                        context=context,
                        logger_name=__name__,
                    )
                # If quantity was parsed, container might be multi-word
                if len(args_clean) > 3:
                    container = " ".join(args_clean[1:-1])
            except ValueError:
                # Last arg is not a number, container might be multi-word
                container = " ".join(args_clean[1:])

        return GetCommand(item=item, container=container, quantity=quantity)

    @staticmethod
    def create_equip_command(args: list[str]) -> EquipCommand:
        """Create equip command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: equip <inventory-number|item-name> [slot]",
                context=context,
                logger_name=__name__,
            )

        selector_tokens = list(args)
        index: int | None = None
        search_term: str | None = None
        target_slot: str | None = None

        def _maybe_extract_slot(tokens: list[str]) -> tuple[list[str], str | None]:
            if not tokens:
                return tokens, None

            possible_slot = tokens[-1]
            normalized = possible_slot.strip().lower()
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
                return tokens[:-1], normalized
            return tokens, None

        try:
            index_candidate = int(selector_tokens[0])
        except ValueError:
            index_candidate = None

        if index_candidate is not None:
            if index_candidate <= 0:
                context = create_error_context()
                context.metadata = {"args": args, "index": index_candidate}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Inventory index must be a positive integer.",
                    context=context,
                    logger_name=__name__,
                )
            index = index_candidate
            if len(selector_tokens) > 1:
                target_slot = selector_tokens[1].strip().lower()
        else:
            trimmed_tokens, inferred_slot = _maybe_extract_slot(selector_tokens)
            search_term = " ".join(trimmed_tokens or selector_tokens).strip()
            if not search_term:
                context = create_error_context()
                context.metadata = {"args": args}
                log_and_raise_enhanced(
                    MythosValidationError,
                    "Equip item name cannot be empty.",
                    context=context,
                    logger_name=__name__,
                )
            target_slot = inferred_slot

        return EquipCommand(index=index, search_term=search_term, target_slot=target_slot)

    @staticmethod
    def create_unequip_command(args: list[str]) -> UnequipCommand:
        """Create unequip command."""

        if not args:
            context = create_error_context()
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                context=context,
                logger_name=__name__,
            )

        candidate = " ".join(args).strip()
        if not candidate:
            context = create_error_context()
            context.metadata = {"args": args}
            log_and_raise_enhanced(
                MythosValidationError,
                "Usage: unequip <slot|item-name>",
                context=context,
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
