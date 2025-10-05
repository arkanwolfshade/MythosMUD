# Spec Summary (Lite)

Extend the existing `look` command to accept NPC targets, enabling players to examine NPCs in their current room by name using case-insensitive partial matching. When a single NPC matches, display their name, description, and flavor text. When multiple NPCs match, show a list of matching names. NPC look takes priority over direction look, and no matches return "You don't see anyone like that here."
