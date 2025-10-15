# Troubleshooting Guide for MythosMUD

*As documented in the restricted archives of Miskatonic University, the proper diagnosis and resolution of system anomalies requires both technical expertise and an understanding of the deeper patterns that govern our digital realm.*

## Overview

This guide provides comprehensive troubleshooting procedures for common issues in the MythosMUD system. Our structured error logging and monitoring tools provide the foundation for effective problem diagnosis and resolution.

## Quick Diagnostic Commands

### System Health Check

```bash
# Check server status
python scripts/error_monitoring.py --log-dir logs/development --rate

# Generate error report
python scripts/analyze_error_logs.py --log-dir logs/development --report

# Monitor real-time errors
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 10 --duration 300
```

### Log Analysis

```bash
# Analyze error patterns
python scripts/analyze_error_logs.py --log-dir logs/development --patterns

# Detect error trends
python scripts/analyze_error_logs.py --log-dir logs/development --trends

# Check for alerts
python scripts/error_monitoring.py --log-dir logs/development --alerts
```

## Common Issues and Solutions

### 1. Database Connection Issues

#### Symptoms
- Errors in logs: "Database connection failed"
- Players unable to save progress
- API endpoints returning 500 errors
- High error rates in monitoring

#### Diagnosis
```bash
# Check database-specific errors
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | grep -i database

# Monitor database errors in real-time
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 5
```

#### Common Causes and Solutions

**Database File Permissions**
```bash
# Check database file permissions
ls -la data/players/
# Should show read/write permissions for the server user

# Fix permissions if needed
chmod 664 data/players/*.db
chown mythosmud:mythosmud data/players/*.db
```

**Database Lock Issues**
```bash
# Check for database locks
lsof data/players/*.db

# Kill processes holding locks (if safe to do so)
kill -9 <process_id>
```

**Database Corruption**
```bash
# Check database integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"

# If corruption detected, restore from backup
cp data/players/local_players.db.backup data/players/local_players.db
```

**Connection Pool Exhaustion**
```python
# Check connection pool status in logs
grep -i "connection.*pool" logs/development/server.log

# Look for patterns like:
# "Database connection pool exhausted"
# "No available connections in pool"
```

### 2. WebSocket Connection Issues

#### Symptoms
- Players experiencing disconnections
- "WebSocket connection timeout" errors
- Real-time features not working
- High network error rates

#### Diagnosis
```bash
# Analyze network errors
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | grep -i websocket

# Check connection manager logs
grep -i "connection.*manager" logs/development/server.log
```

#### Common Causes and Solutions

**Connection Timeout**
```python
# Check WebSocket timeout configuration
# In server configuration
WEBSOCKET_TIMEOUT = 30  # seconds
WEBSOCKET_PING_INTERVAL = 20  # seconds
WEBSOCKET_PING_TIMEOUT = 10  # seconds
```

**Memory Leaks in Connections**
```bash
# Monitor memory usage
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 30

# Look for increasing memory usage patterns
# Check for connection cleanup in logs
grep -i "cleaning.*connection" logs/development/server.log
```

**Network Configuration Issues**
```bash
# Check server network configuration
netstat -tlnp | grep :8000

# Check firewall rules
iptables -L | grep 8000

# Test WebSocket connectivity
curl -i -N -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Key: test" -H "Sec-WebSocket-Version: 13" http://localhost:8000/ws
```

### 3. Authentication Issues

#### Symptoms
- Users unable to log in
- "Invalid credentials" errors
- Token validation failures
- Authentication timeouts

#### Diagnosis
```bash
# Check authentication errors
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | grep -i auth

# Monitor authentication attempts
grep -i "authentication" logs/development/authentication.log
```

#### Common Causes and Solutions

**Token Expiration**
```python
# Check token expiration configuration
JWT_EXPIRATION_TIME = 3600  # 1 hour
REFRESH_TOKEN_EXPIRATION = 86400  # 24 hours

# Look for token expiration errors in logs
grep -i "token.*expired" logs/development/authentication.log
```

**Password Hashing Issues**
```bash
# Check for hashing errors
grep -i "hashing.*error" logs/development/authentication.log

# Verify Argon2 configuration
python -c "import argon2; print('Argon2 available')"
```

**Session Management**
```bash
# Check session storage
ls -la data/sessions/

# Look for session cleanup issues
grep -i "session.*cleanup" logs/development/server.log
```

### 4. Performance Issues

#### Symptoms
- Slow response times
- High CPU usage
- Memory consumption growing
- Timeout errors

#### Diagnosis
```bash
# Monitor system performance
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 10

# Check for performance-related errors
grep -i "timeout\|slow\|performance" logs/development/server.log
```

#### Common Causes and Solutions

**Database Query Performance**
```python
# Check for slow queries in logs
grep -i "duration.*ms" logs/development/server.log | sort -k5 -nr

# Look for patterns like:
# "Database query executed", "duration_ms": 5000
```

**Memory Leaks**
```bash
# Monitor memory usage over time
python -c "
import psutil
import time
for i in range(10):
    print(f'Memory: {psutil.virtual_memory().percent}%')
    time.sleep(30)
"

# Check for memory-related errors
grep -i "memory\|out of memory" logs/development/server.log
```

**Resource Exhaustion**
```bash
# Check system resources
top -p $(pgrep -f mythosmud)
df -h
free -h

# Look for resource-related errors
grep -i "resource.*exhausted\|too many" logs/development/server.log
```

### 5. Game Logic Issues

#### Symptoms
- Players unable to move
- Commands not working
- Room transitions failing
- Game state inconsistencies

#### Diagnosis
```bash
# Check game logic errors
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | grep -i "game\|player\|room"

# Monitor command processing
grep -i "command.*failed" logs/development/commands.log
```

#### Common Causes and Solutions

**Room Data Corruption**
```bash
# Check room data integrity
find data/world/ -name "*.json" -exec python -m json.tool {} \; > /dev/null

# Look for room loading errors
grep -i "room.*not found\|room.*invalid" logs/development/world.log
```

**Player State Issues**
```bash
# Check player data integrity
sqlite3 data/players/local_players.db "SELECT COUNT(*) FROM players WHERE current_room_id IS NULL;"

# Look for player state errors
grep -i "player.*state\|player.*not found" logs/development/server.log
```

**Command Processing Failures**
```bash
# Check command processing errors
grep -i "command.*processing\|validation.*failed" logs/development/commands.log

# Look for specific command failures
grep -i "go.*command\|move.*command" logs/development/commands.log
```

## Advanced Troubleshooting

### Log Analysis Techniques

#### Pattern Recognition
```bash
# Find most common error patterns
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | head -20

# Analyze error trends over time
python scripts/analyze_error_logs.py --log-dir logs/development --trends
```

#### Error Correlation
```bash
# Find errors that occur together
grep -A 5 -B 5 "Database connection failed" logs/development/server.log

# Look for error cascades
grep -i "caused by\|due to" logs/development/server.log
```

#### Performance Analysis
```bash
# Find slow operations
grep -E "duration_ms.*[5-9][0-9]{3,}" logs/development/server.log

# Analyze response times
grep -E "API request completed.*duration_ms" logs/development/server.log | awk '{print $NF}' | sort -n
```

### System Monitoring

#### Real-time Monitoring
```bash
# Monitor errors in real-time
python scripts/error_monitoring.py --log-dir logs/development --monitor --interval 5 --duration 600

# Check for alert conditions
python scripts/error_monitoring.py --log-dir logs/development --alerts
```

#### Resource Monitoring
```bash
# Monitor system resources
watch -n 5 'ps aux | grep mythosmud; echo; free -h; echo; df -h'

# Monitor network connections
watch -n 5 'netstat -an | grep :8000 | wc -l'
```

### Debugging Techniques

#### Enable Debug Logging
```python
# In development configuration
LOGGING_LEVEL = "DEBUG"
ENABLE_DEBUG_LOGGING = True

# Restart server to apply changes
./scripts/stop_server.ps1
./scripts/start_local.ps1
```

#### Trace Specific Operations
```python
# Add detailed logging to specific operations
import structlog
logger = structlog.get_logger(__name__)

def debug_operation():
    logger.debug("Operation started", operation="debug_test")
    # ... operation code ...
    logger.debug("Operation completed", operation="debug_test", result="success")
```

#### Use Debugging Tools
```bash
# Use Python debugger
python -m pdb server/main.py

# Use profiling tools
python -m cProfile -o profile.stats server/main.py
python -c "import pstats; pstats.Stats('profile.stats').sort_stats('cumulative').print_stats(20)"
```

## Emergency Procedures

### System Recovery

#### Database Recovery
```bash
# Stop server
./scripts/stop_server.ps1

# Backup current database
cp data/players/local_players.db data/players/local_players.db.emergency_backup

# Restore from last known good backup
cp data/players/local_players.db.backup data/players/local_players.db

# Verify database integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"

# Restart server
./scripts/start_local.ps1
```

#### Log File Management
```bash
# Archive current logs
mkdir -p logs/archives/$(date +%Y%m%d_%H%M%S)
mv logs/development/*.log logs/archives/$(date +%Y%m%d_%H%M%S)/

# Restart server to create new log files
./scripts/stop_server.ps1
./scripts/start_local.ps1
```

#### Memory Recovery
```bash
# Check for memory leaks
ps aux | grep mythosmud

# Restart server if memory usage is excessive
./scripts/stop_server.ps1
sleep 5
./scripts/start_local.ps1
```

### Incident Response

#### High Error Rate
```bash
# Immediate response
python scripts/error_monitoring.py --log-dir logs/development --alerts

# If critical errors detected
./scripts/stop_server.ps1
# Investigate logs
python scripts/analyze_error_logs.py --log-dir logs/development --report
# Fix issues
# Restart server
./scripts/start_local.ps1
```

#### System Unresponsive
```bash
# Check if server is running
ps aux | grep mythosmud

# If not responding, force kill
pkill -f mythosmud

# Check for core dumps
ls -la core.*

# Restart server
./scripts/start_local.ps1
```

#### Data Corruption
```bash
# Stop server immediately
./scripts/stop_server.ps1

# Backup current state
tar -czf emergency_backup_$(date +%Y%m%d_%H%M%S).tar.gz data/

# Restore from backup
tar -xzf latest_backup.tar.gz

# Verify data integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"

# Restart server
./scripts/start_local.ps1
```

## Prevention Strategies

### Monitoring Setup

#### Automated Monitoring
```bash
# Set up cron job for regular monitoring
crontab -e

# Add line for every 5 minutes
*/5 * * * * /path/to/mythosmud/scripts/error_monitoring.py --log-dir /path/to/mythosmud/logs/development --alerts >> /var/log/mythosmud_monitoring.log 2>&1
```

#### Alert Configuration
```python
# Configure alert thresholds
ALERT_THRESHOLDS = {
    "error_rate": 10,      # errors per minute
    "error_spike": 50,     # errors in 5 minutes
    "critical_errors": 5,  # critical errors in 5 minutes
    "memory_usage": 85,    # memory usage percentage
    "cpu_usage": 90,       # CPU usage percentage
}
```

### Regular Maintenance

#### Daily Checks
```bash
# Check system health
python scripts/error_monitoring.py --log-dir logs/development --rate

# Review error patterns
python scripts/analyze_error_logs.py --log-dir logs/development --patterns | head -10

# Check disk space
df -h
```

#### Weekly Maintenance
```bash
# Generate comprehensive report
python scripts/analyze_error_logs.py --log-dir logs/development --report > weekly_report.txt

# Clean up old logs
find logs/ -name "*.log.*" -mtime +7 -delete

# Check database integrity
sqlite3 data/players/local_players.db "PRAGMA integrity_check;"
```

#### Monthly Reviews
```bash
# Analyze error trends
python scripts/analyze_error_logs.py --log-dir logs/development --trends

# Review performance metrics
grep -E "duration_ms.*[0-9]+" logs/development/server.log | awk '{print $NF}' | sort -n | tail -100

# Update documentation based on findings
```

## Getting Help

### Internal Resources

1. **Log Analysis Tools**: Use our custom tools for detailed analysis
2. **Documentation**: Consult this guide and related documentation
3. **Code Comments**: Check source code for implementation details

### External Resources

1. **FastAPI Documentation**: https://fastapi.tiangolo.com/
2. **SQLite Documentation**: https://www.sqlite.org/docs.html
3. **Structlog Documentation**: https://www.structlog.org/

### Escalation Procedures

1. **Level 1**: Check logs and apply common solutions
2. **Level 2**: Use advanced troubleshooting techniques
3. **Level 3**: Contact system administrators
4. **Level 4**: Escalate to development team

## Conclusion

Effective troubleshooting requires a systematic approach and the proper use of our monitoring and analysis tools. By following this guide:

- Use our log analysis tools for pattern recognition
- Apply systematic diagnosis procedures
- Implement proper monitoring and alerting
- Maintain regular system health checks
- Document issues and solutions for future reference

Remember: *As the restricted archives teach us, the proper diagnosis of system anomalies requires both technical expertise and an understanding of the deeper patterns that govern our digital realm. With proper tools and procedures, even the most obscure issues can be resolved.*

---

*This guide is maintained by the Department of Occult Studies, Miskatonic University. For questions or clarifications, consult the restricted archives or contact the system administrators.*
