"""Unit tests for QuestRewardsMixin (quest reward application, split out of QuestService)."""

import uuid
from typing import final

import pytest

from server.game.quest.quest_rewards import QuestRewardsMixin, SpellLearner, XpGranter
from server.schemas.quest import QuestDefinitionSchema


class _Levels:
    def __init__(self) -> None:
        self.granted: list[tuple[uuid.UUID, int]] = []

    async def grant_xp(self, player_id: uuid.UUID, amount: int) -> object:
        self.granted.append((player_id, amount))
        return None


class _Spells:
    def __init__(self) -> None:
        self.learned: list[tuple[uuid.UUID, str, str]] = []

    async def learn_spell_from_quest(self, player_id: uuid.UUID, quest_id: str, spell_id: str) -> object:
        self.learned.append((player_id, quest_id, spell_id))
        return None


class _Inventory:
    def __init__(self, *, has_slot: bool = True) -> None:
        self.has_slot: bool = has_slot
        self.added: list[tuple[uuid.UUID, str, int]] = []

    def has_inventory_slot(self, _player_id: uuid.UUID) -> bool:
        return self.has_slot

    async def add_item_to_inventory(self, player_id: uuid.UUID, item_id: str, count: int) -> None:
        self.added.append((player_id, item_id, count))


@final
class _Host(QuestRewardsMixin):
    """Stands in for QuestService, which provides these services."""

    def __init__(
        self,
        levels: XpGranter | None = None,
        spells: SpellLearner | None = None,
        inventory: object | None = None,
    ) -> None:
        self._level_service = levels
        self._spell_learning_service = spells
        self._inventory_service = inventory
        self._async_persistence = None


def _definition(rewards: list[dict[str, object]]) -> QuestDefinitionSchema:
    return QuestDefinitionSchema.model_validate(
        {
            "name": "test_quest",
            "title": "Test Quest",
            "description": "A quest for reward tests.",
            "goals": [{"type": "complete_activity", "target": "exit_somewhere", "config": {}}],
            "rewards": rewards,
            "triggers": [],
            "requires_all": [],
            "requires_any": [],
            "auto_complete": True,
            "turn_in_entities": [],
        }
    )


@pytest.mark.asyncio
async def test_rewards_grant_xp_spell_and_item() -> None:
    levels, spells, inventory = _Levels(), _Spells(), _Inventory()
    player_id = uuid.uuid4()
    rewards: list[dict[str, object]] = [
        {"type": "xp", "config": {"amount": 10}},
        {"type": "spell", "config": {"spell": "elder_sign"}},
        {"type": "item", "config": {"item_id": "pack_dark_ages.weapon.sling"}},
    ]

    await _Host(levels, spells, inventory)._apply_rewards(player_id, "test_quest", _definition(rewards))  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert levels.granted == [(player_id, 10)]
    assert spells.learned == [(player_id, "test_quest", "elder_sign")]
    assert inventory.added == [(player_id, "pack_dark_ages.weapon.sling", 1)]


@pytest.mark.asyncio
async def test_malformed_or_unservable_rewards_are_skipped() -> None:
    """Wrong-typed config, missing services, and a full inventory never raise or grant."""
    levels, spells, inventory = _Levels(), _Spells(), _Inventory(has_slot=False)
    rewards: list[dict[str, object]] = [
        {"type": "xp", "config": {"amount": "ten"}},
        {"type": "xp", "amount": 10},  # top-level amount: config is empty (the old tutorial shape)
        {"type": "spell", "config": {"spell_id": 7}},
        {"type": "item", "config": {"item_id": "pack_dark_ages.weapon.sling"}},
        {"type": "respawn_room", "config": {"room_id": "earth_arkhamcity_sanitarium_room_foyer_001"}},
    ]

    await _Host(levels, spells, inventory)._apply_rewards(uuid.uuid4(), "test_quest", _definition(rewards))  # pyright: ignore[reportPrivateUsage] -- unit-tested directly
    await _Host()._apply_rewards(uuid.uuid4(), "test_quest", _definition(rewards))  # pyright: ignore[reportPrivateUsage] -- unit-tested directly

    assert levels.granted == []
    assert spells.learned == []
    assert inventory.added == []


def test_turn_in_inventory_full_error_only_for_item_rewards() -> None:
    player_id = uuid.uuid4()
    item = _definition([{"type": "item", "config": {"item_id": "pack_dark_ages.weapon.sling"}}])
    xp_only = _definition([{"type": "xp", "config": {"amount": 5}}])

    full = _Host(inventory=_Inventory(has_slot=False))
    assert full._turn_in_inventory_full_error(player_id, item) == {  # pyright: ignore[reportPrivateUsage] -- unit-tested directly
        "success": False,
        "message": "Your inventory is full. Free a slot before turning in.",
    }
    assert full._turn_in_inventory_full_error(player_id, xp_only) is None  # pyright: ignore[reportPrivateUsage] -- unit-tested directly
    assert _Host(inventory=_Inventory())._turn_in_inventory_full_error(player_id, item) is None  # pyright: ignore[reportPrivateUsage] -- unit-tested directly
    assert _Host()._turn_in_inventory_full_error(player_id, item) is None  # pyright: ignore[reportPrivateUsage] -- unit-tested directly
