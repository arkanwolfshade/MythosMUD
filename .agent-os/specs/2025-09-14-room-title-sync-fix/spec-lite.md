# Spec Summary (Lite)

Fix the race condition in client-side event processing that causes the Room Info panel to display stale room titles when players move between rooms. The issue occurs when room_occupants events overwrite room_update events with old room data, creating UI inconsistencies. The solution involves proper event ordering, state synchronization, and validation to ensure the Room Info panel always displays accurate room information immediately after movement commands.
