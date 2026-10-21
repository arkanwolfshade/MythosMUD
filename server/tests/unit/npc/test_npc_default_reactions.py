"""Unit tests for default NPC event reaction registration."""

from unittest.mock import MagicMock, patch

from server.npc.npc_default_reactions import (
    DEFAULT_FAREWELL_EMOTE,
    DEFAULT_GREETING_EMOTE,
    DEFAULT_SILENCE_EMOTE,
    register_default_reactions_for_npc,
)


def test_register_shopkeeper_greeting_reads_corruption_from_stats():
    """#815: the greeting reaction is built from the NPC's static base_stats corruption, not
    behavior_config -- passing stats must reach build_corruption_aware_greeting untouched."""
    system = MagicMock()
    with patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as build_greeting:
        register_default_reactions_for_npc(
            "npc-6",
            "shopkeeper",
            {"greeting_message": "Welcome"},
            system,
            stats={"corruption": 75},
        )
    build_greeting.assert_called_once_with("npc-6", 75, "Welcome", as_emote=False)


def test_register_shopkeeper_greeting_defaults_corruption_to_zero_without_stats():
    """No stats argument (or no 'corruption' key in it) must not raise -- defaults to 0 (pure)."""
    system = MagicMock()
    with patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as build_greeting:
        register_default_reactions_for_npc("npc-7", "shopkeeper", {"greeting_message": "Welcome"}, system)
    build_greeting.assert_called_once_with("npc-7", 0, "Welcome", as_emote=False)


def test_register_passive_mob_reactions():
    system = MagicMock()
    register_default_reactions_for_npc(
        "npc-pm",
        "passive_mob",
        {"greeting_message": "Hi", "farewell_message": "Bye", "response_message": "Ok"},
        system,
    )
    reactions = system.register_npc_reactions.call_args[0][1]
    assert len(reactions) == 3


def test_register_shopkeeper_reactions():
    system = MagicMock()
    register_default_reactions_for_npc(
        "npc-1",
        "shopkeeper",
        {"greeting_message": "Welcome", "farewell_message": "Bye", "response_message": "Hmm"},
        system,
    )
    system.register_npc_reactions.assert_called_once()
    reactions = system.register_npc_reactions.call_args[0][1]
    assert len(reactions) == 3


def test_register_aggressive_mob_retaliation_only():
    system = MagicMock()
    register_default_reactions_for_npc("npc-2", "aggressive_mob", {}, system)
    reactions = system.register_npc_reactions.call_args[0][1]
    assert len(reactions) == 1


def test_register_unknown_type_no_reactions():
    system = MagicMock()
    register_default_reactions_for_npc("npc-3", "quest_giver", {}, system)
    system.register_npc_reactions.assert_not_called()


@patch("server.npc.npc_default_reactions.logger")
def test_register_shopkeeper_logs_debug(mock_logger):
    system = MagicMock()
    register_default_reactions_for_npc(
        "npc-5",
        "shopkeeper",
        {"greeting_message": "Hi", "farewell_message": "Bye", "response_message": "Ok"},
        system,
    )
    mock_logger.debug.assert_called_once()


@patch("server.npc.npc_default_reactions.logger")
def test_register_handles_import_error(mock_logger):
    """#815: the greeting branch now builds a corruption-aware reaction
    (build_corruption_aware_greeting) instead of the plain template -- patch that instead."""
    system = MagicMock()
    with patch(
        "server.npc.corruption_reactions.build_corruption_aware_greeting",
        side_effect=TypeError("broken"),
    ):
        register_default_reactions_for_npc("npc-4", "shopkeeper", {}, system)
    mock_logger.error.assert_called_once()


def test_an_npc_with_no_authored_lines_gets_gesture_emotes():
    """#1103: the generic fallbacks are gestures ("<NPC> offers a wary nod..."), not words put in its mouth."""
    system = MagicMock()
    with (
        patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as greeting,
        patch("server.npc.event_reaction_system.NPCEventReactionTemplates.player_left_room_farewell") as farewell,
        patch("server.npc.event_reaction_system.NPCEventReactionTemplates.player_spoke_response") as response,
    ):
        register_default_reactions_for_npc("npc-8", "passive_mob", {}, system)

    greeting.assert_called_once_with("npc-8", 0, DEFAULT_GREETING_EMOTE, as_emote=True)
    farewell.assert_called_once_with("npc-8", DEFAULT_FAREWELL_EMOTE, as_emote=True)
    response.assert_called_once_with("npc-8", DEFAULT_SILENCE_EMOTE, as_emote=True)


def test_authored_lines_stay_speech():
    system = MagicMock()
    with (
        patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as greeting,
        patch("server.npc.event_reaction_system.NPCEventReactionTemplates.player_left_room_farewell") as farewell,
        patch("server.npc.event_reaction_system.NPCEventReactionTemplates.player_spoke_response") as response,
    ):
        register_default_reactions_for_npc(
            "npc-9",
            "passive_mob",
            {"greeting_message": "Hi", "farewell_message": "Bye", "response_message": "Ok"},
            system,
        )

    greeting.assert_called_once_with("npc-9", 0, "Hi", as_emote=False)
    farewell.assert_called_once_with("npc-9", "Bye", as_emote=False)
    response.assert_called_once_with("npc-9", "Ok", as_emote=False)
