# MythosMUD Party System Reference

_"Even in the depths, companionship can ward off the worst of the darkness."_ — Miskatonic field notes

---

## Table of Contents

1. [Overview](#overview)
2. [Commands](#commands)
3. [Party Chat](#party-chat)
4. [Integration Hooks](#integration-hooks)
5. [References](#references)

---

## Overview

The party system provides **ephemeral** in-session grouping: no persistence between logins, no clans or
long-lived groups. Party state is in-memory only and is cleared when the server restarts or when all
members leave or disconnect.

### Key properties

- **Formation**: One player becomes leader by inviting another (`party invite <name>`). The inviter
  creates the party if they are not already in one.
- **Leadership**: Only the leader can invite and kick members. Leadership does not transfer when the
  leader leaves; the party is disbanded when the last member leaves.
- **Target resolution**: Invite and kick use the same target resolution as other commands (e.g. by
  player name; same-room rule may apply depending on configuration).

---

## Commands

All party commands use the root verb `party` with an optional subcommand and target. The client may
expose these as `party`, `party invite <name>`, etc.

| Command               | Description                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `party`               | When not in a party: show "You are not in a party" and hint to use `party invite <name>`. When in a party with no subcommand and no message: same as `party list`. |
| `party list`          | List current party members with (leader) beside the leader. Fails if not in a party.                                                                               |
| `party invite <name>` | Create a party (if needed) and add the named player. Only the leader can invite. Target must resolve to a player (e.g. by name).                                   |
| `party leave`         | Leave the current party. If you were the only member, the party is disbanded.                                                                                      |
| `party kick <name>`   | Remove the named player from the party. Only the leader can kick. Target must be a current member.                                                                 |
| `party <message>`     | Send a message to the party chat channel. Only valid when in a party; see [Party Chat](#party-chat).                                                               |

### Example flow

1. Alice runs `party invite Bob` → party is created with Alice as leader, Bob added.
2. Alice or Bob runs `party list` → both see "Your party:" with Alice (leader) and Bob.
3. Alice runs `party We go north at midnight.` → Bob sees the message in party chat.
4. Bob runs `party leave` → Bob leaves; Alice remains leader of a one-member party.
5. Alice runs `party leave` → party is disbanded.

---

## Party Chat

- **Channel**: Dedicated party channel; messages are sent only to current party members.
- **Usage**: `party <message>` (no subcommand, with non-empty message). If not in a party, the
  server returns: "You are not in a party. Use 'party invite <name>' to form one."
- **Rate limit**: Party chat is subject to the same per-channel rate limit as other chat (e.g. 30
  messages per minute per user); excess messages are rejected with an error.
- **NATS**: Messages are published on the pattern `chat.party.group.{party_id}`. See
  [NATS_SUBJECT_PATTERNS.md](NATS_SUBJECT_PATTERNS.md) for full pattern documentation.
- **Client**: The client provides a party channel in the channel list; selecting it and typing a
  message sends `party <message>`.

---

## Integration Hooks

Other systems can use the party service without implementing full party logic in this phase.

- **Combat**: `PartyService.is_in_same_party(player_id_a, player_id_b)` indicates whether two
  players are in the same party. The combat validator can use this (e.g. to block or theme
  attacks on party members). See `CombatValidator(party_service=...)` and
  `validate_can_attack_target(attacker_id, target_id)` in the server.
- **Lucidity / quests**: `PartyService.get_party_members(player_id)` returns the list of party
  member IDs for that player's current party (including the player). Use this from lucidity or
  quest code when party context is needed (e.g. group solace, companion presence). No quest sync or
  shared progress is implemented in the ephemeral phase.

---

## References

| Document                                                                         | Relevance                                                   |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [PLANNING_ephemeral_grouping.md](PLANNING_ephemeral_grouping.md)                 | Scope, phases, acceptance criteria, implementation overview |
| [NATS_SUBJECT_PATTERNS.md](NATS_SUBJECT_PATTERNS.md)                             | `chat.party.group.{party_id}` and subject management        |
| [archive/ADVANCED_CHAT_CHANNELS_SPEC.md](archive/ADVANCED_CHAT_CHANNELS_SPEC.md) | Party channel (section 14.1)                                |
| [archive/lucidity-system.md](archive/lucidity-system.md)                         | Party/group context for lucidity features                   |
