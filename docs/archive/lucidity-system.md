# MythosMUD lucidity System Specification

## 1. Overview

This document formalizes the MythosMUD lucidity mechanics inspired by classic Call of Cthulhu systems while accommodating persistent multiplayer play. lucidity (`LCD`) serves as a parallel resource to health, impacting perception, command reliability, and long-term character liabilities. The design emphasizes:

- A single intuitive LCD track with clear tier thresholds
- Passive environmental flux based on time, location, and party context
- Active gains and losses tied to narrative encounters, abilities, and recovery rituals
- Phenomenological feedback (hallucinations, phantom threats, command disruption)
- Fail-state handling that mirrors unconsciousness and death flows

Implementation notes throughout call out tracking requirements, cooldown expectations, and hooks for future balancing.

## 2. lucidity Scale, Tiers, and Catatonia

### 2.1 LCD Track

- **Numeric range:** +100 (utter composure) down to −100 (irrecoverable collapse)
- **Starting LCD:** 100 for newly created characters (subject to heritage modifiers later)
- **Floor/ceiling:** LCD cannot exceed 100 and can drop as low as −100
- **Negative values:** expose the character to catatonic rescue rules before final institutionalization

### 2.2 Tier Thresholds

| Tier              | LCD Range | Mechanical Theme                                          |
| ----------------- | --------- | --------------------------------------------------------- |
| Lucid             | 70 – 100  | No penalties; ambient descriptive hints only              |
| Uneasy            | 40 – 69   | Mild sensory distortion, heightened passive losses        |
| Fractured         | 20 – 39   | Frequent hallucinations, nascent command interference     |
| Deranged          | 1 – 19    | Severe misperception, high disruption, involuntary flight |
| Catatonic         | 0 – −99   | Immobilized; eligible for ally intervention               |
| Institutionalized | −100      | Sanitarium respawn with persistent liability              |

### 2.3 Catatonic Rescue Window

- Characters between −99 and 0 LCD are considered **catatonic** rather than dead.
- Allies may use `ground <target>` (working name) to stabilize the victim:
  - 30-second channel that can be interrupted by damage or hallucination events.
  - Success restores the target to LCD 1 (entering Deranged tier) and removes catatonia.
  - Cooldown: rescuer-specific 10 in-game minutes; target receives a 30-minute grace period before catatonia can recur.
- Failure (channel break or hostile interference) applies an additional −5 LCD to the target.
- LCD reaching −100 immediately triggers the Sanitarium fail state (Section 5.4).

## 3. Passive lucidity Flux

Passive LCD change is evaluated once per in-game minute. Modifiers stack additively unless noted.

### 3.1 Recovery Anchors

| Context                                                           | Modifier                                 | Notes                                                   |
| ----------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------- |
| Sun-bathed sanctuaries (temples, campus quads, bright safehouses) | +0.6 LCD/min (day), +0.3 LCD/min (night) | Requires ambient light level ≥ “bright”                 |
| Neutral civil zones (markets, libraries, lounges)                 | +0.2 LCD/min (08:00–18:00)               | No effect outside daytime                               |
| Active sacred rites (choirs, communal prayer)                     | +1.0 LCD/min                             | Limited to one completion per character per in-game day |
| Protected lodging (rented room, warded camp)                      | +0.2 LCD/min                             | Character must remain stationary and awake              |

### 3.2 Drain Zones

| Context                                                | Modifier                                 | Notes                                        |
| ------------------------------------------------------ | ---------------------------------------- | -------------------------------------------- |
| Haunted locales (graveyards, battlefields)             | −0.4 LCD/min (day), −0.8 LCD/min (night) | Drains doubled during eclipses               |
| Eldritch hotspots (portals, non-Euclidean chambers)    | −1.2 LCD/min                             | −1.5 LCD/min during cosmic events            |
| Liminal weather exposure (deep fog, dimensional storm) | −0.3 LCD/min                             | Applies outdoors only                        |
| Forsaken interiors (abandoned asylums, hospitals)      | −0.5 LCD/min                             | Reduced to −0.2 with an active warding charm |

### 3.3 Stabilizing Modifiers

- **Companion presence:** +0.1 LCD/min per lucid/uneasy companion in group (max +0.3). If any companion is Deranged or worse, group bonus flips to −0.2 LCD/min.
- **Lighting:** Handheld lantern or fixed electric lighting halves ambient drain values (round toward zero).
- **Adaptive resistance:** For every continuous 10 in-game minutes in the same room, passive drain magnitude drops by 25% (minimum 50% of original) to mitigate AFK griefing while still encouraging movement.

## 4. Active Interactions

### 4.1 Active LCD Loss Triggers

#### Encounter Shock Categories

| Category   | Examples                                  | First-time Loss | Repeat Loss | Notes                                      |
| ---------- | ----------------------------------------- | --------------- | ----------- | ------------------------------------------ |
| Disturbing | Ghouls, deep ones, corpse piles           | −6 LCD          | −2 LCD      | Track per creature archetype               |
| Horrific   | Star spawn, ritual sacrifices in progress | −12 LCD         | −5 LCD      | Applies when observer perceives full scene |
| Cosmic     | Great Old Ones, dimensional breaches      | −20 LCD         | −10 LCD     | Always inflicts a hallucination event      |

- Exposure is logged per character and creature archetype. First contact bonus applies if the character lacks prior “acclimation” record. After 5 repeat exposures, the loss stabilizes at half the repeat value (minimum −1).

#### Mythos Knowledge Events

| Event                                          | LCD Loss | Additional Effects                                                           |
| ---------------------------------------------- | -------- | ---------------------------------------------------------------------------- |
| Reading minor Mythos text / unsettling journal | −5 LCD   | Unlocks minor lore flag                                                      |
| Studying major grimoire                        | −10 LCD  | Adds *Forbidden Insight* tag; future Mythos spells cost −2 LCD less to learn |
| Learning a Mythos ritual (per spell)           | −8 LCD   | Ritual casts do **not** incur extra LCD; cost paid up front                  |
| Witnessing forbidden rite completion           | −12 LCD  | Forced Willpower save to avoid immediate hallucination                       |

Religious magic and folk remedies explicitly avoid LCD penalties.

#### NPC Abilities

- **Mind-rending attacks:** −3 LCD on failed Willpower save; success halves loss.
- **Eldritch shrieks:** −5 LCD (area), with a 20% chance to trigger involuntary flee for Deranged targets.
- **Dream invasion (sleep-based):** −8 LCD, bypasses passive recovery until target visits a sanctuary.

#### Environmental Events

- **Sudden reality shift (room transforms, temporal jump):** Flat −7 LCD.
- **Party member death within line of sight:** −4 LCD (−8 if caused by Mythos entity).

### 4.2 Active Recovery Actions

| Action                  | Requirements                                   | Effect                                                           | Cooldown                     |
| ----------------------- | ---------------------------------------------- | ---------------------------------------------------------------- | ---------------------------- |
| `pray`                  | At deity altar, offering item                  | +8 LCD instantly                                                 | 15 in-game minutes           |
| `meditate`              | Quiet location, uninterrupted 3-minute channel | +6 LCD over channel duration                                     | 10 minutes                   |
| `group solace`          | ≥3 players, sanctified zone, 60-second chant   | +4 LCD to participants, removes one minor hallucination          | 20 minutes (per participant) |
| `therapy session`       | Sanitarium NPC, pay 50 silver                  | +15 LCD; heals one liability stack stage                         | 2 sessions per in-game day   |
| `folk tonic` consumable | Brewed item                                    | +3 LCD instantly; grants +0.1 LCD/min buffer for next 10 minutes | Item-specific reuse timer    |

Active recovery cannot raise LCD above 100. Attempting a recovery action while Deranged doubles interruption chances from hallucination events (Section 5.1).

### 4.3 Curses and Liabilities

**Trigger:** When a single event causes ≥15 LCD loss (before mitigations) or when LCD crosses into a lower tier due to one event, roll on the liability table. Multiple liabilities can stack; duplicates deepen existing severity.

| Liability             | Effect                                                        | Removal Path                                                   |
| --------------------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| Night-Frayed Reflexes | −10% attack accuracy during in-game night                     | Complete a moonlit cleansing quest or 3 therapy sessions       |
| Murmuring Chorus      | Random intrusive whispers reduce incoming chat clarity by 25% | Perform group solace twice within 24 in-game hours             |
| Ritual Compulsion     | Must perform `ward` ritual daily or suffer −5 LCD tick        | Fulfill compulsion for 7 consecutive days or complete exorcism |
| Ethereal Chill        | −15% resistance to cold/void damage                           | Acquire hearthstone charm, then pray at volcano shrine         |
| Bleak Outlook         | Passive recovery reduced by 50%                               | Consume rare folk tonic + therapy combo within the same day    |

Liabilities persist through death and sanitarium resets unless explicitly cleared.

## 5. Phenomenology and Fail-State Feedback

### 5.1 Hallucination & Phantom Event Tables

| Tier      | Hallucination Frequency   | Event Palette                                                                                              |
| --------- | ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Uneasy    | 10% chance per room entry | Ambient whispers, fleeting shadows, misleading exit highlight                                              |
| Fractured | 25% chance per 30 seconds | Phantom hostile spawns (15% chance of non-damaging combat), fake NPC tells, room text overlays             |
| Deranged  | 45% chance per 20 seconds | Aggressive phantom mobs (attackable but vanish on hit), reversed compass directions, phantom damage popups |

- **Phantom hostiles:** Share a health bar equal to 1 HP; on attack they dissipate but consume commands, spell slots, and stamina. Combat log marks them as “[Phantom]” only after dismissal.
- **Muffled comms:** In Fractured tier, 30% of incoming chat lines lose punctuation; in Deranged tier, 10% of syllables are scrambled.

### 5.2 Command Disruption & Involuntary Actions

- **Misfires:** Starting at Fractured, 10% of complex commands (`cast`, `craft`, `sneak`) fizzle with a LCD warning. Deranged increases misfire chance to 25%.
- **Involuntary flee:** Deranged characters have a 20% chance to auto-flee when taking >15% max HP damage in one hit; cooldown 2 minutes.
- **Motor lock:** Catatonic characters cannot move or act until rescued or they hit −100 LCD.

### 5.3 Communication Dampening

- Whispered speech from Uneasy characters is flagged with `[strained]`.
- Fractured characters’ outgoing chat has a 20% chance to append Mythos glyphs (purely cosmetic but unsettling).
- Deranged characters cannot initiate `shout`; attempts instead create an echoing hallucination visible only to nearby Deranged players.

### 5.4 Sanitarium Fail State

When LCD reaches −100:

1. Character collapses; all active hallucination timers clear.
2. System auto-transports the character to Arkham Sanitarium after a 10-second fade (no player input).
3. Inventory handling mirrors standard death rules (drop table configurable per future design).
4. Attached liability increases one stage (up to max severity). If the character has no liabilities, roll once on the table in Section 4.3.
5. Character respawns at LCD 1 (Deranged tier) inside the sanitarium recovery ward.
6. A mandatory `debrief` interaction becomes available, granting narrative recap and optional immediate therapy session (counts against daily cap).

## 6. Tracking & Implementation Notes

- **Exposure ledger:** Store per-character dictionaries keyed by `entity_archetype`, `ritual_id`, and `lore_item_id` to determine first-time vs repeat LCD losses.
- **Passive loop:** Align LCD tick evaluation with existing stamina/health regen ticks to minimize scheduler load.
- **Hallucination controller:** Maintain a weighted queue to avoid repeating identical hallucinations within a 5-minute window for the same player.
- **Cooldown registry:** Centralize recovery-action cooldowns in player state so effects persist across reconnects.
- **Logging:** Route all LCD adjustments through the enhanced logging system (`get_logger`) with structured fields `san_change`, `reason`, `tier_before`, `tier_after`.

## 7. Balancing & Playtesting Roadmap

- **Initial tuning:** Focus on ensuring a typical 30-minute expedition through haunted zones results in net LCD change between −10 and −25 with attentive play.
- **Playtest milestones:**
  - Closed-group lucidity dungeon run to observe hallucination cadence
  - Stress test of group solace/therapy loops to prevent trivial farming
  - PvP edge cases (e.g., intentionally griefing others into catatonia)
- **Telemetry goals:** Track average LCD per tier, frequency of liabilities, time-to-rescue in catatonia, and sanitarium visits per player-week.
- **Future extensions:** Consider LCD-based skill trees (e.g., “Occult Fortitude”), personalized nightmares, or cross-tier cooperative abilities once baseline is stable.

Balancing should iterate alongside narrative content releases to maintain the intended mix of dread, agency, and camaraderie in the MythosMUD experience.
