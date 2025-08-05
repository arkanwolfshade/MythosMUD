import os
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

# Import our Argon2 implementation
from server.auth.argon2_utils import hash_password as argon2_hash_password
from server.auth.argon2_utils import verify_password as argon2_verify_password

# Use environment variable for secret key - CRITICAL: Must be set in production
SECRET_KEY = os.getenv("MYTHOSMUD_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError(
        "MYTHOSMUD_SECRET_KEY environment variable must be set. Generate a secure random key for production deployment."
    )
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using Argon2id.

    This function provides superior security compared to bcrypt,
    implementing the gold standard for password hashing as documented
    in the restricted archives of Miskatonic University.
    """
    return argon2_hash_password(password)


def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify a plaintext password against a hash.

    This function safely handles both Argon2 and legacy bcrypt hashes,
    ensuring backward compatibility during the transition period.
    """
    return argon2_verify_password(password, password_hash)


def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None,
    secret_key: str = SECRET_KEY,
    algorithm: str = ALGORITHM,
) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)


def decode_access_token(token: str, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM) -> dict:
    if token is None:
        return None
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm], audience="fastapi-users:auth")
        return payload
    except JWTError:
        return None
