# Argon2 Password Hashing

> 227 nodes

## Key Concepts

- **ContainerServiceError** (49 connections) — `server/services/container_service_helpers.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **AuthenticationError** (37 connections) — `server/exceptions.py`
- **container_service.py** (36 connections) — `server/services/container_service.py`
- **inventory_service.py** (34 connections) — `server/services/inventory_service.py`
- **models/container.py** (32 connections) — `server/models/container.py`
- **container_service_transfer_to.py** (30 connections) — `server/services/container_service_transfer_to.py`
- **container_service_session.py** (29 connections) — `server/services/container_service_session.py`
- **corpse_lifecycle_service.py** (28 connections) — `server/services/corpse_lifecycle_service.py`
- **hash_password()** (26 connections) — `server/auth/argon2_utils.py`
- **container_service_lock.py** (26 connections) — `server/services/container_service_lock.py`
- **container_service_transfer_from.py** (25 connections) — `server/services/container_service_transfer_from.py`
- **container_service_helpers.py** (23 connections) — `server/services/container_service_helpers.py`
- **test_error_logging.py** (23 connections) — `server/tests/unit/utils/test_error_logging.py`
- **ContainerSessionMixin** (21 connections) — `server/services/container_service_session.py`
- **ContainerAccessMixin** (20 connections) — `server/services/container_service_access.py`
- **ContainerNotFoundError** (20 connections) — `server/services/container_service_helpers.py`
- **argon2_utils.py** (20 connections) — `server/auth/argon2_utils.py`
- **auth_utils.py** (17 connections) — `server/auth_utils.py`
- **audit_logger.py** (17 connections) — `server/utils/audit_logger.py`
- **ContainerCapacityError** (16 connections) — `server/services/container_service_helpers.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **container_service_access.py** (16 connections) — `server/services/container_service_access.py`
- **ContainerAccessDeniedError** (15 connections) — `server/services/container_service_helpers.py`
- **ContainerInteractionEvent** (14 connections) — `server/utils/audit_logger.py`
- *... and 202 more nodes in this community*

## Relationships

- [Container API Models](Container_API_Models.md) (73 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (54 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (35 shared connections)
- [Community 104](Community_104.md) (24 shared connections)
- [Community 94](Community_94.md) (23 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (19 shared connections)
- [Community 592](Community_592.md) (16 shared connections)
- [Community 791](Community_791.md) (13 shared connections)
- [Community 80](Community_80.md) (13 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (12 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (10 shared connections)
- [Community 235](Community_235.md) (10 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/exceptions.py`
- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/container_service_access.py`
- `server/services/container_service_helpers.py`
- `server/services/container_service_lock.py`
- `server/services/container_service_session.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/inventory_service.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/audit_logger.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 696 (88%)
- INFERRED: 99 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*