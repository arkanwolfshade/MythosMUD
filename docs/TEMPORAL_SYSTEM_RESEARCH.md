<!-- Mythic Temporal Spec Draft — prepared for Prof. Wolfshade -->
# MythosMUD Temporal Compression Briefing

## 1. Research Synthesis

- **DikuMUD baseline compression** – 30 real-world minutes advance a full 24-hour in-game cycle, bundled with weather ticks and an alternate calendar; demonstrates how even venerable codebases decouple world rhythm from wall clocks while keeping scheduling simple.[^1]
- **Wheel of Time MUD (Farede calendar)** – adopts 13 months of 28 days (364-day year) with fixed 24-tick days, illustrating how lore-aligned structures can diverge from Gregorian norms yet remain predictable for storytellers.[^2]
- **Builder best-practice discussion** – designers report success with a 1 game hour : 4 real minutes ratio (96-minute days, 30-day months, 12-month years) and stress staggering cycles so recurring events wander across real-world hours, plus leveraging seasons for crafting gates (e.g., spring planting, autumn harvest).[^3]

### Key takeaways

- Favor ratios that make a complete day shorter than 24 real hours so event windows circulate globally.
- Keep calendar arithmetic approachable (uniform month lengths, modest year span) to reduce quest design friction.
- Tie environmental narration and activity availability to time-of-day and season changes so compression feels meaningful rather than cosmetic.

## 2. Mythos Time Model Draft

- **Compression ratio** – Anchor 9.6 in-game hours per real hour (as configured in `server/config/models.py`). Outcomes:
  - 1 in-game hour = 1/9.6 = 0.10417 real hours = 6.25 real minutes.
  - 1 in-game day (24 hours) = 24/9.6 = 2.5 real hours = 150 real minutes (2h30m), nudging daily landmarks forward by 2h30m each real day so no cohort monopolizes midnight festivals.
- **Calendar structure**
  - The implementation uses standard Python `datetime`, which means standard Gregorian calendar (365/366 days per year).
  - 6 Mythos days per week to echo hexadic occult numerology (calculated from day-of-month).
  - Standard month lengths (28-31 days) as per Gregorian calendar.
  - 12 months per Mythos year; full year (365 days) elapses in 365 × 2.5 = 912.5 real hours (~38 real days).
- **Holiday mirroring**
  - Retain Gregorian month names and holiday labels, but allow them to recur whenever that month/day combination rolls around. Real-world December 25th becomes the canonical “anchor”; every time Mythos calendar hits `December 25`, trigger the Yuletide events—even though it may happen multiple times per real month.
  - Maintain a real-world scheduler mapping actual dates to “spotlight” holiday runs so we can optionally mark one cycle per real year as the “prime” celebration with extra spectacle.
- **Day-night cadence**
  - Dawn at 06:00 Mythos (6 × 6.25 = 37.5 real minutes into each cycle); dusk at 18:00 Mythos (18 × 6.25 = 112.5 real minutes).
  - Environmental descriptions: adjust room lighting text, ambient audio cues, and lucidity mechanics around thresholds (pre-dawn haze, witching hour 23:00–01:00 Mythos).
  - NPC behaviors: shops staffed 08:00–20:00 Mythos, night watch patrols 20:00–04:00, eldritch phenomena peaking during the witching hour.
- **Seasonal beats**
  - Standard Gregorian months inherit real-world season of their anchor (e.g., March = vernal rites). With the accelerated cycle, players encounter seasonal content roughly every 38 real days (one in-game year).
  - Introduce season-locked systems (farm plots, migration events, cult ceremonies) to showcase accelerated cycles without overwhelming players—cap availability windows to a minimum of two real hours.

### Major religious observances

- **Catholic solemnities (canon 1246)**[^4]

  | Observance                       | Gregorian anchor                                                    | Notes                                           |
  | -------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
  | Mary, Mother of God              | January 1                                                           | Opens the civil year with Marian devotion       |
  | Epiphany                         | January 6 (transferable)                                            | Manifestation of Christ to the nations          |
  | Saint Joseph                     | March 19                                                            | Patron of the universal Church                  |
  | Easter Sunday                    | First Sunday after the first full moon following the vernal equinox | Central Paschal celebration of the Resurrection |
  | All Saints                       | November 1                                                          | Communal remembrance of sanctified lives        |
  | Immaculate Conception            | December 8                                                          | Highlights Marian doctrine central to Advent    |
  | Nativity of the Lord (Christmas) | December 25                                                         | Core Christological feast for winter cycle      |

- **Islamic festivals**[^5]

  | Observance                | Hijri timing                       | Gregorian anchor (approx.)              | Notes                                  |
  | ------------------------- | ---------------------------------- | --------------------------------------- | -------------------------------------- |
  | Ramadan                   | Month of Ramadan                   | Shifts ~11 days earlier each solar year | Month-long fast with nightly rituals   |
  | Eid al-Fitr               | 1 Shawwal                          | Immediately after Ramadan               | Joyous feast marking fast’s end        |
  | Hajj peak & Day of Arafah | 9 Dhu al-Hijjah                    | Two lunar months after Ramadan          | Pilgrimage climax preceding sacrifice  |
  | Eid al-Adha               | 10 Dhu al-Hijjah                   | Follows Day of Arafah                   | Sacrificial commemoration tied to Hajj |
  | Islamic New Year          | 1 Muharram                         | Marks Hijri year transition             | Reflective reset for communal planning |
  | Mawlid al-Nabi            | 12 Rabi al-Awwal (Sunni tradition) | Shifts by lunar cycle                   | Celebration of the Prophet’s birth     |

- **Jewish High Holy Days and festivals**[^6]

  | Observance                      | Hebrew timing                 | Gregorian anchor (approx.) | Notes                                            |
  | ------------------------------- | ----------------------------- | -------------------------- | ------------------------------------------------ |
  | Rosh Hashanah                   | 1–2 Tishrei                   | Early autumn               | Jewish New Year launching Days of Awe            |
  | Yom Kippur                      | 10 Tishrei                    | Early autumn               | Day of Atonement, fasting and repentance         |
  | Sukkot                          | 15–21 Tishrei                 | Mid-autumn                 | Pilgrimage feast with temporary shelters         |
  | Shemini Atzeret & Simchat Torah | 22–23 Tishrei                 | Mid-autumn                 | Culminates Torah reading cycle                   |
  | Passover (Pesach)               | 15–22 Nisan                   | Spring                     | Commemorates Exodus with ritual meals            |
  | Shavuot                         | 6–7 Sivan                     | Late spring                | Marks Torah giving and harvest first fruits      |
  | Hanukkah                        | 25 Kislev–2 Tevet             | Early winter               | Festival of Lights recalling Temple rededication |
  | Purim                           | 14 Adar (15 in walled cities) | Late winter                | Celebration of Esther narrative and deliverance  |

- **Neo-pagan Wheel of the Year**[^7]

  | Sabbat                  | Gregorian anchor      | Season in Mythos cycle | Notes                                      |
  | ----------------------- | --------------------- | ---------------------- | ------------------------------------------ |
  | Imbolc                  | February 1–2          | Late winter thaw       | Hearth-fire rites anticipating spring      |
  | Ostara (Vernal Equinox) | Around March 20       | Early spring balance   | Equinox ceremonies for renewal             |
  | Beltane                 | April 30–May 1        | Mid-spring bloom       | Fertility fires, maypole revels            |
  | Litha (Summer Solstice) | Around June 21        | High summer zenith     | Longest-day sun vigils                     |
  | Lughnasadh / Lammas     | August 1              | Early harvest          | First-fruits offerings to agrarian deities |
  | Mabon (Autumn Equinox)  | Around September 22   | Mid-harvest balance    | Gratitude rites at equal night             |
  | Samhain                 | October 31–November 1 | Late harvest veil      | Ancestor veneration, veil-thinning         |
  | Yule (Winter Solstice)  | Around December 21    | Deep winter            | Rebirth of the sun amid darkness           |

## 3. Implementation Blueprint

- **Core services**
  - Introduce `server/time/time_service.py` housing a `MythosChronicle` singleton for deterministic conversions between UTC timestamps and Mythos calendar units (year, month, day, hour, minute) using the 1:9.6 scale.
  - Provide utility APIs:
    - `get_current_mythos_datetime()`
    - `to_mythos_datetime(dt: datetime)`
    - `to_real_datetime(mythos_dt)`
    - `advance_mythos(duration: MythosDelta)`
  - Expose formatted strings for UI (`format_mythos_clock`, `format_mythos_calendar`).
- **Configuration & persistence**
  - Persist epoch anchor (e.g., 2025-01-01 00:00 UTC ↔ Mythos Year 100, January 1 00:00) in config to keep deployments deterministic.
- Store holiday metadata in `data/<environment>/calendar/holidays.json` (e.g., `data/local/calendar/holidays.json`), capturing Gregorian anchor date, Mythos month/day names, recurrence flags, and optional “prime cycle” decorators.
  - Cache frequently used conversions with structlog-aware tracing (`get_logger` from enhanced logging).
- **Integration points**
  - **Event scheduler**: extend existing task registry (`server/app/task_registry.py`) with Mythos-aware cron expressions so designers can schedule on Mythos midnight, equinox markers, etc.
  - **Narrative hooks**: room descriptions (likely under `server/game/room_service.py`) should request current Mythos time to swap textual variants.
  - **NPC AI**: inject time checks into behavior services (`server/game/npc_*.py`) for shift-based routines.
  - **Client updates**: expose Mythos clock via websocket payloads so UI can render both Mythos time and real-world reference.
- **Testing strategy**
  - Unit tests in `server/tests/time/` validating conversion math, leap handling at month/year boundaries, and ensuring wrap-around after epochs.
  - Property-based tests to verify round-trip fidelity (`real → mythos → real`).
  - Integration tests covering scheduler triggers around day/night transitions and holiday recurrence rotation.
  - Load-test scenario to ensure accelerated cycling doesn’t overload logging or event queues (simulate multiple Mythos days in quick succession).

## 4. Client HUD Implementation

- **Chronicle bootstrap**
  - The client now calls `/game/time` once after authentication to hydrate the HUD immediately instead of waiting for the next hour tick.
  - The response mirrors the broadcast payload so designers can experiment with calendar data without reconnecting.
- **Mythos hour broadcasts**
  - `MythosTimeEventConsumer` publishes `mythos_time_update` SSE packets every accelerated hour (and whenever a holiday/schedule transition occurs) via `broadcast_game_event`.
  - Each payload includes clock string, date line, daypart, season, schedule summaries, and serialized holiday metadata.
- **HUD rendering**
  - `MythosTimeHud` displays connection state, formatted Mythos time, and contextual cues (daypart/season/witching-hour flag).
  - Active holidays render through `HolidayBanner`, using tradition-specific palettes and badge lists for `bonus_tags`.
  - When the daypart or holiday roster changes, `GameTerminalWithPanels` injects atmospheric system messages (e.g., witching hour warnings, holiday start/end notifications) so log archives capture the state shifts.

---
[^1]: <https://www.mudconnect.com/mudfaq/mudfaq-p4.html>
[^2]: <https://wotmud.fandom.com/wiki/Calendar>
[^3]: <https://www.mudbytes.net/forum/comment/39632/>
[^4]: <https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib4-cann1244-1258_en.html#TITLE_I.>
[^5]: <https://www.bbc.co.uk/religion/religions/islam/holydays/>
[^6]: <https://www.britannica.com/topic/Jewish-religious-year>
[^7]: <https://www.britannica.com/topic/Wicca>
