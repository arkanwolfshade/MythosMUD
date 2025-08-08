#!/usr/bin/env python3
"""
Manual test script for multiplayer functionality.

This script simulates multiple clients connecting to the server
and tests the real-time communication between them.
"""

import asyncio
import json

import websockets


class MultiplayerTestClient:
    """Test client for multiplayer functionality."""

    def __init__(self, player_id: str, player_name: str):
        self.player_id = player_id
        self.player_name = player_name
        self.websocket = None
        self.messages_received = []
        self.connected = False

    async def connect(self, uri: str):
        """Connect to the WebSocket server."""
        try:
            self.websocket = await websockets.connect(uri)
            self.connected = True
            print(f"[{self.player_name}] Connected to server")

            # Start listening for messages
            asyncio.create_task(self._listen_for_messages())

        except Exception as e:
            print(f"[{self.player_name}] Failed to connect: {e}")

    async def _listen_for_messages(self):
        """Listen for incoming messages."""
        try:
            while self.connected:
                message = await self.websocket.recv()
                data = json.loads(message)
                self.messages_received.append(data)
                print(f"[{self.player_name}] Received: {data.get('event_type', 'unknown')}")

        except websockets.exceptions.ConnectionClosed:
            print(f"[{self.player_name}] Connection closed")
            self.connected = False
        except Exception as e:
            print(f"[{self.player_name}] Error receiving message: {e}")
            self.connected = False

    async def send_command(self, command: str, args: list[str] = None):
        """Send a command to the server."""
        if not self.connected or not self.websocket:
            print(f"[{self.player_name}] Not connected")
            return

        try:
            message = {"type": "command", "data": {"command": command, "args": args or []}}
            await self.websocket.send(json.dumps(message))
            print(f"[{self.player_name}] Sent command: {command} {args}")

        except Exception as e:
            print(f"[{self.player_name}] Error sending command: {e}")

    async def disconnect(self):
        """Disconnect from the server."""
        if self.websocket:
            await self.websocket.close()
        self.connected = False
        print(f"[{self.player_name}] Disconnected")


async def test_multiplayer_functionality():
    """Test multiplayer functionality with multiple clients."""

    # Create test clients
    client1 = MultiplayerTestClient("testuser1", "Professor Armitage")
    client2 = MultiplayerTestClient("testuser2", "Dr. Wilmarth")

    # Connect both clients
    print("Connecting clients...")
    await client1.connect("ws://localhost:54731/api/ws/testuser1")
    await client2.connect("ws://localhost:54731/api/ws/testuser2")

    # Wait for initial connection
    await asyncio.sleep(2)

    # Test 1: Have client1 move to a different room
    print("\n=== Test 1: Player Movement ===")
    await client1.send_command("go", ["north"])
    await asyncio.sleep(1)

    # Check if client2 received the movement notification
    print(f"\nClient2 received {len(client2.messages_received)} messages")
    for msg in client2.messages_received:
        if msg.get("event_type") in ["player_entered", "player_left", "room_update"]:
            print(f"  - {msg.get('event_type')}: {msg.get('data', {}).get('message', 'No message')}")

    # Test 2: Have client2 move to the same room
    print("\n=== Test 2: Second Player Movement ===")
    await client2.send_command("go", ["north"])
    await asyncio.sleep(1)

    # Check if client1 received the movement notification
    print(f"\nClient1 received {len(client1.messages_received)} messages")
    for msg in client1.messages_received:
        if msg.get("event_type") in ["player_entered", "player_left", "room_update"]:
            print(f"  - {msg.get('event_type')}: {msg.get('data', {}).get('message', 'No message')}")

    # Test 3: Have client1 move back
    print("\n=== Test 3: Player Leaving ===")
    await client1.send_command("go", ["south"])
    await asyncio.sleep(1)

    # Check if client2 received the leave notification
    print(f"\nClient2 received {len(client2.messages_received)} total messages")
    for msg in client2.messages_received:
        if msg.get("event_type") in ["player_entered", "player_left", "room_update"]:
            print(f"  - {msg.get('event_type')}: {msg.get('data', {}).get('message', 'No message')}")

    # Disconnect clients
    print("\n=== Disconnecting ===")
    await client1.disconnect()
    await client2.disconnect()

    # Summary
    print("\n=== Test Summary ===")
    print(f"Client1 received {len(client1.messages_received)} messages")
    print(f"Client2 received {len(client2.messages_received)} messages")

    # Check for multiplayer events
    multiplayer_events = []
    for client in [client1, client2]:
        for msg in client.messages_received:
            if msg.get("event_type") in ["player_entered", "player_left", "room_occupants"]:
                multiplayer_events.append(msg)

    print(f"Found {len(multiplayer_events)} multiplayer events")
    for event in multiplayer_events:
        print(f"  - {event.get('event_type')}: {event.get('data', {}).get('message', 'No message')}")

    if multiplayer_events:
        print("\n✅ Multiplayer functionality is working!")
    else:
        print("\n❌ No multiplayer events detected")


if __name__ == "__main__":
    print("Testing MythosMUD Multiplayer Functionality")
    print("Make sure the server is running on localhost:54731")
    print("=" * 50)

    try:
        asyncio.run(test_multiplayer_functionality())
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"\nTest failed: {e}")
