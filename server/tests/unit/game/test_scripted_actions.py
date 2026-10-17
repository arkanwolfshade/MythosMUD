"""Unit tests for scripted actions: the declarative vocabulary and the single runner that executes it."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import cast

import pytest
from pydantic import ValidationError

from server.game import scripted_actions as runner
from server.game.scripted_actions import ScriptedActionContext, run_scripted_actions
from server.models.player import Player
from server.schemas.scripted_actions import (
    ApplyEffectAction,
    CorruptionAtLeastAction,
    NarrateAction,
    QuestActivityAction,
    StartQuestAction,
    on_put_actions,
    parse_scripted_actions,
)
from server.services.corruption_service import CorruptionPersistencePlayer

HOT_EFFECT: dict[str, object] = {"type": "heal_over_time", "healing": 4, "duration": 5}


@dataclass
class FakePersistence:
    saved: list[CorruptionPersistencePlayer] = field(
        default_factory=lambda: cast(list[CorruptionPersistencePlayer], [])
    )

    async def get_player_by_id(self, player_id: uuid.UUID) -> None:  # pragma: no cover - the service is faked
        _ = player_id

    async def save_player(self, player: CorruptionPersistencePlayer) -> None:
        self.saved.append(player)


@dataclass
class FakeQuests:
    started: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
    activity: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))
    fail_start: bool = False

    async def start_quest(self, player_id: uuid.UUID, quest_id: str) -> dict[str, object]:
        if self.fail_start:
            raise RuntimeError("quest store down")
        self.started.append((player_id, quest_id))
        return {"success": True}

    async def record_complete_activity(self, player_id: uuid.UUID, activity_target: str) -> None:
        self.activity.append((player_id, activity_target))


@dataclass
class Rig:
    player: Player
    persistence: FakePersistence
    quests: FakeQuests
    narrated: list[str]
    adjustments: list[int]

    def context(self, *, with_quests: bool = True) -> ScriptedActionContext:
        return ScriptedActionContext(
            player=self.player, persistence=self.persistence, quest_service=self.quests if with_quests else None
        )


def _player(corruption: int = 0) -> Player:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.set_stats({"corruption": corruption})
    player.set_status_effects([])
    return player


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    narrated: list[str] = []
    adjustments: list[int] = []

    async def fake_deliver(player_id: uuid.UUID | str, message: str) -> dict[str, object]:
        _ = player_id
        narrated.append(message)
        return {}

    class FakeCorruptionService:
        def __init__(self, persistence: object) -> None:
            _ = persistence

        async def apply_corruption_adjustment(self, player_id: uuid.UUID, delta: int, *, reason_code: str) -> object:
            _ = player_id, reason_code
            adjustments.append(delta)
            return type("Result", (), {"new_value": max(1, delta)})()

    monkeypatch.setattr(runner, "deliver_personal_system", fake_deliver)
    monkeypatch.setattr(runner, "CorruptionService", FakeCorruptionService)
    return Rig(_player(), FakePersistence(), FakeQuests(), narrated, adjustments)


# --- vocabulary -------------------------------------------------------------------------------------------------


def test_parse_builds_each_action_type_from_plain_json() -> None:
    actions = parse_scripted_actions(
        [
            {"type": "narrate", "text": "A hush."},
            {"type": "apply_effect", "effect": HOT_EFFECT},
            {"type": "corruption_at_least", "value": 1},
            {"type": "start_quest", "quest_id": "act_two"},
            {"type": "quest_activity", "target": "cmd_look"},
        ]
    )

    assert [type(action) for action in actions] == [
        NarrateAction,
        ApplyEffectAction,
        CorruptionAtLeastAction,
        StartQuestAction,
        QuestActivityAction,
    ]


@pytest.mark.parametrize(
    "broken",
    [
        [{"type": "teleport", "room": "x"}],
        [{"type": "narrate"}],
        [{"type": "narrate", "text": "ok"}, {"type": "corruption_at_least", "value": 0}],
        [{"type": "apply_effect", "effect": {"healing": 1}}],
        "not a list",
    ],
)
def test_parse_drops_a_malformed_script_whole_rather_than_running_half_of_it(broken: object) -> None:
    assert parse_scripted_actions(broken) == []


def test_apply_effect_requires_a_typed_effect() -> None:
    with pytest.raises(ValidationError):
        _ = ApplyEffectAction.model_validate({"type": "apply_effect", "effect": {"healing": 1}})


def test_on_put_actions_select_only_the_rules_for_the_item_put() -> None:
    metadata: dict[str, object] = {
        "name": "coffin",
        "on_put": [
            {"item": "jade_amulet", "actions": [{"type": "narrate", "text": "The lid settles."}]},
            {"item": "bone_dice", "actions": [{"type": "narrate", "text": "Rattle."}]},
        ],
    }

    assert on_put_actions(metadata, "jade_amulet") == [NarrateAction(text="The lid settles.")]
    assert on_put_actions(metadata, "wrench") == []


def test_on_put_actions_tolerate_missing_or_malformed_metadata() -> None:
    assert on_put_actions({}, "jade_amulet") == []
    assert on_put_actions({"on_put": "nonsense"}, "jade_amulet") == []
    assert on_put_actions({"on_put": [{"item": "jade_amulet", "actions": [{"type": "teleport"}]}]}, "jade_amulet") == []


# --- runner -----------------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_narrate_sends_the_text_to_the_player(rig: Rig) -> None:
    await run_scripted_actions([NarrateAction(text="The yew sighs.")], rig.context())

    assert rig.narrated == ["The yew sighs."]


@pytest.mark.asyncio
async def test_apply_effect_adds_the_effect_to_the_player_and_saves(rig: Rig) -> None:
    await run_scripted_actions([ApplyEffectAction(effect=HOT_EFFECT)], rig.context())

    assert rig.player.get_status_effects() == [HOT_EFFECT]
    assert rig.persistence.saved == [rig.player]


@pytest.mark.asyncio
async def test_each_apply_effect_is_its_own_copy(rig: Rig) -> None:
    action = ApplyEffectAction(effect=HOT_EFFECT)

    await run_scripted_actions([action, action], rig.context())
    effects = rig.player.get_status_effects()
    effects[0]["remaining"] = 1
    rig.player.set_status_effects(effects)

    assert "remaining" not in action.effect
    assert len(rig.player.get_status_effects()) == 2


@pytest.mark.asyncio
async def test_corruption_at_least_raises_a_clean_soul_to_the_floor(rig: Rig) -> None:
    await run_scripted_actions([CorruptionAtLeastAction(value=1)], rig.context())

    assert rig.adjustments == [1]
    assert rig.player.get_stats()["corruption"] == 1


@pytest.mark.asyncio
async def test_corruption_at_least_is_idempotent_and_never_adds(rig: Rig) -> None:
    rig.player.set_stats({"corruption": 3})

    await run_scripted_actions([CorruptionAtLeastAction(value=1), CorruptionAtLeastAction(value=3)], rig.context())

    assert rig.adjustments == []
    assert rig.player.get_stats()["corruption"] == 3


@pytest.mark.asyncio
async def test_a_later_save_does_not_clobber_the_corruption_the_service_wrote(rig: Rig) -> None:
    """The service edits its own copy of the player; the script's copy must reflect the new value before it saves."""
    await run_scripted_actions([CorruptionAtLeastAction(value=2), ApplyEffectAction(effect=HOT_EFFECT)], rig.context())

    assert rig.player.get_stats()["corruption"] == 2
    assert rig.persistence.saved == [rig.player]


@pytest.mark.asyncio
async def test_start_quest_and_quest_activity_reach_the_quest_service(rig: Rig) -> None:
    await run_scripted_actions(
        [StartQuestAction(quest_id="act_two"), QuestActivityAction(target="cmd_look")], rig.context()
    )

    player_id = uuid.UUID(str(rig.player.player_id))
    assert rig.quests.started == [(player_id, "act_two")]
    assert rig.quests.activity == [(player_id, "cmd_look")]


@pytest.mark.asyncio
async def test_quest_actions_are_skipped_when_there_is_no_quest_service(rig: Rig) -> None:
    await run_scripted_actions(
        [StartQuestAction(quest_id="act_two"), NarrateAction(text="still runs")], rig.context(with_quests=False)
    )

    assert rig.narrated == ["still runs"]


@pytest.mark.asyncio
async def test_a_failing_action_does_not_stop_the_rest_of_the_script(rig: Rig) -> None:
    rig.quests.fail_start = True

    await run_scripted_actions([StartQuestAction(quest_id="act_two"), NarrateAction(text="after")], rig.context())

    assert rig.narrated == ["after"]
