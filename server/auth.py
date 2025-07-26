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
from server.security_utils import ensure_directory_exists

router = APIRouter(prefix="/auth", tags=["auth"])

# Use secure path construction for auth files
SERVER_DIR = ensure_directory_exists(os.path.dirname(__file__))
USERS_FILE = os.path.join(SERVER_DIR, "users.json")
INVITES_FILE = os.path.join(SERVER_DIR, "invites.json")


def get_users_file() -> str:
    """Get the secure path to the users file."""
    return USERS_FILE


def get_invites_file() -> str:
    """Get the secure path to the invites file."""
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
    # Use PersistenceLayer for player lookup
    persistence = request.app.state.persistence
    if persistence.get_player_by_name(req.username):
        raise HTTPException(status_code=409, detail="Username already exists")
    # TODO: Migrate invites and users to PersistenceLayer
    # Load invites
    try:
        with open(invites_file, "r", encoding="utf-8") as f:
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
        with open(users_file, "r", encoding="utf-8") as f:
            users = json.load(f)
    except Exception:
        users = []
    if any(u["username"] == req.username for u in users):
        raise HTTPException(status_code=409, detail="Username already exists.")
    password_hash = hash_password(req.password)
    user = {
        "username": req.username,
        "password_hash": password_hash,
        "invite_code": req.invite_code,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    users.append(user)
    with open(users_file, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)
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
