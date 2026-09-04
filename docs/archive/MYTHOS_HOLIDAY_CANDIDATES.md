# Mythos Holiday Candidates

> Research log for Professor Wolfshade — prospective in-game observances drawn from Lovecraftian and wider Mythos lore.
> All dates assume alignment with the Mythos chronicle's compressed calendar; "Needs Alignment" indicates the source
> text gives only a season or circumstance.

## Canonical and Derived Observances

| Observance | Mythos Date (Gregorian anchor) | Source and Citation | Notes | Date Certainty |
| --- | --- | --- | --- | --- |
| Kingsport Yule Procession | Winter Solstice (approx 21 Dec) | Lovecraft, "The Festival," Weird Tales (Jan 1925) | Ancestor-led descent beneath Kingsport during the ancient Yuletide rite older than Christmas. | Explicit (solstice) |
| Cthulhu Cult – Feast of the Equinox | Spring Equinox (23 Mar 1925 in text) | Lovecraft, "The Call of Cthulhu," Section III | Equinoctial storms and tide surges; awakening attempt on equinox. | Explicit (equinox) |
| Cthulhu Cult – All-Hallows Vigil | All-Hallows (1 Nov) | Lovecraft, "The Call of Cthulhu," Section II | New Orleans raid broke up an annual swamp rite on All-Halloween. | Explicit (calendar date) |
| Dunwich May-Eve Sabbat | Walpurgis Night (30 Apr–1 May) | Lovecraft, "The Dunwich Horror," Weird Tales (Apr 1929) | Wizard Whateley opens Yog-Sothoth's gateway on May-Eve. | Explicit (May-Eve) |
| Dunwich Lammas Convergence | Lammas (1 Aug) | Lovecraft, "The Dunwich Horror" | 1928 barn-breaking on Lammas Night for final summoning. | Explicit (Lammas) |
| Arkham Witch-Cult Rite | Walpurgis Night (30 Apr) | Lovecraft, "The Dreams in the Witch House" (Jul 1933) | Keziah Mason and Brown Jenkin on Walpurgis Nacht. | Explicit (Walpurgis) |
| Akeley's Warning – Mi-Go Gathering | May Day (1 May) | Lovecraft, "The Whisperer in Darkness" (Aug 1931) | Rural congregations each May Day when Mi-Go increase activity. | Implicit (stated day) |
| Esoteric Order of Dagon Offerings | Easter + 7 days | Lovecraft, "The Shadow over Innsmouth" (Apr 1936) | Devil Reef sacrifices a week after Easter for spring tides. | Anchored (derivative) |
| Feast of Yig | Night before Autumn Equinox (approx 21 Sep) | Lovecraft and Bishop, "The Curse of Yig" (Nov 1929) | Father of Serpents appeasement as harvest ends. | Anchored (derivative) |
| Festival of the Black Goat | New moon nights in deep woods | Derleth / Chaosium tradition | Shub-Niggurath worshippers at the dark of the moon. | Derived (lunar phase) |
| Sleeper's Vigil of R'lyeh | Star-aligned equinox (13–23 Mar window) | Lovecraft, "The Call of Cthulhu" | When the stars are right; oceanic anomalies near equinoxes. | Derived (astral) |
| Ghoulish Necropolis Moot | 24 Oct (week before Halloween) | Lovecraft and Price, "Through the Gates of the Silver Key" | Subterranean conclave before All Hallows. | Anchored (derivative) |

## Implementation Notes

**Overlap Management:** Walpurgis (30 Apr) appears twice (Arkham witches, Dunwich sabbat). Treat as region-specific
variants sharing buff templates with localized flavor.

**Duration Constraints:** For compliance with the two-day holiday cap, keep each observance to at most 48 Mythos hours
even if the lore implies longer revels.

**Event Hooks:** Map rituals to gameplay beats (for example cult raids, NPC migrations, lucidity effects). Use
`tradition` values (`kingsport`, `cthulhu_cult`, `witch_cult`, and so on) in holiday JSON for filtering.

**Needs Alignment Entries:** propose alignment during design sprint—for example, tie Innsmouth offerings to the first
spring tide after the Vernal Equinox and the autumn equinox supermoon.

### Narrative Flavor Seeds

**Sevenfold Tide Offering (Innsmouth):** One week after Easter, Innsmouth foghorns fall silent as Deep One processions
slip from Shadow Alley to the reef. Fishing hauls double, but townsfolk whisper of wet footprints leading back inland.
Players assisting the Order gain rare pearls at the cost of mounting suspicion.

**Equinox Serpent Vigil (Feast of Yig):** On the eve of the autumn equinox, prairie winds carry a rattling susurrus.
Snake effigies decorate crossroads; offending reptiles must be placated with fresh milk and braided corn dolls.
Travelers who ignore the rites risk waking to scales etched into their skin and lucidity erosion.

**Ghoulmarket Convocation (24 Oct):** A week before Halloween, catacomb doors grind open beneath Arkham and Kingsport.
Ghouls arrange a neutral-market parley where human artisans trade grave goods for rare alchemical reagents. Surface
dwellers who prove respectful may secure forbidden lore—so long as they stomach the banquet.

## Opportunities for Expansion

**Chaosium Supplements:** Review Call of Cthulhu RPG materials (for example *Arkham Unveiled*, *Secrets of Innsmouth*)
for additional cult calendars once licensing considerations are cleared.

**Regional Variants:** Create derivative observances (for example Innsmouth "Gilman Night" boat festival, Kingsport
"Harbor Mist Vigil") to fill calendar gaps without canon conflict.

**Dynamic Star Alignments:** Leverage the MythosChronicle to schedule "star right" anomalies using astronomical
calculations for bonus unpredictable events.
