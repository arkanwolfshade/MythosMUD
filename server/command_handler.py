import re

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel

from .auth import get_current_user

router = APIRouter(prefix="/command", tags=["command"])


class CommandRequest(BaseModel):
    command: str


# Patterns to reject for command injection (expand as needed)
INJECTION_PATTERNS = [
    r"[;|&]",  # shell metacharacters
    r"\b(or|and)\b.*=",  # SQL injection
    r"__import__|eval|exec|system|os\.",  # Python injection
    r"%[a-zA-Z]",  # format string
]


def is_suspicious_input(command: str) -> bool:
    for pat in INJECTION_PATTERNS:
        if re.search(pat, command, re.IGNORECASE):
            return True
    return False


def clean_command_input(command: str) -> str:
    # Collapse multiple spaces, strip
    return re.sub(r"\s+", " ", command).strip()


MAX_COMMAND_LENGTH = 50


@router.post("/", status_code=status.HTTP_200_OK)
def handle_command(
    req: CommandRequest,
    current_user: dict = Depends(get_current_user),
    request: Request = None,
):
    command_line = req.command
    if len(command_line) > MAX_COMMAND_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Command too long (max {MAX_COMMAND_LENGTH} characters)",
        )
    if is_suspicious_input(command_line):
        raise HTTPException(status_code=400, detail="Invalid characters or suspicious input detected")
    command_line = clean_command_input(command_line)
    if not command_line:
        return {"result": ""}
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    app = request.app if request else None
    persistence = app.state.persistence if app else None
    if cmd == "look":
        if not persistence:
            return {"result": "You see nothing special."}
        player = persistence.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You see nothing special."}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You see nothing special."}
        if args:
            direction = args[0].lower()
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = persistence.get_room(target_room_id)
                if target_room:
                    name = target_room.get("name", "")
                    desc = target_room.get("description", "You see nothing special.")
                    return {"result": f"{name}\n{desc}"}
            return {"result": "You see nothing special that way."}
        name = room.get("name", "")
        desc = room.get("description", "You see nothing special.")
        exits = room.get("exits", {})
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "go":
        if not persistence:
            return {"result": "You can't go that way"}
        if not args:
            return {"result": "Go where? Usage: go <direction>"}
        direction = args[0].lower()
        player = persistence.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You can't go that way"}
        room_id = player.current_room_id
        room = persistence.get_room(room_id)
        if not room:
            return {"result": "You can't go that way"}
        exits = room.get("exits", {})
        target_room_id = exits.get(direction)
        if not target_room_id:
            return {"result": "You can't go that way"}
        target_room = persistence.get_room(target_room_id)
        if not target_room:
            return {"result": "You can't go that way"}
        # Move the player: update and persist current_room_id
        player.current_room_id = target_room_id
        persistence.save_player(player)
        current_user["current_room_id"] = target_room_id
        name = target_room.get("name", "")
        desc = target_room.get("description", "You see nothing special.")
        exits = target_room.get("exits", {})
        # Only include exits that have valid room IDs (not null)
        valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
        exit_list = ", ".join(valid_exits) if valid_exits else "none"
        return {"result": f"{name}\n{desc}\n\nExits: {exit_list}"}
    elif cmd == "say":
        message = " ".join(args).strip()
        if not message:
            return {"result": "You open your mouth, but no words come out"}
        return {"result": f"You say: {message}"}
    else:
        return {"result": f"Unknown command: {cmd}"}
