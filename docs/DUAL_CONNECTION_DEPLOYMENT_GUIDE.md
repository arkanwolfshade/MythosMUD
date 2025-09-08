# Dual Connection System Deployment Guide

## Overview

This guide provides comprehensive instructions for deploying the dual WebSocket/SSE connection system in various environments. The system is designed to be scalable, reliable, and performant across different deployment scenarios.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Environment Configuration](#environment-configuration)
3. [Server Deployment](#server-deployment)
4. [Client Deployment](#client-deployment)
5. [Database Configuration](#database-configuration)
6. [Monitoring Setup](#monitoring-setup)
7. [Load Balancing](#load-balancing)
8. [Security Configuration](#security-configuration)
9. [Performance Tuning](#performance-tuning)
10. [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements

**Server Requirements:**
- Python 3.12+
- Node.js 18+
- SQLite 3.35+ (or PostgreSQL 13+ for production)
- 4GB+ RAM (8GB+ recommended for production)
- 2+ CPU cores (4+ recommended for production)

**Client Requirements:**
- Modern web browser with WebSocket and EventSource support
- JavaScript enabled
- HTTPS connection (required for production)

### Dependencies

**Server Dependencies:**
```bash
# Python dependencies
uvicorn>=0.24.0
fastapi>=0.104.0
websockets>=12.0
structlog>=23.0.0
pydantic>=2.0.0
sqlalchemy>=2.0.0

# Node.js dependencies (for client)
react>=18.0.0
typescript>=4.9.0
vite>=4.0.0
```

## Environment Configuration

### Environment Variables

Create a `.env` file with the following configuration:

```bash
# Server Configuration
DATABASE_URL=sqlite:///./data/players/mythos.db
SECRET_KEY=your-secret-key-here
DEBUG=false
LOG_LEVEL=INFO

# Connection Configuration
MAX_CONNECTIONS_PER_PLAYER=4
CONNECTION_TIMEOUT=300
HEALTH_CHECK_INTERVAL=30
CLEANUP_INTERVAL=60

# Performance Configuration
MESSAGE_BATCH_SIZE=100
CONNECTION_POOL_SIZE=1000
PERFORMANCE_MONITORING=true

# Security Configuration
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60

# Monitoring Configuration
ENABLE_METRICS=true
METRICS_PORT=9090
LOG_FORMAT=json
```

### Production Environment Variables

```bash
# Production-specific settings
DATABASE_URL=postgresql://user:password@localhost:5432/mythos_prod
SECRET_KEY=your-production-secret-key
DEBUG=false
LOG_LEVEL=WARNING

# Enhanced security
CORS_ORIGINS=https://yourdomain.com
RATE_LIMIT_REQUESTS=50
RATE_LIMIT_WINDOW=60

# Performance optimization
MAX_CONNECTIONS_PER_PLAYER=2
CONNECTION_TIMEOUT=180
HEALTH_CHECK_INTERVAL=15
CLEANUP_INTERVAL=30

# Monitoring
ENABLE_METRICS=true
METRICS_PORT=9090
LOG_FORMAT=json
SENTRY_DSN=your-sentry-dsn
```

## Server Deployment

### Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create data directory
RUN mkdir -p /app/data/players

# Expose ports
EXPOSE 8000 9090

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start server
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  mythos-server:
    build: .
    ports:
      - "8000:8000"
      - "9090:9090"
    environment:
      - DATABASE_URL=sqlite:///./data/players/mythos.db
      - SECRET_KEY=your-secret-key
      - DEBUG=false
      - LOG_LEVEL=INFO
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  mythos-client:
    build:
      context: ./client
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
      - REACT_APP_WS_URL=ws://localhost:8000
    depends_on:
      - mythos-server
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - mythos-server
      - mythos-client
    restart: unless-stopped
```

### Manual Deployment

**1. Install Dependencies:**
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
cd client
npm install
npm run build
cd ..
```

**2. Initialize Database:**
```bash
# Create database directory
mkdir -p data/players

# Initialize database schema
python server/scripts/init_db.py

# Verify database
python server/scripts/verify_db.py
```

**3. Start Server:**
```bash
# Development
uvicorn server.main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn server.main:app --host 0.0.0.0 --port 8000 --workers 4
```

**4. Start Client:**
```bash
cd client
npm run build
npm run preview
```

## Client Deployment

### Build Configuration

**vite.config.ts:**
```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'terser',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          connection: ['./src/hooks/useGameConnection.ts']
        }
      }
    }
  },
  server: {
    proxy: {
      '/api': 'http://localhost:8000',
      '/ws': {
        target: 'ws://localhost:8000',
        ws: true
      },
      '/sse': 'http://localhost:8000'
    }
  }
});
```

### Environment Configuration

**Client Environment Variables:**
```bash
# .env.production
REACT_APP_API_URL=https://api.yourdomain.com
REACT_APP_WS_URL=wss://api.yourdomain.com
REACT_APP_SSE_URL=https://api.yourdomain.com
REACT_APP_ENVIRONMENT=production
REACT_APP_DEBUG=false
```

### Build and Deploy

```bash
# Build for production
npm run build

# Deploy to static hosting
# Copy dist/ contents to your web server
```

## Database Configuration

### SQLite (Development)

```bash
# Create database directory
mkdir -p data/players

# Initialize database
python server/scripts/init_db.py

# Verify database
python server/scripts/verify_db.py
```

### PostgreSQL (Production)

**1. Install PostgreSQL:**
```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# CentOS/RHEL
sudo yum install postgresql-server postgresql-contrib
```

**2. Create Database:**
```sql
-- Connect to PostgreSQL
sudo -u postgres psql

-- Create database and user
CREATE DATABASE mythos_prod;
CREATE USER mythos_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE mythos_prod TO mythos_user;
```

**3. Update Configuration:**
```bash
# Update .env
DATABASE_URL=postgresql://mythos_user:secure_password@localhost:5432/mythos_prod
```

**4. Initialize Database:**
```bash
python server/scripts/init_db.py
```

## Monitoring Setup

### Prometheus Configuration

**prometheus.yml:**
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'mythos-server'
    static_configs:
      - targets: ['localhost:9090']
    metrics_path: '/metrics'
    scrape_interval: 5s
```

### Grafana Dashboard

**Dashboard Configuration:**
```json
{
  "dashboard": {
    "title": "MythosMUD Dual Connection System",
    "panels": [
      {
        "title": "Connection Statistics",
        "type": "stat",
        "targets": [
          {
            "expr": "mythos_connections_total",
            "legendFormat": "Total Connections"
          }
        ]
      },
      {
        "title": "Connection Health",
        "type": "gauge",
        "targets": [
          {
            "expr": "mythos_connection_health_percentage",
            "legendFormat": "Health Percentage"
          }
        ]
      },
      {
        "title": "Message Delivery Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(mythos_messages_delivered_total[5m])",
            "legendFormat": "Messages/sec"
          }
        ]
      }
    ]
  }
}
```

### Logging Configuration

**log_config.yaml:**
```yaml
version: 1
disable_existing_loggers: false

formatters:
  standard:
    format: '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
  json:
    format: '%(asctime)s %(levelname)s %(name)s %(message)s'

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    formatter: standard
    stream: ext://sys.stdout

  file:
    class: logging.handlers.RotatingFileHandler
    level: INFO
    formatter: json
    filename: logs/mythos.log
    maxBytes: 10485760  # 10MB
    backupCount: 5

loggers:
  server:
    level: INFO
    handlers: [console, file]
    propagate: false

  server.realtime:
    level: DEBUG
    handlers: [console, file]
    propagate: false

root:
  level: INFO
  handlers: [console]
```

## Load Balancing

### Nginx Configuration

**nginx.conf:**
```nginx
upstream mythos_backend {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
    server 127.0.0.1:8003;
}

upstream mythos_websocket {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
    server 127.0.0.1:8003;
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # WebSocket proxy
    location /ws/ {
        proxy_pass http://mythos_websocket;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }

    # SSE proxy
    location /sse/ {
        proxy_pass http://mythos_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
        proxy_cache off;
    }

    # API proxy
    location /api/ {
        proxy_pass http://mythos_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files
    location / {
        root /var/www/mythos/client/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

### Multiple Server Deployment

**docker-compose.prod.yml:**
```yaml
version: '3.8'

services:
  mythos-server-1:
    build: .
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/mythos_prod
      - SERVER_ID=1
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis

  mythos-server-2:
    build: .
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/mythos_prod
      - SERVER_ID=2
    ports:
      - "8001:8000"
    depends_on:
      - postgres
      - redis

  mythos-server-3:
    build: .
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/mythos_prod
      - SERVER_ID=3
    ports:
      - "8002:8000"
    depends_on:
      - postgres
      - redis

  mythos-server-4:
    build: .
    environment:
      - DATABASE_URL=postgresql://user:password@postgres:5432/mythos_prod
      - SERVER_ID=4
    ports:
      - "8003:8000"
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=mythos_prod
      - POSTGRES_USER=mythos_user
      - POSTGRES_PASSWORD=secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## Security Configuration

### SSL/TLS Setup

**1. Generate SSL Certificate:**
```bash
# Using Let's Encrypt
sudo certbot --nginx -d yourdomain.com

# Or using self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

**2. Update Nginx Configuration:**
```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
}
```

### Firewall Configuration

**UFW (Ubuntu):**
```bash
# Allow SSH
sudo ufw allow ssh

# Allow HTTP and HTTPS
sudo ufw allow 80
sudo ufw allow 443

# Allow monitoring port (restrict to localhost)
sudo ufw allow from 127.0.0.1 to any port 9090

# Enable firewall
sudo ufw enable
```

**iptables:**
```bash
# Allow HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow monitoring port (localhost only)
iptables -A INPUT -p tcp -s 127.0.0.1 --dport 9090 -j ACCEPT

# Save rules
iptables-save > /etc/iptables/rules.v4
```

### Rate Limiting

**Nginx Rate Limiting:**
```nginx
http {
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=ws:10m rate=5r/s;

    server {
        location /api/ {
            limit_req zone=api burst=20 nodelay;
            proxy_pass http://mythos_backend;
        }

        location /ws/ {
            limit_req zone=ws burst=10 nodelay;
            proxy_pass http://mythos_websocket;
        }
    }
}
```

## Performance Tuning

### Server Optimization

**1. Connection Pool Configuration:**
```python
# server/config.py
CONNECTION_POOL_SIZE = 1000
MAX_CONNECTIONS_PER_PLAYER = 4
CONNECTION_TIMEOUT = 300
HEALTH_CHECK_INTERVAL = 30
CLEANUP_INTERVAL = 60
```

**2. Database Optimization:**
```sql
-- PostgreSQL optimization
CREATE INDEX CONCURRENTLY idx_connections_player_id ON connections(player_id);
CREATE INDEX CONCURRENTLY idx_connections_session_id ON connections(session_id);
CREATE INDEX CONCURRENTLY idx_connections_created_at ON connections(created_at);

-- Analyze tables
ANALYZE connections;
ANALYZE sessions;
```

**3. Memory Optimization:**
```python
# server/main.py
import gc
import asyncio

# Enable garbage collection
gc.set_threshold(700, 10, 10)

# Optimize asyncio
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
```

### Client Optimization

**1. Connection Management:**
```typescript
// client/src/hooks/useGameConnection.ts
const CONNECTION_RETRY_DELAY = 5000;
const MAX_RETRY_ATTEMPTS = 5;
const HEALTH_CHECK_INTERVAL = 30000;
```

**2. Message Batching:**
```typescript
// Batch messages to reduce network overhead
const messageBatch: Message[] = [];
const BATCH_SIZE = 10;
const BATCH_TIMEOUT = 100; // ms

const flushMessages = () => {
  if (messageBatch.length > 0) {
    sendBatch(messageBatch);
    messageBatch.length = 0;
  }
};
```

## Troubleshooting

### Common Deployment Issues

**1. Connection Refused:**
```bash
# Check if server is running
netstat -tlnp | grep :8000

# Check server logs
tail -f logs/mythos.log

# Test connectivity
curl -v http://localhost:8000/health
```

**2. Database Connection Issues:**
```bash
# Check database connectivity
python -c "import sqlite3; print(sqlite3.connect('data/players/mythos.db').execute('SELECT 1').fetchone())"

# For PostgreSQL
psql -h localhost -U mythos_user -d mythos_prod -c "SELECT 1;"
```

**3. SSL Certificate Issues:**
```bash
# Check certificate validity
openssl x509 -in cert.pem -text -noout

# Test SSL connection
openssl s_client -connect yourdomain.com:443
```

### Performance Issues

**1. High Memory Usage:**
```bash
# Monitor memory usage
htop
ps aux | grep python

# Check for memory leaks
python -m memory_profiler server/main.py
```

**2. Slow Connection Establishment:**
```bash
# Check network latency
ping yourdomain.com
traceroute yourdomain.com

# Monitor connection times
curl -w "@curl-format.txt" -o /dev/null -s http://yourdomain.com/api/health
```

**3. Database Performance:**
```sql
-- Check slow queries
SELECT query, mean_time, calls
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Check connection count
SELECT count(*) FROM pg_stat_activity;
```

### Monitoring and Alerting

**1. Health Check Endpoint:**
```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "connections": connection_manager.get_active_connection_count(),
        "database": await check_database_health()
    }
```

**2. Alerting Configuration:**
```yaml
# alertmanager.yml
route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'web.hook'

receivers:
- name: 'web.hook'
  webhook_configs:
  - url: 'http://yourdomain.com/alerts'
    send_resolved: true

# prometheus.yml
rule_files:
  - "mythos_alerts.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093
```

**3. Log Analysis:**
```bash
# Monitor error rates
grep "ERROR" logs/mythos.log | tail -100

# Check connection patterns
grep "WebSocket connected" logs/mythos.log | wc -l

# Monitor performance
grep "connection_establishment" logs/mythos.log | tail -50
```

## Maintenance

### Regular Maintenance Tasks

**1. Database Maintenance:**
```bash
# Daily database backup
pg_dump mythos_prod > backup_$(date +%Y%m%d).sql

# Weekly database optimization
psql mythos_prod -c "VACUUM ANALYZE;"

# Monthly database cleanup
psql mythos_prod -c "DELETE FROM old_connections WHERE created_at < NOW() - INTERVAL '30 days';"
```

**2. Log Rotation:**
```bash
# Configure logrotate
cat > /etc/logrotate.d/mythos << EOF
/var/log/mythos/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 mythos mythos
    postrotate
        systemctl reload mythos
    endscript
}
EOF
```

**3. Security Updates:**
```bash
# Update system packages
sudo apt update && sudo apt upgrade

# Update Python dependencies
pip install --upgrade -r requirements.txt

# Update Node.js dependencies
cd client && npm update
```

### Backup and Recovery

**1. Database Backup:**
```bash
#!/bin/bash
# backup_db.sh
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/mythos"
mkdir -p $BACKUP_DIR

# PostgreSQL backup
pg_dump mythos_prod | gzip > $BACKUP_DIR/mythos_$DATE.sql.gz

# Keep only last 30 days
find $BACKUP_DIR -name "mythos_*.sql.gz" -mtime +30 -delete
```

**2. Configuration Backup:**
```bash
#!/bin/bash
# backup_config.sh
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/config"
mkdir -p $BACKUP_DIR

# Backup configuration files
tar -czf $BACKUP_DIR/config_$DATE.tar.gz \
    /etc/nginx/nginx.conf \
    /etc/nginx/ssl/ \
    .env \
    docker-compose.yml
```

**3. Recovery Procedures:**
```bash
# Database recovery
gunzip -c backup_20250106_120000.sql.gz | psql mythos_prod

# Configuration recovery
tar -xzf config_20250106_120000.tar.gz -C /

# Service restart
systemctl restart mythos
systemctl restart nginx
```

---

*This deployment guide is maintained as part of the MythosMUD dual connection system implementation. Last updated: 2025-01-06*
