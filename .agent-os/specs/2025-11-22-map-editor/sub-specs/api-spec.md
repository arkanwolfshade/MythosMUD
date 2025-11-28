# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-11-22-map-editor/spec.md

## Endpoints

### GET /api/rooms/list

**Purpose:** Fetch bulk room data optimized for map visualization with optional filtering by zone/subzone.

**Parameters:**
- `plane` (required, query string): Filter rooms by plane identifier
- `zone` (required, query string): Filter rooms by zone identifier
- `sub_zone` (optional, query string): Filter rooms by sub-zone identifier
- `include_exits` (optional, boolean, default: true): Include exit relationship data in response

**Response Format:**
```json
{
  "rooms": [
    {
      "id": "earth_arkhamcity_campus_room_boundary_st_001",
      "name": "Boundary Street - Near Crane Intersection",
      "description": "...",
      "plane": "earth",
      "zone": "arkhamcity",
      "sub_zone": "campus",
      "environment": "street_paved",
      "exits": {
        "north": null,
        "south": "earth_arkhamcity_campus_intersection_boundary_crane",
        "east": null,
        "west": "earth_arkhamcity_campus_intersection_boundary_crane",
        "up": null,
        "down": null
      },
      "map_x": 100.5,
      "map_y": 200.3
    }
  ],
  "total": 150,
  "filtered": true
}
```

**Errors:**
- `400 Bad Request`: Invalid filter parameters (missing required plane/zone parameters)
- `500 Internal Server Error`: Server error during data fetch

**Authentication:** Required (standard user authentication)

**Rate Limiting:** Same as existing room endpoints

### POST /api/map/layout (Optional - for edit mode)

**Purpose:** Save node positions and layout data for map visualization.

**Request Body:**
```json
{
  "layout_id": "default",
  "positions": {
    "earth_arkhamcity_campus_room_boundary_st_001": {"x": 100, "y": 200},
    "earth_arkhamcity_campus_intersection_boundary_crane": {"x": 150, "y": 250}
  },
  "zone": "arkhamcity",
  "sub_zone": "campus"
}
```

**Response Format:**
```json
{
  "success": true,
  "layout_id": "default",
  "saved_at": "2025-11-22T12:00:00Z"
}
```

**Errors:**
- `400 Bad Request`: Invalid position data or missing required fields
- `403 Forbidden`: Not authorized (admin only)
- `500 Internal Server Error`: Server error during save

**Authentication:** Required (admin authentication for edit operations)

### GET /api/map/layout (Optional - for edit mode)

**Purpose:** Retrieve saved layout positions for map visualization.

**Parameters:**
- `layout_id` (optional, query string): Specific layout to retrieve (default: "default")
- `zone` (optional, query string): Filter layout by zone
- `sub_zone` (optional, query string): Filter layout by sub-zone

**Response Format:**
```json
{
  "layout_id": "default",
  "positions": {
    "earth_arkhamcity_campus_room_boundary_st_001": {"x": 100, "y": 200}
  },
  "created_at": "2025-11-22T12:00:00Z",
  "updated_at": "2025-11-22T12:00:00Z"
}
```

**Errors:**
- `404 Not Found`: Layout not found
- `500 Internal Server Error`: Server error during retrieval

**Authentication:** Required (standard user authentication)

## Implementation Notes

- The `/api/rooms/list` endpoint should leverage existing room caching infrastructure for performance
- Layout persistence stores positions in `rooms` table columns (`map_x`, `map_y`) - positions are included in response if they exist
- Exit relationships should be included in response to enable edge creation without additional queries
- Response format matches existing room endpoints for consistency
- Exit data includes both string room IDs and object format (with target, flags, description) - both should be handled
