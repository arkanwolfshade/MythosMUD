#!/usr/bin/env python3
"""
Script to fix all NPC admin API test authentication issues.
This script replaces the old authentication mocking pattern with the consistent _mock_auth pattern.
"""

import re


def fix_npc_tests():
    """Fix all NPC admin API tests to use consistent authentication mocking."""

    file_path = "server/tests/test_npc_admin_api.py"

    # Read the file
    with open(file_path, encoding="utf-8") as f:
        content = f.read()

    # Pattern to match the old authentication mocking
    old_pattern = r'        with \(\s*patch\("server\.auth\.users\.get_current_user", return_value=mock_admin_user\),\s*patch\("server\.api\.admin\.npc\.([^"]+)", return_value=([^)]+)\),\s*\):\s*response = client\.([^(]+)\(([^)]+)\)\s*assert response\.status_code == status\.HTTP_([0-9_]+)\s*data = response\.json\(\)\s*assert data\["([^"]+)"\] == ([^\n]+)'

    # New pattern using _mock_auth
    new_pattern = r"""        # Use consistent authentication mocking
        self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.\1", return_value=\2):
                response = client.\3(\4)
                assert response.status_code == status.HTTP_\5

                data = response.json()
                assert data["\6"] == \7
        finally:
            client.app.dependency_overrides.clear()"""

    # Apply the replacement
    content = re.sub(old_pattern, new_pattern, content, flags=re.MULTILINE | re.DOTALL)

    # Write the file back
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("Fixed NPC admin API tests authentication patterns")


if __name__ == "__main__":
    fix_npc_tests()
