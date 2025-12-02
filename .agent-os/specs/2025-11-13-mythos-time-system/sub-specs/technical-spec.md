# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-13-mythos-time-system/spec.md

## Technical Requirements

- **MythosChronicle service**
  - Implement `server/time/time_service.py` with a singleton `MythosChronicle`.
  - Maintain canonical epoch (`MYTHOS_EPOCH_REAL_UTC`, `MYTHOS_EPOCH_MYTHOS`) configurable via settings.
  - Provide conversion API: `to_mythos_datetime(real_dt)`, `to_real_datetime(mythos_dt)`, `get_current_mythos_datetime()`, `format_clock()`, and `advance_mythos(delta_hours)`.
  - Persist state to `data/system/time_state.json` (atomically written with temp file swap) storing last known real UTC timestamp and Mythos datetime; load at startup and freeze when server shuts down gracefully.
  - Emit structured logs via `get_logger` and expose Prometheus counters (`mythos_chronicle_ticks_total`, `mythos_chronicle_freeze_events_total`).

- **Hourly tick engine**
  - Integrate with `server/app/task_registry.py` to schedule hourly callbacks keyed to Mythos time.
  - Broadcast events through `EventBus` (`event_type="mythos.hour.tick"`) including day, month, season, and active holidays.
  - Provide synchronous helpers for modules that need immediate evaluation (e.g., `is_witching_hour()`).

- **JSON schedule ingestion**
  - Create schema files in `schemas/calendar/holiday.schema.json` and `schemas/calendar/schedule.schema.json`.
  - Source data from `data/calendar/holidays.json` (pre-populated with Catholic/Islamic/Jewish/neo-pagan entries plus Mythos cult stubs such as Sevenfold Tide Offering, Equinox Serpent Vigil, Ghoulmarket Convocation) and `data/calendar/schedules/<category>.json`.
  - Enforce validations with `pydantic` models under `server/schemas/calendar.py`:
    - Fields: `id`, `name`, `tradition`, `month`, `day`, `duration_hours` (clamped to 48), `season`, `bonus_tags`.
    - Fixed lunar mapping: encode predetermined Mythos month/day for historically movable feasts.
  - Add CLI validator `scripts/validate_calendar.py` to check JSON via pytest-friendly exit codes.
  - Treat `docs/MYTHOS_HOLIDAY_CANDIDATES.md` as the canonical reference catalog for faction observances; unit tests should load this document to ensure listed IDs appear in JSON.

- **System integrations**
  - **NPC behavior**: Extend relevant services (`server/game/npc_*`) to subscribe to `mythos.hour.tick` for shift changes (shop open/close, patrols).
  - **Environment**: Update `room_service` to request current Mythos daypart and apply lighting descriptions; integrate with passive lucidity flux to adjust the witching hour logic.
  - **Holiday engine**: Add middleware or dedicated manager (`server/game/holiday_service.py`) to track active holidays, trigger celebratory events, and ensure bonuses automatically sunset after 48 Mythos hours.
  - **Admin tooling**: Provide `/admin/time` command returning current Mythos timestamp, active holidays, next three triggers, and freeze status.

- **Client UI/UX**
  - Update React HUD component (`client/src/components/Hud/TimePanel.tsx`) to show Mythos clock (HH:MM) and day/season badge; use Tailwind for styling within existing theme.
  - Show holiday banners via toast/announcement panel (existing notification system) with icon keyed to tradition.
  - Update command output (`/time`, `/who`, room descriptions) so that server responses embed Mythos time metadata—client will render plain text inside terminal.

- **Testing and quality**
  - **Unit tests**: Add `server/tests/unit/time/test_chronicle.py` covering conversions, freeze/resume, and duration limits.
  - **Integration tests**: Add `server/tests/integration/time/test_scheduler.py` to simulate accelerated ticks and verify event bus payloads; ensure fixtures write temp JSON configs.
  - **Playwright scenario**: Add `e2e-tests/scenarios/scenario-XX-mythos-time.md` automating two clients witnessing day/night and holiday transitions.
  - **Load testing**: Extend performance suite (`artifacts/perf/`) to ensure hourly processing stays under 10 ms average per tick.
  - Update CI lint/test pipelines to include schema validation step (`make lint` runs `scripts/validate_calendar.py`).

- **Operational considerations**
  - Ensure freeze/resume logic runs before/after `start_local.ps1` by adding hooks in server lifespan handlers.
  - Expose metrics to monitoring stack; document Grafana additions for day/night cycle visualization.
  - Provide runbook updates in `docs/` describing JSON change process and testing expectations.
