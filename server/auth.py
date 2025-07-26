from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import json
import os
from datetime import datetime, timedelta
from auth_utils import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token,
)
from security_utils import ensure_directory_exists, validate_secure_path

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


def load_json_file_safely(file_path: str, default: list = None) -> list:
    """
    Safely load a JSON file with proper error handling.

    Args:
        file_path: The path to the JSON file
        default: Default value to return if file cannot be loaded

    Returns:
        The loaded JSON data or default value
    """
    if default is None:
        default = []

    try:
        # Validate the file path is within our secure directory
        validate_secure_path(SERVER_DIR, os.path.relpath(file_path, SERVER_DIR))

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return default
    except Exception as e:
        # Log the error in production, but don't expose it to users
        print(f"Warning: Could not load {file_path}: {e}")
        return default


def save_json_file_safely(file_path: str, data: list) -> bool:
    """
    Safely save data to a JSON file with proper error handling.

    Args:
        file_path: The path to save the JSON file
        data: The data to save

    Returns:
        True if successful, False otherwise
    """
    try:
        # Validate the file path is within our secure directory
        validate_secure_path(SERVER_DIR, os.path.relpath(file_path, SERVER_DIR))

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        # Log the error in production, but don't expose it to users
        print(f"Warning: Could not save {file_path}: {e}")
        return False


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
        invites = load_json_file_safely(invites_file)
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
        users = load_json_file_safely(users_file)
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
    save_json_file_safely(users_file, users)
    for i in invites:
        if i["code"] == req.invite_code:
            i["used"] = True
    save_json_file_safely(invites_file, invites)
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
        users = load_json_file_safely(users_file)
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
        users = load_json_file_safely(users_file)
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
