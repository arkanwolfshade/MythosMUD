# Database Connection Pool Configuration

This document explains the connection pool configuration strategy for MythosMUD's PostgreSQL database connections.

## Overview

The codebase uses two different connection pool implementations:

1. **SQLAlchemy AsyncAdaptedQueuePool** - For SQLAlchemy ORM operations
2. **asyncpg Pool** - For direct asyncpg operations (AsyncPersistenceLayer)

## SQLAlchemy Connection Pool

**Location**: `server/database.py`

**Pool Type**: `AsyncAdaptedQueuePool` (default for async engines)

**Configuration**:

- `pool_size`: Number of connections to maintain in pool (default: 5)
- `max_overflow`: Additional connections beyond pool_size (default: 10)
- `pool_timeout`: Seconds to wait for connection from pool (default: 30)
- `pool_pre_ping`: Enable connection health checks (default: true)

**Current Settings** (from `server/config/models.py`):

```python
pool_size: int = 5
max_overflow: int = 10
pool_timeout: int = 30
```

**Total Maximum Connections**: `pool_size + max_overflow = 15` connections

**Test Configuration**: Uses `NullPool` (no connection pooling) for test isolation

## AsyncPG Connection Pool

**Location**: `server/async_persistence.py`

**Pool Type**: `asyncpg.Pool`

**Configuration**:

- `min_size`: Minimum connections in pool (default: 1)
- `max_size`: Maximum connections in pool (default: 10)
- `command_timeout`: Command timeout in seconds (default: 60)

**Current Settings** (from `server/config/models.py`):

```python
asyncpg_pool_min_size: int = 1
asyncpg_pool_max_size: int = 10
asyncpg_command_timeout: int = 60
```

## Pool Sizing Strategy

### Production Recommendations

**For Low Traffic (< 100 concurrent users)**:

- SQLAlchemy: `pool_size=5`, `max_overflow=10` (total: 15)
- AsyncPG: `min_size=2`, `max_size=10`

**For Medium Traffic (100-500 concurrent users)**:

- SQLAlchemy: `pool_size=10`, `max_overflow=20` (total: 30)
- AsyncPG: `min_size=5`, `max_size=20`

**For High Traffic (500+ concurrent users)**:

- SQLAlchemy: `pool_size=20`, `max_overflow=30` (total: 50)
- AsyncPG: `min_size=10`, `max_size=50`

### Sizing Formula

```
pool_size = (expected_concurrent_requests / avg_request_duration_seconds) * 1.2
max_overflow = pool_size * 2
```

**Example**:

- 100 concurrent requests
- Average request duration: 0.1 seconds
- `pool_size = (100 / 0.1) * 1.2 = 12` (round to 15)
- `max_overflow = 15 * 2 = 30`

## Configuration via Environment Variables

All pool settings can be configured via environment variables:

```bash
# SQLAlchemy pool settings

DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20
DATABASE_POOL_TIMEOUT=30

# AsyncPG pool settings

DATABASE_ASYNCPG_POOL_MIN_SIZE=2
DATABASE_ASYNCPG_POOL_MAX_SIZE=20
DATABASE_ASYNCPG_COMMAND_TIMEOUT=60
```

## Monitoring Pool Health

### Key Metrics to Track

1. **Pool Exhaustion Events**

   - Monitor for `PoolAcquireTimeoutError` exceptions
   - Indicates pool is too small or connections are held too long

2. **Connection Wait Time**

   - Time spent waiting for available connection
   - Should be < 100ms under normal load

3. **Active Connections**

   - Number of connections currently in use
   - Should stay below `pool_size + max_overflow`

4. **Connection Creation Rate**

   - Frequency of new connection creation
   - High rate indicates pool churn

### Logging

Pool events are logged at debug level:

- Connection acquisition
- Connection release
- Pool exhaustion warnings
- Connection errors

Enable debug logging to monitor pool behavior:

```python
# In logging configuration

logger.setLevel(logging.DEBUG)
```

## Troubleshooting Pool Exhaustion

### Symptoms

`PoolAcquireTimeoutError` exceptions

- Slow response times
- High connection wait times
- Database connection errors

### Diagnosis

1. **Check Active Connections**:

   ```sql
   SELECT count(*) FROM pg_stat_activity WHERE datname = 'your_database';
   ```

2. **Check Pool Configuration**:

   - Verify `pool_size` and `max_overflow` settings
   - Check if connections are being held too long

3. **Review Application Code**:

   - Ensure sessions are properly closed
   - Check for long-running transactions
   - Verify no connection leaks

### Solutions

1. **Increase Pool Size**:

   ```bash
   DATABASE_POOL_SIZE=20
   DATABASE_MAX_OVERFLOW=30
   ```

2. **Reduce Connection Hold Time**:

   - Use shorter transactions
   - Close sessions promptly
   - Avoid blocking operations in transactions

3. **Add Connection Pooling at Database Level**:

   - Use PgBouncer for connection pooling
   - Reduces connection overhead

## Best Practices

### Do's

✅ Use connection pools for all database operations

✅ Configure pool size based on expected load

✅ Monitor pool metrics in production

✅ Use context managers for session management

✅ Close sessions promptly after use

### Don'ts

❌ Don't create connections outside of pools

❌ Don't hold connections for long periods

❌ Don't ignore pool exhaustion warnings

❌ Don't use excessive pool sizes (wastes resources)

❌ Don't mix pool configurations across environments

## Performance Tuning

### Connection Pool Pre-Ping

SQLAlchemy's `pool_pre_ping=True` (enabled by default) checks connection health before use. This adds slight overhead
but prevents stale connection errors.

**When to Disable**: Only if you have very high connection churn and can tolerate occasional stale connection errors.

### Pool Timeout

`pool_timeout` determines how long to wait for a connection. Too short causes failures; too long causes slow responses.

**Recommended**: 30 seconds (current default)

### Command Timeout

AsyncPG's `command_timeout` prevents queries from hanging indefinitely.

**Recommended**: 60 seconds (current default)

## Production Checklist

[ ] Pool size configured for expected load

- [ ] Monitoring enabled for pool metrics
- [ ] Alerts configured for pool exhaustion
- [ ] Connection leaks tested and fixed
- [ ] Pool configuration documented
- [ ] Load testing performed with pool settings
- [ ] Backup pool configuration ready

## References

[SQLAlchemy Connection Pooling](https://docs.sqlalchemy.org/en/20/core/pooling.html)

- [asyncpg Connection Pooling](https://magicstack.github.io/asyncpg/current/api/index.html#connection-pools)
- [PostgreSQL Connection Pooling Best Practices](https://www.postgresql.org/docs/current/runtime-config-connection.html)

---

*"In the restricted archives, we learn that connection pools are like the dimensional gateways of the Mythos - they must
be carefully maintained lest they collapse under the weight of too many simultaneous travelers, or remain empty and
unused, wasting precious resources."*
