
# MythosMUD Dependency Upgrade Implementation Plan
Generated: 2025-09-06T10:24:01.658963

## Overview
This plan implements the incremental upgrade strategy for MythosMUD dependencies.
Total packages to upgrade: 37
Major updates: 9 (HIGH RISK)
Minor updates: 18 (MEDIUM RISK)
Patch updates: 10 (LOW RISK)

## Risk Assessment
- **Overall Risk**: HIGH
- **Strategy**: INCREMENTAL
- **Timeline**: 2-3 weeks
- **Testing**: Comprehensive at each phase


# Phase 1: Patch Updates (Low Risk)
## Timeline: 1-2 days
## Risk Level: LOW

### NPM Patch Updates
```bash
cd client
npm install @types/node@24.3.1
npm install @types/react@19.1.12
npm install @types/react-dom@19.1.9
npm install @vitejs/plugin-react@5.0.2
npm install vite@7.1.4
```

### Python Patch Updates
```bash
uv pip install click@8.2.1
uv pip install email-validator@2.3.0
uv pip install exceptiongroup@1.3.0
uv pip install pytest@8.4.2
uv pip install pytest-cov@6.3.0
uv pip install python-dotenv@1.1.1
uv pip install requests@2.32.5
uv pip install ruff@0.12.12
uv pip install tomli@2.2.1
```

### Testing Strategy
1. **Pre-upgrade**: Run full test suite
2. **Post-upgrade**: Run full test suite
3. **Verification**: Manual testing of key features
4. **Rollback**: Git commit point available

### Success Criteria
- All tests pass
- No new linting errors
- Application starts successfully
- No performance regressions



# Phase 2: Minor Updates (Medium Risk)
## Timeline: 3-5 days
## Risk Level: MEDIUM

### NPM Minor Updates
```bash
cd client
npm install @eslint/js@9.35.0
npm install @playwright/test@1.55.0
npm install @tailwindcss/postcss@4.1.13
npm install @testing-library/jest-dom@6.8.0
npm install eslint@9.35.0
npm install lucide-react@0.542.0
npm install tailwindcss@4.1.13
npm install typescript-eslint@8.42.0
```

### Python Minor Updates
```bash
uv pip install pydantic-core@2.39.0
uv pip install rich@14.1.0
```

### Testing Strategy
1. **Pre-upgrade**: Full test suite + integration tests
2. **Post-upgrade**: Full test suite + integration tests
3. **ESLint**: Check for new linting rules
4. **Playwright**: Verify test compatibility
5. **UI Testing**: Manual testing of client interface

### Success Criteria
- All tests pass
- ESLint rules updated successfully
- Playwright tests compatible
- UI components render correctly
- No breaking changes in APIs



# Phase 3: Major Updates (High Risk)
## Timeline: 1-2 weeks
## Risk Level: HIGH

## 3.1: Low-Impact Major Updates
### Timeline: 2-3 days each

#### argon2-cffi (23.1.0 → 25.1.0)
```bash
uv pip install argon2-cffi@25.1.0
uv pip install argon2-cffi-bindings@25.1.0
```

**Migration Steps:**
1. Update password hashing tests
2. Verify authentication flows
3. Test user registration/login
4. Check password reset functionality

**Testing Focus:**
- Authentication system
- Password hashing/verification
- User management

#### protobuf (4.25.8 → 6.32.0)
```bash
uv pip install protobuf@6.32.0
```

**Migration Steps:**
1. Update any protobuf message definitions
2. Test API communication
3. Verify message serialization
4. Check client-server communication

**Testing Focus:**
- API endpoints
- Message serialization
- Client-server communication

## 3.2: High-Impact Major Updates
### Timeline: 1 week each

#### pytest-asyncio (0.24.0 → 1.1.0)
```bash
uv pip install pytest-asyncio@1.1.0
```

**Migration Steps:**
1. **CRITICAL**: Update all async test fixtures
2. Review and update test configuration
3. Update async test patterns
4. Verify all async tests work correctly

**Breaking Changes:**
- Event loop management changed
- Fixture patterns updated
- Async test handling modified

**Testing Focus:**
- All async tests
- Test fixtures
- Test configuration
- Database tests
- WebSocket tests

### Success Criteria for Phase 3
- All major updates completed
- Full test suite passes
- No breaking changes in production
- Performance maintained or improved
- Documentation updated



# Migration Guides for Major Updates

## pytest-asyncio Migration Guide

### Current State (0.24.0)
```python
import pytest_asyncio

@pytest_asyncio.fixture
async def async_fixture():
    # Current async fixture pattern
    pass

@pytest.mark.asyncio
async def test_async_function():
    # Current async test pattern
    pass
```

### Target State (1.1.0)
```python
import pytest

@pytest.fixture
async def async_fixture():
    # New async fixture pattern
    pass

@pytest.mark.asyncio
async def test_async_function():
    # Updated async test pattern
    pass
```

### Migration Steps
1. **Update imports**: Remove `pytest_asyncio` imports
2. **Update fixtures**: Use `@pytest.fixture` for async fixtures
3. **Update configuration**: Modify pytest configuration
4. **Test compatibility**: Verify all async tests work

### Configuration Updates
```python
# pytest.ini or pyproject.toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```

## argon2-cffi Migration Guide

### Current State (23.1.0)
```python
from argon2 import PasswordHasher

hasher = PasswordHasher()
hash = hasher.hash("password")
```

### Target State (25.1.0)
```python
from argon2 import PasswordHasher

# API remains largely the same
hasher = PasswordHasher()
hash = hasher.hash("password")
```

### Migration Steps
1. **Update dependencies**: Install new version
2. **Test compatibility**: Verify existing code works
3. **Performance testing**: Check for performance improvements
4. **Security review**: Ensure security features are maintained

## protobuf Migration Guide

### Current State (4.25.8)
```python
import google.protobuf.message

# Current protobuf usage
```

### Target State (6.32.0)
```python
import google.protobuf.message

# Updated protobuf usage with performance improvements
```

### Migration Steps
1. **Update dependencies**: Install new version
2. **Test serialization**: Verify message serialization works
3. **Performance testing**: Check for performance improvements
4. **API compatibility**: Ensure API calls work correctly



# Rollback Procedures

## Emergency Rollback (Immediate)
```bash
# If critical issues arise during upgrade
git checkout HEAD~1
cd client && npm install
uv pip install -r requirements.txt  # or use uv.lock
```

## Phase-Specific Rollback

### Phase 1 Rollback
```bash
# Rollback patch updates
git checkout HEAD~1
cd client && npm install
uv pip install click@8.1.8
uv pip install email-validator@2.2.0
# ... other patch rollbacks
```

### Phase 2 Rollback
```bash
# Rollback minor updates
git checkout HEAD~2
cd client && npm install
uv pip install pydantic-core@2.33.2
uv pip install rich@13.5.3
```

### Phase 3 Rollback
```bash
# Rollback major updates
git checkout HEAD~3
cd client && npm install
uv pip install argon2-cffi@23.1.0
uv pip install pytest-asyncio@0.24.0
uv pip install protobuf@4.25.8
```

## Verification After Rollback
```bash
# Verify rollback was successful
make test
make lint
cd client && npm test
```

## Database Rollback (if needed)
```bash
# If database schema changes were made
# Restore from backup or migrate back
./scripts/restore_database.sh
```



# Post-Upgrade Monitoring Plan

## Immediate Monitoring (First 24 hours)
- **Application startup**: Verify all services start correctly
- **API endpoints**: Test critical API endpoints
- **Database connections**: Verify database connectivity
- **Authentication**: Test login/logout flows
- **Error rates**: Monitor for increased error rates

## Short-term Monitoring (First week)
- **Performance metrics**: Monitor response times
- **Memory usage**: Check for memory leaks
- **Test suite**: Run full test suite daily
- **User feedback**: Monitor for user-reported issues
- **Log analysis**: Review logs for new errors

## Long-term Monitoring (First month)
- **Stability**: Monitor overall system stability
- **Performance trends**: Track performance over time
- **Security**: Monitor for security issues
- **Dependency updates**: Plan next upgrade cycle

## Monitoring Tools
- **Application logs**: Structured logging with structlog
- **Performance metrics**: Built-in FastAPI metrics
- **Test coverage**: Maintain test coverage reports
- **Error tracking**: Monitor error rates and patterns

## Alert Thresholds
- **Error rate**: > 1% increase
- **Response time**: > 20% increase
- **Memory usage**: > 50% increase
- **Test failures**: Any test failures


## Success Metrics
- All tests pass at each phase
- No performance regressions
- No security vulnerabilities introduced
- Application stability maintained
- User experience unchanged or improved

## Next Steps
1. **Review plan** with team
2. **Schedule upgrade windows** for each phase
3. **Prepare rollback procedures**
4. **Begin Phase 1** (patch updates)
5. **Monitor and iterate** through phases
