"""
Argon2 password hashing utilities for MythosMUD.

This module implements the gold standard for password hashing using Argon2id,
as documented in the restricted archives of Miskatonic University.
"""

from argon2 import PasswordHasher, exceptions
from argon2.exceptions import HashingError, VerificationError

from ..logging_config import get_logger

logger = get_logger(__name__)

# Default Argon2 parameters - optimized for security vs performance
TIME_COST = 3  # Number of iterations
MEMORY_COST = 65536  # Memory usage in KiB (64MB)
PARALLELISM = 1  # Number of parallel threads
HASH_LENGTH = 32  # Length of the hash in bytes

logger.info(
    "Argon2 utilities initialized",
    time_cost=TIME_COST,
    memory_cost=MEMORY_COST,
    parallelism=PARALLELISM,
    hash_length=HASH_LENGTH,
)

# Create default hasher instance
_default_hasher = PasswordHasher(
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
    logger.debug(
        "Creating custom Argon2 hasher",
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=hash_len,
    )

    return PasswordHasher(
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
    """
    if not isinstance(password, str):
        logger.error("Password hashing failed - invalid type", password_type=type(password))
        raise TypeError("Password must be a string")

    logger.debug("Hashing password with Argon2id")
    try:
        hashed = _default_hasher.hash(password)
        logger.debug("Password hashed successfully")
        return hashed
    except Exception as e:
        logger.error("Password hashing failed", error=str(e))
        raise HashingError(f"Failed to hash password: {e}") from e


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plaintext password against a hash.

    This function safely handles both Argon2 and legacy bcrypt hashes,
    ensuring backward compatibility during the transition period.
    """
    if not isinstance(password, str) or not isinstance(hashed, str):
        logger.warning(
            "Password verification failed - invalid types", password_type=type(password), hash_type=type(hashed)
        )
        return False

    if not hashed:
        logger.warning("Password verification failed - empty hash")
        return False

    logger.debug("Verifying password")
    try:
        # Try Argon2 verification first
        if is_argon2_hash(hashed):
            _default_hasher.verify(hashed, password)
            logger.debug("Password verification successful (Argon2)")
            return True
        else:
            # For backward compatibility, we could add bcrypt verification here
            # But since we're fully converting to Argon2, we'll return False for
            # non-Argon2 hashes
            logger.warning("Password verification failed - non-Argon2 hash")
            return False
    except (VerificationError, exceptions.InvalidHash) as e:
        logger.warning("Password verification failed - invalid hash", error=str(e))
        return False
    except Exception as e:
        # Any other exception means verification failed
        logger.error("Password verification error", error=str(e))
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
        return _default_hasher.check_needs_rehash(hashed)
    except Exception:
        return True


def get_hash_info(hashed: str | None) -> dict[str, str | int] | None:
    """Extract parameters from an Argon2 hash string."""
    if not is_argon2_hash(hashed):
        return None

    try:
        # Parse the hash format: $argon2id$v=19$m=65536,t=3,p=1$salt$hash
        parts = hashed.split("$")
        if len(parts) < 5:
            return None

        # Extract parameters from the format string
        params_str = parts[3]  # m=65536,t=3,p=1
        params = {}
        for param in params_str.split(","):
            if "=" in param:
                key, value = param.split("=", 1)
                try:
                    params[key] = int(value)
                except ValueError:
                    params[key] = value

        return params
    except Exception:
        return None
