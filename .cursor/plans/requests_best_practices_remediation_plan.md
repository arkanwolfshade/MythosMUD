# Requests Library Best Practices Remediation Plan

**Date**: 2026-01-14
**Reviewer**: AI Agent (Auto)
**Scope**: Codebase review against `.cursor/rules/requests.mdc` best practices

## Executive Summary

After conducting a comprehensive review of the codebase against the `requests` library best practices defined in `.cursor/rules/requests.mdc`, **no violations were found** because the `requests` library is **not actually used anywhere in the codebase**.

However, several important findings and recommendations have been identified:

1. **Unused Dependency**: `requests>=2.32.5` is listed in `pyproject.toml` but not imported or used anywhere
2. **Async-First Architecture**: The codebase uses FastAPI (async) and would benefit from `httpx` if external HTTP calls are needed
3. **Future-Proofing**: If HTTP client functionality is added, it should follow best practices from the start

## Findings

### 1. Unused Dependency (Low Priority)

**Location**: `pyproject.toml:16`

```toml
"requests>=2.32.5",
```

**Issue**: The `requests` library is declared as a dependency but has zero usage in the codebase.

**Evidence**:

- No `import requests` or `from requests` statements found in `server/`, `scripts/`, or `tools/` directories
- No `requests.get()`, `requests.post()`, or other `requests.*` method calls found
- Type stubs are included (`types-requests>=2.32.4.20260107`) but unused

**Impact**:

- Unnecessary dependency bloat
- Potential security surface area (even if unused)
- Confusion about whether HTTP client functionality exists

**Recommendation**:

**Option A (Recommended)**: Remove `requests` from dependencies if not needed

**Option B**: Keep it if there are plans to use it, but document why in a comment

**Option C**: Replace with `httpx` if async HTTP client is needed (better fit for FastAPI/async codebase)

### 2. Architecture Alignment (Informational)

**Finding**: The codebase is async-first:

- FastAPI (async web framework)
- SQLAlchemy async sessions
- NATS async messaging
- All server code uses `async/await` patterns

**Implication**: If external HTTP calls are needed in the future, `httpx` (async HTTP client) would be more appropriate than `requests` (synchronous).

**Note**: The codebase already has `.cursor/rules/httpx.mdc` with best practices for async HTTP clients.

### 3. Client-Side HTTP Calls (Informational)

**Finding**: The TypeScript/React client uses native `fetch()` API for HTTP calls.

**Status**: ✅ **No action needed** - Client-side code is outside Python `requests` library scope.

**Examples**:

- `client/src/components/StatsRollingScreen.tsx` - Uses `fetch()` with proper error handling
- `client/src/hooks/useWebSocketConnection.ts` - Uses `fetch()` for health checks
- `client/src/components/map/hooks/useRoomMapData.ts` - Uses `fetch()` with error handling

**Note**: Client-side code follows good practices (error handling, timeout awareness via browser defaults).

## Remediation Plan

### Phase 1: Dependency Cleanup (Low Priority)

**Task 1.1**: Decide on `requests` dependency future

- [x] Determine if `requests` is needed for future features - **Decision: Not needed, removed**
- [x] If not needed: Remove from `pyproject.toml` dependencies - **Completed**
- [x] If needed: Add comment explaining planned usage - **N/A - Removed**
- [x] If async HTTP needed: Consider adding `httpx` instead - **Noted for future use**

**Task 1.2**: Update dependency analysis scripts

- [x] Review `scripts/manual_dependency_analysis.py` - mentions `requests` in medium_risk_packages - **Completed**
- [x] Review `scripts/dependency_analyzer.py` - mentions `requests` in medium_risk_packages - **Completed**
- [x] Update scripts to reflect actual dependency usage - **Completed**

**Task 1.3**: Remove unused type stubs (if removing requests)

- [x] Remove `types-requests>=2.32.4.20260107` from `pyproject.toml` dev dependencies (line 64) - **Completed**
- [x] Remove from `dependency-groups.dev` (line 346) if present - **Completed**

### Phase 2: Future-Proofing (When HTTP Client is Needed)

**Task 2.1**: Create HTTP client infrastructure (if needed)

- [ ] If using `requests`: Create dedicated API client class following `.cursor/rules/requests.mdc`
- [ ] If using `httpx`: Create dedicated async API client class following `.cursor/rules/httpx.mdc`
- [ ] Implement:
  - Session/Client objects with connection pooling
  - Retry logic with exponential backoff
  - Explicit timeouts on all requests
  - Robust error handling (`raise_for_status()`, JSON decode error handling)
  - Environment variable configuration (no hardcoded URLs/credentials)
  - Comprehensive logging

**Task 2.2**: Add tests for HTTP client (when implemented)

- [ ] Mock HTTP calls using `unittest.mock` or `responses` library
- [ ] Test retry logic
- [ ] Test timeout handling
- [ ] Test error scenarios (4xx, 5xx, connection errors, JSON decode errors)

### Phase 3: Documentation (Optional)

**Task 3.1**: Document HTTP client decision

- [ ] Add decision record if choosing between `requests` vs `httpx`
- [ ] Document any external API integrations
- [ ] Update architecture documentation

## Best Practices Checklist (For Future Implementation)

When implementing HTTP client functionality, ensure:

- [ ] ✅ Use `Session` objects (or `httpx.AsyncClient` for async)
- [ ] ✅ Configure retries with `HTTPAdapter` and `Retry` strategy
- [ ] ✅ Set explicit timeouts on all requests: `timeout=(connect_timeout, read_timeout)`
- [ ] ✅ Use `raise_for_status()` to handle HTTP errors
- [ ] ✅ Handle `JSONDecodeError` separately from other exceptions
- [ ] ✅ Encapsulate in dedicated API client class/module
- [ ] ✅ Use environment variables for URLs and credentials
- [ ] ✅ Add comprehensive logging for debugging
- [ ] ✅ Write tests with mocked HTTP calls

## Risk Assessment

| Finding                            | Severity | Priority | Effort               |
| ---------------------------------- | -------- | -------- | -------------------- |
| Unused `requests` dependency       | Low      | Low      | Low (simple removal) |
| Missing HTTP client infrastructure | N/A      | N/A      | N/A (not needed yet) |

## Recommendations

1. **Immediate Action**: Review whether `requests` dependency is needed. If not, remove it to reduce dependency bloat.

2. **Future Planning**: If external HTTP API calls are planned:

   - Prefer `httpx` over `requests` for async compatibility
   - Follow `.cursor/rules/httpx.mdc` for async HTTP clients
   - If `requests` is chosen, strictly follow `.cursor/rules/requests.mdc`

3. **Code Quality**: The codebase is well-structured and would easily accommodate proper HTTP client implementation when needed.

## Conclusion

The codebase currently has **zero violations** of `requests` best practices because the library is not used. The primary action item is to clean up the unused dependency and prepare for future HTTP client needs with appropriate async-first tooling (`httpx`).

---

**Next Steps**:

1. Review and decide on `requests` dependency removal
2. Update dependency analysis scripts if `requests` is removed
3. When HTTP client functionality is needed, implement following best practices from the start
