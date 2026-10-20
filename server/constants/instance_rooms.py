"""
Shared identifiers for instanced rooms.

Kept free of project imports so persistence, NPC, movement and realtime code can all use it without import cycles.
"""

import re

# Instance room ids: instance_{instance_uuid}_{template_stable_id}
INSTANCE_ROOM_PREFIX: str = "instance_"

# players.tutorial_instance_id of a player whose tutorial instance has not been built yet (a new
# character, before first connect). It names no live instance, so the reconnect path creates one.
PENDING_INSTANCE_ID: str = "pending"


_INSTANCE_ROOM_ID = re.compile(r"instance_[0-9a-fA-F-]{36}_(?P<template>.+)")


def template_room_id_of(room_id: str) -> str:
    """The template room's stable id behind an instance room id; any other id comes back unchanged.

    An instance room is a clone of a template room, and the database only knows the template: maps and exploration
    look rooms up by that id (#1108).
    """
    match = _INSTANCE_ROOM_ID.fullmatch(room_id)
    return match["template"] if match else room_id


def is_instance_room_id(room_id: str) -> bool:
    """True for per-player instance rooms (instance_<uuid>_<stable_id>), false for world and template ids."""
    return room_id.startswith(INSTANCE_ROOM_PREFIX) and room_id.count("_") >= 2
