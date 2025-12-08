# 🐙 MythosMUD – Product Requirements Document (PRD)

---

## **1. Overview**

**Project Name:** *MythosMUD*
**Author:** Mark Henry
**Purpose:** A personal passion project for creating a text-based, browser-accessible Multi-User Dungeon (MUD) inspired by the Cthulhu Mythos. Intended to engage the developer’s teenage son and close friends in collaborative storytelling and programming.

---

## **2. Goals & Vision**

- Create a beginner-friendly codebase for exploration and contribution.
- Provide a persistent, text-based multiplayer experience.
- Incorporate real-time gameplay with a Lovecraftian horror theme.
- Prioritize exploration, narrative, and combat in a light horror setting.

---

## **3. Target Audience**

- Developer's personal network: friends and family.
- Teenagers with interest in storytelling, horror, or programming.
- Invite-only audience; not intended for general public release.

---

## **4. Game Design**

### **4.1 Gameplay Loop**

- Players explore a persistent world.
- Interact via text commands (`look`, `go`, `say`, `attack`, `cast`, etc.).
- Participate in quests, combat, discovery of secrets, and roleplay.
- Level up to gain attributes, skills, and unlock new areas.

### **4.2 Combat System**

- **Real-time with server ticks.**
- Command-driven: players must actively type commands during combat rounds.
- **Room-based combat**: all participants in a room can interact with one another directly; no spatial positioning or grid movement.
- **Aggro system**: mobs track the most threatening target (tank) and allow for:
  - **Tanking mechanics**
  - **Flanking opportunities**
- ASCII map provides **navigation aid only**, not tactical positioning.
- Client includes ZMud-like enhancements:
  - Triggers
  - Aliases
  - Highlighting
  - Command history

### **4.3 lucidity System**

- Based on Call of Cthulhu mechanics.
- lucidity drops from encounters with Mythos elements or spells.
- Below-threshold effects:
  - Hallucinations
  - Distorted messages or room descriptions
  - Temporary stat/movement impairments
- Gradual recovery or assisted recovery via:
  - Visiting therapists
  - Checking into asylums
  - Resting at specific locations

### **4.4 Death & Resurrection**

- Player death:
  - Leaves a **corpse with dropped gear**
  - Transports player to an **"afterlife" zone** for a short time
  - Can be **resurrected by allies** from the corpse
  - Otherwise, **respawns at last save point**

---

## **5. World & Content**

### **5.1 Initial World Design**

- **Starting city**: Arkham
- Core zones (accessible by walking):
  - Arkham
  - Innsmouth
  - Dunwich
  - Kingsport
- Remote zones (via transportation: train, boat, teleportation):
  - Antarctic
  - Plateau of Leng

### **5.2 Zone Generation**

- World built using a **hybrid model**:
  - Hand-authored content for critical/landmark locations
  - Procedural generation for filler and secondary zones

### **5.3 NPCs**

- Types:
  - Quest givers (static and repeatable)
  - Shopkeepers
  - Hostile mobs
  - Ambient population for immersion
- All major NPCs and mobs support basic AI behaviors.

### **5.4 Quests**

- Linear/railroad design at launch.
- No branching or morality systems (yet).
- Faction-tied story elements.
- Potential to expand quest complexity post-MVP.

---

## **6. Character System**

- Character creation modeled after **pre-D20 Call of Cthulhu**:
  - Attributes include STR, DEX, INT, CON, EDU, LCD, etc.
- XP-based leveling system:
  - Levels grant health, mana, lucidity, skill points
- Inventory system with equipables and consumables
- Magic system (Mythos spells, lucidity costs)
- Crafting system: **TBD**

---

## **7. Factions**

- **Investigators** (playable at launch): Resist Mythos forces.
- **Cultists** (future release): Summon Mythos powers, sabotage world.
- PvP reserved for **Cultist vs Investigator** (not enabled at launch).

---

## **8. Multiplayer Features**

### **8.1 Communication**

- Chat channels:
  - Global
  - Local
  - Party
  - Say
  - Whisper
- Communication controls:
  - Mute/toggle for global and local
  - Profanity and harm-related keyword filter
  - Admin/mod alerting and log audit trail

### **8.2 Grouping**

- Players can form parties
  - Shared XP
  - Combat support
  - Quest progress sync

### **8.3 Admin/Moderator Tools**

- In-game commands:
  - Spawn/despawn NPCs
  - Kick/ban/mute
  - Move players
  - Set weather/time
- Real-time monitoring panel (web-based optional)

---

## **9. Technical Requirements**

### **9.1 Client (Front-End)**

- Web-based terminal interface:
  - Compatible with modern browsers
  - Supports mobile (optional) and desktop
  - Terminal-like experience with enhancements:
    - Triggers
    - Aliases/macros
    - Syntax highlighting
    - Scrollback and history
- ASCII navigation map

### **9.2 Server**

- Real-time tick-based event loop
- Event-driven architecture
- Modular codebase designed for beginner readability
- Room-based world logic with MUD command handling

### **9.3 Persistence Layer**

- Database-backed:
  - Character data
  - World state
  - Inventory
  - Quest status
  - lucidity levels
- Suggested tech: PostgreSQL, or AWS DynamoDB for low-cost hosting

### **9.4 Hosting**

- Hosted on AWS (cost-optimized):
  - EC2 (or Fargate) for runtime
  - RDS/DynamoDB for storage
  - S3/CloudFront for static content (if needed)
- SSL/TLS secured
- Authentication via invite-only accounts

---

## **10. Development Philosophy**

- Solo developer project
- Codebase designed to be beginner-friendly:
  - Clear modular design (MVC or ECS suggested)
  - Comments, docstrings, README for every module
  - Use of high-level languages (Python, JavaScript)
- Source control: GitHub
- CI/CD optional but considered for future polish

---

## **11. Future Considerations**

- Cultist faction release with PvP mechanics
- Complex quest arcs and moral choices
- Full crafting and alchemy systems
- Dynamic world events (Mythos incursions)
- Content creation tools or web-based builder
- Optional plugin/modding system

---
