# Profession System Specification

## Overview

The Profession System allows players to choose a character profession during character creation. Professions are gated by stat requirements and will influence combat, social, and other game mechanics. This system provides a foundation for character specialization and future mechanical depth.

## User Experience Flow

### Character Creation Flow

1. **Registration** → **Profession Selection** → **Stat Rolling** → **Stat Confirmation** → **Enter Game**

### Navigation Rules

**Profession Selection Screen**:

- "Back" button returns to registration
- "Next" button disabled until profession selected
- Clicking anywhere on profession card selects it
- **Stat Rolling Screen**:
  - "Back" button returns to profession selection
  - Stat rolling only shows combinations that meet profession requirements

## Database Schema

### Professions Table

```sql
CREATE TABLE professions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    flavor_text TEXT NOT NULL,
    stat_requirements TEXT NOT NULL, -- JSON: {"strength": 12, "intelligence": 10}
    mechanical_effects TEXT NOT NULL, -- JSON: future bonuses/penalties
    is_available BOOLEAN NOT NULL DEFAULT 1
);

CREATE INDEX idx_professions_available ON professions(is_available);
```

### Player Table Modification

```sql
ALTER TABLE players ADD COLUMN profession_id INTEGER NOT NULL DEFAULT 0;
-- Foreign key constraint will be added after professions table is populated
```

### Seeded Data

```sql
INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects) VALUES
(0, 'Tramp', 'A wandering soul with no fixed abode', 'You have learned to survive on the streets, finding shelter where you can and making do with what you have.', '{}', '{}'),
(1, 'Gutter Rat', 'A street-smart survivor of the urban underbelly', 'You know the hidden passages and dark corners of the city, where others fear to tread.', '{}', '{}');
```

## API Endpoints

### Modified Stat Rolling Endpoint

```
POST /api/character/roll-stats
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

### New Profession Endpoints

```
GET /api/professions
GET /api/professions/{id}
```

## UI Components

### Profession Selection Screen

**Layout**: Card-based grid of available professions

**Card Content**:

  - Profession name (header)
  - Description (body text)
  - Stat requirements (highlighted box)
  - Flavor text (italic, smaller text)
- **Interaction**: Click anywhere on card to select
- **Navigation**: Back to registration, Next to stat rolling (disabled until selection)

### Stat Requirements Display

**Format**: "Minimum: Strength 12, Intelligence 10"

**No Requirements**: "No requirements"

**Styling**: Highlighted background, clear typography

## Stat Rolling Logic

### Weighted Probability System

1. Roll stats normally (3d6 for each stat)

2. Check if combination meets profession requirements

3. If requirements not met:

   - Discard roll

   - Apply weighted probabilities to favor valid combinations

   - Re-roll with adjusted weights

4. Continue until valid combination found

### Requirements Validation

Parse `stat_requirements` JSON from profession data

- Check each stat against minimum values
- Return only combinations that meet all requirements

## Technical Implementation

### Database Scripts

**DDL Script**: `server/scripts/create_professions_table.sql`

**Integration**: Add to existing database initialization scripts

**Migration**: Upgrade in place, no separate migration needed

### Server Code Changes

**Models**: Add `Profession` model and update `Player` model

**Endpoints**: Modify stat rolling endpoint, add profession endpoints

**Logic**: Implement weighted stat rolling with profession requirements

### Client Code Changes

**Screens**: Add profession selection screen

**Navigation**: Update character creation flow

**Components**: Create profession card component
- **API**: Add profession API calls

## MVP Professions

### Tramp (ID: 0)

**Description**: A wandering soul with no fixed abode

**Flavor Text**: You have learned to survive on the streets, finding shelter where you can and making do with what you have.

**Requirements**: None
- **Effects**: None (MVP)

### Gutter Rat (ID: 1)

**Description**: A street-smart survivor of the urban underbelly

**Flavor Text**: You know the hidden passages and dark corners of the city, where others fear to tread.

**Requirements**: None
- **Effects**: None (MVP)

## Future Considerations

### Stat Requirements Examples

**Scholar**: Intelligence ≥ 14, Wisdom ≥ 12

**Warrior**: Strength ≥ 14, Constitution ≥ 12

**Rogue**: Dexterity ≥ 14, Charisma ≥ 12

### Mechanical Effects Examples

**Combat Bonuses**: Damage modifiers, hit bonuses

**Social Bonuses**: Persuasion bonuses, intimidation effects

**Exploration Bonuses**: Movement speed, detection abilities

## Testing Requirements

### Unit Tests

Profession model validation

- Stat rolling logic with requirements
- API endpoint responses
- Database schema creation

### Integration Tests

Character creation flow with profession selection

- Stat rolling with profession requirements
- Database persistence of profession choice

### E2E Tests

Complete character creation flow

- Profession selection and stat rolling
- Navigation between screens

## Security Considerations

### Input Validation

Validate profession_id exists and is available

- Sanitize profession data before display
- Validate stat requirements format

### Data Integrity

Foreign key constraints on profession_id

- Ensure profession exists before player creation
- Validate stat requirements JSON format

## Performance Considerations

### Database Optimization

Index on professions.is_available

- Index on players.profession_id
- Efficient stat rolling algorithm

### Caching

Cache profession data for stat rolling

- Cache available professions list
- Minimize database queries during character creation

## Implementation Priority

### Phase 1 (MVP)

1. Database schema and DDL scripts
2. Basic profession models and API endpoints
3. Profession selection UI screen
4. Modified stat rolling with profession support
5. Integration with character creation flow

### Phase 2 (Enhancement)

1. Stat requirements validation
2. Weighted probability stat rolling
3. Enhanced UI with requirements display
4. Comprehensive testing

### Phase 3 (Future)

1. Mechanical effects implementation
2. Additional professions with requirements
3. Profession-based game mechanics
4. Advanced UI features

## Acceptance Criteria

### Functional Requirements

[ ] Players can select profession during character creation

- [ ] Profession selection screen displays all available professions
- [ ] Stat rolling respects profession requirements
- [ ] Profession choice is persisted to database
- [ ] Navigation between screens works correctly
- [ ] Existing players default to "Tramp" profession

### Non-Functional Requirements

[ ] Database schema supports future profession expansion

- [ ] Stat rolling algorithm is efficient and fair
- [ ] UI is responsive and user-friendly
- [ ] Code follows project standards and patterns
- [ ] Comprehensive test coverage (80%+)
- [ ] All linting and formatting checks pass

## Dependencies

### Database

SQLite for MVP

- PostgreSQL migration path planned
- Existing database initialization scripts

### Frontend

React/TypeScript client

- Existing character creation components
- Navigation system

### Backend

FastAPI server

- Existing stat rolling system
- Database models and persistence

## Risks and Mitigation

### Technical Risks

**Stat rolling complexity**: Implement weighted algorithm carefully with extensive testing

**Database migration**: Use upgrade-in-place approach to avoid data loss

**UI complexity**: Start with simple card layout, enhance iteratively

### User Experience Risks

**Confusion about requirements**: Clear, highlighted display of stat requirements

**Navigation issues**: Consistent back/next button placement

**Performance**: Efficient stat rolling algorithm

## Success Metrics

### User Engagement

Players successfully complete character creation with profession selection

- Low bounce rate on profession selection screen
- Positive feedback on profession system

### Technical Performance

Fast stat rolling response times

- Reliable database persistence
- Clean, maintainable code

### Future Readiness

Easy addition of new professions

- Flexible stat requirements system
- Extensible mechanical effects framework
