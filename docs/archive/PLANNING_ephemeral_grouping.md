# MythosMUD Ephemeral Grouping (Party) Planning

Single source of truth for **ephemeral** player grouping (parties): in-session only, no persistence
between logins, no clans or long-lived groups. Consolidated from PRD, multiplayer/chat planning,
GitHub [#59](https://github.com/arkanwolfshade/MythosMUD/issues/59), and MUD research.

---

## 1. Scope

### In scope

- **Ephemeral parties only**: Formed and dissolved within a play session.
- No persistence of party state between logins or sessions (party state is in-memory only).
- Party formation and management, leadership, shared XP, combat coordination, quest progress sync,
  party chat, and member status tracking.

### Out of scope (this phase)

- **Party state persists between sessions** (listed in [#59](https://github.com/arkanwolfshade/MythosMUD/issues/59)
  acceptance criteria) — explicitly out of scope for the ephemeral phase.
- **Clans, guilds, or long-lived groups** — not in scope; treat as future work.

---

## 2. Requirements

Merged from PRD §8.2, [#59](https://github.com/arkanwolfshade/MythosMUD/issues/59), and
chat/multiplayer docs.

### Functional

- **Party formation and management**: Players can form and join parties; invite-based (e.g. same
  location); leader designee; disband when all leave or session ends.
- **Party leadership and permissions**: Leader can invite, kick, and manage members (and optionally
  group movement).
- **Shared XP**: XP distribution among party members (consider level-weighted split to avoid
  griefing).
- **Combat coordination**: Party-based combat support and coordination.
- **Party chat channel**: Dedicated `/party <message>` channel for group communication; rate limit
  (e.g. 30 messages per minute per user) per chat spec.
- **Party member status tracking**: Visibility of who is in the party and basic status.

### Non-functional

- **Integration**: With existing chat, combat, and player management systems.
- **In-memory only**: No database persistence of party membership or party state between sessions.

---

## 3. How Other MUDs Do It

Summary of common ephemeral group/party patterns (Discworld MUD, ZombieMUD, CircleMUD, social/identity
docs).

- **Lifecycle**: Session-only; no persistence between logins; group dissolves when all leave or
  session ends.
- **Formation**: Dedicated command (e.g. `group create` / `party`); one leader; invite-based,
  often requiring same room.
- **Mechanics**: Leader can invite/kick, manage movement; dedicated group/party chat; XP split
  (often level-weighted); optional auto-follow; some MUDs use level-range checks to avoid
  imbalanced groups.
- **Implementation**: Group as in-memory affiliation (e.g. flags, leader pointer); not stored
  long-term. Permanent affiliations use separate guild/club systems.

---

## 4. Integration Points

- **Chat**: Party Channel (Phase 3 in chat plan); `/party <message>`; mute applies to party channel.
  NATS subject pattern: `chat.party.group.{party_id}` (see [NATS_SUBJECT_PATTERNS.md](NATS_SUBJECT_PATTERNS.md)).
- **Follow system**: Optional integration (e.g. party members may follow leader); follow is
  independent of party but can be used with it.
- **Combat**: Party-based combat coordination and support (design TBD).
- **Quests**: Quest progress synchronization for party (design TBD).
- **Lucidity**: [lucidity-system.md](archive/lucidity-system.md) assumes party/group context (e.g.
  companion presence in group, group solace ≥3 players, party member death within line of sight).
  Party system must exist for those features to apply.

---

## 5. Dependencies

- **Depends on**: [#42](https://github.com/arkanwolfshade/MythosMUD/issues/42) Chat System; player
  management system.
- **Blocks**: [#28](https://github.com/arkanwolfshade/MythosMUD/issues/28) Prepare for limited
  invite-only launch.

---

## 6. Acceptance Criteria

From [#59](https://github.com/arkanwolfshade/MythosMUD/issues/59), adjusted for ephemeral scope.

- [ ] Players can form and join parties.
- [ ] XP is shared among party members.
- [ ] Party combat coordination works.
- [ ] Quest progress is synchronized (where applicable).
- [ ] Party chat functions properly.
- [ ] Party leadership can manage members.
- [ ] ~~Party state persists between sessions~~ **Out of scope (ephemeral phase).**
- [ ] Integration with existing systems (chat, combat, player management).

---

## 7. Implementation overview

Implementation is phased: server is authoritative, party state is in-memory only. Follow patterns
from [follow_service.py](../server/game/follow_service.py) and
[follow_commands.py](../server/commands/follow_commands.py). Integrate with EventBus,
command_service, and NATS chat where applicable.

---

## 8. Implementation phases and todos

### Phase 1 – Core party model and service

- [x] Define in-memory party model (party_id, leader_id, member_ids, created_at).
- [x] Add `PartyService` in `server/game/` (create/disband party, add/remove member, get party
      for player, leader checks). No persistence.
- [x] Register PartyService in container ([server/container/](../server/container/)); ensure
      cleanup on disconnect/session end.
- [x] Unit tests for PartyService (create, invite, leave, kick, disband, same-room or
      configurable invite rule).

### Phase 2 – Party commands and realtime updates

- [x] Add party commands (e.g. `party`, `party invite <name>`, `party leave`, `party kick
<name>`, `party list`) following [follow_commands.py](../server/commands/follow_commands.py)
      and command_service patterns.
- [x] Define realtime event(s) for party membership changes (e.g. party_updated or
      member_joined/left) and emit from PartyService; document in
      [event_types.py](../server/events/event_types.py) if new types are added.
- [x] Wire commands in [command_handler/](../server/command_handler/) and
      [command_factories](../server/utils/command_factories.py) so clients can invoke party
      commands.
- [x] Integration test: two players, invite/accept or join, leave, disband; verify in-memory
      state and events.

### Phase 3 – Party chat channel

- [x] Add NATS pattern for party chat (e.g. `chat.party.group.{party_id}`) in
      [patterns.py](../server/services/nats_subject_manager/patterns.py) and document in
      [NATS_SUBJECT_PATTERNS.md](NATS_SUBJECT_PATTERNS.md).
- [x] Implement party chat send/route: only party members can send/receive on party subject;
      enforce rate limit (e.g. 30 msg/min per user) per existing chat spec.
- [x] Client: support `/party <message>` and display party channel messages (align with
      existing channel UX).
- [x] Tests: party chat visibility and rate limiting.

### Phase 4 – Integration hooks (minimal scope)

- [x] **Combat:** Add hook or placeholder so combat/validator can check "is in same party" for
      future party-friendly rules; no full combat redesign in this phase.
- [x] **Lucidity/quests:** Add minimal hooks (e.g. "get party members for this player") so
      lucidity or quest code can consume party membership later; no quest sync implementation in
      this phase.
- [x] **Optional:** Same-room or configurable rule for invite (document in plan; implement if
      specified).

**Phase 4 notes:**

- **Combat hook:** `PartyService.is_in_same_party(player_id_a, player_id_b)` and
  `CombatValidator(party_service=...).validate_can_attack_target(attacker_id, target_id)`.
  When party_service is wired, attacking a party member can be blocked (thematic message).
  Current combat flow only targets NPCs; call `validate_can_attack_target` when adding
  player-vs-player or other target types.
- **Lucidity/quests:** `PartyService.get_party_members(player_id)` returns the list of party
  member IDs (including the player) for the player's current party; use from lucidity or
  quest code as needed. No quest sync in this phase.
- **Same-room invite:** Not implemented. A future rule could restrict `party invite` to
  targets in the same room (or make it configurable).

### Phase 5 – Playwright tests

- [x] Add Playwright tests for party commands and functionality
      (`client/tests/e2e/runtime/party/party-commands.spec.ts`: not in party, invite/list,
      party chat cross-player, leave).

### Phase 6 – Documentation

- [x] Add documentation for party system and commands ([PARTY_SYSTEM_REFERENCE.md](PARTY_SYSTEM_REFERENCE.md)).

---

## 9. References

| Document                                                                 | Relevance                                                |
| ------------------------------------------------------------------------ | -------------------------------------------------------- |
| [PRD.md](archive/PRD.md) §8.2                                            | Grouping: parties, shared XP, combat support, quest sync |
| [PLANNING_multiplayer.md](archive/PLANNING_multiplayer.md)               | Player Groups (planned + short-term)                     |
| [PLANNING.md](../PLANNING.md)                                            | Player Groups under Real-Time                            |
| [PLANNING_chat_system.md](archive/PLANNING_chat_system.md)               | Party System (Phase 3), Party Channel, `/party`          |
| [ADVANCED_CHAT_CHANNELS_SPEC.md](archive/ADVANCED_CHAT_CHANNELS_SPEC.md) | Party Channel (14.1)                                     |
| [NATS_SUBJECT_PATTERNS.md](NATS_SUBJECT_PATTERNS.md)                     | `chat.party.group.{party_id}`                            |
| [PARTY_SYSTEM_REFERENCE.md](PARTY_SYSTEM_REFERENCE.md)                   | Party commands, chat, and integration hooks reference    |
| [lucidity-system.md](archive/lucidity-system.md)                         | Party/group context (group solace, companion, etc.)      |
| [GitHub #59](https://github.com/arkanwolfshade/MythosMUD/issues/59)      | Implement Party/Grouping System                          |
