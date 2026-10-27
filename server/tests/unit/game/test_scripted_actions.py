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
    DebriefAction,
    NarrateAction,
    QuestActivityAction,
    StartQuestAction,
    on_put_actions,
    parse_scripted_actions,
)
from server.services.corruption_service import CorruptionPersistencePlayer
from server.services.debrief_service import DebriefOutcome
from server.services.lucidity_service import CatatoniaObserverProtocol

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
    debriefs: list[tuple[Player, bool, object | None]]
    stored_effects: list[tuple[uuid.UUID, dict[str, object]]]

    def context(self, *, with_quests: bool = True) -> ScriptedActionContext:
        return ScriptedActionContext(
            player=self.player, persistence=self.persistence, quest_service=self.quests if with_quests else None
        )


def _player(corruption: int = 0) -> Player:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.set_stats({"corruption": corruption})
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

    monkeypatch.setattr(runner, "deliver_personal_system", fake_deliver)  # the debrief's staff recap
    monkeypatch.setattr(runner, "deliver_personal_quest", fake_deliver)  # `narrate`: quest narration
    monkeypatch.setattr(runner, "CorruptionService", FakeCorruptionService)
    debriefs: list[tuple[Player, bool, object | None]] = []

    async def fake_debrief(
        player: Player, *, wants_therapy: bool = False, catatonia_observer: object | None = None
    ) -> DebriefOutcome:
        debriefs.append((player, wants_therapy, catatonia_observer))
        return DebriefOutcome("The staff recap.", completed=True)

    monkeypatch.setattr(runner, "perform_debrief", fake_debrief)
    stored_effects: list[tuple[uuid.UUID, dict[str, object]]] = []

    async def fake_add_content_effect(player_id: uuid.UUID, effect: dict[str, object]) -> str:
        stored_effects.append((player_id, dict(effect)))
        return str(uuid.uuid4())

    # apply_effect stores a player_effects row (ADR-029 step 3b-i); a unit test must not reach the database.
    monkeypatch.setattr(runner, "add_content_effect", fake_add_content_effect)
    return Rig(_player(), FakePersistence(), FakeQuests(), narrated, adjustments, debriefs, stored_effects)


# --- vocabulary -------------------------------------------------------------------------------------------------


def test_parse_builds_each_action_type_from_plain_json() -> None:
    actions = parse_scripted_actions(
        [
            {"type": "narrate", "text": "A hush."},
            {"type": "apply_effect", "effect": HOT_EFFECT},
            {"type": "corruption_at_least", "value": 1},
            {"type": "start_quest", "quest_id": "act_two"},
            {"type": "quest_activity", "target": "cmd_look"},
            {"type": "debrief"},
        ]
    )

    assert [type(action) for action in actions] == [
        NarrateAction,
        ApplyEffectAction,
        CorruptionAtLeastAction,
        StartQuestAction,
        QuestActivityAction,
        DebriefAction,
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
async def test_apply_effect_stores_the_effect_for_the_player_without_a_player_save(rig: Rig) -> None:
    await run_scripted_actions([ApplyEffectAction(effect=HOT_EFFECT)], rig.context())

    assert rig.stored_effects == [(uuid.UUID(str(rig.player.player_id)), HOT_EFFECT)]
    assert rig.persistence.saved == []  # a player_effects row, not a player save


@pytest.mark.asyncio
async def test_each_apply_effect_is_its_own_row_and_leaves_the_action_untouched(rig: Rig) -> None:
    action = ApplyEffectAction(effect=HOT_EFFECT)

    await run_scripted_actions([action, action], rig.context())

    assert len(rig.stored_effects) == 2
    assert action.effect == HOT_EFFECT


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
async def test_an_apply_effect_after_a_corruption_floor_writes_no_stale_player(rig: Rig) -> None:
    """apply_effect no longer saves the player, so it cannot overwrite the corruption the service just wrote."""
    await run_scripted_actions([CorruptionAtLeastAction(value=2), ApplyEffectAction(effect=HOT_EFFECT)], rig.context())

    assert rig.player.get_stats()["corruption"] == 2
    assert rig.persistence.saved == []
    assert len(rig.stored_effects) == 1


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


def test_debrief_action_defaults_to_no_therapy() -> None:
    assert DebriefAction().therapy is False
    assert DebriefAction.model_validate({"type": "debrief", "therapy": True}).therapy is True


@pytest.mark.asyncio
async def test_debrief_runs_the_service_and_narrates_its_message(rig: Rig) -> None:
    observer = object()
    ctx = ScriptedActionContext(
        player=rig.player,
        persistence=rig.persistence,
        quest_service=rig.quests,
        catatonia_observer=cast(CatatoniaObserverProtocol, observer),
    )

    await run_scripted_actions([DebriefAction(therapy=True)], ctx)

    assert rig.debriefs == [(rig.player, True, observer)]
    assert rig.narrated == ["The staff recap."]
