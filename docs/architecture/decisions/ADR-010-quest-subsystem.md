# ADR-010: Quest Subsystem Architecture

**Status:** Accepted
**Date:** 2026-02-19

## Context

MythosMUD needs a data-driven quest system so builders can add and tune quests without code
changes. Requirements (from [QUEST_SYSTEM_FEATURES.md](../../QUEST_SYSTEM_FEATURES.md)): goal
types (e.g. complete-activity, kill N), reward types (XP, item, spell), triggers (room, NPC,
item), event-driven progression, persistent per-character state, quest log/journal, and
prerequisite chains. The server must remain authoritative; the client displays quest state
provided by the server (game_state.quest_log or GET /api/players/{id}/quests).

## Decision

1. **Storage**: Quest definitions live in PostgreSQL: table `quest_definitions` (id, definition
   JSONB, timestamps). Per-character state in `quest_instances` (player_id, quest_id, state,
   progress JSONB, accepted_at, completed_at). Table `quest_offers` links quests to entities
   (room or NPC) that offer them. JSONB holds the full definition schema (name, title,
   goals[], rewards[], triggers[], requires_all, requires_any, auto_complete, turn_in_entities).

2. **Repositories**: QuestDefinitionRepository (get_by_id, get_by_name, list_quest_ids_offered_by)
   and QuestInstanceRepository (create, get_by_player_and_quest, update_state_and_progress,
   list_active_by_player, list_completed_by_player). Both use get_session_maker() and async
   sessions per ADR-005.

3. **QuestService**: Single domain service (injected with definition and instance repos, optional
   level/inventory/spell services for rewards). Responsibilities: resolve_name_to_quest_id,
   start_quest (prerequisite DAG check), start_quest_by_trigger, record_complete_activity,
   record_kill, turn_in, abandon, get_quest_log. Reward application (XP, item, spell) is
   delegated to existing services; quest layer does not duplicate their logic.

4. **Event wiring**: EventBus subscriptions (PlayerEnteredRoom, PlayerLeftRoom, NPC/item
   interaction) evaluate triggers and call start_quest_by_trigger; room exit and NPC death
   events drive progress for complete_activity and kill_n goals. Completion (auto_complete or
   turn_in) applies rewards and sets instance state to completed.

5. **API and commands**: GET /api/players/{player_id}/quests returns the quest log (auth and
   character ownership enforced). Commands `journal` and `quests` (alias) return formatted
   quest log; `quest abandon <name>` abandons by common name. Initial WebSocket game_state
   includes quest_log so the client Journal panel can render without a separate API call.

6. **Client**: Journal panel (default layout, title "Journal") displays quest_log from
   game_state or refreshed via GET /quests; server-authoritative.

## Alternatives Considered

- **YAML/JSON files on disk**: Rejected in favor of JSONB in PostgreSQL for consistency with
  ADR-006, single source of truth, and no file-path or reload concerns. Migrations can seed
  initial quests.
- **Hard-coded quest logic per quest**: Rejected; generic goal/reward types and data-driven
  definitions keep the codebase maintainable and allow builders to add quests via data.
- **Client-authoritative progress**: Rejected; server is authoritative (server-authority rule);
  progress is updated only when server-side events occur.

## Consequences

- **Positive**: Builders can add quests via migrations or future tooling; quest log and
  abandon are covered by API and commands; event-driven progression fits existing EventBus
  usage; prerequisites support linear chains.
- **Negative**: Repeatable quests were deferred; turn-in and some reward types require
  inventory/spell services to be wired.
- **Neutral**: Quest design guidelines (e.g. lysator principles) live in developer docs;
  content quality is a separate concern from architecture.
