# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-23-profession-system/spec.md

## Endpoints

### GET /api/professions

**Purpose:** Retrieve all available professions for character creation
**Parameters:** None
**Response:**


```json
{
  "professions": [
    {
      "id": 0,
      "name": "Tramp",
      "description": "A wandering soul with no fixed abode",
      "flavor_text": "You have learned to survive on the streets, finding shelter where you can and making do with what you have.",
      "stat_requirements": {},
      "mechanical_effects": {},
      "is_available": true
    }
  ]
}

```

**Errors:** 500 Internal Server Error if database query fails

### GET /api/professions/{id}


**Purpose:** Retrieve specific profession details by ID
**Parameters:**


- `id` (path parameter): Profession ID
**Response:**

```json
{
  "id": 0,
  "name": "Tramp",
  "description": "A wandering soul with no fixed abode",
  "flavor_text": "You have learned to survive on the streets, finding shelter where you can and making do with what you have.",
  "stat_requirements": {},

  "mechanicl_effects": {},

  "is_available": true
}
```

**Errors:**

- 404 Not Found if profession doesn't exist

- 500 Internal Server Error if database query fails

### POST /api/character/roll-stats (Modified)

**Purpose:** Roll character stats with profession requirements validation

**Parameters:**


```json
{
  "profession_id": 0
}
```

**Response:**

```json
{
  "stats": {
    "strength": 12,
    "intelligence": 10,

    "constitution": 14,

    "dexterity": 11,
    "wisdom": 13,
    "charisma": 9
  },
  "profession_id": 0,
  "meets_requirements": true

}
```

**Errors:**


- 400 Bad Request if profession_id is invalid or profession doesn't exist
- 500 Internal Server Error if stat rolling algorithm fails

## Controllers

### ProfessionController

- **get_all_professions()**: Query professions table filtering by is_available=true
- **get_profession_by_id(id)**: Query professions table by ID with existence validation
- **validate_profession_exists(id)**: Helper method to check profession existence and availability


### CharacterController (Modified)

- **roll_stats_with_profession(profession_id)**: Modified stat rolling logic that:
  1. Validates profession exists and is available
  2. Retrieves profession stat requirements
  3. Implements weighted probability stat rolling
  4. Validates rolled stats against requirements

  5. Re-rolls if requirements not met
  6. Returns valid stat combination

## Business Logic

### Stat Rolling Algorithm


1. **Validation**: Ensure profession_id exists and profession is available
2. **Requirements Retrieval**: Parse stat_requirements JSON from profession data
3. **Weighted Rolling**: Roll stats with probabilities favoring valid combinations
4. **Validation Loop**: Check rolled stats against requirements, re-roll if invalid
5. **Response**: Return valid stat combination with profession_id and validation flag


### Error Handling

- **Invalid Profession**: Return 400 with descriptive error message
- **Database Errors**: Return 500 with generic error message (log details server-side)
- **Stat Rolling Failures**: Implement retry logic with maximum attempts before failing

## Integration Points

### Database Integration

- **Professions Table**: Primary data source for profession information
- **Players Table**: Future integration for storing player profession choices
- **Caching**: Cache profession data to minimize database queries during stat rolling

### Frontend Integration

- **Character Creation Flow**: API calls integrated into profession selection and stat rolling screens
- **Error Handling**: Proper error display for invalid profession selections and stat rolling failures
- **Loading States**: Appropriate loading indicators during API calls
