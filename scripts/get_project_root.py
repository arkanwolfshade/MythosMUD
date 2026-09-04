#!/usr/bin/env python3
"""Print project root: parent of cwd if cwd contains 'MythosMUD-', else cwd. Used by Makefile."""

import os

c = os.getcwd()
print(os.path.dirname(c) if "MythosMUD-" in c else c)
