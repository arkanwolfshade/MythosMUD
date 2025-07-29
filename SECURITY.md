# Security Documentation for MythosMUD

## Critical Security Issues and Fixes

### 1. Hardcoded Secret Key (FIXED)

**Issue**: JWT secret key was hardcoded in source code
**Fix**: Now uses environment variable `MYTHOSMUD_SECRET_KEY`
**Action Required**: Set environment variable in production:

```bash
export MYTHOSMUD_SECRET_KEY="your-secure-random-key-here"
```

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

- [ ] Set secure `MYTHOSMUD_SECRET_KEY` environment variable
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
