# Item System Observability Runbook

## Purpose

This runbook equips operators with the steps required to keep the MythosMUD item
system healthy during prototype updates, administrative summon rituals, and data
recoveries.  It complements the structured logging and alerting hooks delivered
in Phase 4 of the Item System implementation.

---

### Seed Regeneration Checklist

1. **Stop Game Services**

   - `./scripts/stop_server.ps1`
   - Confirm ports `54731` and `5173` are free.

2. **Regenerate Databases**

   - `./scripts/items/init_item_databases.ps1`

   - Verify databases under `/data/<env>/items/` were updated within the last

     minute.

3. **Smoke Test Prototype Loads**

   - `uv run pytest server/tests/unit/game/test_prototype_registry.py`

   - Confirm no `prototype_registry_failure` alerts appear in

     `/monitoring/alerts`.

4. **Restart Services**

   - `./scripts/start_local.ps1`
   - Monitor logs for `Monitoring dashboard initialized`.

---

### Administrative Summon Etiquette

Treat `quantity > 5` as an escalation.  The observability harness will emit a
  `summon_quantity_spike` alert that pings the on-call engineer.  Reduce the
  quantity or obtain leadership approval before retrying.

- All summon activity is now recorded with `source=admin_summon`, `summoned_by`,

  and `quantity`.  Reference `/logs/local/admin_actions_*.log` when auditing.

- NPC requests are still stubbed—use `npc spawn` instead.  The harness records a

  `prototype_registry_failure` if the registry is offline and enforces alerting
  on repeated misuse.

---

### Migration & Durability Recovery

1. **Identify the Alert**

   - Alert type `prototype_registry_failure` → review affected file paths.

   - Alert type `durability_anomaly` → a prototype with

     `component.durability` lacks an explicit `durability` value.

2. **Rollback / Fix**

   - Restore the offending prototype JSON from source control or add the

     missing durability field.

   - Re-run `scripts/items/validate_prototypes.ps1`.

3. **Validate**

   - `uv run pytest server/tests/unit/game/test_prototype_registry.py -k durability`
   - Resolve the alert via `POST /monitoring/alerts/{alert_id}/resolve`.

4. **Document Outcome**

   - Update the operational log with the root cause, fix, and validation steps.
   - If durability values were altered, notify design to confirm balance impact.
