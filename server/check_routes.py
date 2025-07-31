#!/usr/bin/env python3
"""Check FastAPI app routes."""

import sys
from pathlib import Path

# Add the server directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from main import app

print("Routes:")
for route in app.routes:
    print(f"{route.methods} {route.path}")
