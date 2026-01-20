# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-15-container-system/spec.md

## Technical Requirements

**ContainerComponent data contract**: implement a pydantic/dataclass entity with identifiers (`container_id`, `source_type`, `owner_id`), state (`capacity_slots`, `weight_limit`, `lock_state`, `decay_at`, `allowed_roles`), and `items: list[InventoryStack]` leveraging existing `InventoryService` schemas for serialization.

**Persistence layer**: extend `InventoryPayload` and `PLAYER_INVENTORY_SCHEMA` to support nested `inner_container` structures; create a new SQLite table `containers` (and planned PostgreSQL equivalent) storing instance metadata plus JSON blob of contents keyed by `room_id` or `entity_id`; ensure migrations via CLI scripts.

**ContainerService module**: orchestrate open/insert/remove/close commands, wrap operations in `InventoryMutationGuard`, publish structured logging events, and emit websocket/NATS events `container.opened`, `container.updated`, `container.closed`.
- **Corpse lifecycle automation**: hook death events to instantiate containers, enforce configurable owner-only windows, bind decay timers into `time_service`, and flush unclaimed items to room drops with audit logs.
- **API + command layer**: add REST/WebSocket endpoints or command handlers (`open_container`, `transfer_to_container`, `transfer_from_container`, `close_container`) with validation (container exists, user proximity, ACL/lock), rate limiting, and error codes.
- **React client updates**: create container context store, split-pane component (container vs personal inventory), backpack tab/pill, corpse overlay with countdown, drag-and-drop plus keyboard interactions, and SSE/WebSocket listeners that reconcile container diffs.
- **Testing**: expand pytest suites for ContainerService, persistence round-trips, concurrency guard behavior, corpse decay; implement Vitest + Playwright MCP tests for UI flows and multi-client synchronization.

## External Dependencies (Conditional)

No new external dependencies are required; reuse existing FastAPI, Pydantic, and React toolchains.
