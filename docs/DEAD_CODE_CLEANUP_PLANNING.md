# Dead Code Cleanup Planning Document

## Overview

This document outlines the plan for cleaning up dead code identified in the MythosMUD server codebase. The cleanup will improve code maintainability, reduce cognitive load, and eliminate potential confusion for developers.

**As noted in the Pnakotic Manuscripts, the proper organization of arcane knowledge is essential for maintaining the delicate balance between order and chaos in our digital realm.**

## Objectives

1. **Remove completely unused files** that serve no purpose
2. **Eliminate deprecated code** that has been superseded
3. **Clean up unused classes and functions** that add noise without value
4. **Improve code maintainability** by reducing dead code surface area
5. **Ensure no functionality is lost** during the cleanup process

## Risk Assessment

### Low Risk Items

- Completely unused files with no imports
- Explicitly deprecated classes
- Functions used only in tests but not in production

### Medium Risk Items

- Legacy files with partial usage
- Classes that might be used in future features
- Utility functions that could be needed for debugging

### High Risk Items

- None identified in this cleanup

## Cleanup Phases

### Phase 1: High Priority - Remove Completely Unused Files

**Estimated Time**: 1-2 hours
**Risk Level**: Low

#### 1.1 Remove `server/check_routes.py` ✅ **COMPLETED**

- **Reason**: Standalone utility script with no imports
- **Action**: Delete file entirely
- **Verification**: Run test suite to ensure no impact
- **Files to modify**: None (deletion only)
- **Status**: ✅ Completed - File and associated test file deleted, all tests pass

#### 1.2 Remove `server/check_invites.py`

- **Reason**: Standalone utility script with no imports
- **Action**: Delete file entirely
- **Verification**: Run test suite to ensure no impact
- **Files to modify**: None (deletion only)
- **Status**: ✅ Completed - File deleted, all tests pass

#### 1.3 Remove `server/test_integration.py`

- **Reason**: Unused integration test script
- **Action**: Delete file entirely
- **Verification**: Run test suite to ensure no impact
- **Files to modify**: None (deletion only)

#### 1.4 Remove `server/player_manager.py`

- **Reason**: Explicitly deprecated class that raises NotImplementedError
- **Action**: Delete file entirely
- **Verification**: Run test suite to ensure no impact
- **Files to modify**: None (deletion only)

### Phase 2: Medium Priority - Extract and Remove Legacy Code

**Estimated Time**: 2-3 hours
**Risk Level**: Medium

#### 2.1 Refactor `server/real_time.py` ✅ **COMPLETED**

- **Current State**: Legacy file with only `load_motd()` function used
- **Action**:
  1. Create `server/utils/motd_loader.py` for the `load_motd()` function
  2. Update imports in files that use `load_motd()`
  3. Remove `server/real_time.py`
- **Files to modify**:
  - Create: `server/utils/motd_loader.py`
  - Update: `server/api/__init__.py` (if imports real_time)
  - Update: `server/tests/test_real_time.py` (rename to test_motd_loader.py)
- **Verification**: Ensure MOTD loading still works correctly
- **Status**: ✅ Completed - MOTD function extracted to utils module, tests updated, legacy file removed

### Phase 3: Low Priority - Remove Unused Classes and Functions

**Estimated Time**: 1-2 hours
**Risk Level**: Low

#### 3.1 Remove `MultiFileHandler` class from `server/logging_config.py` ✅ **COMPLETED**

- **Reason**: Defined but never used
- **Action**: Remove class definition
- **Verification**: Run test suite to ensure no impact
- **Files to modify**: `server/logging_config.py`
- **Status**: ✅ Completed - Class removed, all tests pass, no linting errors

#### 3.2 Remove `CircuitBreaker` class from `server/error_handlers.py`

- **Reason**: Used only in tests, not in production
- **Action**: Remove class definition and related tests
- **Verification**: Run test suite to ensure no impact
- **Files to modify**:
  - `server/error_handlers.py`
  - `server/tests/test_exceptions.py` (remove CircuitBreaker tests)

#### 3.3 Remove `benchmark_hash_time()` function from `server/auth/argon2_utils.py`

- **Reason**: Used only in tests, not in production
- **Action**: Remove function definition and related tests
- **Verification**: Run test suite to ensure no impact
- **Files to modify**:
  - `server/auth/argon2_utils.py`
  - `server/tests/test_argon2_utils.py` (remove benchmark tests)

#### 3.4 Remove `graceful_degradation()` function from `server/error_handlers.py`

- **Reason**: Used only in tests, not in production
- **Action**: Remove function definition and related tests
- **Verification**: Run test suite to ensure no impact
- **Files to modify**:
  - `server/error_handlers.py`
  - `server/tests/test_exceptions.py` (remove graceful_degradation tests)

### Phase 4: Review and Future Planning

**Estimated Time**: 1 hour
**Risk Level**: Low

#### 4.1 Review Object and NPC Event Types

- **Current State**: `ObjectAddedToRoom`, `ObjectRemovedFromRoom`, `NPCEnteredRoom`, `NPCLeftRoom` defined but unused
- **Action**: Document these for future feature planning
- **Decision**: Keep for future object/NPC system implementation
- **Files to modify**: None (documentation only)

## Implementation Checklist

### Pre-Cleanup Tasks

- [ ] Create backup branch: `git checkout -b backup/dead-code-cleanup`
- [ ] Run full test suite to establish baseline
- [ ] Document current code coverage metrics
- [ ] Review any pending pull requests that might be affected

### Phase 1 Tasks

- [ ] Delete `server/check_routes.py`
- [ ] Delete `server/check_invites.py`
- [ ] Delete `server/test_integration.py`
- [ ] Delete `server/player_manager.py`
- [ ] Run test suite and verify no regressions
- [ ] Commit changes with message: "Remove completely unused utility files"

### Phase 2 Tasks

- [x] Create `server/utils/` directory if it doesn't exist
- [x] Create `server/utils/motd_loader.py` with `load_motd()` function
- [x] Update imports in `server/api/__init__.py` (if needed)
- [x] Rename `server/tests/test_real_time.py` to `server/tests/test_motd_loader.py`
- [x] Update test imports to use new module
- [x] Delete `server/real_time.py`
- [x] Test MOTD loading functionality
- [x] Run test suite and verify no regressions
- [x] Commit changes with message: "Refactor MOTD loading from legacy real_time module"

### Phase 3 Tasks

- [x] Remove `MultiFileHandler` class from `server/logging_config.py`
- [ ] Remove `CircuitBreaker` class from `server/error_handlers.py`
- [ ] Remove `CircuitBreaker` tests from `server/tests/test_exceptions.py`
- [ ] Remove `benchmark_hash_time()` function from `server/auth/argon2_utils.py`
- [ ] Remove benchmark tests from `server/tests/test_argon2_utils.py`
- [ ] Remove `graceful_degradation()` function from `server/error_handlers.py`
- [ ] Remove graceful_degradation tests from `server/tests/test_exceptions.py`
- [ ] Run test suite and verify no regressions
- [ ] Commit changes with message: "Remove unused classes and functions"

### Post-Cleanup Tasks

- [ ] Run full test suite to ensure no regressions
- [ ] Update code coverage metrics
- [ ] Update documentation if needed
- [ ] Create pull request for review
- [ ] Update this planning document with results

## Success Criteria

### Functional Requirements

- [ ] All existing functionality remains intact
- [ ] Test suite passes with no regressions
- [ ] Code coverage remains at or above current levels
- [ ] No new linting errors introduced

### Quality Requirements

- [ ] Reduced codebase size by removing dead code
- [ ] Improved code maintainability
- [ ] Reduced cognitive load for developers
- [ ] Cleaner project structure

### Documentation Requirements

- [ ] Update any documentation that referenced removed files
- [ ] Document any new utility modules created
- [ ] Update this planning document with lessons learned

## Rollback Plan

If issues are discovered during cleanup:

1. **Immediate Rollback**: Use backup branch to restore previous state
2. **Incremental Rollback**: Revert specific commits that caused issues
3. **Partial Rollback**: Keep some changes while reverting problematic ones

## Communication Plan

### Internal Communication

- Update `TASKS.local.md` with cleanup progress
- Document any issues or unexpected findings
- Update team on completion status

### External Communication

- Update GitHub Issues if any were related to dead code
- Update project documentation if needed
- Consider blog post about code cleanup process (optional)

## Future Considerations

### Monitoring

- Set up automated dead code detection in CI/CD pipeline
- Regular code reviews to identify new dead code
- Periodic cleanup sprints

### Prevention

- Implement stricter import policies
- Add linting rules for unused imports
- Regular code audits

### Documentation

- Maintain this planning document for future cleanup efforts
- Document patterns that lead to dead code
- Create guidelines for preventing dead code accumulation

## Timeline

- **Phase 1**: Day 1 (1-2 hours)
- **Phase 2**: Day 1-2 (2-3 hours)
- **Phase 3**: Day 2 (1-2 hours)
- **Phase 4**: Day 2 (1 hour)
- **Total Estimated Time**: 5-8 hours

## Resources Required

- Development environment access
- Test database access
- Git repository access
- Code review from team members

## Dependencies

- No external dependencies
- Requires approval for production deployment
- May require coordination with other developers if they're working on affected files

---

*"As the ancient texts state: 'The proof of the pudding is in the eating, and the proof of the system is in the testing.'"*

**Document Version**: 1.0
**Created**: 2025-01-16
**Last Updated**: 2025-01-16
**Status**: Planning Phase
