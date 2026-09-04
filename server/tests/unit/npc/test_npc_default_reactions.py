"""Unit tests for default NPC event reaction registration."""

from unittest.mock import MagicMock, patch

from server.npc.npc_default_reactions import register_default_reactions_for_npc


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
    system = MagicMock()
    with patch(
        "server.npc.event_reaction_system.NPCEventReactionTemplates.player_entered_room_greeting",
        side_effect=TypeError("broken"),
    ):
        register_default_reactions_for_npc("npc-4", "shopkeeper", {}, system)
    mock_logger.error.assert_called_once()
