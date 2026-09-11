"""Unit tests for default NPC event reaction registration."""

from unittest.mock import MagicMock, patch

from server.npc.npc_default_reactions import register_default_reactions_for_npc


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
    build_greeting.assert_called_once_with("npc-6", 75, "Welcome")


def test_register_shopkeeper_greeting_defaults_corruption_to_zero_without_stats():
    """No stats argument (or no 'corruption' key in it) must not raise -- defaults to 0 (pure)."""
    system = MagicMock()
    with patch("server.npc.corruption_reactions.build_corruption_aware_greeting") as build_greeting:
        register_default_reactions_for_npc("npc-7", "shopkeeper", {"greeting_message": "Welcome"}, system)
    build_greeting.assert_called_once_with("npc-7", 0, "Welcome")


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
