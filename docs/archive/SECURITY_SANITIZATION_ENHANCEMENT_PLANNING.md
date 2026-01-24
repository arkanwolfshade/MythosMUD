F# Security Sanitization Enhancement Planning

## Overview

This document outlines the implementation plan for enhancing MythosMUD's input **sanitization** system with `ftfy` (Unicode normalization) and `strip-ansi` (ANSI code removal) libraries to provide more robust protection against malicious input while maintaining user input freedom.

**Key Principle**: We focus on **sanitization** (cleaning dangerous content) rather than **validation** (rejecting input), allowing users freeform expression while protecting against injection attacks.

## Background

### Current State

Basic injection pattern detection via regex in `security_validator.py`

- Simple whitespace normalization in `command_validator.py`
- No Unicode normalization or ANSI code handling
- Limited protection against encoding-based attacks
- **Current approach**: Mix of validation (rejection) and sanitization (cleaning)

### Problem Statement

1. **Unicode Issues**: Players may input text with encoding problems (mojibake, combining characters, invisible Unicode)
2. **ANSI Codes**: Terminal clients might send ANSI escape sequences that could hide malicious content
3. **Security Gaps**: Current sanitization doesn't address these attack vectors
4. **Client Compatibility**: Various client types may send differently encoded input
5. **Input Philosophy**: Current system mixes validation (rejection) with sanitization (cleaning), potentially limiting user expression

## Proposed Solution

### Input Philosophy: Sanitization Over Validation

**Core Principle**: Users should have maximum freedom to express themselves in the MUD environment. Our security approach focuses on **sanitizing** potentially dangerous content rather than **validating** and rejecting input.

**Sanitization vs Validation**:

**Sanitization**: Clean dangerous content while preserving user intent

**Validation**: Reject input that doesn't meet specific criteria

**Examples**:

✅ **Sanitization**: Remove ANSI codes from "Hello \033[31mWorld\033[0m" → "Hello World"

❌ **Validation**: Reject "Hello \033[31mWorld\033[0m" entirely

✅ **Sanitization**: Fix Unicode "café" (combining characters) → "café" (composed)
- ❌ **Validation**: Reject text with combining characters

### Libraries to Implement

#### 1. ftfy (Fixes Text For You)

**Purpose**: Fixes common Unicode encoding issues

**Version**: `>=6.1.3`

**Key Features**:
  - Mojibake detection and correction
  - Combining character normalization
  - Invisible Unicode character removal
  - Curly quote conversion
  - Line break normalization

#### 2. strip-ansi

**Purpose**: Removes ANSI escape codes from text

**Version**: `>=0.1.1`

**Key Features**:
  - ANSI color code removal
  - Cursor movement code removal
  - Terminal escape sequence cleanup

## Implementation Plan

### Phase 1: Dependency Addition

1. **Add dependencies to `pyproject.toml`**

   ```toml
   "ftfy>=6.1.3", # Fixes "bad" Unicode input safely
   "strip-ansi>=0.1.1", # Removes ANSI escape codes
   ```

2. **Update virtual environment**

   - Run `uv sync` to install new dependencies
   - Verify installation with test imports

### Phase 2: Security Validator Enhancement

1. **Enhance `server/validators/security_validator.py`**

   - Add import statements for new libraries
   - Create `sanitize_unicode_input()` function using ftfy
   - Create `strip_ansi_codes()` function using strip-ansi
   - Create `comprehensive_sanitize_input()` function that combines both
   - Add control character removal for additional security
   - **Review existing validation patterns**: Ensure they focus on sanitization rather than rejection

2. **Function Specifications**

   ```python
   def sanitize_unicode_input(text: str) -> str:
       """Fix Unicode encoding issues using ftfy."""

   def strip_ansi_codes(text: str) -> str:
       """Remove ANSI escape codes from text."""

   def comprehensive_sanitize_input(text: str) -> str:
       """Apply all sanitization layers to input."""
   ```

### Phase 3: Command Validator Integration

1. **Update `server/validators/command_validator.py`**

   - Import new sanitization functions
   - Modify `clean_command_input()` to use comprehensive sanitization
   - Maintain backward compatibility with existing function signatures
   - Add logging for sanitization operations
   - **Review validation logic**: Ensure `is_suspicious_input()` focuses on true injection attempts, not legitimate user expression

2. **Integration Points**

   - Apply sanitization before command normalization
   - Log sanitization changes for debugging
   - Preserve original input for comparison

### Phase 4: Package Export Updates

1. **Update `server/validators/__init__.py`**

   - Export new sanitization functions
   - Update `__all__` list
   - Maintain existing API compatibility

### Phase 5: Testing Implementation

1. **Create comprehensive test suite**

   - Test Unicode normalization scenarios
   - Test ANSI code removal scenarios
   - Test combined sanitization
   - Test edge cases and error conditions
   - Test performance impact
   - **Test user expression freedom**: Ensure legitimate user input isn't rejected
   - **Test sanitization vs validation**: Verify we're cleaning, not rejecting

2. **Test Scenarios**

   - Mojibake text (double-encoded Unicode)
   - Combining characters (e.g., e + combining acute accent)
   - Invisible Unicode characters (zero-width spaces)
   - ANSI color codes and cursor movement
   - Mixed malicious input
   - Empty and null inputs
   - **Legitimate user expression**: Creative text, roleplay content, non-English text
   - **Edge cases**: Unusual but harmless Unicode sequences
   - **False positive prevention**: Ensure normal user input isn't flagged as suspicious

### Phase 6: Documentation and Validation

1. **Update documentation**

   - Add security enhancement notes to relevant docs
   - Document new function APIs
   - Update security guidelines

2. **Performance validation**

   - Measure sanitization overhead
   - Test with various input sizes
   - Ensure acceptable performance for real-time use

## Technical Details

### ftfy Configuration

```python
# Recommended ftfy settings for MUD environment

ftfy.fix_text(
    text,
    normalization='NFC',  # Normalize to composed form
    remove_terminal_escapes=True,  # Remove terminal codes
    fix_encoding=True,  # Fix encoding issues
    remove_control_chars=True,  # Remove control characters
)
```

### strip-ansi Usage

```python
# Simple ANSI removal

import strip_ansi
cleaned_text = strip_ansi.strip_ansi(input_text)
```

### Error Handling Strategy

1. **Graceful degradation**: If sanitization fails, fall back to basic cleaning
2. **Logging**: Record sanitization operations and failures
3. **Input preservation**: Keep original input for debugging
4. **Performance monitoring**: Track sanitization time impact

## Security Considerations

### Attack Vectors Addressed

1. **Unicode-based injection**: Fixed by ftfy normalization
2. **ANSI code hiding**: Prevented by strip-ansi
3. **Control character injection**: Removed by additional regex
4. **Encoding confusion attacks**: Resolved by proper Unicode handling

### Potential Risks

1. **Performance impact**: Sanitization adds processing overhead
2. **False positives**: Over-sanitization might affect legitimate input
3. **Library vulnerabilities**: Dependencies must be kept updated
4. **Backward compatibility**: Ensure existing functionality isn't broken
5. **Over-validation**: Accidentally rejecting legitimate user expression
6. **User experience impact**: Sanitization that changes user intent

## Success Criteria

### Functional Requirements

[ ] All Unicode encoding issues are properly fixed

- [ ] ANSI escape codes are completely removed
- [ ] Control characters are stripped appropriately
- [ ] Existing command processing continues to work
- [ ] Performance impact is minimal (<5ms per command)
- [ ] **User expression preserved**: Legitimate user input is not rejected
- [ ] **Sanitization focus**: System cleans rather than validates input
- [ ] **False positive prevention**: Normal user behavior isn't flagged as suspicious

### Security Requirements

[ ] No malicious Unicode sequences can bypass sanitization

- [ ] ANSI codes cannot hide malicious content
- [ ] Control character injection is prevented
- [ ] Input validation remains effective

### Quality Requirements

[ ] Comprehensive test coverage (>90%)

- [ ] All existing tests continue to pass
- [ ] Documentation is updated
- [ ] Performance benchmarks are met

## Implementation Timeline

### Week 1: Foundation

Add dependencies and verify installation

- Create basic sanitization functions
- Write initial tests

### Week 2: Integration

Integrate with command validator

- Update package exports
- Complete test suite

### Week 3: Validation

Performance testing and optimization

- Security validation
- Documentation updates

### Week 4: Deployment

Code review and final testing

- Gradual rollout with monitoring
- Post-deployment validation

## Monitoring and Maintenance

### Post-Implementation Monitoring

1. **Performance metrics**: Track sanitization time per command
2. **Error rates**: Monitor sanitization failures
3. **Security incidents**: Track any bypass attempts
4. **User feedback**: Monitor for legitimate input issues
5. **False positive tracking**: Monitor for legitimate input being rejected
6. **User expression impact**: Track if sanitization affects user creativity

### Maintenance Tasks

1. **Dependency updates**: Keep ftfy and strip-ansi updated
2. **Security reviews**: Regular assessment of sanitization effectiveness
3. **Performance optimization**: Continuous improvement of sanitization speed
4. **Test maintenance**: Keep test suite current with new attack vectors

## Rollback Plan

### Rollback Triggers

1. Performance degradation >10%
2. Increased error rates in command processing
3. User complaints about legitimate input being blocked
4. Security vulnerabilities in dependencies
5. **User expression complaints**: Users report being unable to express themselves freely
6. **False positive reports**: Legitimate user behavior being flagged as suspicious

### Rollback Procedure

1. Revert to previous sanitization implementation
2. Remove new dependencies
3. Update documentation
4. Investigate and resolve issues
5. Plan revised implementation approach

## Conclusion

This enhancement will significantly improve MythosMUD's input sanitization capabilities, providing better protection against Unicode-based attacks and improving compatibility with various client types. The phased approach ensures minimal disruption while delivering robust security improvements.

**Key Success Factor**: The implementation prioritizes **user expression freedom** through sanitization rather than validation, ensuring that the MUD remains both safe and welcoming for creative user interaction. Users should feel free to express themselves without fear of their legitimate input being rejected or flagged as suspicious.

The implementation prioritizes security, performance, backward compatibility, and **user experience**, ensuring that the MUD remains both safe and functional for all users.
