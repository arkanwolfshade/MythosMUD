"""
ADR-024: hallucination code never chooses a message category.

A hallucinated line must carry exactly the category of the real thing it imitates, which only holds if it flows
through the same shared builder. So no module that produces hallucinated or phantom output may import
``MessageCategory`` (or the module that defines it), nor spell a category value out as a string literal.

The scan is static (``ast``, nothing is imported). ``HALLUCINATION_MODULES`` is the audited list; a new module
with ``hallucination`` or ``phantom`` in its name fails ``test_every_hallucination_named_module_is_listed`` until
someone adds it here, which is the moment to confirm it builds its output through a shared builder.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from server.constants.message_category import MessageCategory

_SERVER_ROOT = Path(__file__).resolve().parents[3]

# Modules that produce, schedule, or deliver hallucinated or phantom player-visible output.
HALLUCINATION_MODULES = frozenset(
    {
        "commands/admin_hallucinate_command.py",
        "game/chat_npc_system.py",  # fake NPC whispers
        "realtime/room_update_event_builder.py",  # builds the per-viewer hallucinated room payloads
        "realtime/room_viewer_fanout.py",
        "realtime/websocket_room_updates.py",  # fans room updates out through room_viewer_fanout
        "services/exit_hallucination.py",
        "services/fake_hallucination_service.py",
        "services/fake_sender_registry.py",
        "services/hallucination_frequency_service.py",
        "services/hallucination_rng.py",
        "services/passive_lucidity_flux/hallucinations.py",
        "services/passive_lucidity_flux/service.py",  # schedules passive hallucination ticks
        "services/phantom_hostile_service.py",
        "services/phantom_visibility.py",
    }
)

_CATEGORY_VALUES = frozenset(member.value for member in MessageCategory)


def _import_violations(node: ast.Import | ast.ImportFrom) -> list[str]:
    """What an import statement pulls in that chooses a message category."""
    if isinstance(node, ast.Import):
        return [f"imports {alias.name}" for alias in node.names if alias.name.endswith("message_category")]
    module = node.module or ""
    found = [f"imports from {module}"] if module.endswith("message_category") else []
    found.extend(
        f"imports {alias.name}" for alias in node.names if alias.name in {"MessageCategory", "message_category"}
    )
    return found


def category_violations(source: str) -> list[str]:
    """What in ``source`` chooses or names a message category: imports of it, or literal category values."""
    found: list[str] = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import | ast.ImportFrom):
            found.extend(_import_violations(node))
        elif isinstance(node, ast.Constant) and node.value in _CATEGORY_VALUES:
            found.append(f"literal category {node.value!r}")
    return found


@pytest.mark.parametrize("relative_path", sorted(HALLUCINATION_MODULES))
def test_hallucination_module_never_chooses_a_category(relative_path: str) -> None:
    path = _SERVER_ROOT / relative_path
    assert path.is_file(), f"{relative_path} moved or was renamed: update HALLUCINATION_MODULES"
    assert category_violations(path.read_text(encoding="utf-8")) == []


def test_every_hallucination_named_module_is_listed() -> None:
    """A new module named for hallucination or phantoms must be added to the audited list above."""
    named = {
        path.relative_to(_SERVER_ROOT).as_posix()
        for path in _SERVER_ROOT.rglob("*.py")
        if "tests" not in path.relative_to(_SERVER_ROOT).parts and ("hallucin" in path.name or "phantom" in path.name)
    }
    assert named <= HALLUCINATION_MODULES, f"add to HALLUCINATION_MODULES: {sorted(named - HALLUCINATION_MODULES)}"


@pytest.mark.parametrize(
    "source",
    [
        "from server.constants.message_category import MessageCategory",
        "from ..constants.message_category import MessageCategory as MC",
        "from ..constants import message_category",
        "import server.constants.message_category",
        "label = 'chat.whisper'",
    ],
)
def test_scanner_flags_each_way_of_choosing_a_category(source: str) -> None:
    """Guard the scanner itself so the ban cannot pass vacuously."""
    assert category_violations(source)


def test_scanner_ignores_ordinary_code() -> None:
    assert (
        category_violations("from ..constants import spawn_defaults\nname = 'whisper'\nroom = 'room.exit.north'") == []
    )
