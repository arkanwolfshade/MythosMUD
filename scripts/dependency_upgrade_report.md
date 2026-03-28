
# MythosMUD Dependency Upgrade Report
Generated: 2026-03-27T19:31:06.842685

## Executive Summary

**Overall Strategy**: INCREMENTAL
**Priority Level**: HIGH
**Total Packages**: 36
**Overall Risk**: HIGH

## Update Statistics

### By Update Type
- Major Updates: 9
- Minor Updates: 18
- Patch Updates: 9

### By Risk Level
- High Risk: 9
- Medium Risk: 1
- Low Risk: 26

## Priority Update List


### 1. argon2-cffi [HIGH] (major)
- **Current**: 23.1.0 -> **Latest**: 25.1.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 2. argon2-cffi-bindings [HIGH] (major)
- **Current**: 21.2.0 -> **Latest**: 25.1.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 3. boltons [HIGH] (major)
- **Current**: 21.0.0 -> **Latest**: 25.0.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 4. glom [HIGH] (major)
- **Current**: 22.1.0 -> **Latest**: 24.11.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 5. importlib-metadata [HIGH] (major)
- **Current**: 7.1.0 -> **Latest**: 8.7.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 6. protobuf [HIGH] (major)
- **Current**: 4.25.8 -> **Latest**: 6.32.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 7. pytest-asyncio [HIGH] (major)
- **Current**: 0.24.0 -> **Latest**: 1.1.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 8. rich [HIGH] (major)
- **Current**: 13.5.3 -> **Latest**: 14.1.0
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 9. wcmatch [HIGH] (major)
- **Current**: 8.5.2 -> **Latest**: 10.1
- **Update Type**: major
- **Risk Level**: HIGH
- **Ecosystem**: pip
- **Priority Score**: 120

### 10. eslint [MED] (minor)
- **Current**: 9.33.0 -> **Latest**: 9.35.0
- **Update Type**: minor
- **Risk Level**: MEDIUM
- **Ecosystem**: npm
- **Priority Score**: 60

### 11. @eslint/js [LOW] (minor)
- **Current**: 9.33.0 -> **Latest**: 9.35.0
- **Update Type**: minor
- **Risk Level**: LOW
- **Ecosystem**: npm
- **Priority Score**: 50

### 12. @playwright/test [LOW] (minor)
- **Current**: 1.54.2 -> **Latest**: 1.55.0
- **Update Type**: minor
- **Risk Level**: LOW
- **Ecosystem**: npm
- **Priority Score**: 50

### 13. @testing-library/jest-dom [LOW] (minor)
- **Current**: 6.7.0 -> **Latest**: 6.8.0
- **Update Type**: minor
- **Risk Level**: LOW
- **Ecosystem**: npm
- **Priority Score**: 50

### 14. lucide-react [LOW] (minor)
- **Current**: 0.540.0 -> **Latest**: 0.542.0
- **Update Type**: minor
- **Risk Level**: LOW
- **Ecosystem**: npm
- **Priority Score**: 50

### 15. typescript-eslint [LOW] (minor)
- **Current**: 8.40.0 -> **Latest**: 8.42.0
- **Update Type**: minor
- **Risk Level**: LOW
- **Ecosystem**: npm
- **Priority Score**: 50

## Breaking Changes Detected

- **argon2-cffi**: 23.1.0 -> 25.1.0 (pip)
- **argon2-cffi-bindings**: 21.2.0 -> 25.1.0 (pip)
- **boltons**: 21.0.0 -> 25.0.0 (pip)
- **glom**: 22.1.0 -> 24.11.0 (pip)
- **importlib-metadata**: 7.1.0 -> 8.7.0 (pip)
- **protobuf**: 4.25.8 -> 6.32.0 (pip)
- **pytest-asyncio**: 0.24.0 -> 1.1.0 (pip)
- **rich**: 13.5.3 -> 14.1.0 (pip)
- **wcmatch**: 8.5.2 -> 10.1 (pip)

## Detailed Recommendations


### Incremental Upgrade Strategy
1. **Phase 1**: Update patch versions (low risk)
2. **Phase 2**: Update minor versions (medium risk)
3. **Phase 3**: Plan major version updates (high risk)
4. **Testing**: Full test suite after each phase

## Upgrade Commands

### NPM Package Updates

```bash
cd client
npm install eslint@9.35.0
npm install @eslint/js@9.35.0
npm install @playwright/test@1.55.0
npm install @testing-library/jest-dom@6.8.0
npm install lucide-react@0.542.0
```

### Python Package Updates

```bash
uv pip install argon2-cffi==25.1.0
uv pip install argon2-cffi-bindings==25.1.0
uv pip install boltons==25.0.0
uv pip install glom==24.11.0
uv pip install importlib-metadata==8.7.0
```


## Testing Strategy

### Pre-Upgrade Testing
1. **Current State**: Run full test suite to establish baseline
2. **Backup**: Create git commit point before upgrades
3. **Documentation**: Note current working state

### Post-Upgrade Testing
1. **Unit Tests**: `make test` (from project root)
2. **Integration Tests**: `make test`
3. **Client Tests**: `cd client && npm test`
4. **Linting**: `make lint`
5. **Manual Testing**: Key user flows

### Rollback Plan
```bash
# If issues arise, rollback to previous state
git checkout HEAD~1
cd client && npm install
uv pip install -r requirements.txt  # or equivalent
```
