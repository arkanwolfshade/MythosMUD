# Services Rescue Service

> 12 nodes

## Key Concepts

- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_returns_false_on_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_runtime_error()** (3 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Verify a plaintext password against a hash.      This function safely handles** (1 connections) — `server/auth_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test that verify_password returns False on error.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verify_password handles AttributeError and returns False.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test verify_password handles RuntimeError and returns False.** (1 connections) — `server/tests/unit/auth/test_auth_utils.py`

## Relationships

- [Auth Token Utilities](Auth_Token_Utilities.md) (6 shared connections)
- [Combat Disconnect Bug](Combat_Disconnect_Bug.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*