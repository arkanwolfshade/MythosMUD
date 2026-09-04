# Lucidity Communication Dampening

> 23 nodes

## Key Concepts

- **apply_communication_dampening()** (15 connections) — `server/services/lucidity_communication_dampening.py`
- **lucidity_communication_dampening.py** (11 connections) — `server/services/lucidity_communication_dampening.py`
- **test_lucidity_communication_dampening.py** (11 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **DampeningResult** (8 connections) — `server/services/lucidity_communication_dampening.py`
- **_apply_receiver_effects()** (5 connections) — `server/services/lucidity_communication_dampening.py`
- **should_block_shout()** (4 connections) — `server/services/lucidity_communication_dampening.py`
- **patch** (4 connections)
- **_apply_sender_effects()** (3 connections) — `server/services/lucidity_communication_dampening.py`
- **_maybe_muffle_fractured_message()** (3 connections) — `server/services/lucidity_communication_dampening.py`
- **_maybe_scramble_deranged_message()** (3 connections) — `server/services/lucidity_communication_dampening.py`
- **test_deranged_incoming_scrambles_words()** (3 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_incoming_strips_punctuation()** (3 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_appends_glyph()** (3 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_no_glyph_when_roll_high()** (3 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_deranged_shout_blocked()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_should_block_shout_deranged()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_whisper_uneasy_adds_strained_tag()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **TypedDict** (1 connections)
- **Communication dampening utilities for lucidity system. Implements communication…** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Check if shout should be blocked based on tier.** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Filtered chat payload after lucidity-tier effects.** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Apply communication dampening based on lucidity tiers. Args: message: Original…** (1 connections) — `server/services/lucidity_communication_dampening.py`
- **Unit tests for lucidity communication dampening.** (1 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Nats Message Handler Broadcast](Nats_Message_Handler_Broadcast.md) (2 shared connections)

## Source Files

- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*