"""
Verification script to check NPCs in lifecycle manager and test occupant query logic.

This script verifies:
1. NPCs exist in lifecycle manager's active_npcs dict
2. Query logic correctly finds NPCs by room ID
3. NPCs have correct room assignments
"""

import asyncio
import sys
from pathlib import Path

# Add server directory to path
server_dir = Path(__file__).parent.parent
sys.path.insert(0, str(server_dir))

from server.services.npc_instance_service import get_npc_instance_service  # noqa: E402


async def verify_npcs_in_lifecycle_manager() -> None:
    """Verify NPCs exist in lifecycle manager and test query logic."""
    print("=" * 80)
    print("NPC LIFECYCLE MANAGER VERIFICATION")
    print("=" * 80)

    try:
        # Get NPC instance service
        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service:
            print("❌ ERROR: NPC instance service not available")
            return

        print("✅ NPC instance service retrieved")

        # Check lifecycle manager
        lifecycle_manager = getattr(npc_instance_service, "lifecycle_manager", None)
        if not lifecycle_manager:
            print("❌ ERROR: Lifecycle manager not available in NPC instance service")
            return

        print("✅ Lifecycle manager retrieved")

        # Check active_npcs
        active_npcs = getattr(lifecycle_manager, "active_npcs", None)
        if active_npcs is None:
            print("❌ ERROR: active_npcs not available in lifecycle manager")
            return

        print(f"✅ active_npcs dict available (type: {type(active_npcs)})")

        # Count NPCs
        npc_count = len(active_npcs)
        print(f"\n📊 ACTIVE NPC COUNT: {npc_count}")

        if npc_count == 0:
            print("⚠️  WARNING: No NPCs found in active_npcs dict!")
            print("   This could mean:")
            print("   - NPCs haven't been spawned yet")
            print("   - NPCs were despawned")
            print("   - Server needs to be restarted")
            return

        # List all NPCs and their rooms
        print("\n" + "=" * 80)
        print("ACTIVE NPCs AND THEIR ROOMS")
        print("=" * 80)

        npcs_by_room: dict[str, list[dict[str, str]]] = {}

        for npc_id, npc_instance in active_npcs.items():
            # Get room ID from NPC instance
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

        # Test query logic for specific room
        print("=" * 80)
        print("TESTING QUERY LOGIC FOR ROOM: earth_arkhamcity_sanitarium_room_foyer_001")
        print("=" * 80)

        test_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        found_npcs: list[str] = []

        for npc_id, npc_instance in active_npcs.items():
            # Check both current_room and current_room_id for compatibility
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

        # Summary
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

    except Exception as e:
        print(f"\n❌ ERROR during verification: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(verify_npcs_in_lifecycle_manager())
