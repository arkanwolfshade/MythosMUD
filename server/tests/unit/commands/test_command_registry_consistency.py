"""Regression guard for #813: the command registry has three sources of truth that must
agree -- CommandType, the parser's command-type-to-factory-method map, and
_COMMAND_HANDLERS. A key present in one but not the others is either unreachable
(handler with no CommandType/factory entry) or broken (CommandType with no factory
entry, which clears the parser's initial gate but then fails at command creation).

#813 itself was six handlers (pray, meditate, therapy, folk_tonic, group_solace,
debrief) registered in _COMMAND_HANDLERS with no CommandType member. Investigating it
surfaced three more (read, stop, teach) with the same defect, plus a fourth failure
mode: 'global' had a CommandType member but no factory entry, so it passed the parser's
`valid_commands` check and then died at `_create_command_object` with 'Unsupported
command: global' instead of 'Unknown command: global'.

These tests import the live registries -- never re-derive them from source text -- so
a future divergence fails here instead of shipping as a silent dead command.
"""

from server.commands import command_service
from server.models.command_base import CommandType
from server.utils.command_parser import command_parser

# Commands that are intentionally NOT symmetric across all three registries, with the
# reason. Do not add an entry here to silence a real gap -- add the missing
# CommandType/factory/handler instead.
ALLOWED_GAPS = {
    "l": "single-letter alias; _resolve_command_alias maps it to 'local' before factory lookup",
    "g": "single-letter alias; _resolve_command_alias maps it to 'global' before factory lookup",
    "spawn": "builds an NPCCommand (alias for 'npc spawn'); routed to the 'npc' handler by command_type",
}

_COMMAND_TYPE_VALUES = {cmd.value for cmd in CommandType}
_FACTORY_KEYS = set(
    command_parser._command_factory.keys()  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access  # Reason: the parser's internal command-type-to-factory map is exactly what this guard must inspect; there is no public accessor and adding one solely for this test would be speculative API surface
)
_HANDLER_KEYS = set(
    command_service._COMMAND_HANDLERS.keys()  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access  # Reason: this guard exists specifically to inspect the module's private handler registry; there is no public accessor and adding one solely for this test would be speculative API surface
)


def test_every_handler_has_a_command_type():
    """Every _COMMAND_HANDLERS key must be parseable, i.e. present in CommandType.

    A handler missing here is dead code: CommandParser.parse_command() rejects the
    command with 'Unknown command: <name>' before _COMMAND_HANDLERS is ever consulted.
    This is the exact bug #813 reported (pray, meditate, therapy, folk_tonic,
    group_solace, debrief) plus three more it missed (read, stop, teach).
    """
    unreachable = _HANDLER_KEYS - _COMMAND_TYPE_VALUES - set(ALLOWED_GAPS)
    assert not unreachable, (
        f"Handlers registered in _COMMAND_HANDLERS but missing from CommandType "
        f"(unreachable -- parse_command() rejects them before the handler ever runs): "
        f"{sorted(unreachable)}. Add each to CommandType, or to ALLOWED_GAPS with a reason "
        f"if the gap is intentional."
    )


def test_every_handler_has_a_factory():
    """Every _COMMAND_HANDLERS key must also have a factory entry, i.e. be constructable.

    A CommandType member alone is not sufficient -- parse_command() also needs a
    factory method to build the Command object before the handler can run.
    """
    unconstructable = _HANDLER_KEYS - _FACTORY_KEYS - set(ALLOWED_GAPS)
    assert not unconstructable, (
        f"Handlers registered in _COMMAND_HANDLERS but with no factory entry in "
        f"CommandParser._command_factory (the command object can never be built, so "
        f"the handler is unreachable even if CommandType has a matching member): "
        f"{sorted(unconstructable)}. Register a factory method, or add to ALLOWED_GAPS."
    )


def test_every_command_type_has_a_factory():
    """Every CommandType member must have a factory entry.

    Without one, the command clears CommandParser's initial `valid_commands` gate and
    then fails inside `_create_command_object` with 'Unsupported command: <name>' -- a
    different, more confusing failure than 'Unknown command'. This is exactly what
    happened to 'global' before create_global_command existed.
    """
    orphaned = _COMMAND_TYPE_VALUES - _FACTORY_KEYS - set(ALLOWED_GAPS)
    assert not orphaned, (
        f"CommandType members with no factory entry (these pass the parser's initial "
        f"gate and then fail with 'Unsupported command: <name>'): {sorted(orphaned)}. "
        f"Register a factory method, or add to ALLOWED_GAPS."
    )
