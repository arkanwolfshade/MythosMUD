# Argon2 Implementation Plan

## Overview

Replace passlib with argon2-cffi for password hashing in MythosMUD authentication system. Argon2 is the current gold standard for password hashing, offering superior security through memory-hard functions and resistance to GPU/ASIC attacks.

## Current State Analysis

### Existing Authentication System
- Uses passlib with bcrypt for password hashing
- Authentication handled in `server/auth/` modules
- Password verification in `server/auth_utils.py`
- Database stores bcrypt hashes in player records

### Files Requiring Updates
- `server/auth_utils.py` - Core password hashing/verification
- `server/auth/` - Authentication endpoints and logic
- `server/models/` - Player model password field handling
- `server/tests/` - Update test fixtures and mocks
- `pyproject.toml` - Add argon2-cffi dependency
- `requirements.txt` - Update dependencies

## Implementation Strategy

### Phase 1: Dependency and Setup
1. **Add argon2-cffi dependency**
   - Add to `pyproject.toml` and `requirements.txt`
   - Install and verify functionality
   - Create basic hashing/verification tests

2. **Create Argon2 utility module**
   - New file: `server/auth/argon2_utils.py`
   - Implement PasswordHasher class wrapper
   - Add configuration for time_cost, memory_cost, parallelism
   - Include helper functions for hash generation and verification

### Phase 2: Dual-Hashing System
1. **Implement backward compatibility**
   - Modify `auth_utils.py` to support both bcrypt and Argon2
   - Add hash type detection (bcrypt vs Argon2)
   - Implement gradual migration logic

2. **Update authentication flow**
   - Modify login process to check both hash types
   - Update password change functionality
   - Ensure new registrations use Argon2

### Phase 3: Database Migration
1. **Hash migration strategy**
   - Implement automatic hash upgrade on successful login
   - Add migration script for existing users
   - Update test data to use Argon2 hashes

2. **Database schema considerations**
   - Ensure password field can store Argon2 hashes (longer than bcrypt)
   - Add migration script if field length needs adjustment

### Phase 4: Testing and Validation
1. **Comprehensive testing**
   - Unit tests for Argon2 utilities
   - Integration tests for authentication flow
   - Performance testing with realistic load
   - Security testing for hash verification

2. **Backward compatibility testing**
   - Verify existing bcrypt hashes still work
   - Test migration of bcrypt to Argon2 hashes
   - Ensure no authentication failures during transition

## Technical Implementation Details

### Argon2 Configuration
```python
# Recommended settings for web applications
TIME_COST = 3        # Number of iterations
MEMORY_COST = 65536  # Memory usage in KiB (64MB)
PARALLELISM = 4      # Number of parallel threads
```

### Hash Format
- Argon2 hashes are self-contained (include salt and parameters)
- Format: `$argon2id$v=19$m=65536,t=3,p=4$...`
- No additional database fields needed

### Migration Logic
```python
def verify_password(password: str, hash_value: str) -> bool:
    """Verify password against hash, supporting both bcrypt and Argon2"""
    if hash_value.startswith('$2b$'):
        # Legacy bcrypt hash
        return verify_bcrypt(password, hash_value)
    else:
        # Argon2 hash
        return verify_argon2(password, hash_value)
```

## Security Considerations

### Hash Parameters
- **Time Cost**: 3 iterations (balance between security and performance)
- **Memory Cost**: 64MB (resistant to GPU attacks)
- **Parallelism**: 4 threads (utilize modern CPUs)
- **Hash Type**: Argon2id (hybrid approach, recommended)

### Migration Security
- Maintain backward compatibility during transition
- Upgrade hashes only on successful authentication
- No plaintext password storage during migration
- Audit trail for hash upgrades

## Testing Strategy

### Unit Tests
- Test Argon2 hash generation and verification
- Test backward compatibility with bcrypt
- Test hash migration logic
- Test parameter validation

### Integration Tests
- Test complete authentication flow with Argon2
- Test mixed hash types in database
- Test performance under load
- Test error handling and edge cases

### Security Tests
- Verify hash uniqueness (no collisions)
- Test against common attack vectors
- Validate parameter security
- Test memory usage patterns

## Performance Considerations

### Hash Generation Time
- Target: 100-500ms per hash generation
- Adjustable via time_cost parameter
- Consider user experience vs security trade-offs

### Memory Usage
- 64MB per hash operation (configurable)
- Monitor server memory usage
- Consider concurrent user limits

### Database Impact
- Argon2 hashes are longer than bcrypt (~95 chars vs ~60)
- Ensure database field can accommodate longer hashes
- No additional database operations required

## Rollback Plan

### Emergency Rollback
1. Revert to passlib/bcrypt implementation
2. Maintain backward compatibility code
3. Keep dual-hashing system as safety net

### Monitoring and Alerts
- Monitor authentication success rates
- Track hash migration progress
- Alert on authentication failures
- Monitor performance metrics

## Implementation Timeline

### Week 1: Foundation
- Add argon2-cffi dependency
- Create Argon2 utility module
- Implement basic hashing/verification
- Write initial tests

### Week 2: Integration
- Implement dual-hashing system
- Update authentication flow
- Test backward compatibility
- Performance testing

### Week 3: Migration
- Implement hash migration logic
- Update test data
- Database schema verification
- Integration testing

### Week 4: Validation
- Security testing
- Load testing
- Documentation updates
- Production deployment preparation

## Success Criteria

### Functional Requirements
- [ ] All existing users can authenticate successfully
- [ ] New registrations use Argon2 hashing
- [ ] Hash migration occurs automatically
- [ ] No authentication failures during transition
- [ ] Performance remains acceptable

### Security Requirements
- [ ] Argon2 hashes meet security standards
- [ ] No plaintext password exposure
- [ ] Hash parameters are secure
- [ ] Migration process is secure
- [ ] Backward compatibility maintained

### Quality Requirements
- [ ] 80%+ test coverage for new code
- [ ] All tests pass
- [ ] Code follows project standards
- [ ] Documentation updated
- [ ] Performance benchmarks met

## Risk Assessment

### Low Risk
- Adding new dependency (argon2-cffi is well-maintained)
- Implementing dual-hashing system
- Unit testing new functionality

### Medium Risk
- Database migration of existing hashes
- Performance impact on authentication
- Integration with existing auth flow

### High Risk
- Authentication failures during transition
- Security vulnerabilities in new implementation
- Performance degradation under load

## Mitigation Strategies

### Authentication Failures
- Maintain backward compatibility
- Extensive testing before deployment
- Gradual rollout with monitoring
- Quick rollback capability

### Security Vulnerabilities
- Use well-vetted argon2-cffi library
- Follow security best practices
- Comprehensive security testing
- Code review by security experts

### Performance Issues
- Benchmark performance before deployment
- Adjustable hash parameters
- Monitor performance metrics
- Load testing with realistic scenarios

## Future Considerations

### Long-term Maintenance
- Monitor Argon2 security research
- Update hash parameters as needed
- Consider hardware-specific optimizations
- Plan for next-generation hashing algorithms

### Scalability
- Monitor memory usage patterns
- Consider hash parameter adjustments
- Plan for increased user load
- Evaluate caching strategies

## References

- [Argon2 Specification](https://github.com/P-H-C/phc-winner-argon2/blob/master/argon2/argon2.h)
- [argon2-cffi Documentation](https://argon2-cffi.readthedocs.io/)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Password Hashing Competition](https://password-hashing.net/)

---

*"In the realm of cryptographic defenses, as in the study of eldritch tomes, one must always seek the most current and well-vetted protections against the ever-evolving threats that lurk in the digital shadows."* - Dr. Armitage's notes on modern security practices
