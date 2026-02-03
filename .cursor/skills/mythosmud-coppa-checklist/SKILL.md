---
name: mythosmud-coppa-checklist
description: Apply MythosMUD COPPA checklist when adding or changing user data, registration, or features affecting minors: no PII from minors without consent, minimize data, secure storage, right to deletion. Use when implementing auth, user data, or features that collect or display user information.
---

# MythosMUD COPPA Checklist

Apply when adding or changing:

- User data collection or storage
- Registration, login, or account features
- Any feature that could be used by or affect minors (under 13)

## Checklist

- [ ] **No PII from minors without consent:** Do not collect personal information from minors unless explicit parental consent is in place.
- [ ] **Data minimization:** Collect only data essential for the feature or game functionality.
- [ ] **Secure storage:** Data must be encrypted and stored securely.
- [ ] **Right to deletion:** Users (and parents for minors) must be able to delete their data through supported flows.
- [ ] **No tracking:** No behavioral tracking or profiling of minors.

## Implementation

- **Privacy by design:** Consider privacy in the design of the feature, not as an afterthought.
- **Secure by default:** No optional hardening; defaults must be secure.
- **Secrets:** Use environment variables only; never hardcode secrets.
- **Input validation:** Validate and sanitize all inputs on the server.

## Reference

- Full requirements: [CLAUDE.md](../../CLAUDE.md) "CRITICAL SECURITY & PRIVACY REQUIREMENTS" and "COPPA Compliance Requirements"
- Security standards: [CLAUDE.md](../../CLAUDE.md) "Security Implementation Standards"
