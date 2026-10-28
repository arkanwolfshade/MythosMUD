"""Importing chat_npc_system first must not hit a circular import (#1128).

chat_npc_system -> chat_message_helpers -> server.services -> ... -> corruption_service used to ask for
``deliver_personal_system`` while chat_npc_system was still initialising. Inside a test process the import order is
whatever ran first, so the cycle only shows in a fresh interpreter, one per entry point.
"""

import os
import subprocess
import sys

import pytest

from server.utils.project_paths import get_project_root

ENTRY_POINTS = [
    "server.game.chat_npc_system",
    "server.game.movement_helpers",
    "server.services.corruption_service",
]


@pytest.mark.parametrize("module", ENTRY_POINTS)
def test_the_module_imports_first_in_a_fresh_interpreter(module: str) -> None:
    result = subprocess.run(  # noqa: S603  # Reason: fixed argv, no shell, module names are constants above
        [sys.executable, "-c", f"import {module}"],
        cwd=get_project_root(),
        env=os.environ.copy(),
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )

    assert result.returncode == 0, result.stderr[-1500:]
