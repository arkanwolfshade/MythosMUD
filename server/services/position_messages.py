"""Player-facing posture transition copy (leaf module; no service imports)."""

from __future__ import annotations

POSITION_MESSAGES: dict[str, dict[str, str]] = {
    "sitting": {
        "success": "You settle into a seated position.",
        "already": "You are already seated.",
    },
    "standing": {
        "success": "You rise to your feet.",
        "already": "You are already standing.",
    },
    "lying": {
        "success": "You stretch out and lie down.",
        "already": "You are already lying down.",
    },
}
