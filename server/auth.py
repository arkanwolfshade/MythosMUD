from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import json
import os
from datetime import datetime, timedelta
from server.auth_utils import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)

router = APIRouter(prefix="/auth", tags=["auth"])

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
INVITES_FILE = os.path.join(os.path.dirname(__file__), "invites.json")


def get_users_file() -> str:
    return USERS_FILE


def get_invites_file() -> str:
    return INVITES_FILE


class RegisterRequest(BaseModel):
    username: str
    password: str
    invite_code: str


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(
    req: RegisterRequest,
    request: Request,
    users_file: str = Depends(get_users_file),
    invites_file: str = Depends(get_invites_file),
):
    player_manager = request.app.state.player_manager
    if player_manager.get_player_by_name(req.username):
        raise HTTPException(status_code=409, detail="Username already exists")
    # Load invites
    try:
        # Validate the invites_file path
        base_path = os.path.realpath(os.path.dirname(INVITES_FILE))
        normalized_path = os.path.realpath(invites_file)
        if not normalized_path.startswith(base_path):
            normalized_path = INVITES_FILE  # Fallback to default

        with open(normalized_path, "r", encoding="utf-8") as f:
            invites = json.load(f)
    except Exception:
        invites = []

    invite = next(
        (
            i
            for i in invites
            if i["code"] == req.invite_code and not i.get("used", False)
        ),
        None,
    )
    if not invite:
        raise HTTPException(
            status_code=400, detail="Invite code is invalid or already used."
        )

    # Load users
    try:
        # Validate the users_file path
        base_path = os.path.realpath(os.path.dirname(USERS_FILE))
        normalized_path = os.path.realpath(users_file)
        if not normalized_path.startswith(base_path):
            normalized_path = USERS_FILE  # Fallback to default

        with open(normalized_path, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        users = []

    # Check for duplicate username before creating player
    if any(u["username"] == req.username for u in users):
        raise HTTPException(status_code=409, detail="Username already exists.")

    # Hash password
    password_hash = hash_password(req.password)

    # Create user object
    user = {
        "username": req.username,
        "password_hash": password_hash,
        "invite_code": req.invite_code,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    users.append(user)

    # Save users
    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

    # Mark invite as used
    for i in invites:
        if i["code"] == req.invite_code:
            i["used"] = True
    with open(invites_file, "w", encoding="utf-8") as f:
        json.dump(invites, f, indent=2)

    return {"message": "Registration successful. You may now log in."}


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login_user(
    req: LoginRequest,
    users_file: str = Depends(get_users_file),
):
    # Load users
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        users = []

    user = next((u for u in users if u["username"] == req.username), None)
    if not user or not verify_password(req.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}


bearer_scheme = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    users_file: str = Depends(get_users_file),
) -> dict:
    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")
    username = payload["sub"]
    # Load users
    try:
        with open(users_file, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        users = []
    user = next((u for u in users if u["username"] == username), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    # Exclude password_hash from response
    user_info = {k: v for k, v in user.items() if k != "password_hash"}
    return user_info


@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return current_user
