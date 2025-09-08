# Tech Stack

## Context

Global tech stack defaults for Agent OS projects, overridable in project-specific `.agent-os/product/tech-stack.md`.

- App Framework: TypeScript and React; and Python
- Language: Python 3.12, TypeScript 5.9.2, React 19.1.1
- Primary Database: SQLite (development), PostgreSQL 17+ (production)
- ORM: SQLAlchemy 2.0+
- Backend Framework: FastAPI 0.116.1
- JavaScript Framework: React 19.1.1
- Build Tool: Vite 7.1.3
- Import Strategy: Node.js modules
- Package Manager: npm (client), uv (server)
- Node Version: 22 LTS
- CSS Framework: TailwindCSS 4.1.12
- UI Components: Custom Mythos-themed components
- UI Installation: Direct component imports
- Font Provider: System fonts (Courier New for terminal theme)
- Font Loading: Self-hosted for performance
- Icons: Lucide React 0.540.0
- Application Hosting: Digital Ocean App Platform/Droplets
- Hosting Region: Primary region based on user base
- Database Hosting: Digital Ocean Managed PostgreSQL
- Database Backups: Daily automated
- Asset Storage: Amazon S3
- CDN: CloudFront
- Asset Access: Private with signed URLs
- CI/CD Platform: GitHub Actions
- CI/CD Trigger: Push to main/staging branches
- Tests: Run before deployment
- Production Environment: main branch
- Staging Environment: staging branch
