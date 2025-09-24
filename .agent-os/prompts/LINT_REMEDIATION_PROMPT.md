# Lint Remediation Prompt

## Purpose
This prompt guides the systematic remediation of linting errors in the MythosMUD codebase, ensuring code quality and consistency across Python and TypeScript components.

## Current Linting Issues Detected

### Python (Ruff) Issues
- **B017**: Do not assert blind exception: `Exception`
  - Location: `server/tests/test_profession_models.py:292:18`
  - Location: `server/tests/test_profession_models.py:307:18`
  - Issue: Using generic `Exception` in pytest.raises instead of specific exception types

### TypeScript (ESLint) Issues
- **@typescript-eslint/no-explicit-any**: Unexpected any. Specify a different type
  - Location: `client/src/components/ProfessionCard.tsx:9:38`
  - Issue: Using `any` type instead of proper TypeScript typing

- **react-hooks/exhaustive-deps**: Missing dependency in useEffect
  - Location: `client/src/components/ProfessionSelectionScreen.tsx:29:6`
  - Issue: useEffect missing dependency 'fetchProfessions'

## Remediation Strategy

### Phase 1: Python Issues
1. Replace generic `Exception` with specific exception types
2. For SQLite operations, use `sqlalchemy.exc.IntegrityError` or `sqlalchemy.exc.OperationalError`
3. Ensure proper exception handling for database constraint violations

### Phase 2: TypeScript Issues
1. Replace `any` types with proper TypeScript interfaces/types
2. Fix useEffect dependency arrays to include all required dependencies
3. Consider using useCallback for function dependencies

### Phase 3: Verification
1. Run `make lint` to verify all issues are resolved
2. Run `make test` to ensure no functionality is broken
3. Verify code coverage remains above 80%

## Expected Outcomes
- All linting errors resolved
- Code quality improved
- Type safety enhanced
- No regression in functionality
- All tests passing

## Files to Modify
- `server/tests/test_profession_models.py`
- `client/src/components/ProfessionCard.tsx`
- `client/src/components/ProfessionSelectionScreen.tsx`
