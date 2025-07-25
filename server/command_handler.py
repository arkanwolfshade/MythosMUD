from fastapi import APIRouter, Depends, HTTPException, status, Request
from pydantic import BaseModel
from server.auth import get_current_user
import re


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
        raise HTTPException(
            status_code=400, detail="Invalid characters or suspicious input detected"
        )
    command_line = clean_command_input(command_line)
    if not command_line:
        return {"result": ""}
    parts = command_line.split()
    cmd = parts[0].lower()
    args = parts[1:]

    app = request.app if request else None
    if cmd == "look":
        if not app or not hasattr(app.state, "rooms") or not hasattr(app.state, "player_manager"):
            return {"result": "You see nothing special."}
        player_manager = app.state.player_manager
        player = player_manager.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You see nothing special."}
        room_id = player.current_room_id
        room = app.state.rooms.get(room_id)
        if not room:
            return {"result": "You see nothing special."}
        if args:
            direction = args[0].lower()
            exits = room.get("exits", {})
            target_room_id = exits.get(direction)
            if target_room_id:
                target_room = app.state.rooms.get(target_room_id)
                if target_room:
                    name = target_room.get("name", "")
                    desc = target_room.get("description", "You see nothing special.")
                    return {"result": f"{name}\n{desc}"}
            return {"result": "You see nothing special that way."}
        desc = room.get("description", "You see nothing special.")
        name = room.get("name", "")
        exits = room.get("exits", {})
        exits_list = [d for d, v in exits.items() if v]
        exits_str = (
            f"Exits: {', '.join(exits_list)}" if exits_list else "No obvious exits."
        )
        return {"result": f"{name}\n{desc}\n{exits_str}"}
    elif cmd == "go":
        if (
            not app
            or not hasattr(app.state, "rooms")
            or not hasattr(app.state, "player_manager")
        ):
            return {"result": "You can't go that way"}
        if not args:
            return {"result": "Go where? Usage: go <direction>"}
        direction = args[0].lower()
        player_manager = app.state.player_manager
        player = player_manager.get_player_by_name(current_user["username"])
        if not player:
            return {"result": "You can't go that way"}
        room_id = player.current_room_id
        room = app.state.rooms.get(room_id)
        if not room:
            return {"result": "You can't go that way"}
        exits = room.get("exits", {})
        target_room_id = exits.get(direction)
        if not target_room_id:
            return {"result": "You can't go that way"}
        target_room = app.state.rooms.get(target_room_id)
        if not target_room:
            return {"result": "You can't go that way"}
        # Move the player: update and persist current_room_id
        player.current_room_id = target_room_id
        player_manager.update_player(player)
        # Update current_user for this request (not persistent for JWT, but for immediate look)
        current_user["current_room_id"] = target_room_id
        name = target_room.get("name", "")
        desc = target_room.get("description", "You see nothing special.")
        exits = target_room.get("exits", {})
        exits_list = [d for d, v in exits.items() if v]
        exits_str = (
            f"Exits: {', '.join(exits_list)}" if exits_list else "No obvious exits."
        )
        return {"result": f"{name}\n{desc}\n{exits_str}"}
    elif cmd == "say":
        message = " ".join(args).strip()
        if not message:
            return {"result": "You open your mouth, but no words come out"}
        return {"result": f"You say: {message}"}
    else:
        return {"result": f"Unknown command: {cmd}"}
