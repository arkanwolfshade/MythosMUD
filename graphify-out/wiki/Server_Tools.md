# Server Tools

> 33 nodes

## Key Concepts

- **._initialize_database()** (17 connections) — `server/database.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **set_test_database_url()** (9 connections) — `server/database_config_helpers.py`
- **load_database_url()** (7 connections) — `server/database_config_helpers.py`
- **main()** (7 connections) — `tools/invite_tools/generate_invites_db.py`
- **.get_session_maker()** (6 connections) — `server/database.py`
- **get_test_database_url()** (6 connections) — `server/database_config_helpers.py`
- **validate_database_url()** (6 connections) — `server/database_config_helpers.py`
- **normalize_database_url()** (6 connections) — `server/database_config_helpers.py`
- **create_invite_in_db()** (6 connections) — `tools/invite_tools/generate_invites_db.py`
- **async_sessionmaker** (5 connections)
- **AsyncSession** (5 connections)
- **_set_database_url_from_env()** (5 connections) — `tools/invite_tools/generate_invites_db.py`
- **parse_expires_date()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **generate_unique_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **get_existing_codes()** (4 connections) — `tools/invite_tools/generate_invites_db.py`
- **.get_database_url()** (3 connections) — `server/database.py`
- **datetime** (3 connections)
- **generate_invite_code()** (3 connections) — `tools/invite_tools/generate_invites_db.py`
- **Initialize database engine and session maker from configuration.          CRITIC** (2 connections) — `server/database.py`
- **Get test override database URL.** (2 connections) — `server/database_config_helpers.py`
- **Get the async session maker, initializing if necessary.          Returns:** (1 connections) — `server/database.py`
- **Get the database URL, initializing if necessary.          Returns:             s** (1 connections) — `server/database.py`
- **Load database URL from config or test override.      Returns:         Database U** (1 connections) — `server/database_config_helpers.py`
- **Validate database URL is set and is PostgreSQL.      Args:         database_url:** (1 connections) — `server/database_config_helpers.py`
- *... and 8 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (8 shared connections)
- [Server Infrastructure (2)](Server_Infrastructure_%282%29.md) (6 shared connections)
- [Server Services (42)](Server_Services_%2842%29.md) (6 shared connections)
- [Server Utils](Server_Utils.md) (5 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (5 shared connections)
- [Server Persistence](Server_Persistence.md) (3 shared connections)
- [Server Api](Server_Api.md) (3 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (2 shared connections)
- [Server Services](Server_Services.md) (2 shared connections)
- [Server Infrastructure (5)](Server_Infrastructure_%285%29.md) (2 shared connections)
- [Server Models (15)](Server_Models_%2815%29.md) (2 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)

## Source Files

- `server/database.py`
- `server/database_config_helpers.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 127 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*