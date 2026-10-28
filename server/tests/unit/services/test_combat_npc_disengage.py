"""Unit tests for NPC disengage: an NPC with disengage_at_target_dp_ratio breaks off once its target is hurt enough."""

# pyright: reportPrivateUsage=false
# Reason: the turn wiring test drives the module-private _resolve_npc_target seam, as its sibling tests do.

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast, override

import pytest

from server.constants.npc_disposition import NpcDisposition
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import combat_npc_disengage as disengage_module
from server.services import combat_turn_participant_actions as turn_actions
from server.services.combat_npc_disengage import (
    DEFAULT_DISENGAGE_LINE,
    disengage,
    disengage_ratio,
    should_disengage,
)
from server.services.combat_service import CombatService

NPC_STRING_ID = "ghoul_hostile_001"


def _npc(**behavior: object) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="Ghoul",
        current_dp=40,
        max_dp=40,
        dexterity=50,
        npc_behavior_config=dict(behavior) if behavior else None,
    )


def _target(current_dp: int, max_dp: int = 100) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=current_dp,
        max_dp=max_dp,
        dexterity=50,
    )


# --- policy -----------------------------------------------------------------------------------------------------


def test_ratio_is_none_without_config_or_with_an_unusable_value() -> None:
    assert disengage_ratio(_npc()) is None
    for bad in ("0.25", 0, -0.5, 1.5, True, None):
        assert disengage_ratio(_npc(disengage_at_target_dp_ratio=bad)) is None


def test_ratio_accepts_a_fraction_up_to_one() -> None:
    assert disengage_ratio(_npc(disengage_at_target_dp_ratio=0.25)) == 0.25
    assert disengage_ratio(_npc(disengage_at_target_dp_ratio=1)) == 1.0


@pytest.mark.parametrize(("target_dp", "expected"), [(100, False), (26, False), (25, True), (10, True), (1, True)])
def test_the_npc_disengages_once_the_target_is_at_or_below_the_ratio(target_dp: int, expected: bool) -> None:
    assert should_disengage(_npc(disengage_at_target_dp_ratio=0.25), _target(target_dp)) is expected


def test_an_npc_without_the_setting_never_disengages() -> None:
    assert should_disengage(_npc(), _target(1)) is False


def test_a_target_with_no_max_dp_never_triggers_a_disengage() -> None:
    assert should_disengage(_npc(disengage_at_target_dp_ratio=0.25), _target(0, max_dp=0)) is False


# --- orchestration ----------------------------------------------------------------------------------------------


@dataclass
class FakeMessaging:
    sent: list[tuple[str, str, str, str, NpcDisposition | None]] = field(
        default_factory=lambda: cast(list[tuple[str, str, str, str, NpcDisposition | None]], [])
    )

    async def broadcast_npc_disengage(
        self,
        room_id: str,
        combat_id: str,
        npc_name: str,
        clause: str,
        npc_disposition: NpcDisposition | None = None,
    ) -> dict[str, object]:
        self.sent.append((room_id, combat_id, npc_name, clause, npc_disposition))
        return {}


@dataclass
class FakeNpcService:
    messaging: FakeMessaging
    string_id: str | None = NPC_STRING_ID

    def get_messaging_integration(self) -> FakeMessaging:
        return self.messaging

    def get_npc_disposition(self, participant_id: uuid.UUID) -> NpcDisposition:
        _ = participant_id
        return NpcDisposition.AGGRESSIVE_MOB

    def get_original_string_id(self, uuid_id: uuid.UUID) -> str | None:
        _ = uuid_id
        return self.string_id


@dataclass
class FakeCombatService:
    npc_service: FakeNpcService | None
    ended: list[tuple[uuid.UUID, str]] = field(default_factory=lambda: cast(list[tuple[uuid.UUID, str]], []))

    def get_npc_combat_integration_service(self) -> FakeNpcService | None:
        return self.npc_service

    async def end_combat(self, combat_id: uuid.UUID, reason: str = "Combat ended") -> None:
        self.ended.append((combat_id, reason))


@dataclass
class FakeLifecycle:
    despawned: list[tuple[str, str]] = field(default_factory=lambda: cast(list[tuple[str, str]], []))

    def despawn_npc(self, npc_id: str, reason: str = "manual") -> bool:
        self.despawned.append((npc_id, reason))
        return True


def _service(npc_service: FakeNpcService | None) -> CombatService:
    return cast(CombatService, cast(object, FakeCombatService(npc_service)))


def _combat(npc: CombatParticipant) -> CombatInstance:
    return CombatInstance(room_id="room_6", participants={npc.participant_id: npc})


@pytest.mark.asyncio
async def test_disengage_announces_ends_the_combat_and_despawns_the_npc() -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25, disengage_line="recoils, snarling, and melts into the dark.")
    combat = _combat(npc)
    messaging = FakeMessaging()
    service = _service(FakeNpcService(messaging))
    lifecycle = FakeLifecycle()

    await disengage(service, combat, npc, lifecycle)

    assert messaging.sent == [
        (
            "room_6",
            str(combat.combat_id),
            "Ghoul",
            "recoils, snarling, and melts into the dark.",
            NpcDisposition.AGGRESSIVE_MOB,
        )
    ]
    assert cast(FakeCombatService, cast(object, service)).ended == [(combat.combat_id, "Ghoul disengaged")]
    assert lifecycle.despawned == [(NPC_STRING_ID, "disengaged")]


@dataclass
class EndedFirstMessaging(FakeMessaging):
    """Records whether the combat had already ended when the disengage line went out."""

    combat_service: FakeCombatService | None = None
    ended_before_line: list[bool] = field(default_factory=lambda: cast(list[bool], []))

    @override
    async def broadcast_npc_disengage(
        self,
        room_id: str,
        combat_id: str,
        npc_name: str,
        clause: str,
        npc_disposition: NpcDisposition | None = None,
    ) -> dict[str, object]:
        self.ended_before_line.append(self.combat_service is not None and bool(self.combat_service.ended))
        return await super().broadcast_npc_disengage(room_id, combat_id, npc_name, clause, npc_disposition)


@pytest.mark.asyncio
async def test_disengage_ends_the_combat_before_announcing_it() -> None:
    """A client acting on the line (e.g. `go east`) must find the server already out of combat."""
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    messaging = EndedFirstMessaging()
    fake_service = FakeCombatService(FakeNpcService(messaging))
    messaging.combat_service = fake_service

    await disengage(cast(CombatService, cast(object, fake_service)), _combat(npc), npc, FakeLifecycle())

    assert messaging.ended_before_line == [True]


@pytest.mark.asyncio
async def test_disengage_uses_the_default_line_when_the_npc_declares_none() -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    messaging = FakeMessaging()

    await disengage(_service(FakeNpcService(messaging)), _combat(npc), npc, FakeLifecycle())

    assert messaging.sent[0][3] == DEFAULT_DISENGAGE_LINE


@pytest.mark.asyncio
async def test_disengage_still_ends_combat_without_messaging_or_a_lifecycle_manager() -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    service = _service(None)

    await disengage(service, _combat(npc), npc, None)

    assert len(cast(FakeCombatService, cast(object, service)).ended) == 1


@pytest.mark.asyncio
async def test_disengage_ends_combat_but_cannot_despawn_an_npc_with_no_string_id() -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    lifecycle = FakeLifecycle()
    service = _service(FakeNpcService(FakeMessaging(), string_id=None))

    await disengage(service, _combat(npc), npc, lifecycle)

    assert len(cast(FakeCombatService, cast(object, service)).ended) == 1
    assert lifecycle.despawned == []


# --- wiring into the NPC turn -----------------------------------------------------------------------------------


@dataclass
class AttackRecorder:
    attacks: int = 0
    disengaged: list[CombatParticipant] = field(default_factory=lambda: cast(list[CombatParticipant], []))


@pytest.fixture(name="turn")
def _turn(monkeypatch: pytest.MonkeyPatch) -> AttackRecorder:
    recorder = AttackRecorder()

    async def fake_attack(service: object, npc: CombatParticipant, target: CombatParticipant, tick: int) -> None:
        _ = service, target
        recorder.attacks += 1
        npc.last_action_tick = tick

    async def fake_disengage(
        service: object, combat: CombatInstance, npc: CombatParticipant, lifecycle: object
    ) -> None:
        _ = service, combat, lifecycle
        recorder.disengaged.append(npc)

    def fake_lifecycle(config: object) -> None:
        _ = config

    monkeypatch.setattr(turn_actions, "_execute_npc_attack", fake_attack)
    monkeypatch.setattr(turn_actions, "disengage", fake_disengage)
    monkeypatch.setattr(turn_actions, "npc_lifecycle_manager", fake_lifecycle)
    monkeypatch.setattr(turn_actions, "get_config", lambda: cast(object, None))
    return recorder


def _resolve_to(monkeypatch: pytest.MonkeyPatch, target: CombatParticipant) -> None:
    async def resolve(combat: object, npc: CombatParticipant, service: object) -> CombatParticipant | None:
        _ = combat, npc, service
        return target

    monkeypatch.setattr(turn_actions, "_resolve_npc_target", resolve)


@pytest.mark.asyncio
async def test_a_hurt_enough_target_makes_the_npc_break_off_instead_of_attacking(
    monkeypatch: pytest.MonkeyPatch, turn: AttackRecorder
) -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    target = _target(20)
    _resolve_to(monkeypatch, target)

    await turn_actions.process_npc_turn(_service(None), _combat(npc), npc, current_tick=3)

    assert turn.disengaged == [npc]
    assert turn.attacks == 0


@pytest.mark.asyncio
async def test_a_healthy_target_still_gets_attacked(monkeypatch: pytest.MonkeyPatch, turn: AttackRecorder) -> None:
    npc = _npc(disengage_at_target_dp_ratio=0.25)
    _resolve_to(monkeypatch, _target(80))

    await turn_actions.process_npc_turn(_service(None), _combat(npc), npc, current_tick=3)

    assert turn.disengaged == []
    assert turn.attacks == 1


def test_the_lifecycle_resolver_reads_the_manager_off_the_app_container() -> None:
    lifecycle = FakeLifecycle()
    app = SimpleNamespace(state=SimpleNamespace(container=SimpleNamespace(npc_lifecycle_manager=lifecycle)))

    assert disengage_module.npc_lifecycle_manager(SimpleNamespace(_app_instance=app)) is lifecycle
    assert disengage_module.npc_lifecycle_manager(SimpleNamespace()) is None
