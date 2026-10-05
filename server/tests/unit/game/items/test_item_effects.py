"""Unit tests for item-use effects (the effect_components tag -> handler registry, #870)."""

from dataclasses import dataclass
from datetime import timedelta
from types import SimpleNamespace
from typing import final
from uuid import UUID, uuid4

import pytest

from server.game.items import item_effects
from server.game.items.item_effects import (
    ITEM_EFFECTS,
    LUCIDITY_RECOVERY_TAG,
    ItemUseContext,
    find_effect,
)
from server.game.items.models import ItemPrototypeModel
from server.services.active_lucidity_service import LucidityActionOnCooldownError

OBSERVER = object()


def _prototype(
    effect_components: list[str], metadata: dict[str, object] | None = None, item_type: str = "consumable"
) -> ItemPrototypeModel:
    return ItemPrototypeModel.model_validate(
        {
            "prototype_id": "consumable.folk_tonic",
            "name": "Folk Tonic",
            "short_description": "a stoppered bottle of folk tonic",
            "long_description": "A squat brown bottle.",
            "item_type": item_type,
            "weight": 0.3,
            "base_value": 15,
            "effect_components": effect_components,
            "metadata": metadata if metadata is not None else {},
        }
    )


TONIC_METADATA: dict[str, object] = {
    "lucidity_recovery": {"cooldown_key": "folk_tonic", "lcd_delta": 3, "cooldown_minutes": 30}
}


@dataclass
class FakeSession:
    commits: int = 0
    rollbacks: int = 0

    async def commit(self) -> None:
        self.commits += 1

    async def rollback(self) -> None:
        self.rollbacks += 1


@dataclass
class FakeResult:
    delta: int
    new_lcd: int


@final
class FakeService:
    """Stands in for ActiveLucidityService; class attributes carry the scripted behavior and call log."""

    on_cooldown = False
    calls: list[dict[str, object]] = []
    observers: list[object] = []

    def __init__(self, session: FakeSession, *, catatonia_observer: object = None) -> None:
        _ = session
        FakeService.observers.append(catatonia_observer)

    async def apply_timed_recovery(
        self, player_id: UUID, *, cooldown_key: str, lcd_delta: int, cooldown: timedelta, location_id: str | None
    ) -> FakeResult:
        FakeService.calls.append(
            {
                "player_id": player_id,
                "cooldown_key": cooldown_key,
                "lcd_delta": lcd_delta,
                "cooldown": cooldown,
                "location_id": location_id,
            }
        )
        if FakeService.on_cooldown:
            raise LucidityActionOnCooldownError(cooldown_key)
        return FakeResult(delta=lcd_delta, new_lcd=57)


@pytest.fixture
def session(monkeypatch: pytest.MonkeyPatch) -> FakeSession:
    fake_session = FakeSession()

    async def fake_get_async_session():
        yield fake_session

    FakeService.on_cooldown = False
    FakeService.calls = []
    FakeService.observers = []
    monkeypatch.setattr(item_effects, "get_async_session", fake_get_async_session)
    monkeypatch.setattr(item_effects, "ActiveLucidityService", FakeService)
    return fake_session


def _context(prototype: ItemPrototypeModel, app: object | None = None) -> ItemUseContext:
    return ItemUseContext(app=app, player_id=uuid4(), room_id="room-1", prototype=prototype)


@pytest.mark.asyncio
async def test_lucidity_recovery_applies_the_prototypes_numbers(session: FakeSession) -> None:
    ctx = _context(_prototype([LUCIDITY_RECOVERY_TAG], TONIC_METADATA))

    outcome = await ITEM_EFFECTS[LUCIDITY_RECOVERY_TAG](ctx)

    assert outcome.ok
    assert "+3 LCD" in outcome.message
    assert "57/100" in outcome.message
    [call] = FakeService.calls
    assert call == {
        "player_id": ctx.player_id,
        "cooldown_key": "folk_tonic",
        "lcd_delta": 3,
        "cooldown": timedelta(minutes=30),
        "location_id": "room-1",
    }
    assert (session.commits, session.rollbacks) == (1, 0)


@pytest.mark.asyncio
async def test_lucidity_recovery_on_cooldown_refuses_and_rolls_back(session: FakeSession) -> None:
    FakeService.on_cooldown = True

    outcome = await ITEM_EFFECTS[LUCIDITY_RECOVERY_TAG](_context(_prototype([LUCIDITY_RECOVERY_TAG], TONIC_METADATA)))

    assert not outcome.ok
    assert outcome.message == "You don't think you can stomach another tonic at this time."
    assert (session.commits, session.rollbacks) == (0, 1)


@pytest.mark.asyncio
@pytest.mark.parametrize("metadata", [{}, {"lucidity_recovery": {"lcd_delta": 3}}])
async def test_lucidity_recovery_with_bad_metadata_does_nothing(
    session: FakeSession, metadata: dict[str, object]
) -> None:
    outcome = await ITEM_EFFECTS[LUCIDITY_RECOVERY_TAG](_context(_prototype([LUCIDITY_RECOVERY_TAG], metadata)))

    assert not outcome.ok
    assert FakeService.calls == []
    assert (session.commits, session.rollbacks) == (0, 0)


@pytest.mark.asyncio
async def test_catatonia_observer_comes_from_the_container_then_app_state(session: FakeSession) -> None:
    _ = session
    prototype = _prototype([LUCIDITY_RECOVERY_TAG], TONIC_METADATA)
    from_container = SimpleNamespace(state=SimpleNamespace(container=SimpleNamespace(catatonia_registry=OBSERVER)))
    from_state = SimpleNamespace(state=SimpleNamespace(container=None, catatonia_registry=OBSERVER))

    for app in (from_container, from_state, None):
        _ = await ITEM_EFFECTS[LUCIDITY_RECOVERY_TAG](_context(prototype, app))

    assert FakeService.observers == [OBSERVER, OBSERVER, None]


def test_find_effect_returns_the_first_tag_with_a_handler() -> None:
    prototype = _prototype(["component.durability", LUCIDITY_RECOVERY_TAG])

    assert find_effect(prototype) is ITEM_EFFECTS[LUCIDITY_RECOVERY_TAG]


@pytest.mark.parametrize("tags", [[], ["component.durability"]])
def test_find_effect_is_none_without_a_handled_tag(tags: list[str]) -> None:
    assert find_effect(_prototype(tags)) is None
