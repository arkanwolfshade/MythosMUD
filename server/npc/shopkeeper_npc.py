"""
Shopkeeper NPC type for MythosMUD.

This module provides the ShopkeeperNPC class with buy/sell functionality.
"""

from typing import TYPE_CHECKING, Any

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_base import NPCBase

if TYPE_CHECKING:
    from ..events import EventBus
    from .event_reaction_system import NPCEventReactionSystem

logger = get_logger(__name__)


class ShopkeeperNPC(NPCBase):
    """Shopkeeper NPC type with buy/sell functionality."""

    def __init__(
        self,
        definition: Any,
        npc_id: str,
        event_bus: "EventBus | None" = None,
        event_reaction_system: "NPCEventReactionSystem | None" = None,
    ):
        """Initialize shopkeeper NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._shop_inventory: list[dict[str, Any]] = []
        self._buyable_items: dict[str, int] = {}  # item_id -> base_price
        self._setup_shopkeeper_behavior_rules()

    def _setup_shopkeeper_behavior_rules(self):
        """Setup shopkeeper-specific behavior rules."""
        shopkeeper_rules = [
            {
                "name": "greet_customer",
                "condition": "player_nearby == true",
                "action": "greet_customer",
                "priority": 5,
            },
            {
                "name": "restock_inventory",
                "condition": "time_since_last_action > 3600",
                "action": "restock_inventory",
                "priority": 3,
            },
        ]

        for rule in shopkeeper_rules:
            self._behavior_engine.add_rule(rule)

        # Register shopkeeper action handlers
        self._behavior_engine.register_action_handler("greet_customer", self._handle_greet_customer)
        self._behavior_engine.register_action_handler("restock_inventory", self._handle_restock_inventory)

    def get_behavior_rules(self) -> list[dict[str, Any]]:
        """Get shopkeeper-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def get_shop_inventory(self) -> list[dict[str, Any]]:
        """Get shop inventory."""
        return self._shop_inventory.copy()

    def add_shop_item(self, item: dict[str, Any]) -> bool:
        """Add item to shop inventory."""
        try:
            self._shop_inventory.append(item)
            logger.debug("Added item to shop inventory", npc_id=self.npc_id, item_id=item.get("id"))
            return True
        except (TypeError, AttributeError) as e:
            logger.error(
                "Error adding item to shop inventory", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def add_buyable_item(self, item_id: str, base_price: int) -> bool:
        """Add item to buyable items list."""
        try:
            self._buyable_items[item_id] = base_price
            logger.debug("Added buyable item", npc_id=self.npc_id, item_id=item_id, base_price=base_price)
            return True
        except (TypeError, AttributeError) as e:
            logger.error("Error adding buyable item", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def buy_from_player(self, player_id: str, item: dict[str, Any]) -> bool:
        """Buy item from player."""
        try:
            item_id = item.get("id")
            if item_id not in self._buyable_items:
                logger.warning("Item not in buyable list", npc_id=self.npc_id, item_id=item_id)
                return False

            # Add to NPC inventory
            self.add_item_to_inventory(item)
            logger.info("Bought item from player", npc_id=self.npc_id, player_id=player_id, item_id=item_id)
            return True
        except (KeyError, TypeError, AttributeError) as e:
            logger.error("Error buying from player", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def sell_to_player(self, player_id: str, item_id: str, quantity: int = 1) -> bool:
        """Sell item to player."""
        try:
            # Find item in shop inventory
            for item in self._shop_inventory:
                if item.get("id") == item_id and item.get("quantity", 0) >= quantity:
                    # Reduce quantity
                    item["quantity"] = item.get("quantity", 0) - quantity
                    if item["quantity"] <= 0:
                        self._shop_inventory.remove(item)

                    logger.info(
                        "Sold item to player",
                        npc_id=self.npc_id,
                        player_id=player_id,
                        item_id=item_id,
                        quantity=quantity,
                    )
                    return True

            logger.warning("Item not available for sale", npc_id=self.npc_id, item_id=item_id)
            return False
        except (TypeError, KeyError, AttributeError, ValueError) as e:
            logger.error("Error selling to player", npc_id=self.npc_id, error=str(e), error_type=type(e).__name__)
            return False

    def calculate_price(self, base_price: int, markup: float | None = None) -> int:
        """Calculate final price with markup."""
        if markup is None:
            markup = self._behavior_config.get("markup", 1.0)
        return int(base_price * markup)

    def _handle_greet_customer(self, _context: dict[str, Any]) -> bool:
        """Handle greeting customer action."""
        self.speak("Welcome to my shop! How may I help you today?")
        return True

    def _handle_restock_inventory(self, _context: dict[str, Any]) -> bool:
        """Handle restocking inventory action."""
        # Placeholder for restocking logic
        logger.debug("Restocking shop inventory", npc_id=self.npc_id)
        return True
