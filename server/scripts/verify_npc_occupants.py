"""
Verification script to check NPCs in lifecycle manager and test occupant query logic.

This script verifies:
1. NPCs exist in lifecycle manager's active_npcs dict
2. Query logic correctly finds NPCs by room ID
3. NPCs have correct room assignments
"""

import sys
from pathlib import Path
from typing import Any

from anyio import run

# Add server directory to path
server_dir = Path(__file__).parent.parent
sys.path.insert(0, str(server_dir))

from server.services.npc_instance_service import (  # noqa: E402  # pylint: disable=wrong-import-position
    get_npc_instance_service,
)


def _check_service_availability() -> tuple[Any, Any, dict[str, Any]] | None:
    """
    Check if NPC service, lifecycle manager, and active_npcs are available.

    Returns:
        Tuple of (npc_instance_service, lifecycle_manager, active_npcs) if available, None otherwise
    """
    npc_instance_service = get_npc_instance_service()
    if not npc_instance_service:
        print("❌ ERROR: NPC instance service not available")
        return None

    print("✅ NPC instance service retrieved")

    lifecycle_manager = getattr(npc_instance_service, "lifecycle_manager", None)
    if not lifecycle_manager:
        print("❌ ERROR: Lifecycle manager not available in NPC instance service")
        return None

    print("✅ Lifecycle manager retrieved")

    active_npcs = getattr(lifecycle_manager, "active_npcs", None)
    if active_npcs is None:
        print("❌ ERROR: active_npcs not available in lifecycle manager")
        return None

    print(f"✅ active_npcs dict available (type: {type(active_npcs)})")
    return (npc_instance_service, lifecycle_manager, active_npcs)


def _collect_npcs_by_room(active_npcs: dict[str, Any]) -> dict[str, list[dict[str, str]]]:
    """
    Collect NPCs grouped by room ID.

    Args:
        active_npcs: Dictionary of active NPC instances

    Returns:
        Dictionary mapping room IDs to lists of NPC info dicts
    """
    npcs_by_room: dict[str, list[dict[str, str]]] = {}

    for npc_id, npc_instance in active_npcs.items():
        current_room = getattr(npc_instance, "current_room", None)
        current_room_id = getattr(npc_instance, "current_room_id", None)
        npc_room_id = current_room or current_room_id
        npc_name = getattr(npc_instance, "name", "Unknown")
        room_key = npc_room_id or "UNKNOWN_ROOM"

        if room_key not in npcs_by_room:
            npcs_by_room[room_key] = []

        npcs_by_room[room_key].append(
            {
                "npc_id": npc_id,
                "npc_name": npc_name,
                "room_id": room_key,
            }
        )

        print(f"  NPC: {npc_name}")
        print(f"    ID: {npc_id}")
        print(f"    Room (current_room): {current_room}")
        print(f"    Room (current_room_id): {current_room_id}")
        print(f"    Room (used): {npc_room_id}")
        print()

    return npcs_by_room


def _test_query_for_room(
    active_npcs: dict[str, Any], test_room_id: str, npcs_by_room: dict[str, list[dict[str, str]]]
) -> list[str]:
    """
    Test query logic for a specific room.

    Args:
        active_npcs: Dictionary of active NPC instances
        test_room_id: Room ID to test
        npcs_by_room: Dictionary of NPCs grouped by room

    Returns:
        List of NPC IDs found in the test room
    """
    found_npcs: list[str] = []

    for npc_id, npc_instance in active_npcs.items():
        npc_room_id = getattr(npc_instance, "current_room", None) or getattr(npc_instance, "current_room_id", None)

        if npc_room_id == test_room_id:
            found_npcs.append(npc_id)
            npc_name = getattr(npc_instance, "name", "Unknown")
            print(f"  ✅ FOUND: {npc_name} ({npc_id})")

    if not found_npcs:
        print(f"  ❌ NO NPCs found in room: {test_room_id}")
        print("\n  NPCs exist in these rooms:")
        for room_id in sorted(npcs_by_room.keys()):
            npcs_in_room = npcs_by_room[room_id]
            print(f"    - {room_id}: {len(npcs_in_room)} NPC(s)")
            for npc_info in npcs_in_room:
                print(f"        • {npc_info['npc_name']} ({npc_info['npc_id']})")
    else:
        print(f"\n  ✅ SUCCESS: Found {len(found_npcs)} NPC(s) in room")

    return found_npcs


def _print_summary(
    npc_count: int, test_room_id: str, found_npcs: list[str], npcs_by_room: dict[str, list[dict[str, str]]]
) -> None:
    """
    Print verification summary.

    Args:
        npc_count: Total number of active NPCs
        test_room_id: Room ID that was tested
        found_npcs: List of NPC IDs found in test room
        npcs_by_room: Dictionary of NPCs grouped by room
    """
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total active NPCs: {npc_count}")
    print(f"NPCs in test room ({test_room_id}): {len(found_npcs)}")
    print(f"Unique rooms with NPCs: {len(npcs_by_room)}")

    if npc_count > 0:
        print("\n✅ VERIFICATION PASSED: NPCs exist in lifecycle manager")
    else:
        print("\n❌ VERIFICATION FAILED: No NPCs found in lifecycle manager")


async def verify_npcs_in_lifecycle_manager() -> None:
    """Verify NPCs exist in lifecycle manager and test query logic."""
    print("=" * 80)
    print("NPC LIFECYCLE MANAGER VERIFICATION")
    print("=" * 80)

    try:
        service_result = _check_service_availability()
        if service_result is None:
            return

        _, _, active_npcs = service_result

        npc_count = len(active_npcs)
        print(f"\n📊 ACTIVE NPC COUNT: {npc_count}")

        if npc_count == 0:
            print("⚠️  WARNING: No NPCs found in active_npcs dict!")
            print("   This could mean:")
            print("   - NPCs haven't been spawned yet")
            print("   - NPCs were despawned")
            print("   - Server needs to be restarted")
            return

        print("\n" + "=" * 80)
        print("ACTIVE NPCs AND THEIR ROOMS")
        print("=" * 80)

        npcs_by_room = _collect_npcs_by_room(active_npcs)

        print("=" * 80)
        print("TESTING QUERY LOGIC FOR ROOM: earth_arkhamcity_sanitarium_room_foyer_001")
        print("=" * 80)

        test_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        found_npcs = _test_query_for_room(active_npcs, test_room_id, npcs_by_room)

        _print_summary(npc_count, test_room_id, found_npcs, npcs_by_room)

    except Exception as e:
        print(f"\n❌ ERROR during verification: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    run(verify_npcs_in_lifecycle_manager)
