# MythosMUD Environment Type Categorization Plan

## Current State Analysis

**Findings:**
- **Total rooms analyzed:** 79
- **Current environment type:** All rooms use "outdoors"
- **Subzones present:** downtown, northside, campus, french_hill, waterfront, merchant, east_town, lower_southside, uptown, river_town

## Categorization Strategy

### Phase 1: Subzone-Based Defaults

Based on our subzone analysis, here are the recommended environment types:

#### Downtown (Commercial District)
- **Street rooms:** `street_paved`
- **Intersection rooms:** `intersection`
- **Building rooms:** `commercial`

#### Northside (Residential District)
- **Street rooms:** `street_paved`
- **Intersection rooms:** `intersection`
- **Building rooms:** `residential`

#### Campus (Miskatonic University)
- **All rooms:** `campus`

#### French Hill (Historic District)
- **Street rooms:** `street_cobblestone`
- **Intersection rooms:** `intersection`
- **Building rooms:** `residential`
- **Special areas:** `cemetery`

#### Waterfront (Harbor District)
- **Street rooms:** `street_paved`
- **Intersection rooms:** `intersection`
- **Special areas:** `waterfront`, `docks`

#### Merchant District
- **Street rooms:** `street_paved`
- **Building rooms:** `commercial`

#### Other Residential Areas
- **East Town, Lower Southside, Uptown, River Town:**
  - **Street rooms:** `street_paved`
  - **Building rooms:** `residential`

### Phase 2: Room-Specific Analysis

#### Street Room Patterns
- **Room IDs containing `_st_`:** Street rooms → `street_paved` or `street_cobblestone`
- **Room IDs containing `_ave_`:** Avenue rooms → `street_paved`
- **Room IDs containing `_ln_`:** Lane rooms → `street_paved`

#### Intersection Room Patterns
- **Room IDs containing `intersection_`:** → `intersection`

#### Building Room Patterns
- **Room IDs containing `room_` but not `intersection_`:** → Based on subzone

### Phase 3: Special Cases

#### Campus Area
- **All campus rooms:** → `campus` (regardless of room ID pattern)

#### French Hill
- **All rooms:** → `street_cobblestone` for streets, `residential` for buildings

#### Waterfront Areas
- **All rooms:** → `waterfront` for general areas, `docks` for specific dock rooms

## Implementation Plan

### Step 1: Create Environment Update Script
- Analyze room ID patterns
- Apply subzone-based defaults
- Handle special cases
- Generate update recommendations

### Step 2: Manual Review
- Review suggested changes
- Adjust for specific room descriptions
- Handle edge cases

### Step 3: Bulk Update
- Apply environment type updates
- Test with map builder
- Verify visual improvements

### Step 4: Validation
- Run map builder on updated rooms
- Verify environment types render correctly
- Check for any issues

## Expected Results

### Before (Current State)
```
outdoors: 79 rooms
```

### After (Target State)
```
street_paved: ~45 rooms
intersection: ~15 rooms
campus: ~10 rooms
residential: ~5 rooms
street_cobblestone: ~2 rooms
waterfront: ~2 rooms
```

## Benefits

1. **Visual Distinction:** Different areas will be visually distinct on maps
2. **Better Navigation:** Players can understand their location better
3. **Atmospheric Enhancement:** More accurate representation of Arkham's character
4. **Development Tool:** Easier to spot connectivity and design issues

## Next Steps

1. **Create update script** with subzone-based logic
2. **Run categorization** and review results
3. **Apply updates** to room JSON files
4. **Test with map builder** to verify improvements
5. **Document changes** for future reference
