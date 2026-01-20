# BUG INVESTIGATION REPORT: Unable to Cast Basic Healing Spell

**Investigation Date:** 2025-12-14
**Investigator:** AI Assistant
**Session ID:** 2025-12-14_session-002_spell-cast-failure
**Bug Report:** Unable to cast basic healing spell

---

## EXECUTIVE SUMMARY

Players are unable to cast spells with multi-word names (e.g., "Basic Heal").
The `/cast` command factory method only parses the first word as the spell
name, causing spell lookup failures. When a user types `/cast basic heal`,
the system searches for a spell named "basic" instead of "basic heal",
resulting in "Spell 'basic' not found" errors.

**Root Cause:** The `create_cast_command` factory method in
`server/utils/command_factories_utility.py` only uses the first argument as
the spell name, unlike `create_learn_command` which correctly handles
multi-word spell names.

**Impact:** High - Players cannot cast spells with multi-word names, which likely includes most spells in the game.

---

## DETAILED FINDINGS

### 1. Bug Description Analysis

**User-Reported Symptoms**:

- Attempted `/cast heal` - Result: "Spell 'heal' not found."

- Attempted `/cast basic heal` - Result: "Spell 'basic' not found."

- Player successfully learned "Basic Heal" using `/learn basic_heal`

- Player has full MP (15/15) and is wounded (17/27 HP), making healing

  attempt logical

- Player is not in combat, so combat restrictions don't apply

**Error Messages from UI**:

- `Spell 'basic' not found.`
- `Spell 'heal' not found.`

### 2. Code Analysis

#### 2.1 Command Factory Method

**File:** `server/utils/command_factories_utility.py` (lines 227-237)

```python
@staticmethod
def create_cast_command(args: list[str]) -> CastCommand:
    """Create CastCommand from arguments."""
    if not args:
        # ... error handling ...

    spell_name = args[0]  # ❌ Only takes first word!
    target = " ".join(args[1:]) if len(args) > 1 else None
    return CastCommand(spell_name=spell_name, target=target)
```

**Finding:** The factory method only uses `args[0]` as the spell name, ignoring
subsequent words.

**Comparison with Learn Command:**

**File:** `server/utils/command_factories_utility.py` (lines 262-273)

```python
@staticmethod
def create_learn_command(args: list[str]) -> LearnCommand:
    """Create LearnCommand from arguments."""
    if not args:
        # ... error handling ...

    spell_name = " ".join(args)  # ✅ Correctly handles multi-word names
    return LearnCommand(spell_name=spell_name)
```

**Finding:** `create_learn_command` correctly joins all arguments as the
spell name, allowing multi-word spell names like "Basic Heal".

#### 2.2 Spell Lookup Logic

**File:** `server/game/magic/magic_service.py` (lines 150-156)

```python
# Get spell from registry

spell = self.spell_registry.get_spell(spell_id)
if not spell:
    # Try by name

    spell = self.spell_registry.get_spell_by_name(spell_id)
    if not spell:
        return {"success": False, "message": f"Spell '{spell_id}' not found."}
```

**Finding:** The spell lookup tries by ID first, then by name. The error message shows it's failing at the name lookup stage.

**File:** `server/game/magic/spell_registry.py` (lines 87-105)

```python
def get_spell_by_name(self, name: str) -> Spell | None:
    """Get a spell by name (case-insensitive)."""
    if not self._loaded:
        logger.warning("Spells not loaded, returning None", spell_name=name)
        return None

    name_lower = name.lower()
    for spell in self._spells.values():
        if spell.name.lower() == name_lower:
            return spell
    return None
```

**Finding:** The spell registry does case-insensitive exact matching. It
requires the full spell name to match exactly (case-insensitive). Partial
matches are not supported.

#### 2.3 Command Data Extraction

**File:** `server/commands/magic_commands.py` (lines 82-84)

```python
# Extract spell name and optional target

spell_name = command_data.get("spell_name") or command_data.get("spell")
target_name = command_data.get("target")
```

**Finding:** The handler correctly extracts `spell_name` and `target` from
command data. The issue is that `spell_name` is already truncated to the
first word by the factory method.

### 3. Root Cause Analysis

**Primary Root Cause:**

The `create_cast_command` factory method incorrectly parses multi-word spell
names. When a user types `/cast basic heal`:

1. **Command Parsing:** The command is split into args: `["basic", "heal"]`
2. **Factory Method:** Only `args[0]` ("basic") is used as the spell name
3. **Spell Lookup:** The system searches for a spell named "basic"
4. **Lookup Failure:** No spell named "basic" exists, so lookup fails
5. **Error Message:** "Spell 'basic' not found."

**Expected Behavior:**

When a user types `/cast basic heal`:

1. **Command Parsing:** The command is split into args: `["basic", "heal"]`
2. **Factory Method:** All args should be joined as the spell name: "basic heal"
3. **Spell Lookup:** The system searches for a spell named "basic heal" (case-insensitive)
4. **Lookup Success:** Finds "Basic Heal" spell
5. **Spell Casting:** Spell is cast successfully

**Why `/learn` Works:**

The `create_learn_command` factory method correctly handles multi-word spell names by joining all arguments:

```python
spell_name = " ".join(args)  # "basic heal"
```

**Why `/cast` Fails:**

The `create_cast_command` factory method only uses the first argument:

```python
spell_name = args[0]  # "basic" (wrong!)
target = " ".join(args[1:])  # "heal" (treated as target, not part of spell name)
```

### 4. System Impact Assessment

**Severity:** High

**Affected Systems**:

- Spell casting system (`server/commands/magic_commands.py`)
- Command factory system (`server/utils/command_factories_utility.py`)
- Spell registry lookup (`server/game/magic/spell_registry.py`)

**User Impact**:

- Players cannot cast any spell with a multi-word name

- This likely affects most spells in the game (e.g., "Basic Heal", "Greater

  Healing", "Fire Bolt", etc.)

- Single-word spell names may work, but multi-word names will always fail
- Creates inconsistent user experience (learning works, but casting doesn't)

**Functional Impact**:

- Core spellcasting functionality is partially broken
- Players can learn spells but cannot cast them if they have multi-word names
- Game balance and player experience are significantly affected

### 5. Evidence Documentation

**Code Evidence:**

1. **Factory Method Issue** (`server/utils/command_factories_utility.py:235`):

   ```python
   spell_name = args[0]  # Only first word
   ```

2. **Comparison with Working Command** (`server/utils/command_factories_utility.py:272`):

   ```python
   spell_name = " ".join(args)  # All words
   ```

3. **Spell Lookup** (`server/game/magic/spell_registry.py:101-104`):

   ```python
   name_lower = name.lower()
   for spell in self._spells.values():
       if spell.name.lower() == name_lower:  # Exact match required
           return spell
   ```

**User Evidence (from image description):**

- Command history shows: `/cast heal`, `/cast basic heal`
- Error messages: "Spell 'basic' not found.", "Spell 'heal' not found."
- Player successfully learned "Basic Heal" using `/learn basic_heal`
- Player has full MP and is wounded, making healing attempt logical

---

## INVESTIGATION RECOMMENDATIONS

### Priority 1: Fix Spell Name Parsing

**Action Items:**

1. Update `create_cast_command` factory method to join all arguments as the

   spell name (like `create_learn_command`)

2. Handle target parsing separately - targets should be specified explicitly

   or use a different syntax

3. Consider adding a separator (e.g., `@` or `on`) to distinguish spell name

   from target: `/cast basic heal @ target`

### Priority 2: Improve Spell Name Matching

**Action Items:**

1. Consider adding partial/fuzzy matching for spell names (e.g., "heal" matches "Basic Heal")
2. Add spell name aliases or abbreviations
3. Provide better error messages suggesting similar spell names when lookup fails

### Priority 3: Testing

**Action Items:**

1. Test `/cast` with single-word spell names
2. Test `/cast` with multi-word spell names
3. Test `/cast` with target specification (once implemented)
4. Verify spell registry contains expected spells
5. Test case-insensitive matching

### Priority 4: Documentation

**Action Items:**

1. Document the expected format for `/cast` command
2. Update help text to clarify spell name format
3. Add examples showing multi-word spell names

---

## REMEDIATION PROMPT

**For Cursor Chat**:

```text
Fix the spell casting command parsing issue. The `/cast` command factory
method only uses the first word as the spell name, preventing players from
casting spells with multi-word names like "Basic Heal".

Required changes:
1. Update `create_cast_command` in
   `server/utils/command_factories_utility.py` to join all arguments as the
   spell name (similar to `create_learn_command`)
2. For now, treat all arguments as the spell name (target parsing can be
   added later with a separator syntax)
3. Test with multi-word spell names to ensure lookup works correctly

Reference `create_learn_command` in the same file as a template for the
correct implementation.

```text

---

## INVESTIGATION COMPLETION CHECKLIST

[x] All investigation steps completed as written

- [x] Comprehensive evidence collected and documented
- [x] Root cause analysis completed
- [x] System impact assessed
- [x] Investigation report generated
- [x] No attempt made to fix issues (investigation only)
- [x] All findings clearly documented with evidence
- [x] Only official test credentials were used (ArkanWolfshade/Cthulhu1)
- [x] Session logged in investigation history
- [x] Remediation prompt generated

---

**Investigation Status:** COMPLETE
**Root Cause:** IDENTIFIED
**Remediation:** PROMPT GENERATED
