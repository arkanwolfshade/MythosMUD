"""Custom JWT strategy that invalidates tokens after server restart.

Tokens must include the current auth epoch (srv claim). Tokens issued
before the current server process started are rejected.
"""

from typing import Any

import jwt
from fastapi_users import exceptions, models
from fastapi_users.authentication.strategy.jwt import JWTStrategy
from fastapi_users.jwt import decode_jwt
from fastapi_users.manager import BaseUserManager

from .token_epoch import get_auth_epoch


class RestartInvalidatingJWTStrategy(JWTStrategy[models.UP, models.ID]):
    """JWT strategy that rejects tokens issued before the current server start."""

    async def read_token(
        self, token: str | None, user_manager: BaseUserManager[models.UP, models.ID]
    ) -> models.UP | None:
        """Reads a JWT token, validating its signature, audience, and server epoch. """
        self, token: str | None, user_manager: BaseUserManager[models.UP, models.ID]
    ) -> models.UP | None:
        if token is None:
            return None

        try:
            data: dict[str, Any] = decode_jwt(token, self.decode_key, self.token_audience, algorithms=[self.algorithm])
        except jwt.PyJWTError:
            return None

        # Reject tokens from before this server restart
        if data.get("srv") != get_auth_epoch():
            return None

        user_id = data.get("sub")
        if user_id is None:
            return None

        try:
            parsed_id = user_manager.parse_id(user_id)
            return await user_manager.get(parsed_id)
        except (exceptions.UserNotExists, exceptions.InvalidID):
            return None
