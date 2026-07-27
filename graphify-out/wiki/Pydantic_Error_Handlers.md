# Pydantic Error Handlers

> 26 nodes · cohesion 0.03

## Key Concepts

- **error_types.py** (37 connections) — `server/error_types.py`
- **create_websocket_error_response()** (32 connections) — `server/error_types.py`
- **create_standard_error_response()** (27 connections) — `server/error_types.py`
- **create_sse_error_response()** (17 connections) — `server/error_types.py`
- **ErrorResponseDetails** (8 connections) — `server/error_types.py`
- **_normalize_error_response_details()** (7 connections) — `server/error_types.py`
- **WebSocket** (7 connections) — `server/realtime/websocket_handler_validation.py`
- **Request** (6 connections) — `server/error_handlers/standardized_responses.py`
- **Exception** (5 connections) — `server/error_handlers/standardized_responses.py`
- **RealtimeErrorResponse** (5 connections) — `server/error_types.py`
- **ValidationFieldErrorDetail** (4 connections) — `server/error_types.py`
- **Any** (3 connections) — `server/error_handlers/standardized_responses.py`
- **ErrorContextDetail** (3 connections) — `server/error_types.py`
- **StandardErrorPayload** (3 connections) — `server/error_types.py`
- **HTTPException** (2 connections) — `server/error_handlers/standardized_responses.py`
- **ValidationError** (2 connections) — `server/error_handlers/standardized_responses.py`
- **Centralized error types and constants for MythosMUD.  This module defines standa** (1 connections) — `server/error_types.py`
- **Nested error payload for HTTP standardized responses.** (1 connections) — `server/error_types.py`
- **WebSocket or SSE standardized error response.** (1 connections) — `server/error_types.py`
- **Coerce caller-provided detail mappings into the response TypedDict shape.** (1 connections) — `server/error_types.py`
- **Create a standardized error response.      Args:         error_type: The type of** (1 connections) — `server/error_types.py`
- **Create a standardized WebSocket error response.      Args:         error_type: T** (1 connections) — `server/error_types.py`
- **DEPRECATED: SSE connections are no longer supported.     This function is kept f** (1 connections) — `server/error_types.py`
- **Single field validation error included in error response details.** (1 connections) — `server/error_types.py`
- **Request context included in error response details when available.** (1 connections) — `server/error_types.py`
- *... and 1 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (18 shared connections)

## Source Files

- `server/error_handlers/standardized_responses.py`
- `server/error_types.py`
- `server/realtime/websocket_handler_validation.py`

## Audit Trail

- EXTRACTED: 170 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*