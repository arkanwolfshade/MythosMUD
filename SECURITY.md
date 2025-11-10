# Security Policy

## Reporting a Vulnerability

The security of MythosMUD is of paramount importance. We take all security vulnerabilities seriously and appreciate your efforts to responsibly disclose your findings.

### How to Report

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by emailing the maintainers directly:

- **Primary Contact**: @arkanwolfshade
- **Secondary Contact**: @TylerWolfshade

Please include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability, including how an attacker might exploit it

### What to Expect

When you report a security vulnerability, you can expect:

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
2. **Investigation**: We will investigate the issue and determine its severity
3. **Communication**: We will keep you informed of our progress toward a fix
4. **Credit**: We will credit you for the discovery (unless you prefer to remain anonymous)
5. **Disclosure**: We will coordinate disclosure timing with you

### Timeline

- **Initial Response**: Within 48 hours of report
- **Status Update**: Within 7 days with validation and severity assessment
- **Fix Deployment**: Based on severity (critical issues within 7-14 days)
- **Public Disclosure**: After patch is deployed and tested

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| dev     | :white_check_mark: |
| < 1.0   | :x:                |

**Note**: MythosMUD is currently in beta development. We are actively addressing security issues across all development branches.

## Security Measures

### Implemented Security Features

MythosMUD implements comprehensive security measures to protect users and data:

#### Authentication & Authorization

- Always verify user permissions before allowing access to resources
- Never trust client-side validation alone
- Implement rate limiting for authentication endpoints
- Use secure session management practices
- **Argon2 Password Hashing**: Industry-leading password protection with configurable parameters
- **JWT Token Authentication**: Secure, stateless authentication with proper expiration
- **Invite-Only System**: Controlled access with database-backed invite management
- **Role-Based Access Control**: Admin and user role separation with proper authorization checks

#### Data Protection

- **Environment Variable Configuration**: All secrets managed via environment variables
- **Encrypted Storage**: Sensitive data encrypted at rest
- **Secure Transmission**: HTTPS/WSS for all production communications
- **Input Sanitization**: Comprehensive server-side validation and sanitization
- **SQL Injection Protection**: Parameterized queries throughout

#### Application Security

- **XSS Protection**: Complete client-side XSS vulnerability elimination
- **Path Traversal Prevention**: Secure path validation for all file operations
- **Rate Limiting**: Per-user and per-endpoint abuse prevention
- **Security Headers**: Comprehensive HTTP security headers including CSP, HSTS, X-Frame-Options
- **CORS Configuration**: Properly configured cross-origin resource sharing

#### Privacy & Compliance

- **COPPA Compliance**: Privacy-first design for minor users
- **Minimal Data Collection**: Only essential data collected
- **Data Deletion Rights**: Easy data deletion for all users
- **No Behavioral Tracking**: No user profiling or behavioral analytics

#### Monitoring & Logging

- **Structured Logging**: Enhanced logging with MDC and correlation IDs
- **Security Event Tracking**: Comprehensive audit logging for security events
- **Automatic Sanitization**: Sensitive data automatically redacted from logs
- **Performance Monitoring**: Built-in metrics and monitoring capabilities

### Automated Security Scanning

We employ multiple automated security tools:

- **CodeQL**: Static application security testing
- **Semgrep**: Pattern-based vulnerability detection
- **Dependency Review**: Automated dependency vulnerability scanning
- **Pre-commit Hooks**: Security checks before code is committed
- **GitHub Security Advisories**: Automated vulnerability alerts

## Security Best Practices for Contributors

When contributing to MythosMUD, please follow these security guidelines:

### Code Security

- Never commit secrets, API keys, or passwords to the repository
- Use environment variables for all sensitive configuration
- Always validate and sanitize user input on the server side
- Use parameterized queries for all database operations
- Implement proper error handling without exposing sensitive information

### Data Handling

- Encrypt sensitive data at rest and in transit
- Use Argon2 for password hashing (already implemented)
- Implement proper access controls for user data
- Follow the principle of least privilege

### Testing

- Write security tests for new features
- Test edge cases and potential attack vectors
- Use the existing test framework (80%+ coverage required)
- Test with both valid and malicious input

## Security Architecture

For detailed information about our security architecture and implementation:

- **Security Implementation**: See [docs/archive/SECURITY.md](docs/archive/SECURITY.md)
- **Security Fixes**: See [docs/SECURITY_FIXES.md](docs/SECURITY_FIXES.md)
- **SSE Authentication**: See [docs/SSE_AUTHENTICATION.md](docs/SSE_AUTHENTICATION.md)
- **Command Security**: See [docs/COMMAND_SECURITY_GUIDE.md](docs/COMMAND_SECURITY_GUIDE.md)
- **Development Guide**: See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)

## Known Security Considerations

### Current Environment

- **MVP Status**: MythosMUD is currently in beta development
- **SQLite Database**: Using SQLite for MVP; PostgreSQL planned for production
- **Invite-Only**: Currently limited to invited users only
- **No Public Deployment**: Not yet deployed to production environment

### Planned Enhancements

- Migration to PostgreSQL for production deployment
- Enhanced audit logging and monitoring
- Additional rate limiting refinements
- Comprehensive penetration testing before public release

## Vulnerability Disclosure Policy

We follow responsible disclosure practices:

1. **Private Reporting**: All vulnerabilities should be reported privately
2. **Coordinated Disclosure**: We will work with you to coordinate public disclosure
3. **Recognition**: Security researchers will be acknowledged (with permission)
4. **No Legal Action**: We will not pursue legal action against researchers who follow responsible disclosure

### Out of Scope

The following are explicitly out of scope:

- Vulnerabilities in dependencies (please report directly to the dependency maintainers)
- Social engineering attacks against maintainers or users
- Physical attacks against infrastructure
- Denial of service attacks (unless demonstrating a specific vulnerability)
- Issues in third-party libraries or frameworks (report to their maintainers)

## Security Hall of Fame

We maintain a list of security researchers who have helped improve MythosMUD's security:

- *Your name could be here! Report responsibly and help us keep the Mythos safe.*

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Python Security Best Practices](https://python-security.readthedocs.io/)
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [React Security Best Practices](https://snyk.io/blog/10-react-security-best-practices/)

## Contact

For security-related questions or concerns:

- **GitHub Issues**: For non-sensitive questions (use `security` label)
- **Private Contact**: Email maintainers directly for sensitive issues
- **Documentation**: Review comprehensive security docs in `/docs` directory

---

*"The wards are in place, the sigils inscribed. We guard not only against the eldritch horrors of the Mythos, but also against the all-too-real threats of the digital realm."*

**Last Updated**: January 2025
**Version**: 1.0
**Status**: ✅ Production-ready security implementation
