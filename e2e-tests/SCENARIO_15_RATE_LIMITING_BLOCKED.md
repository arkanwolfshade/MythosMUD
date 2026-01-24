# Scenario 15: Whisper Rate Limiting - BLOCKED

**Status:** ❌ BLOCKED - Missing Feature Implementation

**Date Discovered:** 2025-10-29

**Investigation Phase:** Extended Validation (Phase 2)

---

## Executive Summary

Scenario 15 (Whisper Rate Limiting) has been blocked due to the discovery that **per-recipient rate limiting is not
implemented** in the current whisper system. While the global whisper rate limit (5 messages per minute) is functioning
correctly, the per-recipient rate limit (3 whispers per minute to the same player) specified in the scenario
documentation does not exist in the codebase.

---

## What Was Tested

### Test Setup

**Players:** ArkanWolfshade (AW) and Ithaqua

**Location:** Both in `earth_arkhamcity_sanitarium_room_foyer_001`

**Test Method:** Rapid message sending to trigger rate limits

**Testing Tool:** Playwright MCP (multi-tab interaction)

### Test Execution

**Messages Sent (Within 8 Seconds):**

1. `09:19:28` - "Rate limit message 1" ✅ SUCCESS
2. `09:19:30` - "Rate limit message 2" ✅ SUCCESS (2 seconds after #1)
3. `09:19:33` - "Rate limit message 3" ✅ SUCCESS (5 seconds after #1)
4. `09:19:36` - "Rate limit message 4" ✅ SUCCESS (8 seconds after #1)

**Expected Behavior (Per Scenario):**

- Messages 1-3 should succeed

- Message 4 should be BLOCKED with error: `"Rate limit exceeded. You can only send 3 whispers per minute to the same

  player."`

**Actual Behavior:**

- All 4 messages succeeded
- No rate limit error was triggered
- Messages were delivered successfully to Ithaqua

---

## Root Cause Analysis

### Investigation Process

1. **Client-Side Verification:** Confirmed all 4 messages appeared in chat log
2. **Server Log Analysis:** Found rate limiter tracking global whisper count only
3. **Code Review:** Examined `ChatService.send_whisper_message()` and `RateLimiter` implementation
4. **Configuration Review:** Verified rate limit settings in `server/config/models.py`

### Findings

#### ✅ What IS Implemented

**Global Whisper Rate Limit:**

**Location:** `server/config/models.py:313`

**Configuration:** `rate_limit_whisper: int = Field(default=5, description="Whisper channel rate limit")`

**Implementation:** `server/services/rate_limiter.py:110-163`

**Behavior:** Tracks total whispers sent by a player across ALL recipients

**Limit:** 5 whispers per minute (global)

- **Status:** ✅ WORKING CORRECTLY

**Evidence from Logs:**

```log
2025-10-29 08:19:31 - communications.rate_limiter - DEBUG
player_id=UUID('83f3c6af-dd8b-4d53-ad26-30e4167c756d')
player_name='ArkanWolfshade'
channel='whisper'
current_count=1
limit=5
event='Message recorded for rate limiting'
```

The logs show `limit=5`, confirming the global rate limit is active.

#### ❌ What IS NOT Implemented

**Per-Recipient Whisper Rate Limit:**

**Expected Behavior:** 3 whispers per minute to the same player

**Current Implementation:** **DOES NOT EXIST**

**Missing Logic:** No tracking of whisper counts per individual recipient

**Impact:** Players can send up to 5 whispers to a SINGLE recipient

**Expected Data Structure (Not Found):**

```python
# Expected: Track whispers per target player

self.whisper_windows: dict[str, dict[str, deque]] = {}
# Format: {sender_id: {target_id: deque(timestamps)}}

```

**Current Data Structure:**

```python
# Current: Only tracks global whisper count

self.windows: dict[str, dict[str, deque]] = {}
# Format: {player_id: {channel: deque(timestamps)}}

```

---

## Scenario Documentation vs. Implementation

### Scenario 15 Requirements (Line 26)

```text
- **Rate Limit Settings**: 5 whispers per minute per player, 3 whispers per minute per recipient
```

### Current Implementation

| Rate Limit Type     | Required | Implemented     | Status    |
| ------------------- | -------- | --------------- | --------- |
| Global (per player) | 5/min    | 5/min           | ✅ WORKING |
| Per-recipient       | 3/min    | NOT IMPLEMENTED | ❌ MISSING |

---

## Impact Assessment

### Scenario 15 Test Steps Affected

| Step       | Description                               | Can Execute | Status      |
| ---------- | ----------------------------------------- | ----------- | ----------- |
| Step 1     | Both Players in Same Room                 | ✅ Yes       | COMPLETE    |
| Step 2     | Test Normal Whisper Rate                  | ✅ Yes       | COMPLETE    |
| Step 3     | Test Multiple Whispers Within Rate Limit  | ✅ Yes       | COMPLETE    |
| **Step 4** | **Test Rate Limit Exceeded**              | ❌ **NO**    | **BLOCKED** |
| Step 5     | Test Whisper to Different Player          | ⚠️ Partial   | BLOCKED     |
| Step 6     | Test Ithaqua's Rate Limit                 | ⚠️ Partial   | BLOCKED     |
| Step 7     | Test Rate Limit Reset                     | ⚠️ Partial   | BLOCKED     |
| Step 8     | Test Rate Limit Per Player                | ✅ Yes       | CAN EXECUTE |
| Step 9     | Test Rate Limit Error Messages            | ❌ NO        | BLOCKED     |
| Step 10    | Test System Stability After Rate Limiting | ⚠️ Partial   | BLOCKED     |

### Success Criteria Checklist

[x] Normal whisper rate works correctly

- [x] Multiple whispers within rate limit work correctly
- [ ] **Rate limit is enforced when exceeded** (BLOCKED - per-recipient limit missing)
- [ ] **Rate limit is per recipient, not global** (BLOCKED - not implemented)
- [ ] Rate limiting works for both players (PARTIAL - only global limit)
- [ ] Rate limit resets after time period (CAN TEST - for global limit only)
- [x] Global rate limit is enforced per player
- [ ] **Rate limit error messages are clear and informative** (BLOCKED)
- [ ] System remains stable after rate limiting (PARTIAL)
- [ ] Spam prevention is effective (PARTIAL - only prevents global spam)

**Overall:** **4/10 success criteria met**, **6/10 blocked or partial**

---

## Technical Requirements for Implementation

### Required Changes

#### 1. Rate Limiter Enhancement

**File:** `server/services/rate_limiter.py`

**New Data Structure:**

```python
class RateLimiter:
    def __init__(self):
        # ... existing code ...

        # NEW: Per-recipient whisper tracking

        self.whisper_recipient_windows: dict[str, dict[str, deque]] = defaultdict(
            lambda: defaultdict(deque)
        )
        # Format: {sender_id: {target_id: deque(timestamps)}}

        # NEW: Per-recipient whisper limit (default 3/min)

        self.whisper_recipient_limit = 3
```

**New Method:**

```python
def check_whisper_recipient_limit(
    self,
    sender_id: str,
    target_id: str,
    sender_name: str = None
) -> bool:
    """
    Check if a player is within rate limits for whispers to a specific recipient.

    Args:
        sender_id: ID of player sending whisper
        target_id: ID of player receiving whisper
        sender_name: Sender name for logging

    Returns:
        True if within limits, False if rate limited
    """
    # Implementation needed

```

#### 2. Chat Service Integration

**File:** `server/game/chat_service.py`

**Modified Method (Line 725-776):**

```python
async def send_whisper_message(
    self, sender_id: str, target_id: str, message: str
) -> dict[str, Any]:
    # ... existing validation code ...

    # Check GLOBAL rate limiting (existing)

    if not self.rate_limiter.check_rate_limit(sender_id, "whisper", sender_name):
        return {
            "success": False,
            "error": "Rate limit exceeded. You can only send 5 whispers per minute."
        }

    # NEW: Check PER-RECIPIENT rate limiting

    if not self.rate_limiter.check_whisper_recipient_limit(
        sender_id, target_id, sender_name
    ):
        target_name = getattr(target_obj, "name", "UnknownPlayer")
        return {
            "success": False,
            "error": f"Rate limit exceeded. You can only send 3 whispers per minute to the same player."
        }

    # ... rest of existing code ...

    # Record for BOTH rate limits

    self.rate_limiter.record_message(sender_id, "whisper", sender_name)
    # NEW:

    self.rate_limiter.record_whisper_recipient(sender_id, target_id, sender_name)
```

#### 3. Configuration Enhancement

**File:** `server/config/models.py`

**Add New Configuration:**

```python
class ChatConfig(BaseSettings):
    # ... existing fields ...

    rate_limit_whisper: int = Field(default=5, description="Global whisper rate limit")
    # NEW:

    rate_limit_whisper_per_recipient: int = Field(
        default=3,
        description="Whisper rate limit per recipient"
    )
```

---

## Testing Impact

### What Can Be Tested

1. **Global Rate Limit (Step 8):** Can test that 6th whisper triggers global limit
2. **Rate Limit Reset (Step 7):** Can test global limit reset after 60 seconds
3. **System Stability (Step 10):** Can partially test with global limit only

### What Cannot Be Tested

1. **Per-Recipient Limit (Steps 4-6, 9):** Core scenario functionality is blocked
2. **Error Message Differentiation:** Can't verify per-recipient error messages
3. **Multi-Recipient Behavior:** Can't verify rate limits work independently per recipient

---

## Recommendations

### Immediate Actions

1. **Document as Known Limitation:** ✅ THIS DOCUMENT
2. **Update Investigation Report:** Add finding to whisper system investigation
3. **Create GitHub Issue:** Track per-recipient rate limiting as feature request
4. **Mark Scenario 15 as BLOCKED:** Update scenario status

### Implementation Priority

**Priority:** 🟡 MEDIUM-HIGH

**Rationale:**

**Security Concern:** Without per-recipient limiting, harassment is easier

**User Experience:** Spam prevention is only partially effective

**Scenario Coverage:** Blocks complete E2E testing of whisper system

**Not Critical:** Global limit provides basic spam prevention

### Suggested Implementation Approach

1. **Phase 1: Rate Limiter Enhancement (2-3 hours)**

   - Add per-recipient tracking data structure
   - Implement `check_whisper_recipient_limit()` method
   - Implement `record_whisper_recipient()` method
   - Add unit tests for new methods

2. **Phase 2: Chat Service Integration (1-2 hours)**

   - Modify `send_whisper_message()` to check both limits
   - Implement differentiated error messages
   - Update existing tests

3. **Phase 3: Configuration (30 minutes)**

   - Add `rate_limit_whisper_per_recipient` to config
   - Update documentation
   - Add configuration validation

4. **Phase 4: Testing (2-3 hours)**

   - Write unit tests for per-recipient limiting
   - Update integration tests
   - Execute Scenario 15 to verify implementation

**Total Estimated Effort:** 6-8 hours

---

## Related Documentation

**Main Investigation Report:** `e2e-tests/WHISPER_SYSTEM_INVESTIGATION_REPORT.md`

**Remaining Work Summary:** `e2e-tests/REMAINING_WORK_SUMMARY.md`

**NATS Subject Patterns:** `docs/NATS_SUBJECT_PATTERNS.md`

**Rate Limiter Implementation:** `server/services/rate_limiter.py`

**Chat Service Implementation:** `server/game/chat_service.py`

- **Chat Configuration:** `server/config/models.py`

---

## Test Evidence

### Messages Sent Successfully (Should Have Triggered Rate Limit)

```text
09:19:28 - You whisper to Ithaqua: Rate limit message 1
09:19:30 - You whisper to Ithaqua: Rate limit message 2
09:19:33 - You whisper to Ithaqua: Rate limit message 3
09:19:36 - You whisper to Ithaqua: Rate limit message 4  ← SHOULD HAVE BEEN BLOCKED
```

### Server Logs

```log
player_id=UUID('83f3c6af-dd8b-4d53-ad26-30e4167c756d')
player_name='ArkanWolfshade'
channel='whisper'
current_count=1
limit=5  ← Global limit, not per-recipient limit
```

---

## Next Steps

1. ✅ Close browser tabs and cleanup test environment
2. ✅ Document finding in main investigation report
3. ✅ Update remaining work summary
4. 📋 Create GitHub Issue for per-recipient rate limiting implementation
5. 📋 Continue with Scenario 16 (Whisper Movement) - not affected by this limitation
6. 📋 Return to Scenario 15 after per-recipient rate limiting is implemented

---

**Document Version:** 1.0

**Last Updated:** 2025-10-29 09:20 PST

**Investigation Lead:** Untenured Professor of Occult Studies, Miskatonic University

**Status:** INVESTIGATION COMPLETE - FEATURE IMPLEMENTATION REQUIRED
