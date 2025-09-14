# Spec Summary (Lite)

Fix the occupant count display issue by implementing proper event handling for real-time room occupant updates. The server will broadcast room_occupants events during player movement (not just disconnection), and the client will process these events to update occupant counts immediately. This ensures accurate, synchronized occupant counts across all connected clients during multiplayer gameplay.
