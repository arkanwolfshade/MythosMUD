# Security: Environment Variables

This document describes the environment variables used for secure configuration in MythosMUD.

## Database Configuration

### Required for Production

- `DATABASE_HOST`: Database hostname (default: `localhost`)
- `DATABASE_PORT`: Database port (default: `5432`)
- `DATABASE_USER`: Database username (default: `postgres`)
- `DATABASE_PASSWORD`: **REQUIRED** - Database password (no default in production)

### Development Defaults

For local development, the following defaults are used if environment variables are not set:

- `DATABASE_HOST`: `localhost`
- `DATABASE_PORT`: `5432`
- `DATABASE_USER`: `postgres`
- `DATABASE_PASSWORD`: `Cthulhu1` (development only)

**WARNING**: The default password `Cthulhu1` is for local development only. Never use this password in production or staging environments.

### Usage in Scripts

Migration and database scripts (`verify_migration.py`, `apply_players_migration.py`) will:

1. Check for environment variables first
2. Fall back to development defaults if not set
3. Warn if default password is used in production/staging environments

### Setting Environment Variables

#### Local Development (.env file)

Create a `.env` file in the project root:

```bash
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASSWORD=your_secure_password_here
ENVIRONMENT=development
```

#### Production/Staging

Set environment variables in your deployment environment:

```bash
export DATABASE_HOST=your-db-host
export DATABASE_PORT=5432
export DATABASE_USER=your-db-user
export DATABASE_PASSWORD=your-secure-password
export ENVIRONMENT=production
```

### Security Best Practices

1. **Never commit passwords to version control**
   - Use `.env` files (already in `.gitignore`)
   - Use secret management systems in production (AWS Secrets Manager, HashiCorp Vault, etc.)

2. **Use strong passwords in production**
   - Minimum 16 characters
   - Mix of uppercase, lowercase, numbers, and special characters
   - Unique password for each environment

3. **Rotate passwords regularly**
   - Change database passwords every 90 days
   - Update environment variables immediately after rotation

4. **Limit access to environment variables**
   - Only grant access to authorized personnel
   - Use least-privilege principles
   - Audit access logs regularly

5. **Validate environment variables**
   - Scripts will warn if default passwords are used in production
   - Set `ENVIRONMENT=production` or `ENVIRONMENT=staging` to enable warnings
