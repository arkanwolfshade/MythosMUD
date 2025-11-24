# Spec Summary (Lite)

Extend the `/look` command to support examining players (visible equipment, position, health/sanity labels), items (name and description from prototypes), and containers (contents, capacity, lock status). Add explicit syntax options (`/look player <name>`, `/look item <name>`, `/look container <name>`) and instance targeting (`backpack-2` or `backpack 2`) while establishing priority resolution order (Players > NPCs > Items > Containers > Directions). Remove diagonal direction support to align with cardinal-only movement.
