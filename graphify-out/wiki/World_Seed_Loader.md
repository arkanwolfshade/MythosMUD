# World Seed Loader

> 31 nodes · cohesion 0.11

## Key Concepts

- **load_world_seed.py** (14 connections) — `scripts/load_world_seed.py`
- **_run_psql_file()** (11 connections) — `scripts/load_world_seed.py`
- **main()** (8 connections) — `scripts/load_world_seed.py`
- **Path** (6 connections) — `scripts/load_world_seed.py`
- **_apply_schema()** (5 connections) — `scripts/load_world_seed.py`
- **_apply_schema_with_psql()** (5 connections) — `scripts/load_world_seed.py`
- **_load_dml_with_psql()** (5 connections) — `scripts/load_world_seed.py`
- **_parse_pg_url_for_psql()** (4 connections) — `scripts/load_world_seed.py`
- **_print_current_table_counts()** (4 connections) — `scripts/load_world_seed.py`
- **_print_final_table_counts()** (4 connections) — `scripts/load_world_seed.py`
- **_resolve_psql_executable()** (4 connections) — `scripts/load_world_seed.py`
- **_validate_environment_and_files()** (4 connections) — `scripts/load_world_seed.py`
- **_asyncpg_server_settings()** (3 connections) — `scripts/load_world_seed.py`
- **_database_url_for_cli()** (3 connections) — `scripts/load_world_seed.py`
- **_psql_exit_code_extra()** (3 connections) — `scripts/load_world_seed.py`
- **_psql_heartbeat_wait()** (3 connections) — `scripts/load_world_seed.py`
- **Popen** (2 connections) — `scripts/load_world_seed.py`
- **Connection** (2 connections) — `scripts/load_world_seed.py`
- **Normalize SQLAlchemy/async driver URLs to a plain postgresql:// form for tools.** (1 connections) — `scripts/load_world_seed.py`
- **Return (host, port, user, password, dbname) from DATABASE_URL. Password may be e** (1 connections) — `scripts/load_world_seed.py`
- **Locate psql for DDL (pg_dump files are meant for psql, not one asyncpg.execute b** (1 connections) — `scripts/load_world_seed.py`
- **Match app/e2e search_path: tables live in schema mythos_*; default public would** (1 connections) — `scripts/load_world_seed.py`
- **Human hint when psql exits with code 3 (common for interrupt / server error).** (1 connections) — `scripts/load_world_seed.py`
- **Run a .sql file with psql (-q). Optionally kick competitors before -f (same sess** (1 connections) — `scripts/load_world_seed.py`
- **Apply DDL using psql -f (reliable for large multi-statement dumps; avoids long s** (1 connections) — `scripts/load_world_seed.py`
- *... and 6 more nodes in this community*

## Relationships

- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `scripts/load_world_seed.py`

## Audit Trail

- EXTRACTED: 102 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
