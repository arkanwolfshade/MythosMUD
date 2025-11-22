"""
Argon2 password hashing utilities for MythosMUD.

This module implements the gold standard for password hashing using Argon2id,
as documented in the restricted archives of Miskatonic University.
"""

import os

from argon2 import PasswordHasher, Type, exceptions
from argon2.exceptions import VerificationError

from ..exceptions import AuthenticationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)

# Default Argon2 parameters - optimized for security vs performance
# Can be overridden via environment variables: ARGON2_TIME_COST, ARGON2_MEMORY_COST,
# ARGON2_PARALLELISM, ARGON2_HASH_LENGTH
# TIME_COST: 1-10 range (3 is recommended for web apps, higher = more secure but slower)
# MEMORY_COST: 1024-1048576 KiB range (65536 = 64MB recommended, higher = more secure)
# PARALLELISM: 1-16 range (1 recommended for web servers, higher for dedicated machines)
# HASH_LENGTH: 16-64 bytes range (32 bytes = 256 bits recommended)
TIME_COST = int(os.getenv("ARGON2_TIME_COST", "3"))
MEMORY_COST = int(os.getenv("ARGON2_MEMORY_COST", "65536"))  # 64MB
PARALLELISM = int(os.getenv("ARGON2_PARALLELISM", "1"))
HASH_LENGTH = int(os.getenv("ARGON2_HASH_LENGTH", "32"))  # 256 bits

# Validate parameters are within safe ranges
if TIME_COST < 1 or TIME_COST > 10:
    raise ValueError(f"ARGON2_TIME_COST must be between 1 and 10, got {TIME_COST}")
if MEMORY_COST < 1024 or MEMORY_COST > 1048576:  # 1MB to 1GB
    raise ValueError(f"ARGON2_MEMORY_COST must be between 1024 and 1048576, got {MEMORY_COST}")
if PARALLELISM < 1 or PARALLELISM > 16:
    raise ValueError(f"ARGON2_PARALLELISM must be between 1 and 16, got {PARALLELISM}")
if HASH_LENGTH < 16 or HASH_LENGTH > 64:
    raise ValueError(f"ARGON2_HASH_LENGTH must be between 16 and 64, got {HASH_LENGTH}")

logger.info(
    "Argon2 utilities initialized",
    time_cost=TIME_COST,
    memory_cost=MEMORY_COST,
    parallelism=PARALLELISM,
    hash_length=HASH_LENGTH,
)

# Create default hasher instance with explicit Argon2id variant
_default_hasher = PasswordHasher(
    type=Type.ID,  # Explicitly use Argon2id (hybrid approach, recommended)
    time_cost=TIME_COST,
    memory_cost=MEMORY_COST,
    parallelism=PARALLELISM,
    hash_len=HASH_LENGTH,
)


def create_hasher_with_params(
    time_cost: int = TIME_COST,
    memory_cost: int = MEMORY_COST,
    parallelism: int = PARALLELISM,
    hash_len: int = HASH_LENGTH,
) -> PasswordHasher:
    """Create a PasswordHasher with custom parameters."""
    # Validate parameters are within safe ranges
    if time_cost < 1 or time_cost > 10:
        raise ValueError(f"time_cost must be between 1 and 10, got {time_cost}")
    if memory_cost < 1024 or memory_cost > 1048576:
        raise ValueError(f"memory_cost must be between 1024 and 1048576, got {memory_cost}")
    if parallelism < 1 or parallelism > 16:
        raise ValueError(f"parallelism must be between 1 and 16, got {parallelism}")
    if hash_len < 16 or hash_len > 64:
        raise ValueError(f"hash_len must be between 16 and 64, got {hash_len}")

    # Log warning if parameters are outside recommended ranges
    if time_cost < 3:
        logger.warning("time_cost is below recommended minimum of 3", time_cost=time_cost)
    if memory_cost < 65536:
        logger.warning("memory_cost is below recommended minimum of 65536 (64MB)", memory_cost=memory_cost)

    logger.debug(
        "Creating custom Argon2 hasher",
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=hash_len,
    )

    return PasswordHasher(
        type=Type.ID,  # Explicitly use Argon2id
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=hash_len,
    )


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using Argon2id.

    This function provides superior security compared to bcrypt,
    implementing the gold standard for password hashing as documented
    in the restricted archives of Miskatonic University.

    Args:
        password: Plaintext password. Should be reasonable length (< 1MB)
                  to prevent DoS attacks. Argon2 handles arbitrary input safely.

    Returns:
        Argon2id hash string in format: $argon2id$v=19$m=65536,t=3,p=1$...

    Raises:
        AuthenticationError: If password is not a string or hashing fails
    """
    # Runtime type validation (defensive programming - catches incorrect calls at runtime)
    if not isinstance(password, str):
        logger.error("Password must be a string", password_type=type(password).__name__)  # type: ignore[unreachable]
        raise AuthenticationError("Password must be a string")

    logger.debug("Hashing password with Argon2id")
    try:
        hashed = _default_hasher.hash(password)
        logger.debug("Password hashed successfully")
        assert isinstance(hashed, str)
        return hashed
    except exceptions.HashingError as e:
        logger.error("Argon2 hashing error", error=str(e), error_type=type(e).__name__)
        log_and_raise(
            AuthenticationError,
            f"Failed to hash password: {e}",
            details={"original_error": str(e), "error_type": type(e).__name__},
            user_friendly="Password processing failed",
        )
    except Exception as e:
        logger.error("Unexpected error during password hashing", error=str(e), error_type=type(e).__name__)
        log_and_raise(
            AuthenticationError,
            f"Failed to hash password: {e}",
            details={"original_error": str(e), "error_type": type(e).__name__},
            user_friendly="Password processing failed",
        )


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plaintext password against an Argon2 hash.

    This function verifies passwords using Argon2id hashing.
    All passwords in the system use Argon2 for security.

    Args:
        password: Plaintext password to verify
        hashed: Argon2 hash string to verify against

    Returns:
        True if password matches hash, False otherwise
    """
    # Runtime type validation (defensive programming - catches incorrect calls at runtime)
    if not isinstance(password, str):
        logger.warning("Password verification failed - password not a string", password_type=type(password).__name__)  # type: ignore[unreachable]
        return False

    if not hashed:
        logger.warning("Password verification failed - empty hash")
        return False

    logger.debug("Verifying password")
    try:
        _default_hasher.verify(hashed, password)
        logger.debug("Password verification successful (Argon2)")
        return True
    except (VerificationError, exceptions.InvalidHash) as e:
        logger.warning("Password verification failed - invalid hash", error=str(e))
        return False
    except Exception as e:
        logger.error("Password verification error", error=str(e), error_type=type(e).__name__)
        return False


def is_argon2_hash(hash_value: str | None) -> bool:
    """Check if a given string is an Argon2 hash."""
    if not isinstance(hash_value, str):
        logger.debug("Hash check failed - not a string", hash_type=type(hash_value))
        return False

    is_argon2 = hash_value.startswith("$argon2")
    logger.debug("Hash type check", is_argon2=is_argon2)
    return is_argon2


def needs_rehash(hashed: str) -> bool:
    """Check if a hash needs to be rehashed due to parameter changes."""
    if not is_argon2_hash(hashed):
        return True

    try:
        result = _default_hasher.check_needs_rehash(hashed)
        assert isinstance(result, bool)
        return result
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error checking password rehash needs", error=str(e), error_type=type(e).__name__)
        return True


def get_hash_info(hashed: str | None) -> dict[str, str | int] | None:
    """Extract parameters from an Argon2 hash string."""
    if not is_argon2_hash(hashed):
        return None

    try:
        # Parse the hash format: $argon2id$v=19$m=65536,t=3,p=1$salt$hash
        assert hashed is not None
        parts = hashed.split("$")
        if len(parts) < 5:
            return None

        # Extract parameters from the format string
        params_str = parts[3]  # m=65536,t=3,p=1
        params: dict[str, str | int] = {}
        for param in params_str.split(","):
            if "=" in param:
                key, value = param.split("=", 1)
                try:
                    params[key] = int(value)
                except ValueError:
                    params[key] = value

        return params
    except (ValueError, TypeError, AttributeError) as e:
        logger.error("Error extracting hash parameters", error=str(e), error_type=type(e).__name__)
        return None
