#!/usr/bin/env python3
"""
Fix imports in merged test files.

When legacy files were merged, their relative imports may be incorrect
due to changed directory depth. This script fixes them.
"""

import re
import sys
from pathlib import Path

# Base path
SCRIPT_DIR = Path(__file__).parent
BASE = SCRIPT_DIR.parent

# Patterns to fix - convert relative imports to absolute
IMPORT_FIXES = [
    # Two-level relative imports (from ..module)
    (r"from \.\.api\.", "from server.api."),
    (r"from \.\.auth\.", "from server.auth."),
    (r"from \.\.events\.event_types import", "from server.events.event_types import"),
    (r"from \.\.events import", "from server.events import"),
    (r"from \.\.events\.", "from server.events."),
    (r"from \.\.realtime\.", "from server.realtime."),
    (r"from \.\.models\.", "from server.models."),
    (r"from \.\.models import", "from server.models import"),
    (r"from \.\.persistence import", "from server.persistence import"),
    (r"from \.\.game\.", "from server.game."),
    (r"from \.\.services\.", "from server.services."),
    (r"from \.\.command_handler", "from server.command_handler"),
    (r"from \.\.app\.", "from server.app."),
    (r"from \.\.exceptions import", "from server.exceptions import"),
    (r"from \.\.database import", "from server.database import"),
    (r"from \.\.utils\.", "from server.utils."),
    (r"from \.\.config import", "from server.config import"),
    (r"from \.\.alias_storage import", "from server.alias_storage import"),
    (r"from \.\.commands\.", "from server.commands."),
    (r"from \.\.main import", "from server.main import"),
    (r"from \.\.middleware\.", "from server.middleware."),
    (r"from \.\.logging_config import", "from server.logging_config import"),
    (r"from \.\.schemas\.", "from server.schemas."),
    (r"from \.\.validators\.", "from server.validators."),
    (r"from \.\.message_handler import", "from server.message_handler import"),
    (r"from \.\.player_manager import", "from server.player_manager import"),
    (r"from \.\.room_manager import", "from server.room_manager import"),
    (r"from \.\.help_content import", "from server.help_content import"),
    (r"from \.\.error_types import", "from server.error_types import"),
    (r"from \.\.legacy_error_handlers import", "from server.legacy_error_handlers import"),
    (r"from \.\.dependencies import", "from server.dependencies import"),
    (r"from \.\.help\.", "from server.help."),
    (r"from \.\.message_handlers\.", "from server.message_handlers."),
    (r"from \.\.npc\.", "from server.npc."),
    # Three-level relative imports (from ...module) - should go to server
    (r"from \.\.\.", "from server."),
]


def fix_imports_in_file(file_path: Path) -> tuple[bool, int]:
    """
    Fix imports in a single file.

    Args:
        file_path: Path to file to fix

    Returns:
        Tuple of (was_modified, fix_count)
    """
    try:
        content = file_path.read_text(encoding="utf-8")
        original_content = content
        fix_count = 0

        for pattern, replacement in IMPORT_FIXES:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                fix_count += re.subn(pattern, replacement, content)[1]
                content = new_content

        if content != original_content:
            file_path.write_text(content, encoding="utf-8")
            return True, fix_count

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0


def main():
    """Main entry point."""
    print("Fixing imports in consolidated test files...")
    print("=" * 80)

    test_files = list(BASE.rglob("test_*.py"))
    total_files_fixed = 0
    total_fixes = 0

    for test_file in test_files:
        was_modified, fix_count = fix_imports_in_file(test_file)
        if was_modified:
            rel_path = test_file.relative_to(BASE)
            print(f"  [FIXED] {rel_path} ({fix_count} imports)")
            total_files_fixed += 1
            total_fixes += fix_count

    print()
    print("=" * 80)
    print(f"Fixed {total_fixes} imports in {total_files_fixed} files")
    print("=" * 80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
