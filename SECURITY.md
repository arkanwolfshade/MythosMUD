# Security Documentation for MythosMUD

## Critical Security Issues and Fixes

### 1. Hardcoded Secret Keys (FIXED)

**Issue**: Multiple secret keys were hardcoded in source code
**Fix**: Now uses environment variables for all secrets
**Action Required**: Set environment variables in production:

```bash
export MYTHOSMUD_SECRET_KEY="your-super-secret-key-here"
export MYTHOSMUD_JWT_SECRET="your-jwt-secret-key-here"
export MYTHOSMUD_RESET_TOKEN_SECRET="your-reset-token-secret-here"
export MYTHOSMUD_VERIFICATION_TOKEN_SECRET="your-verification-token-secret-here"
```

**Files Updated**:
- `server/auth_utils.py` - Uses `MYTHOSMUD_SECRET_KEY` for JWT operations
- `server/auth/users.py` - Uses environment variables for FastAPI Users secrets

### 2. Path Injection Vulnerabilities (FIXED)

**Issue**: CodeQL flagged potential path injection in file operations
**Fix**: Implemented secure path validation in `server/security_utils.py`
**Implementation**:

- `validate_secure_path()` - Validates user-provided paths
- `get_secure_file_path()` - Creates secure file paths
- `is_safe_filename()` - Validates filenames

### 3. Client-Side XSS Vulnerability (FIXED)

**Issue**: Multiple cross-site scripting vulnerabilities in test client HTML file
**Location**: `client/public/test_client.html` - multiple functions
**CWE**: CWE-79 (Cross-site Scripting)
**Vulnerabilities**:
- Direct user input insertion into DOM via `innerHTML` in multiple functions
- DOM text reinterpreted as HTML without proper escaping
- User-controlled data from API responses inserted without sanitization
**Fix**: Implemented comprehensive secure DOM manipulation using `textContent`
**Implementation**:
- Replaced all `innerHTML` usage with `textContent` for safe content insertion
- Removed HTML escaping function (no longer needed)
- Use `document.createElement()` and `appendChild()` for safe DOM manipulation
- Set CSS classes via `className` property instead of inline HTML
- Fixed vulnerabilities in: `testServerConnection`, `testRegistration`, `testAuthentication`, `testSSEConnection`, `testWebSocketConnection`, `testCommand`, and `log` functions
- Prevents both direct XSS and DOM text reinterpretation attacks

### 4. File-based User Storage (PLANNED MIGRATION)

**Issue**: Still using JSON files for user storage
**Plan**: Migrate to database storage via PersistenceLayer
**Status**: In progress - TODO items exist in auth.py

## Security Best Practices

### Environment Variables

- **Never hardcode secrets** in source code
- Use environment variables for all sensitive configuration
- Provide secure defaults for development
- **Required Environment Variables**:
  - `MYTHOSMUD_SECRET_KEY` - Main application secret
  - `MYTHOSMUD_JWT_SECRET` - JWT token signing secret
  - `MYTHOSMUD_RESET_TOKEN_SECRET` - Password reset token secret
  - `MYTHOSMUD_VERIFICATION_TOKEN_SECRET` - Email verification token secret

### Path Validation

- Always validate user-provided paths
- Use `os.path.normpath()` and check against base directory
- Reject paths containing `..`, `~`, or directory separators

### Input Validation

- Validate all user inputs before processing
- Use Pydantic models for request validation
- Implement proper error handling

### Authentication

- Use bcrypt for password hashing
- Implement proper JWT token validation
- Set appropriate token expiration times

## Security Checklist

### Before Production Deployment

- [x] Set secure environment variables for all secrets
- [ ] Migrate user storage from JSON files to database
- [ ] Implement rate limiting for auth endpoints
- [ ] Add HTTPS/SSL configuration
- [ ] Review and update all file permissions
- [ ] Implement proper logging for security events
- [ ] Add input sanitization for all user inputs
- [ ] Test for SQL injection vulnerabilities
- [ ] Implement proper session management

### Ongoing Security

- [ ] Regular security audits
- [ ] Keep dependencies updated
- [ ] Monitor for new vulnerabilities
- [ ] Implement security headers
- [ ] Regular backup and recovery testing

## Vulnerability Reporting

If you discover a security vulnerability, please:

1. **DO NOT** create a public issue
2. Contact the maintainers privately
3. Provide detailed reproduction steps
4. Allow time for assessment and fix

## Security Tools

- **CodeQL**: Static analysis for security vulnerabilities
- **Bandit**: Python security linter
- **Safety**: Dependency vulnerability checker
- **Pre-commit hooks**: Automated security checks

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [Python Security Best Practices](https://python-security.readthedocs.io/)
