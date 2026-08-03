"""Unit tests for ShopkeeperNPC buy/sell helpers."""

from unittest.mock import MagicMock, patch

from server.npc.shopkeeper_npc import ShopkeeperNPC, _shop_quantity


def _shopkeeper() -> ShopkeeperNPC:
    definition = MagicMock()
    definition.name = "Merchant"
    definition.room_id = "shop_001"
    definition.base_stats = "{}"
    definition.behavior_config = '{"markup": 1.5}'
    definition.ai_integration_stub = "{}"
    definition.npc_type = "shopkeeper"
    return ShopkeeperNPC(definition=definition, npc_id="shop-npc-1")


def test_shop_quantity_coercion():
    assert _shop_quantity(True, 0) == 0
    assert _shop_quantity(5) == 5
    assert _shop_quantity("bad", 2) == 2


def test_add_shop_item_and_inventory():
    npc = _shopkeeper()
    assert npc.add_shop_item({"id": "potion", "quantity": 3}) is True
    assert npc.get_shop_inventory()[0]["id"] == "potion"


def test_add_buyable_item():
    npc = _shopkeeper()
    assert npc.add_buyable_item("herb", 10) is True


def test_buy_from_player_success():
    npc = _shopkeeper()
    npc.add_buyable_item("herb", 10)
    with patch.object(npc, "add_item_to_inventory", return_value=True):
        assert npc.buy_from_player("player-1", {"id": "herb"}) is True


def test_buy_from_player_not_buyable():
    npc = _shopkeeper()
    assert npc.buy_from_player("player-1", {"id": "unknown"}) is False


def test_sell_to_player_reduces_quantity():
    npc = _shopkeeper()
    npc.add_shop_item({"id": "potion", "quantity": 2})
    assert npc.sell_to_player("player-1", "potion", quantity=1) is True
    assert npc.get_shop_inventory()[0]["quantity"] == 1


def test_sell_to_player_removes_depleted_item():
    npc = _shopkeeper()
    npc.add_shop_item({"id": "potion", "quantity": 1})
    assert npc.sell_to_player("player-1", "potion", quantity=1) is True
    assert npc.get_shop_inventory() == []


def test_sell_to_player_not_available():
    npc = _shopkeeper()
    assert npc.sell_to_player("player-1", "missing") is False


def test_calculate_price_default_markup():
    npc = _shopkeeper()
    assert npc.calculate_price(100) == 150


def test_calculate_price_explicit_markup():
    npc = _shopkeeper()
    assert npc.calculate_price(100, markup=2.0) == 200


def test_behavior_handlers():
    npc = _shopkeeper()
    with patch.object(npc, "speak") as speak:
        assert npc._handle_greet_customer({}) is True
        speak.assert_called_once()
    assert npc._handle_restock_inventory({}) is True


def test_get_behavior_rules():
    npc = _shopkeeper()
    rules = npc.get_behavior_rules()
    assert isinstance(rules, list)


def test_add_shop_item_invalid_item():
    npc = _shopkeeper()
    assert npc.add_shop_item(123) is False


def test_add_buyable_item_invalid():
    npc = _shopkeeper()
    buyable = MagicMock()
    type(buyable).__setitem__ = MagicMock(side_effect=AttributeError("bad"))
    npc._buyable_items = buyable
    assert npc.add_buyable_item("herb", 5) is False


def test_buy_from_player_inventory_failure():
    npc = _shopkeeper()
    npc.add_buyable_item("herb", 10)
    with patch.object(npc, "add_item_to_inventory", return_value=False):
        assert npc.buy_from_player("player-1", {"id": "herb"}) is True


def test_buy_from_player_exception():
    npc = _shopkeeper()
    npc.add_buyable_item("herb", 10)
    with patch.object(npc, "add_item_to_inventory", side_effect=KeyError("bad")):
        assert npc.buy_from_player("player-1", {"id": "herb"}) is False


def test_sell_to_player_insufficient_quantity():
    npc = _shopkeeper()
    npc.add_shop_item({"id": "potion", "quantity": 1})
    assert npc.sell_to_player("player-1", "potion", quantity=5) is False


def test_sell_to_player_exception():
    npc = _shopkeeper()
    bad_item = MagicMock()
    bad_item.get = MagicMock(side_effect=TypeError("bad"))
    npc._shop_inventory = [bad_item]
    assert npc.sell_to_player("player-1", "potion") is False


def test_calculate_price_invalid_markup_config():
    definition = MagicMock()
    definition.name = "Merchant"
    definition.room_id = "shop_001"
    definition.base_stats = "{}"
    definition.behavior_config = '{"markup": "not-a-number"}'
    definition.ai_integration_stub = "{}"
    definition.npc_type = "shopkeeper"
    npc = ShopkeeperNPC(definition=definition, npc_id="shop-npc-2")
    assert npc.calculate_price(100) == 100


def test_get_shop_inventory_returns_copy():
    npc = _shopkeeper()
    npc.add_shop_item({"id": "potion", "quantity": 1})
    inventory = npc.get_shop_inventory()
    inventory.clear()
    assert len(npc.get_shop_inventory()) == 1
