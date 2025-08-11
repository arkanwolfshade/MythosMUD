# Environmental Metadata Requirements for MythosMUD Map Builder

## Current State Analysis

### Existing Environment Types
- **Current:** Only "outdoors" is used across all Arkham City rooms
- **Map Builder Default:** Includes forest, plains, water, wall, cave, default
- **Gap:** No mapping for "outdoors" in the default tile palette

## Recommended Environmental Metadata Schema

### Urban Environment Types (Arkham City)

#### Street & Road Types
```json
{
  "environment": "street_paved",     // Main paved streets (Derby, Garrison, etc.)
  "environment": "street_cobblestone", // Historic cobblestone streets
  "environment": "alley",            // Narrow alleys between buildings
  "environment": "intersection",     // Street intersections
  "environment": "plaza",            // Open public squares
}
```

#### Building Types
```json
{
  "environment": "building_exterior", // Outside of buildings
  "environment": "building_interior", // Inside buildings (shops, homes)
  "environment": "institution",       // Miskatonic University, hospitals, etc.
  "environment": "residential",       // Residential areas
  "environment": "commercial",        // Business districts
}
```

#### Natural Areas
```json
{
  "environment": "park",              // Public parks and gardens
  "environment": "cemetery",          // Burial grounds
  "environment": "waterfront",        // River and harbor areas
  "environment": "hillside",          // Elevated areas (French Hill, etc.)
}
```

#### Special Areas
```json
{
  "environment": "campus",            // Miskatonic University campus
  "environment": "docks",             // Harbor and shipping areas
  "environment": "industrial",        // Factories and warehouses
  "environment": "abandoned",         // Derelict or abandoned areas
}
```

## Enhanced Tile Mapping for MythosMUD

### Updated DEFAULT_TILE_MAP for Urban Settings

```python
DEFAULT_TILE_MAP = {
    # Urban Streets
    "street_paved": {"glyph": "=", "fg": (128, 128, 128), "bg": (0, 0, 0)},
    "street_cobblestone": {"glyph": "≈", "fg": (100, 100, 100), "bg": (0, 0, 0)},
    "alley": {"glyph": "|", "fg": (80, 80, 80), "bg": (0, 0, 0)},
    "intersection": {"glyph": "+", "fg": (150, 150, 150), "bg": (0, 0, 0)},
    "plaza": {"glyph": "□", "fg": (120, 120, 120), "bg": (0, 0, 0)},

    # Buildings
    "building_exterior": {"glyph": "█", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "building_interior": {"glyph": "▒", "fg": (160, 82, 45), "bg": (0, 0, 0)},
    "institution": {"glyph": "▓", "fg": (105, 105, 105), "bg": (0, 0, 0)},
    "residential": {"glyph": "░", "fg": (184, 134, 11), "bg": (0, 0, 0)},
    "commercial": {"glyph": "▄", "fg": (139, 69, 19), "bg": (0, 0, 0)},

    # Natural Areas
    "park": {"glyph": "♠", "fg": (34, 139, 34), "bg": (0, 0, 0)},
    "cemetery": {"glyph": "†", "fg": (169, 169, 169), "bg": (0, 0, 0)},
    "waterfront": {"glyph": "~", "fg": (0, 0, 255), "bg": (0, 0, 0)},
    "hillside": {"glyph": "^", "fg": (139, 69, 19), "bg": (0, 0, 0)},

    # Special Areas
    "campus": {"glyph": "♣", "fg": (0, 100, 0), "bg": (0, 0, 0)},
    "docks": {"glyph": "⚓", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "industrial": {"glyph": "⚙", "fg": (105, 105, 105), "bg": (0, 0, 0)},
    "abandoned": {"glyph": "☠", "fg": (128, 128, 128), "bg": (0, 0, 0)},

    # Legacy Support
    "outdoors": {"glyph": ".", "fg": (100, 220, 100), "bg": (0, 0, 0)},
    "forest": {"glyph": ".", "fg": (0, 200, 0), "bg": (0, 0, 0)},
    "plains": {"glyph": ",", "fg": (100, 220, 100), "bg": (0, 0, 0)},
    "water": {"glyph": "~", "fg": (0, 0, 255), "bg": (0, 0, 0)},
    "wall": {"glyph": "#", "fg": (139, 69, 19), "bg": (0, 0, 0)},
    "cave": {"glyph": "^", "fg": (150, 150, 150), "bg": (0, 0, 0)},
    "default": {"glyph": "?", "fg": (255, 255, 255), "bg": (0, 0, 0)},
}
```

## Implementation Strategy

### Phase 1: Immediate Fixes
1. **Add "outdoors" mapping** to existing DEFAULT_TILE_MAP
2. **Update map builder** to use MythosMUD-specific tile mapping
3. **Test with current rooms** to ensure proper rendering

### Phase 2: Gradual Enhancement
1. **Categorize existing rooms** by actual environment type
2. **Update room JSON files** with appropriate environment values
3. **Add new environment types** as needed for different areas

### Phase 3: Advanced Features
1. **Dynamic tile mapping** based on zone/subzone
2. **Time-of-day variations** in tile appearance
3. **Weather effects** on tile rendering

## Room JSON Schema Enhancement

### Current Schema
```json
{
  "id": "earth_arkham_city_downtown_room_derby_st_001",
  "name": "E. Derby Street",
  "description": "A bustling section of E. Derby Street...",
  "plane": "earth",
  "zone": "arkham_city",
  "sub_zone": "downtown",
  "environment": "outdoors",
  "exits": {...}
}
```

### Enhanced Schema
```json
{
  "id": "earth_arkham_city_downtown_room_derby_st_001",
  "name": "E. Derby Street",
  "description": "A bustling section of E. Derby Street...",
  "plane": "earth",
  "zone": "arkham_city",
  "sub_zone": "downtown",
  "environment": "street_paved",
  "environment_details": {
    "lighting": "street_lamp",
    "weather_exposure": "exposed",
    "traffic_level": "moderate"
  },
  "exits": {...}
}
```

## Subzone-Specific Recommendations

### Downtown
- **Primary:** `street_paved`, `intersection`, `commercial`
- **Secondary:** `building_interior`, `alley`

### Northside
- **Primary:** `residential`, `street_paved`, `hillside`
- **Secondary:** `park`, `cemetery`

### Campus
- **Primary:** `campus`, `institution`, `park`
- **Secondary:** `building_interior`, `plaza`

### French Hill
- **Primary:** `residential`, `hillside`, `cemetery`
- **Secondary:** `park`, `abandoned`

### Waterfront/Innsmouth
- **Primary:** `waterfront`, `docks`, `industrial`
- **Secondary:** `abandoned`, `commercial`

## Migration Plan

### Step 1: Update Map Builder
- Add MythosMUD-specific tile mapping
- Ensure backward compatibility with "outdoors"

### Step 2: Room Categorization
- Analyze existing rooms by subzone and description
- Assign appropriate environment types
- Create migration script for bulk updates

### Step 3: Validation
- Test map rendering with new environment types
- Verify visual distinction between different areas
- Ensure readability in both ASCII and tcod modes

## Benefits

1. **Visual Distinction:** Different areas will be visually distinct on maps
2. **Atmospheric Enhancement:** Better representation of Arkham's eldritch atmosphere
3. **Navigation Aid:** Players can better understand their location
4. **Development Tool:** Easier to spot connectivity issues and gaps
5. **Future Expansion:** Foundation for more advanced visualization features

## Next Steps

1. **Immediate:** Update map builder with MythosMUD tile mapping
2. **Short-term:** Categorize and update room environment types
3. **Medium-term:** Add environment_details for advanced features
4. **Long-term:** Implement dynamic rendering based on game state
