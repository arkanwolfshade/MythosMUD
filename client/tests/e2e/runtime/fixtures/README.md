# E2E Test Fixtures

## Database Seeding

The E2E test database fixtures (`database.ts`) use native Node.js modules for seeding test databases:

- **argon2**: Password hashing (matching production configuration)
- **better-sqlite3**: Direct SQLite database access

### Optional Dependencies

These packages are configured as `optionalDependencies` in `client/package.json` because:

1. **CI Compatibility**: CI environments (GitHub Actions) may lack the build tools needed to compile these native modules
2. **Not Required for Build**: The main client build and linting don't need these packages
3. **Only for E2E Tests**: These fixtures are only used when running E2E tests locally

### Local Development

To run E2E tests locally that require database seeding:

1. **Ensure you have build tools installed**:
   - **Windows**: `npm install --global windows-build-tools` (requires admin)
   - **Linux**: `sudo apt-get install build-essential python3`
   - **macOS**: Install Xcode Command Line Tools

2. **Install optional dependencies**:

   ```bash
   cd client
   npm install
   ```

3. **Verify installation**:
   ```bash
   node -e "require('argon2'); require('better-sqlite3'); console.log('OK')"
   ```

### Alternative: Use Python Backend for Seeding

If native module compilation fails, consider using the Python backend's test database initialization scripts instead:

```bash
# From project root
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python server/tests/init_test_db.py
```

## Troubleshooting

### "Cannot find module 'argon2'" or "'better-sqlite3'"

If you see these errors when running E2E tests:

1. Check if the modules installed successfully: `npm list argon2 better-sqlite3`
2. If not installed, try manual installation: `npm install argon2 better-sqlite3`
3. If compilation fails, ensure you have build tools installed (see above)
4. As a fallback, use the Python backend for test database seeding

### CI Failures

The CI workflow should **not** fail due to these optional dependencies. If you see CI failures related to argon2 or better-sqlite3:

1. Verify they're in `optionalDependencies` (not `devDependencies`)
2. Check that the CI job doesn't explicitly require these packages
3. Ensure the CI workflow doesn't run E2E tests that need database seeding
