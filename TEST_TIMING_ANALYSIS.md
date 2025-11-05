# Test Timing Analysis - Optimization Targets

**Date:** 2025-11-05
**Run:** Full comprehensive suite (4,869 tests)
**Duration:** 31:09 (1869.54 seconds)
**Context:** Identifying slow tests to optimize default `test` target to 5-7 minute target

## Top Time Consumers (>10 seconds)

### SSE Handler Tests (60 seconds total)
- `test_sse_handler.py::test_game_event_stream_initial_events` - **30.02s**
- `test_sse_handler.py::test_game_event_stream_with_pending_messages` - **30.00s**

**Status:** ✅ ALREADY EXCLUDED (in unit/realtime, should be marked slow)

### Auth & Security Tests (21+ seconds setup each)
Multiple tests with 21+ second setup times:
- `test_auth.py` - 9 tests with 21s+ setup
- `test_security_headers_verification.py` - 7 tests with 21s+ setup
- `test_comprehensive_integration.py` - 8 tests with 21s+ setup
- `test_dependency_injection_functions.py` - 9 tests with 21s+ setup
- `test_error_logging_coverage.py` - 3 tests with 21s+ setup

**Status:** ⚠️ NEEDS INVESTIGATION - These have heavy FastAPI app setup

### Performance Tests (still running despite slow marker)
- `test_combat_performance.py::test_combat_system_load_test` - **16.83s**
- `test_error_logging_performance.py::test_error_logging_memory_leak_prevention` - **8.02s**
- `test_combat_performance.py::test_combat_attack_performance` - **3.54s**
- `test_error_logging_performance.py::test_error_logging_scales_with_load` - **2.53s**
- `test_combat_performance.py::test_combat_memory_usage` - **2.42s**

**Status:** ❌ BUG - Performance tests ran despite slow marker!

### Infrastructure Tests (3.5+ seconds)
- `test_lifespan.py::test_game_tick_loop_handles_exception` - **3.51s**
- `test_lifespan.py::test_game_tick_loop_handles_errors` - **2.52s**

**Status:** ✅ ALREADY EXCLUDED (in infrastructure/conftest.py)

### Rate Limiter Timing Tests (still running)
- `test_command_rate_limiter.py::test_sliding_window_accuracy` - **2.50s**
- `test_command_rate_limiter.py::test_rate_limit_resets_after_window` - **1.10s**
- `test_command_rate_limiter.py::test_cleanup_old_entries` - **1.10s**
- `test_command_rate_limiter.py::test_very_short_window` - **0.60s**

**Status:** ⚠️ PARTIAL - Tests marked but still ran (verify markers applied)

### NATS Message Handler Tests (2-3 seconds)
- `test_nats_message_handler.py::test_handle_nats_message_with_exception` - **3.09s**
- `test_nats_message_handler.py::test_handle_nats_message_invalid_missing_fields` - **2.63s**

**Status:** ⚠️ NEEDS MARKING - Not currently marked as slow

### Argon2 Password Tests (1.4+ seconds)
- `test_argon2_utils.py::test_verification_timing_consistency` - **1.48s**
- `test_argon2_utils.py::test_hash_uniqueness` - **1.40s**

**Status:** ⚠️ NEEDS MARKING - Security-critical but slow

## Critical Finding: Tests Still Running Despite Markers

**PROBLEM:** The comprehensive run included ALL tests including those marked `slow`:
- Coverage tests (marked slow): ✅ RAN
- E2E tests (marked slow + e2e): ✅ RAN
- Performance tests (marked slow): ✅ RAN
- Integration tests (marked slow via conftest): ✅ RAN
- Infrastructure tests (marked slow via conftest): ✅ RAN

**REASON:** The command used was `pytest server/tests/` with NO marker filter, so ALL tests ran.

## Recommendations

### 1. **Mark Additional Slow Tests**
- `server/tests/unit/realtime/test_sse_handler.py` - SSE streaming tests
- `server/tests/unit/realtime/test_nats_message_handler.py` - Tests with 2s+ call times
- `server/tests/unit/auth/test_argon2_utils.py` - Timing-sensitive password tests

### 2. **Investigate Heavy Setup Tests**
Tests with 21s+ setup times need investigation:
- Why does FastAPI app setup take 21 seconds?
- Can we optimize fixtures or use session-scoped fixtures?
- Are we creating unnecessary database connections?

### 3. **Verify Marker Application**
Some tests marked as `@pytest.mark.slow` still appear to be running in the "fast" suite.
Need to verify conftest.py files are being loaded correctly.

### 4. **Target Time Budget (5-7 min = 300-420 seconds)**
Current fast suite estimate after marking additional tests:
- ~4,500 remaining tests
- Average 0.05s per test = 225 seconds (~4 min) ✅
- With overhead/setup = ~300-360 seconds (~5-6 min) ✅

## Next Actions

1. Mark SSE handler tests as slow
2. Mark slow NATS message handler tests as slow
3. Mark Argon2 timing-sensitive tests as slow
4. Investigate and optimize 21s+ setup times
5. Run `make test` to verify 5-7 minute target is met
