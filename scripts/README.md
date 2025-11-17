# MythosMUD Scripts

This directory contains utility scripts for managing the MythosMUD development environment.

## PowerShell Scripts

### `start_server.ps1`

Starts the MythosMUD FastAPI server with optional process cleanup.

**Usage:**

```powershell
.\start_server.ps1 [-ServerHost <string>] [-Port <int>] [-Reload]
```

**Parameters:**

- `-ServerHost`: Host address to bind server to (default: "127.0.0.1")
- `-Port`: Port number to bind server to (default: 54731)
- `-Reload`: Enable auto-reload for development (default: true)

**Examples:**

```powershell
# Start with default settings
.\start_server.ps1

# Start on all interfaces, port 8080, without auto-reload
.\start_server.ps1 -ServerHost "0.0.0.0" -Port 8080 -Reload:$false
```

### `stop_server.ps1`

Stops MythosMUD server processes using multiple detection methods.

**Usage:**

```powershell
.\stop_server.ps1 [-Force] [-Verbose]
```

**Parameters:**

- `-Force`: Force termination of all Python processes regardless of command line
- `-Verbose`: Provide detailed output (automatically available due to CmdletBinding)

**Examples:**

```powershell
# Stop server processes gracefully
.\stop_server.ps1

# Force stop all Python processes with detailed output
.\stop_server.ps1 -Force -Verbose
```

### `start_local.ps1`

Starts the complete MythosMUD development environment (both FastAPI server and React client).

**Usage:**

```powershell
.\start_local.ps1
```

**Features:**

- Starts the FastAPI server using `start_server.ps1`
- Starts the React development server
- Provides URLs for all development services

## Python Scripts

### `run.py`

Runs the MythosMUD server using uvicorn.

### `test.py`

Runs the test suite using pytest.

### `lint.py`

Runs code linting using ruff.

### `format.py`

Formats code using ruff.

### `install.py`

Installs project dependencies.

### Database Initialization (PostgreSQL)

Database initialization is now handled via PostgreSQL SQL scripts in `db/schema/`.
See `db/README.md` for database setup instructions.

**Note:** SQLite database initialization scripts have been removed as the project
now uses PostgreSQL exclusively.


### `build.py`

Builds the project for production.

### `coverage.py`

Runs test coverage analysis.

### `clean.py`

Cleans build artifacts and temporary files.

## Requirements

- PowerShell 5.1 or higher (for PowerShell scripts)
- Python 3.12+ (for Python scripts)
- Node.js 18+ (for client development)

## Notes

- All PowerShell scripts include comprehensive help documentation
- Use `Get-Help .\script_name.ps1 -Full` for detailed help
- Scripts automatically handle process cleanup and port management
- Error handling and logging are built into all scripts
