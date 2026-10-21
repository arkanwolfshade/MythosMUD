"""
Unit tests for NPC <-> player corruption relationship (#815 PR-4).

Covers both halves of server/npc/corruption_reactions.py: the discrete speech matrix
(_pick_greeting / build_corruption_aware_greeting) and the continuous aggro affinity curve
(corruption_hostility_scale).
"""

from __future__ import annotations

import uuid
from unittest.mock import patch

from server.models.corruption import CorruptionTier
from server.npc.corruption_reactions import (
    RECOIL_LINE,
    WELCOME_LINE,
    _pick_greeting,  # pyright: ignore[reportPrivateUsage] -- tested directly to isolate the tier-boundary logic from the reaction-firing plumbing tested separately below
    build_corruption_aware_greeting,
    corruption_hostility_scale,
)
from server.services.corruption_tier_cache import corruption_tier_cache


def _reset_cache():
    corruption_tier_cache._tiers.clear()  # noqa: SLF001  # pyright: ignore[reportPrivateUsage] -- test cleanup, mirrors test_corruption_service.py's identical fixture


# --- Speech matrix -----------------------------------------------------------------


def test_pick_greeting_uses_normal_greeting_for_pure_player():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.PURE)
    assert _pick_greeting(90, "Welcome!", player_id) == "Welcome!"


def test_pick_greeting_uses_normal_greeting_for_touched_player():
    """#815: the permanent scar (touched) stays private -- no special greeting for it."""
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.TOUCHED)
    assert _pick_greeting(90, "Welcome!", player_id) == "Welcome!"


def test_pick_greeting_welcomes_marked_player_from_tainted_npc():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.MARKED)
    assert _pick_greeting(25, "Welcome!", player_id) == WELCOME_LINE


def test_pick_greeting_recoils_from_marked_player_when_npc_is_untainted():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.CORRUPTED)
    assert _pick_greeting(0, "Welcome!", player_id) == RECOIL_LINE


def test_pick_greeting_boundary_at_npc_tainted_threshold():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.WARPED)
    assert _pick_greeting(24, "Welcome!", player_id) == RECOIL_LINE
    assert _pick_greeting(25, "Welcome!", player_id) == WELCOME_LINE


def test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.MARKED)
    reaction = build_corruption_aware_greeting("npc-1", 80, "Hello!")

    from server.events.event_types import PlayerEnteredRoom

    event = PlayerEnteredRoom(player_id=player_id, room_id="room-1")
    context = {"npc_id": "npc-1", "current_room": "room-1", "name": "Ezekiel"}
    assert reaction.should_trigger(event, context) is True

    with patch("server.game.chat_npc_system.schedule_npc_room_message") as schedule:
        assert reaction.execute(event, context) is True
    schedule.assert_called_once()
    assert schedule.call_args.kwargs["message"] == WELCOME_LINE
    assert schedule.call_args.kwargs["npc_id"] == "npc-1"
    # #1103: the reaction to what only this player carries is private to this player.
    assert schedule.call_args.kwargs["target_player_id"] == player_id


def test_a_marked_players_greeting_never_reaches_the_room():
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.CORRUPTED)
    reaction = build_corruption_aware_greeting("npc-1", 0, "Hello!")

    from server.events.event_types import PlayerEnteredRoom

    event = PlayerEnteredRoom(player_id=player_id, room_id="room-1")
    with (
        patch("server.game.chat_npc_system.schedule_npc_room_message") as emote,
        patch("server.game.chat_npc_system.schedule_npc_room_speech") as speech,
    ):
        assert reaction.execute(event, {"current_room": "room-1"}) is True
    speech.assert_not_called()
    assert emote.call_args.kwargs["message"] == RECOIL_LINE
    assert emote.call_args.kwargs["target_player_id"] == player_id


def test_an_authored_greeting_stays_speech_and_a_default_gesture_is_a_room_emote():
    """#1103: words an author wrote are the NPC's speech; the generic fallback is a gesture for the whole room."""
    _reset_cache()
    player_id = str(uuid.uuid4())
    corruption_tier_cache.set_tier(player_id, CorruptionTier.PURE)

    from server.events.event_types import PlayerEnteredRoom

    event = PlayerEnteredRoom(player_id=player_id, room_id="room-1")
    context = {"current_room": "room-1"}

    with (
        patch("server.game.chat_npc_system.schedule_npc_room_message") as emote,
        patch("server.game.chat_npc_system.schedule_npc_room_speech") as speech,
    ):
        assert build_corruption_aware_greeting("npc-1", 0, "Well met.").execute(event, context) is True
    emote.assert_not_called()
    assert speech.call_args.kwargs["message"] == "Well met."

    with (
        patch("server.game.chat_npc_system.schedule_npc_room_message") as emote,
        patch("server.game.chat_npc_system.schedule_npc_room_speech") as speech,
    ):
        assert build_corruption_aware_greeting("npc-1", 0, "nods.", as_emote=True).execute(event, context) is True
    speech.assert_not_called()
    assert emote.call_args.kwargs["message"] == "nods."
    assert "target_player_id" not in emote.call_args.kwargs


def test_build_corruption_aware_greeting_does_not_trigger_for_a_different_room():
    reaction = build_corruption_aware_greeting("npc-1", 80, "Hello!")
    from server.events.event_types import PlayerEnteredRoom

    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="elsewhere")
    context = {"npc_id": "npc-1", "current_room": "room-1"}
    assert reaction.should_trigger(event, context) is False


def test_build_corruption_aware_greeting_no_op_without_a_known_room():
    reaction = build_corruption_aware_greeting("npc-1", 80, "Hello!")
    from server.events.event_types import PlayerEnteredRoom

    event = PlayerEnteredRoom(player_id=str(uuid.uuid4()), room_id="room-1")
    context = {"npc_id": "npc-1", "current_room": "unknown"}
    with patch("server.game.chat_npc_system.schedule_npc_room_speech") as schedule:
        assert reaction.execute(event, context) is False
    schedule.assert_not_called()


# --- Aggro affinity ----------------------------------------------------------------


def test_corruption_hostility_scale_neutral_when_either_side_missing():
    assert corruption_hostility_scale(None, 50) == 1.0
    assert corruption_hostility_scale(50, None) == 1.0
    assert corruption_hostility_scale(None, None) == 1.0


def test_corruption_hostility_scale_softens_when_identical():
    assert corruption_hostility_scale(60, 60) == 0.5
    assert corruption_hostility_scale(0, 0) == 0.5


def test_corruption_hostility_scale_sharpens_with_gap():
    assert corruption_hostility_scale(0, 100) == 1.5
    assert corruption_hostility_scale(100, 0) == 1.5


def test_corruption_hostility_scale_intermediate_gap():
    assert corruption_hostility_scale(20, 70) == 0.5 + 0.5


if __name__ == "__main__":
    # ponytail: smallest runnable check for both halves of the module.
    assert corruption_hostility_scale(None, None) == 1.0
    assert corruption_hostility_scale(50, 50) == 0.5
    _reset_cache()
    demo_player = str(uuid.uuid4())
    corruption_tier_cache.set_tier(demo_player, CorruptionTier.MARKED)
    assert _pick_greeting(30, "Hi", demo_player) == WELCOME_LINE
    print("corruption_reactions demo OK")
