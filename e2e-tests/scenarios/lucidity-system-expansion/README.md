# lucidity System Expansion Scenarios

These scenarios extend the multiplayer test suite with coverage for the new lucidity workflows described in
`2025-11-13-lucidity-system-expansion`. Follow the master rules in `@MULTIPLAYER_TEST_RULES.md` before executing any
scenario.

## Scenario Index

`scenario-01-catatonia-grounding.md` – Validate catatonia detection, rescue channeling, and recovery success.

- `scenario-02-sanitarium-failover.md` – Validate automatic sanitarium transfer and the associated client feedback when

  rescue fails.

## Execution Notes

All scenarios require **two browser tabs** driven via Playwright MCP.

- Use the PostgreSQL CLI (psql) to seed catatonia state before connecting players.

- Keep the existing `ArkanWolfshade` (target) and `Ithaqua` (rescuer) fixtures in the PostgreSQL `mythos_e2e` database

  unless instructed otherwise.

- Whenever a scenario requires modifying the lucidity tables, run the SQL commands exactly as written and verify the row

  count before proceeding.

- After finishing each scenario, restore the altered lucidity rows to their original values to avoid cross-scenario

  contamination.
