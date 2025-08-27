# Technical Stack

## Application Framework
- **Backend Framework:** Python FastAPI 0.104.1
- **Frontend Framework:** React 18.2.0 with TypeScript 5.0.0
- **Build Tool:** Vite 4.4.0

## Database System
- **Primary Database:** SQLite 3.42.0 (MVP)
- **Production Database:** PostgreSQL 15.0 (planned migration)
- **ORM:** SQLAlchemy 2.0.0

## JavaScript Framework
- **Frontend Framework:** React 18.2.0
- **Type Safety:** TypeScript 5.0.0
- **State Management:** React Hooks (useState, useEffect, useContext)

## Import Strategy
- **Module System:** Node.js ES modules
- **Package Manager:** npm 9.5.0
- **Dependency Management:** uv for Python, npm for Node.js

## CSS Framework
- **Styling Framework:** TailwindCSS 3.3.0
- **Component Library:** Custom components with MythosMUD theme
- **Terminal Styling:** xterm.js 5.2.0 for terminal interface

## UI Component Library
- **Primary:** Custom React components
- **Terminal Interface:** xterm.js 5.2.0
- **Form Components:** Custom form validation with Pydantic

## Fonts Provider
- **Font System:** Google Fonts
- **Primary Font:** Monospace for terminal interface
- **Secondary Font:** System fonts for UI elements

## Icon Library
- **Icon System:** Custom SVG icons
- **Icon Provider:** Local SVG assets
- **Icon Framework:** React SVG components

## Application Hosting
- **Development:** Local development server (localhost:54731)
- **Production Target:** AWS EC2 or Fargate
- **Container Platform:** Docker

## Database Hosting
- **Development:** Local SQLite file
- **Production Target:** AWS RDS PostgreSQL
- **Backup Strategy:** Automated database backup with timestamp rotation

## Asset Hosting
- **Static Assets:** Vite build system
- **Media Files:** Local storage with CDN planned
- **Room Data:** JSON files in data/rooms/ directory

## Deployment Solution
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Environment Management:** Environment variables with .env files
- **Process Management:** uvicorn for Python, npm scripts for Node.js

## Code Repository URL
- **Repository:** https://github.com/arkanwolfshade/MythosMUD
- **Version Control:** Git with GitHub
- **Branch Strategy:** Feature branches with main integration

## Additional Technical Components

### Real-time Communication
- **Message Broker:** NATS 2.9.0
- **WebSocket Support:** FastAPI WebSocket endpoints
- **Server-Sent Events:** SSE for real-time updates

### Security & Authentication
- **Password Hashing:** Argon2 (TIME_COST=3, MEMORY_COST=65536)
- **Token System:** JWT with configurable expiration
- **Rate Limiting:** Per-user and per-endpoint sliding window
- **Input Validation:** Pydantic models with comprehensive validation

### Testing & Quality
- **Testing Framework:** pytest 8.4.1
- **Code Coverage:** 88% (target: 80% minimum)
- **Linting:** ruff (replaces black/flake8)
- **Pre-commit Hooks:** Automated code quality checks

### Development Tools
- **Python Environment:** uv for dependency management
- **Node.js Management:** NVM for Windows
- **IDE Support:** VS Code with Cursor integration
- **Documentation:** Comprehensive markdown documentation
