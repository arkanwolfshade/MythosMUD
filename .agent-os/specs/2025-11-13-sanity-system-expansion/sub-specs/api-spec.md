# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-11-13-lucidity-system-expansion/spec.md

## Endpoints

### POST /api/v1/lucidity/recovery/pray

**Purpose:** Execute `pray` recovery action at an eligible altar.
**Parameters:** `location_id` (string), `offering_item_id` (optional string).
**Response:** `{ "lucidity_delta": number, "current_san": number, "cooldown_expires_at": iso8601 }`
**Errors:** `400` (invalid location/offering), `409` (cooldown active), `403` (not at sanctuary).

### POST /api/v1/lucidity/recovery/meditate

**Purpose:** Begin three-minute meditation channel and receive ticking updates via SSE/WebSocket.
**Parameters:** `channel_token` (string, optional to resume).
**Response:** `{ "status": "started", "channel_token": string }`
**Errors:** `409` (already channeling), `400` (environment too noisy).

### POST /api/v1/lucidity/recovery/group-solace

**Purpose:** Initiate group solace chant for party members.
**Parameters:** `party_id` (string), `location_id` (string).
**Response:** `{ "status": "pending", "required_participants": number, "cooldown_expires_at": iso8601 }`
**Errors:** `409` (insufficient participants), `403` (location not sanctified).

### POST /api/v1/lucidity/recovery/therapy

**Purpose:** Schedule therapy session with sanitarium NPC.
**Parameters:** `npc_id` (string), `payment_token` (string).
**Response:** `{ "lucidity_delta": number, "liabilities_cleared": [string], "next_available_at": iso8601 }`
**Errors:** `402` (insufficient funds), `429` (daily limit reached).

### POST /api/v1/lucidity/recovery/folk-tonic

**Purpose:** Consume tonic item to gain immediate SAN and buffer effect.
**Parameters:** `item_instance_id` (string).
**Response:** `{ "lucidity_delta": number, "buffer_minutes": number }`
**Errors:** `404` (item missing), `409` (buffer already active).

### POST /api/v1/lucidity/ground

**Purpose:** Attempt to bring a catatonic ally back to SAN 1.
**Parameters:** `target_player_id` (string).
**Response:** `{ "status": "channeling", "expires_at": iso8601 }` with follow-up event on completion.
**Errors:** `409` (channel already in progress), `400` (target not catatonic), `403` (not in range).

### GET /api/v1/lucidity/status

**Purpose:** Fetch current SAN snapshot for authenticated player.
**Response:** `{ "current_san": number, "current_tier": string, "liabilities": [ ... ], "cooldowns": { ... } }`
**Errors:** `401` (unauthorized).

## Real-time Streams

### WebSocket Topic: `lucidity.events`

- **Payload:** `{ "type": "lucidity_change" | "hallucination" | "command_misfire" | "catatonia" | "rescue_update", ... }`
- **Purpose:** Push immediate feedback for SAN adjustments, hallucination prompts, involuntary actions, and rescue progress.
- **Error Handling:** Disconnect client on malformed payload; attempt auto-resubscribe with exponential backoff.

## Controller Notes

- Lucidity controllers must enforce rate limiting and consult cooldown table before accepting recovery requests.
- Rescue controller (`ground`) locks target to single rescuer at a time and cancels on movement/damage.
- SSE/WebSocket services hook into existing session context to include COPPA-compliant metadata only.
