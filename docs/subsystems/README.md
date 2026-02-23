# Game Subsystem Design Documents

This directory contains reverse-engineered design documents for MythosMUD game subsystems. Each document
describes architecture, key decisions, constraints, component interactions, developer guidance, and
troubleshooting. Code is the source of truth; these docs are derived from it.

## Index

| Subsystem      | Document                                                                 | Summary                                                                                                  |
| -------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Movement       | [SUBSYSTEM_MOVEMENT_DESIGN.md](SUBSYSTEM_MOVEMENT_DESIGN.md)             | Atomic player movement between rooms; combat/posture checks; EventBus/NATS.                              |
| Follow         | [SUBSYSTEM_FOLLOW_DESIGN.md](SUBSYSTEM_FOLLOW_DESIGN.md)                 | In-memory follow state; player or NPC target; move followers on enter; request/accept for player.        |
| Rest           | [SUBSYSTEM_REST_DESIGN.md](SUBSYSTEM_REST_DESIGN.md)                     | Clean disconnect; rest location instant, else 10s countdown; interrupt on movement/combat/cast.          |
| Rescue         | [SUBSYSTEM_RESCUE_DESIGN.md](SUBSYSTEM_RESCUE_DESIGN.md)                 | Ground/rescue catatonic players; same room; LucidityService adjustment; rescue_update events.            |
| Emote / Pose   | [SUBSYSTEM_EMOTE_POSE_DESIGN.md](SUBSYSTEM_EMOTE_POSE_DESIGN.md)         | Emote (room broadcast), me (actor-only), pose (persistent); EmoteService and ChatService.                |
| Who            | [SUBSYSTEM_WHO_DESIGN.md](SUBSYSTEM_WHO_DESIGN.md)                       | List online players (last_active 5 min); optional name filter; formatted Name [Level] - Location.        |
| Party          | [SUBSYSTEM_PARTY_DESIGN.md](SUBSYSTEM_PARTY_DESIGN.md)                   | In-memory parties; invite/accept, kick, leave, disband; party chat; combat same-party block.             |
| Combat         | [SUBSYSTEM_COMBAT_DESIGN.md](SUBSYSTEM_COMBAT_DESIGN.md)                 | Player vs NPC; attack/punch/kick/strike; weapon damage; NPCCombatIntegrationService; no_combat rooms.    |
| Status effects | [SUBSYSTEM_STATUS_EFFECTS_DESIGN.md](SUBSYSTEM_STATUS_EFFECTS_DESIGN.md) | DP, posture, incapacitation, death; mechanics and persistence; no_death rooms (ADR-009).                 |
| Magic          | [SUBSYSTEM_MAGIC_DESIGN.md](SUBSYSTEM_MAGIC_DESIGN.md)                   | Cast, spells, spell, learn, stop; MP/lucidity costs; SpellRegistry, SpellEffects, targeting.             |
| Skills / Level | [SUBSYSTEM_SKILLS_LEVEL_DESIGN.md](SUBSYSTEM_SKILLS_LEVEL_DESIGN.md)     | Skills catalog, occupation/personal interest, level/XP curve, level-up hook, teach.                      |
| Lucidity       | [SUBSYSTEM_LUCIDITY_DESIGN.md](SUBSYSTEM_LUCIDITY_DESIGN.md)             | Recovery rituals (meditate, pray, therapy, folk_tonic, group_solace); cooldowns; ActiveLucidityService.  |
| Respawn        | [SUBSYSTEM_RESPAWN_DESIGN.md](SUBSYSTEM_RESPAWN_DESIGN.md)               | Dead (DP -10 or limbo) respawn by user_id; PlayerRespawnWrapper and PlayerRespawnService.                |
| NPC system     | [SUBSYSTEM_NPC_DESIGN.md](SUBSYSTEM_NPC_DESIGN.md)                       | Lifecycle, spawning, behavior, combat/movement/communication integration; population control.            |
| Admin commands | [SUBSYSTEM_ADMIN_COMMANDS_DESIGN.md](SUBSYSTEM_ADMIN_COMMANDS_DESIGN.md) | Mute, teleport, goto, shutdown, summon, setstat, setlucidity, npc; validate_admin_permission; audit log. |

## Related documentation

- [COMMAND_MODELS_REFERENCE.md](../COMMAND_MODELS_REFERENCE.md) – Command handler interface and routing.
- [EVENT_OWNERSHIP_MATRIX.md](../EVENT_OWNERSHIP_MATRIX.md) – Event types and ownership.
- [NATS_SUBJECT_PATTERNS.md](../NATS_SUBJECT_PATTERNS.md) – NATS subjects for real-time events.
- [architecture/decisions/ADR-009-instanced-rooms.md](../architecture/decisions/ADR-009-instanced-rooms.md) –
  Instanced rooms (tutorial, movement integration).
