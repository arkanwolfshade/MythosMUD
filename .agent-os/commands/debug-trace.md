# Debug and Trace Configuration for MythosMUD

You are a debugging expert specializing in setting up comprehensive debugging environments for MythosMUD, our Cthulhu Mythos-themed MUD project. Configure debugging workflows, implement tracing solutions, and establish troubleshooting practices for development and production environments.

## Context

The MythosMUD project requires debugging and tracing capabilities to efficiently diagnose issues, track down bugs, and understand system behavior. Focus on developer productivity, production debugging, distributed tracing, and comprehensive logging strategies specific to our Python/FastAPI backend and React/TypeScript frontend stack.

## Requirements

$ARGUMENTS

## Instructions

### 1. Development Environment Debugging

Set up comprehensive debugging environments for MythosMUD:

**VS Code Debug Configuration**

```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug MythosMUD Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/server/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/server",
                "ENVIRONMENT": "development",
                "DEBUG": "true",
                "LOG_LEVEL": "debug"
            },
            "args": [],
            "justMyCode": false,
            "python": "${workspaceFolder}/.venv/Scripts/python.exe"
        },
        {
            "name": "Debug MythosMUD Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/server",
                "ENVIRONMENT": "test",
                "DEBUG": "true"
            },
            "args": [
                "-v",
                "--tb=short",
                "--maxfail=1"
            ],
            "justMyCode": false,
            "python": "${workspaceFolder}/.venv/Scripts/python.exe"
        },
        {
            "name": "Debug MythosMUD Client",
            "type": "chrome",
            "request": "launch",
            "url": "http://localhost:5173",
            "webRoot": "${workspaceFolder}/client/src",
            "sourceMapPathOverrides": {
                "webpack:///src/*": "${webRoot}/*"
            },
            "userDataDir": "${workspaceFolder}/.vscode/chrome-debug-profile"
        },
        {
            "name": "Debug MythosMUD Client Tests",
            "type": "node",
            "request": "launch",
            "program": "${workspaceFolder}/client/node_modules/.bin/vitest",
            "args": ["--run", "--reporter=verbose"],
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/client",
            "env": {
                "NODE_ENV": "test"
            }
        }
    ],
    "compounds": [
        {
            "name": "Full Stack Debug",
            "configurations": ["Debug MythosMUD Server", "Debug MythosMUD Client"],
            "stopAll": true
        }
    ]
}
```

**Python Debug Configuration**

```python
# server/debug_config.py
import os
import logging
from typing import Dict, Any

class MythosMUDDebugConfig:
    """Debug configuration for MythosMUD server

    Implements debugging capabilities based on findings from
    "Debugging Non-Euclidean Systems" - Dr. Armitage, 1929
    """

    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug_enabled = os.getenv('DEBUG', 'false').lower() == 'true'
        self.log_level = os.getenv('LOG_LEVEL', 'info')

        # Debug features configuration
        self.features = {
            'remote_debugging': self.environment == 'development',
            'tracing': self.environment in ['development', 'staging'],
            'profiling': self.environment == 'development',
            'memory_monitoring': True,  # Always enabled for MythosMUD
            'database_debugging': self.environment == 'development'
        }

        # Debug endpoints and services
        self.endpoints = {
            'jaeger': os.getenv('JAEGER_ENDPOINT', 'http://localhost:14268'),
            'elasticsearch': os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200'),
            'sentry': os.getenv('SENTRY_DSN'),
            'debug_port': int(os.getenv('DEBUG_PORT', '5678'))
        }

        # Sampling rates for production
        self.sampling = {
            'traces': float(os.getenv('TRACE_SAMPLING_RATE', '0.1')),
            'profiles': float(os.getenv('PROFILE_SAMPLING_RATE', '0.01')),
            'logs': float(os.getenv('LOG_SAMPLING_RATE', '1.0'))
        }

    def is_enabled(self, feature: str) -> bool:
        """Check if a debug feature is enabled"""
        return self.features.get(feature, False)

    def should_sample(self, type_name: str) -> bool:
        """Determine if we should sample based on type and environment"""
        if self.environment == 'development':
            return True
        rate = self.sampling.get(type_name, 1.0)
        return os.urandom(8).hex() < rate

    def get_log_level(self) -> int:
        """Get numeric log level"""
        levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        return levels.get(self.log_level.lower(), logging.INFO)

# Global debug configuration instance
debug_config = MythosMUDDebugConfig()
```

### 2. MythosMUD-Specific Debug Tools

**Database Debug Helper**

```python
# server/debug/database_debugger.py
import sqlite3
import logging
from typing import Dict, List, Any
from pathlib import Path

class MythosMUDBDatabaseDebugger:
    """Database debugging utilities for MythosMUD

    Implements database inspection based on research from
    "Dimensional Database Patterns" - Prof. Wilmarth, 1930
    """

    def __init__(self, db_path: str):
        self.db_path = Path(db_path)
        self.logger = logging.getLogger(__name__)

        # Ensure database path follows our strict placement rules
        if not self._validate_db_location():
            raise ValueError(f"Database location {db_path} violates placement rules")

    def _validate_db_location(self) -> bool:
        """Validate database location follows MythosMUD rules"""
        allowed_paths = [
            Path("data/players"),
            Path("server/tests/data/players")
        ]

        for allowed_path in allowed_paths:
            if self.db_path.is_relative_to(allowed_path):
                return True

        self.logger.error(f"Database {self.db_path} in forbidden location")
        return False

    def inspect_database(self) -> Dict[str, Any]:
        """Comprehensive database inspection"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Get table information
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]

            db_info = {
                'path': str(self.db_path),
                'size_mb': self.db_path.stat().st_size / (1024 * 1024),
                'tables': {},
                'integrity_check': self._check_integrity(cursor),
                'performance_stats': self._get_performance_stats(cursor)
            }

            # Inspect each table
            for table in tables:
                db_info['tables'][table] = self._inspect_table(cursor, table)

            conn.close()
            return db_info

        except Exception as e:
            self.logger.error(f"Database inspection failed: {e}")
            return {'error': str(e)}

    def _inspect_table(self, cursor, table_name: str) -> Dict[str, Any]:
        """Inspect individual table structure and data"""
        try:
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()

            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]

            # Get sample data (first 5 rows)
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
            sample_data = cursor.fetchall()

            return {
                'columns': [{'name': col[1], 'type': col[2], 'not_null': col[3]} for col in columns],
                'row_count': row_count,
                'sample_data': sample_data
            }
        except Exception as e:
            return {'error': str(e)}

    def _check_integrity(self, cursor) -> Dict[str, Any]:
        """Check database integrity"""
        try:
            cursor.execute("PRAGMA integrity_check")
            integrity_result = cursor.fetchone()

            cursor.execute("PRAGMA foreign_key_check")
            foreign_key_result = cursor.fetchall()

            return {
                'integrity_check': integrity_result[0] if integrity_result else 'unknown',
                'foreign_key_violations': len(foreign_key_result),
                'foreign_key_details': foreign_key_result
            }
        except Exception as e:
            return {'error': str(e)}

    def _get_performance_stats(self, cursor) -> Dict[str, Any]:
        """Get database performance statistics"""
        try:
            cursor.execute("PRAGMA cache_size")
            cache_size = cursor.fetchone()[0]

            cursor.execute("PRAGMA page_size")
            page_size = cursor.fetchone()[0]

            cursor.execute("PRAGMA page_count")
            page_count = cursor.fetchone()[0]

            return {
                'cache_size': cache_size,
                'page_size': page_size,
                'page_count': page_count,
                'total_size_bytes': page_size * page_count
            }
        except Exception as e:
            return {'error': str(e)}

    def export_debug_report(self, output_path: str = None) -> str:
        """Export comprehensive debug report"""
        if not output_path:
            output_path = f"debug_report_{self.db_path.stem}_{int(time.time())}.json"

        report = {
            'timestamp': time.time(),
            'database_info': self.inspect_database(),
            'system_info': self._get_system_info()
        }

        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)

        return output_path
```

**Game State Debug Helper**

```python
# server/debug/game_debugger.py
import logging
from typing import Dict, List, Any
from server.game.player import Player
from server.game.world import World
from server.game.room import Room

class MythosMUDGameDebugger:
    """Game state debugging utilities for MythosMUD

    Implements game state inspection based on findings from
    "Non-Euclidean Game Mechanics" - Dr. Danforth, 1931
    """

    def __init__(self, world: World):
        self.world = world
        self.logger = logging.getLogger(__name__)

    def inspect_player_state(self, player_id: str) -> Dict[str, Any]:
        """Inspect complete player state"""
        try:
            player = self.world.get_player(player_id)
            if not player:
                return {'error': f'Player {player_id} not found'}

            return {
                'player_id': player_id,
                'location': self._get_location_info(player),
                'inventory': self._get_inventory_info(player),
                'stats': self._get_stats_info(player),
                'connections': self._get_connection_info(player),
                'recent_actions': self._get_recent_actions(player)
            }
        except Exception as e:
            self.logger.error(f"Player state inspection failed: {e}")
            return {'error': str(e)}

    def inspect_room_state(self, room_id: str) -> Dict[str, Any]:
        """Inspect complete room state"""
        try:
            room = self.world.get_room(room_id)
            if not room:
                return {'error': f'Room {room_id} not found'}

            return {
                'room_id': room_id,
                'description': room.description,
                'exits': self._get_exit_info(room),
                'contents': self._get_room_contents(room),
                'players': self._get_room_players(room),
                'connections': self._get_room_connections(room)
            }
        except Exception as e:
            self.logger.error(f"Room state inspection failed: {e}")
            return {'error': str(e)}

    def trace_player_journey(self, player_id: str, steps: int = 10) -> Dict[str, Any]:
        """Trace player's recent movement through the world"""
        try:
            player = self.world.get_player(player_id)
            if not player:
                return {'error': f'Player {player_id} not found'}

            journey = []
            current_room = player.current_room

            for i in range(steps):
                if not current_room:
                    break

                journey.append({
                    'step': i + 1,
                    'room_id': current_room.id,
                    'room_name': current_room.name,
                    'timestamp': time.time() - (steps - i) * 60  # Approximate
                })

                # Move to previous room if possible
                # This is a simplified trace - in reality you'd need movement history
                current_room = None

            return {
                'player_id': player_id,
                'journey': journey,
                'total_steps': len(journey)
            }
        except Exception as e:
            self.logger.error(f"Player journey trace failed: {e}")
            return {'error': str(e)}
```

### 3. MythosMUD Debug Commands

**Debug Command Implementation**

```python
# server/commands/debug_commands.py
from typing import List, Dict, Any
from server.commands.base_command import BaseCommand
from server.debug.game_debugger import MythosMUDGameDebugger
from server.debug.database_debugger import MythosMUDBDatabaseDebugger

class DebugCommand(BaseCommand):
    """Debug commands for MythosMUD

    Implements debugging capabilities based on research from
    "Debugging Non-Euclidean Systems" - Dr. Armitage, 1929
    """

    def __init__(self, world):
        super().__init__("debug", "Debug system and game state")
        self.world = world
        self.game_debugger = MythosMUDGameDebugger(world)
        self.db_debugger = None  # Initialize when needed

    def execute(self, player, args: List[str]) -> str:
        """Execute debug command with various subcommands"""
        if not args:
            return self._show_help()

        subcommand = args[0].lower()

        if subcommand == "player":
            return self._debug_player(player, args[1:])
        elif subcommand == "room":
            return self._debug_room(player, args[1:])
        elif subcommand == "database":
            return self._debug_database(player, args[1:])
        elif subcommand == "system":
            return self._debug_system(player, args[1:])
        elif subcommand == "trace":
            return self._debug_trace(player, args[1:])
        else:
            return f"Unknown debug subcommand: {subcommand}\n{self._show_help()}"

    def _debug_player(self, player, args: List[str]) -> str:
        """Debug player state"""
        if not args:
            target_id = player.id
        else:
            target_id = args[0]

        state = self.game_debugger.inspect_player_state(target_id)
        return self._format_debug_output("Player State", state)

    def _debug_room(self, player, args: List[str]) -> str:
        """Debug room state"""
        if not args:
            room_id = player.current_room.id if player.current_room else "unknown"
        else:
            room_id = args[0]

        state = self.game_debugger.inspect_room_state(room_id)
        return self._format_debug_output("Room State", state)

    def _debug_database(self, player, args: List[str]) -> str:
        """Debug database state"""
        if not self.db_debugger:
            # Initialize with player database
            db_path = f"data/players/{player.id}.db"
            self.db_debugger = MythosMUDBDatabaseDebugger(db_path)

        if not args:
            info = self.db_debugger.inspect_database()
        elif args[0] == "export":
            output_path = self.db_debugger.export_debug_report()
            return f"Database debug report exported to: {output_path}"
        else:
            return "Usage: debug database [export]"

        return self._format_debug_output("Database State", info)

    def _debug_system(self, player, args: List[str]) -> str:
        """Debug system state"""
        import psutil
        import os

        system_info = {
            'memory_usage': dict(psutil.virtual_memory()._asdict()),
            'cpu_usage': psutil.cpu_percent(interval=1),
            'disk_usage': dict(psutil.disk_usage('.')._asdict()),
            'process_info': {
                'pid': os.getpid(),
                'memory_mb': psutil.Process().memory_info().rss / (1024 * 1024)
            },
            'world_stats': {
                'total_players': len(self.world.players),
                'total_rooms': len(self.world.rooms),
                'active_connections': len(self.world.connections)
            }
        }

        return self._format_debug_output("System State", system_info)

    def _debug_trace(self, player, args: List[str]) -> str:
        """Trace player journey"""
        if not args:
            target_id = player.id
        else:
            target_id = args[0]

        steps = 10
        if len(args) > 1:
            try:
                steps = int(args[1])
            except ValueError:
                pass

        trace = self.game_debugger.trace_player_journey(target_id, steps)
        return self._format_debug_output("Player Journey Trace", trace)

    def _format_debug_output(self, title: str, data: Dict[str, Any]) -> str:
        """Format debug output for display"""
        output = [f"\n=== {title} ==="]

        if 'error' in data:
            output.append(f"ERROR: {data['error']}")
        else:
            self._format_dict(output, data, indent=0)

        return "\n".join(output)

    def _format_dict(self, output: List[str], data: Dict[str, Any], indent: int):
        """Recursively format dictionary data"""
        for key, value in data.items():
            prefix = "  " * indent
            if isinstance(value, dict):
                output.append(f"{prefix}{key}:")
                self._format_dict(output, value, indent + 1)
            elif isinstance(value, list):
                output.append(f"{prefix}{key}: [{len(value)} items]")
                if value and isinstance(value[0], dict):
                    for i, item in enumerate(value[:3]):  # Show first 3 items
                        output.append(f"{prefix}  [{i}]:")
                        self._format_dict(output, item, indent + 2)
                    if len(value) > 3:
                        output.append(f"{prefix}  ... and {len(value) - 3} more")
            else:
                output.append(f"{prefix}{key}: {value}")

    def _show_help(self) -> str:
        """Show debug command help"""
        return """
Debug Command Usage:
  debug player [player_id]     - Debug player state
  debug room [room_id]         - Debug room state
  debug database [export]      - Debug database state
  debug system                 - Debug system state
  debug trace [player_id] [steps] - Trace player journey
        """.strip()
```

### 4. MythosMUD Debug Scripts

**Development Debug Scripts**

```powershell
# scripts/debug_server.ps1
param(
    [string]$LogLevel = "debug",
    [switch]$Profile,
    [switch]$Trace,
    [switch]$Memory
)

Write-Host "Starting MythosMUD server in debug mode..." -ForegroundColor Green

# Set debug environment variables
$env:DEBUG = "true"
$env:LOG_LEVEL = $LogLevel
$env:ENVIRONMENT = "development"

# Additional debug options
if ($Profile) {
    $env:ENABLE_PROFILING = "true"
    Write-Host "CPU profiling enabled" -ForegroundColor Yellow
}

if ($Trace) {
    $env:ENABLE_TRACING = "true"
    Write-Host "Distributed tracing enabled" -ForegroundColor Yellow
}

if ($Memory) {
    $env:ENABLE_MEMORY_MONITORING = "true"
    Write-Host "Memory monitoring enabled" -ForegroundColor Yellow
}

# Start server with debug flags
$pythonArgs = @(
    "-u",  # Unbuffered output
    "-X", "dev",  # Development mode
    "server/main.py"
)

if ($Profile) {
    $pythonArgs = @("--cpu-prof", "--cpu-prof-dir=./profiles") + $pythonArgs
}

Write-Host "Starting server with: python $($pythonArgs -join ' ')" -ForegroundColor Cyan
& python $pythonArgs
```

**Test Debug Scripts**

```powershell
# scripts/debug_tests.ps1
param(
    [string]$TestPath = "",
    [string]$LogLevel = "debug",
    [switch]$Coverage,
    [switch]$Verbose
)

Write-Host "Running MythosMUD tests in debug mode..." -ForegroundColor Green

# Set debug environment variables
$env:DEBUG = "true"
$env:LOG_LEVEL = $LogLevel
$env:ENVIRONMENT = "test"

# Build test arguments
$testArgs = @()

if ($TestPath) {
    $testArgs += $TestPath
}

if ($Coverage) {
    $testArgs += "--cov=server", "--cov-report=html", "--cov-report=term"
}

if ($Verbose) {
    $testArgs += "-v", "-s"
}

# Always use our project root for tests
Set-Location $PSScriptRoot/..
Write-Host "Running tests from: $(Get-Location)" -ForegroundColor Cyan

# Use make test as per our development rules
if ($testArgs.Count -gt 0) {
    Write-Host "Running: make test -- $($testArgs -join ' ')" -ForegroundColor Yellow
    & make test -- $testArgs
} else {
    Write-Host "Running: make test" -ForegroundColor Yellow
    & make test
}
```

### 5. MythosMUD Debug Configuration Files

**Logging Configuration**

```python
# server/logging_config.py
import logging
import logging.handlers
import os
from pathlib import Path
from server.debug.debug_config import debug_config

def setup_mythosmud_logging():
    """Setup comprehensive logging for MythosMUD

    Implements logging based on research from
    "Logging in Non-Euclidean Systems" - Dr. Armitage, 1930
    """

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs/development")
    logs_dir.mkdir(parents=True, exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(debug_config.get_log_level())

    # Clear existing handlers
    root_logger.handlers.clear()

    # Console handler with colors
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)

    # File handler for all logs
    file_handler = logging.handlers.RotatingFileHandler(
        logs_dir / "mythosmud.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)

    # Error file handler
    error_handler = logging.handlers.RotatingFileHandler(
        logs_dir / "errors.log",
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setFormatter(file_formatter)
    error_handler.setLevel(logging.ERROR)
    root_logger.addHandler(error_handler)

    # Debug file handler (only in development)
    if debug_config.environment == 'development':
        debug_handler = logging.handlers.RotatingFileHandler(
            logs_dir / "debug.log",
            maxBytes=20*1024*1024,  # 20MB
            backupCount=3
        )
        debug_handler.setFormatter(file_formatter)
        debug_handler.setLevel(logging.DEBUG)
        root_logger.addHandler(debug_handler)

    # Set specific logger levels
    logging.getLogger('uvicorn').setLevel(logging.WARNING)
    logging.getLogger('fastapi').setLevel(logging.WARNING)
    logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

    # MythosMUD loggers
    logging.getLogger('mythosmud').setLevel(logging.DEBUG)
    logging.getLogger('mythosmud.game').setLevel(logging.DEBUG)
    logging.getLogger('mythosmud.network').setLevel(logging.DEBUG)

    logging.info("MythosMUD logging configured successfully")
```

### 6. MythosMUD Debug Middleware

**Debug Middleware for FastAPI**

```python
# server/middleware/debug_middleware.py
import time
import logging
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from server.debug.debug_config import debug_config

class MythosMUDDebugMiddleware(BaseHTTPMiddleware):
    """Debug middleware for MythosMUD FastAPI application

    Implements request/response debugging based on research from
    "HTTP Debugging in Non-Euclidean Systems" - Dr. Danforth, 1932
    """

    def __init__(self, app, debug_config):
        super().__init__(app)
        self.debug_config = debug_config
        self.logger = logging.getLogger(__name__)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()

        # Generate request ID
        request_id = f"req_{int(start_time * 1000)}"
        request.state.request_id = request_id

        # Log request start
        if self.debug_config.is_enabled('tracing'):
            self.logger.debug(f"Request started: {request_id}", extra={
                'request_id': request_id,
                'method': request.method,
                'url': str(request.url),
                'headers': dict(request.headers),
                'client_ip': request.client.host if request.client else 'unknown'
            })

        # Process request
        try:
            response = await call_next(request)

            # Calculate duration
            duration = time.time() - start_time

            # Log response
            if self.debug_config.is_enabled('tracing'):
                self.logger.debug(f"Request completed: {request_id}", extra={
                    'request_id': request_id,
                    'duration_ms': duration * 1000,
                    'status_code': response.status_code,
                    'response_headers': dict(response.headers)
                })

            # Add debug headers
            response.headers['X-Request-ID'] = request_id
            response.headers['X-Response-Time'] = str(duration)

            return response

        except Exception as e:
            duration = time.time() - start_time

            # Log error
            self.logger.error(f"Request failed: {request_id}", extra={
                'request_id': request_id,
                'duration_ms': duration * 1000,
                'error': str(e),
                'error_type': type(e).__name__
            }, exc_info=True)

            raise
```

### 7. MythosMUD Debug Utilities

**Memory Leak Detection**

```python
# server/debug/memory_debugger.py
import gc
import psutil
import logging
import time
from typing import Dict, List, Any
from collections import defaultdict

class MythosMUDMemoryDebugger:
    """Memory leak detection for MythosMUD

    Implements memory monitoring based on research from
    "Memory Patterns in Non-Euclidean Systems" - Dr. Armitage, 1931
    """

    def __init__(self, check_interval: int = 60):
        self.check_interval = check_interval
        self.logger = logging.getLogger(__name__)
        self.memory_history = []
        self.object_counts = defaultdict(int)
        self.last_check = time.time()

        # Start monitoring
        self.start_monitoring()

    def start_monitoring(self):
        """Start memory monitoring"""
        self.logger.info("Memory monitoring started")

        # Schedule periodic checks
        import threading
        def monitor_loop():
            while True:
                time.sleep(self.check_interval)
                self.check_memory()

        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()

    def check_memory(self):
        """Perform memory check and analysis"""
        current_time = time.time()

        # Get current memory usage
        process = psutil.Process()
        memory_info = process.memory_info()

        memory_snapshot = {
            'timestamp': current_time,
            'rss_mb': memory_info.rss / (1024 * 1024),
            'vms_mb': memory_info.vms / (1024 * 1024),
            'heap_mb': memory_info.rss / (1024 * 1024),  # Approximate
            'object_count': len(gc.get_objects())
        }

        self.memory_history.append(memory_snapshot)

        # Keep only last 100 snapshots
        if len(self.memory_history) > 100:
            self.memory_history.pop(0)

        # Analyze for memory leaks
        self._analyze_memory_trends()

        # Update last check time
        self.last_check = current_time

    def _analyze_memory_trends(self):
        """Analyze memory usage trends for potential leaks"""
        if len(self.memory_history) < 5:
            return

        # Calculate trend over last 5 snapshots
        recent = self.memory_history[-5:]
        first = recent[0]
        last = recent[-1]

        # Calculate growth rate
        time_diff = last['timestamp'] - first['timestamp']
        memory_growth = last['rss_mb'] - first['rss_mb']
        growth_rate = memory_growth / time_diff if time_diff > 0 else 0

        # Alert if growth rate is concerning
        if growth_rate > 1.0:  # More than 1MB per minute
            self.logger.warning(f"Potential memory leak detected: {growth_rate:.2f}MB/min growth")

            # Take heap snapshot for analysis
            self._take_heap_snapshot()

    def _take_heap_snapshot(self):
        """Take heap snapshot for memory analysis"""
        try:
            # Force garbage collection
            gc.collect()

            # Get object counts by type
            objects = gc.get_objects()
            type_counts = defaultdict(int)

            for obj in objects:
                obj_type = type(obj).__name__
                type_counts[obj_type] += 1

            # Log top object types
            top_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)[:10]

            self.logger.info("Top object types in memory:", extra={
                'object_counts': dict(top_types)
            })

        except Exception as e:
            self.logger.error(f"Failed to take heap snapshot: {e}")

    def get_memory_report(self) -> Dict[str, Any]:
        """Get comprehensive memory report"""
        if not self.memory_history:
            return {'error': 'No memory data available'}

        current = self.memory_history[-1]
        first = self.memory_history[0]

        return {
            'current_usage': current,
            'total_growth': {
                'rss_mb': current['rss_mb'] - first['rss_mb'],
                'vms_mb': current['vms_mb'] - first['vms_mb'],
                'object_count': current['object_count'] - first['object_count']
            },
            'growth_rate': {
                'rss_mb_per_min': (current['rss_mb'] - first['rss_mb']) /
                                ((current['timestamp'] - first['timestamp']) / 60),
                'objects_per_min': (current['object_count'] - first['object_count']) /
                                  ((current['timestamp'] - first['timestamp']) / 60)
            },
            'history': self.memory_history[-20:],  # Last 20 snapshots
            'last_check': self.last_check
        }
```

### 8. MythosMUD Debug Commands Integration

**Register Debug Commands**

```python
# server/command_handler_unified.py
# Add to existing command registration

def register_debug_commands(self):
    """Register debug commands for MythosMUD"""
    from server.commands.debug_commands import DebugCommand

    # Only register debug commands in development or for admins
    if self.world.config.environment == 'development' or self.is_admin(player):
        debug_cmd = DebugCommand(self.world)
        self.register_command(debug_cmd)

        # Register debug subcommands
        self.register_subcommand("debug", "player", debug_cmd._debug_player)
        self.register_subcommand("debug", "room", debug_cmd._debug_room)
        self.register_subcommand("debug", "database", debug_cmd._debug_database)
        self.register_subcommand("debug", "system", debug_cmd._debug_system)
        self.register_subcommand("debug", "trace", debug_cmd._debug_trace)
```

### 9. MythosMUD Debug Configuration in Main

**Main Application Debug Setup**

```python
# server/main.py
# Add to existing main.py

def setup_debug_environment():
    """Setup debug environment for MythosMUD"""
    from server.debug.debug_config import debug_config
    from server.logging_config import setup_mythosmud_logging
    from server.middleware.debug_middleware import MythosMUDDebugMiddleware

    # Setup logging
    setup_mythosmud_logging()

    # Setup debug middleware if enabled
    if debug_config.is_enabled('tracing'):
        app.add_middleware(MythosMUDDebugMiddleware, debug_config=debug_config)

    # Setup memory monitoring
    if debug_config.is_enabled('memory_monitoring'):
        from server.debug.memory_debugger import MythosMUDMemoryDebugger
        memory_debugger = MythosMUDMemoryDebugger()
        app.state.memory_debugger = memory_debugger

    # Setup debug endpoints
    if debug_config.environment == 'development':
        setup_debug_endpoints(app)

def setup_debug_endpoints(app):
    """Setup debug API endpoints"""

    @app.get("/debug/health")
    async def debug_health():
        """Debug health check endpoint"""
        return {
            "status": "healthy",
            "environment": debug_config.environment,
            "timestamp": time.time(),
            "debug_features": debug_config.features
        }

    @app.get("/debug/memory")
    async def debug_memory():
        """Memory usage debug endpoint"""
        if hasattr(app.state, 'memory_debugger'):
            return app.state.memory_debugger.get_memory_report()
        return {"error": "Memory debugger not available"}

    @app.get("/debug/players")
    async def debug_players():
        """Player state debug endpoint"""
        # This would need proper authentication in production
        return {
            "total_players": len(app.state.world.players),
            "active_players": len([p for p in app.state.world.players.values() if p.is_online])
        }

# Add to main function
if __name__ == "__main__":
    setup_debug_environment()
    # ... rest of main function
```

## Output Format

1. **Debug Configuration**: Complete setup for MythosMUD debugging tools
2. **Integration Guide**: Step-by-step integration with existing MythosMUD codebase
3. **Debug Commands**: In-game debugging capabilities for developers
4. **Debug Scripts**: PowerShell scripts for development environment debugging
5. **Memory Monitoring**: Comprehensive memory leak detection
6. **Logging Setup**: Structured logging with MythosMUD-specific formatting
7. **Debug Middleware**: FastAPI middleware for request/response debugging
8. **Documentation**: Team debugging guidelines aligned with .cursorrules

Focus on creating a comprehensive debugging environment that enhances developer productivity and enables rapid issue resolution in the MythosMUD project, following all security and development rules established in the project.
