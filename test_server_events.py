#!/usr/bin/env python3
"""
Test script to verify the server's event system is working.
"""

import asyncio
import json
import websockets
import time


async def test_server_events():
    """Test the server's event system."""
    
    print("Testing Server Event System")
    print("=" * 40)
    
    # Connect to the server
    uri = "ws://localhost:54731/api/ws/testuser1"
    
    try:
        websocket = await websockets.connect(uri)
        print("✅ Connected to server")
        
        # Wait for initial messages
        await asyncio.sleep(1)
        
        # Send a movement command
        command = {
            "type": "command",
            "data": {
                "command": "go",
                "args": ["north"]
            }
        }
        
        print("Sending movement command...")
        await websocket.send(json.dumps(command))
        
        # Listen for messages for a few seconds
        messages_received = []
        start_time = time.time()
        
        while time.time() - start_time < 3:
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=0.1)
                data = json.loads(message)
                messages_received.append(data)
                print(f"Received: {data.get('event_type', 'unknown')}")
                
                # Check for multiplayer events
                if data.get('event_type') in ['player_entered', 'player_left', 'room_occupants']:
                    print(f"🎉 MULTIPLAYER EVENT DETECTED: {data['event_type']}")
                    print(f"   Data: {data.get('data', {})}")
                
            except asyncio.TimeoutError:
                continue
            except websockets.exceptions.ConnectionClosed:
                print("Connection closed")
                break
        
        print(f"\nTotal messages received: {len(messages_received)}")
        
        # Check for multiplayer events
        multiplayer_events = [
            msg for msg in messages_received 
            if msg.get('event_type') in ['player_entered', 'player_left', 'room_occupants']
        ]
        
        if multiplayer_events:
            print(f"✅ Found {len(multiplayer_events)} multiplayer events!")
            for event in multiplayer_events:
                print(f"   - {event['event_type']}: {event.get('data', {}).get('message', 'No message')}")
        else:
            print("❌ No multiplayer events detected")
            print("Available event types:")
            for msg in messages_received:
                print(f"   - {msg.get('event_type', 'unknown')}")
        
        await websocket.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(test_server_events())
