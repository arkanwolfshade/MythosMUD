"""Prose source for the Arkham street grid (#829).

Every street gets a written character expressed as a handful of segment variants
plus a ``corner`` fragment used to build intersection descriptions. Roughly 150
written pieces cover all 481 rooms, and no two adjacent rooms read identically.

Register, matched to the existing Derby Street room in the seed data: two
sentences, concrete period architecture first, then one detail that is quietly
wrong. No gore, no exclamation, no winking. Arkham is a real New England mill
town that happens to be rotting from underneath.

``scripts/generate_arkham_grid.py`` consumes this; ``VOICES`` must have an entry
for every street key in ``arkham_grid_spec.STREETS``, and ``EXTRA_PROSE`` one for
every key in ``arkham_grid_spec.EXTRAS``. The generator fails loudly if not.
"""

from __future__ import annotations

from typing import NamedTuple


class Voice(NamedTuple):
    """One street's written character."""

    corner: str  # noun phrase for intersection prose: "the shuttered brownstones of Derby Street"
    segments: tuple[str, ...]  # cycled by position along the street


VOICES: dict[str, Voice] = {
    # ---------------------------------------------------------------- north
    "apple": Voice(
        "the rutted cart-track of Apple Lane",
        (
            "The lane runs unpaved along the town's northern hem, its ruts filled with standing water that never seems to drain. Beyond the hedgerow the land rises toward the Innsmouth road.",
            "Orchard remnants line the verge, the trees long unpruned and bearing nothing. A low stone wall follows the lane, its capstones displaced as though something heavy had climbed over.",
            "Wheel tracks cut deep here, sunk into ground that stays soft in the driest month. The air carries salt from somewhere considerably further than the coast has any business being.",
            "The last streetlamp in Arkham stands at this stretch, unlit, its glass long gone. Past it the lane narrows and the dark begins in earnest.",
        ),
    ),
    "derby": Voice(
        "the steep gables of Derby Street",
        (
            "Victorian houses with steep gables and narrow windows line both sides, their dark facades broken only by the occasional flicker of candlelight behind drawn curtains.",
            "A row of shuttered brownstones stands shoulder to shoulder, stoops swept clean and doors uniformly shut. Someone has recently repainted the numbers, and got two of them wrong.",
            "The paving has buckled where roots pushed through, and ailanthus grows from a crack wide enough to take a boot. Nobody has troubled to repair it in some years.",
            "Gas lamps stand at uneven intervals along the walk, two of them leaning inward as though conferring. Their light does not carry as far as it should.",
        ),
    ),
    "curwen": Voice(
        "the crowded frontages of Curwen Street",
        (
            "Narrow houses crowd the street, built so close that their eaves nearly touch above the walk. The gap admits a thin grey ribbon of sky and very little else.",
            "Shopfronts occupy the ground floors, their goods unremarkable and their proprietors uninterested. Above them the residential storeys keep their blinds drawn at every hour.",
            "The street bears an old name that older residents decline to explain. Its cobbles are darker than the surrounding streets, and rain stands on them in curious patterns.",
            "A drain grate here breathes cold air upward even in summer. The houses nearest it have bricked over their ground-floor windows.",
        ),
    ),
    "hyde": Voice(
        "the tidy brick terraces of Hyde Street",
        (
            "Brick terraces run in a tidy line, each with a scrubbed step and a brass knocker. The tidiness has the quality of something maintained against an argument.",
            "Window boxes hold geraniums that do markedly better than the season allows. Their owners water them after dark.",
            "The street is quiet in a way that suggests the quiet is being kept rather than merely happening. Even the gulls give it a wide berth.",
        ),
    ),
    "whateley": Voice(
        "the sagging frame houses of Whateley Street",
        (
            "Frame houses sag toward the street, their clapboards silvered and their porches leaning. The family name on the street sign is not one spoken warmly in Arkham.",
            "Washing hangs on lines strung between the houses, grey and unmoving in air that will not stir. Nobody comes out to collect it.",
            "The paving gives way to packed dirt partway along, and stays that way. This end of town is not much visited by the town's improvers.",
        ),
    ),
    "armitage": Voice(
        "the respectable brick of Armitage Street",
        (
            "Respectable brick houses with fanlights above their doors suggest an Arkham that still believes in itself. The belief is thinner at the eastern end.",
            "Iron railings run the length of the walk, their finials shaped as acorns save for a short stretch where they are shaped as something else.",
            "The street takes the university's overflow: lodgings for junior faculty, and the sort of bookshop that keeps irregular hours.",
            "Elms arch overhead, planted when the century was young. Their leaves turn earlier here than on the neighbouring streets, and fall all in one night.",
        ),
    ),
    "high_ln": Voice(
        "the close brick walls of High Lane",
        (
            "The lane is barely wide enough for a cart, hemmed by brick on both sides. Sound behaves oddly in it, arriving a beat later than it should.",
            "Service doors and coal hatches punctuate the walls, most of them painted shut. One stands ajar onto a darkness that does not resolve.",
            "Rainwater runs the length of the lane's centre channel and vanishes into a grate that no municipal record accounts for.",
        ),
    ),
    "water": Voice(
        "the soot-stained warehouses of Water Street",
        (
            "Warehouses front the street with loading doors and rusted hoists, their brick stained black by decades of rail soot. The river runs close and smells of it.",
            "Handcarts stand abandoned along the kerb. The cobbles here are slick with something that is mostly river and not entirely.",
            "The embankment rises beyond the buildings, carrying the Boston and Maine line above the rooftops. Trains pass without slowing.",
            "Gulls congregate on the warehouse ridgelines in numbers the river cannot possibly support, and do not call.",
        ),
    ),
    # ---------------------------------------------------------------- south
    "river": Voice(
        "the damp frontages of River Street",
        (
            "The street follows the Miskatonic's southern bank, its buildings damp to the second storey. The waterline on the brick is higher than any recorded flood.",
            "Boathouses and chandlers occupy the frontage, most shuttered. The river moves past with the unhurried confidence of something very old.",
            "Mist comes off the water here at all hours and pools at knee height before dispersing. It is colder than the water it comes from.",
            "Westward the street loses its paving and becomes the Aylesbury road, which goes to Dunwich, which is its own problem.",
        ),
    ),
    "church": Voice(
        "the sober stonework of Church Street",
        (
            "Sober grey stonework and a clean-swept walk give the street its name's worth of dignity. The churches here are old and their congregations older.",
            "Railings enclose small burying grounds between the buildings, the stones tilted and their inscriptions worn past reading. The grass on them grows thick.",
            "A bell sounds the hour from somewhere west, half a minute late and one note short of true.",
        ),
    ),
    "main": Voice(
        "the broad commercial front of Main Street",
        (
            "Arkham's principal thoroughfare, broad enough for two carriages and lined with the town's better shopfronts. It is busy in a way the rest of Arkham is not.",
            "Plate glass and painted signboards make a determined show of ordinary commerce. Behind them the buildings are considerably older than their frontages admit.",
            "The paving is granite block here, laid properly and kept so. It rings underfoot with a hollowness that suggests the cellars run deep.",
            "Trolley rails are set into the street, polished bright, though no trolley has run in Arkham within living memory.",
        ),
    ),
    "crane": Voice(
        "the ivy-hung wall of Crane Street",
        (
            "A short street along the university's western wall, hung with ivy that keeps its leaves through winter. The wall is older than the university.",
            "Students' lodgings face the wall across the narrow way, their windows lit at all hours and their curtains seldom drawn.",
        ),
    ),
    "lich": Voice(
        "the graveyard railings of Lich Street",
        (
            "The street runs along the Old Arkham Graveyard's iron railings, close enough to read the nearer stones. The name is older than the graveyard and means what it appears to mean.",
            "Nothing fronts the street on its northern side but the burying ground. The southern side has built no windows facing it.",
        ),
    ),
    "college": Voice(
        "the gaslit elms of College Street",
        (
            "Elms and gas lamps line the approach to Miskatonic University, and the light through the leaves makes shifting patterns on the walk. The patterns do not always match the leaves.",
            "Gothic spires loom above the rooflines, their shadows stretching across the pavement like grasping fingers. The air carries old paper and something underneath it.",
            "Undergraduates pass in twos and threes, talking loudly about nothing. The noise is a comfort and they seem to know it.",
            "Iron gates stand open onto the quadrangle, their hinges maintained with a diligence the rest of the university does not show.",
        ),
    ),
    "pickman": Voice(
        "the close-set lodging houses of Pickman Street",
        (
            "Lodging houses and small workshops crowd the street, their signage hand-painted and frequently repainted. Tenants here do not stay long.",
            "A basement entry drops below the walk at intervals, each with its own iron rail. Several have been boarded, and the boards are new.",
            "The street bears a name that a certain Boston painter made unwelcome, and the residents have petitioned twice to change it.",
            "Handbills paper the wall of a corner building several layers deep, the topmost advertising a lecture that has already happened.",
        ),
    ),
    "high_st": Voice(
        "the plain shopfronts of High Street",
        (
            "Plain shopfronts serve the southern wards: a grocer, a cobbler, a chemist with a window of coloured glass jars. Ordinary trade, ordinarily conducted.",
            "The street climbs almost imperceptibly toward the east. Water spilled here runs the wrong way.",
            "Awnings are cranked out over the walk against a sun that seldom reaches this far down.",
            "A horse trough stands at the kerb, kept full by no one in particular. The water in it is always cold and never freezes.",
        ),
    ),
    "saltonstall": Voice(
        "the shuttered row houses of Saltonstall Street",
        (
            "Row houses run the length of the street, uniform and shuttered, their shared walls carrying sound between them. The residents have learned not to comment on what they hear.",
            "A cast-iron pump stands at the kerb, disused, its handle chained. The chain is not rusted.",
            "Doorsteps are scrubbed white with sand every morning, on every house, without exception or discussion.",
            "Coal chutes open onto the walk at regular intervals, their iron lids worn bright. One of them is not a coal chute.",
        ),
    ),
    "miskatonic": Voice(
        "the wide unkept verge of Miskatonic Avenue",
        (
            "The avenue is wider than its traffic warrants, laid out in optimism and never filled. Grass grows along the centre where paving was never finished.",
            "Larger houses stand back from the road behind low walls, their gardens gone to seed. Several have been divided into apartments; several have not been divided into anything.",
            "The avenue shares the river's name without touching the river, which residents find either charming or troubling depending on how long they have lived here.",
            "A stone horse block survives at one kerb, its top dished by a century of boots and its inscription entirely gone.",
        ),
    ),
    "washington": Voice(
        "the fraying southern edge of Washington Street",
        (
            "The town's southern boundary, where the paving frays into the Boston and Kingsport roads. Buildings thin out and the fields begin.",
            "Milestones stand along the verge, their carved distances no longer agreeing with one another or with the map.",
            "Wind comes off the open country here with nothing to break it, carrying the smell of turned earth and, faintly, of the sea.",
            "Fence posts march away from the street into the fields, carrying no wire and enclosing nothing.",
        ),
    ),
    # -------------------------------------------------- north-south, north
    "brown": Voice(
        "the narrow doorways of Brown Street",
        (
            "A narrow residential street of identical doorways, distinguishable only by their numbers. Two of the numbers repeat.",
            "Chimney pots crowd the rooflines above, far more of them than the houses below could need.",
            "The street runs straight from the lane to the river with no deviation, which in Arkham is itself unusual.",
        ),
    ),
    "jenkin": Voice(
        "the crooked gables of Jenkin Street",
        (
            "The houses lean gently toward one another, their gables meeting at angles no builder intended. One garret window is shuttered from the inside.",
            "The street is named for a family that left Arkham abruptly and completely, and whose house is still standing and still empty.",
            "Rats keep to this street in preference to the alleys, and move with more purpose than rats generally manage.",
        ),
    ),
    "gedney": Voice(
        "the soot-dark brick of Gedney Street",
        (
            "Brick tenements rise four storeys, their walls dark with a century of coal smoke. Lines of washing cross the street overhead.",
            "The stairwells are lit by a single window each and smell of cabbage, damp plaster, and something sweeter beneath.",
            "Children play in the street until dusk, at which point they go in together, all at once, without being called.",
        ),
    ),
    "dyer": Voice(
        "the short brick run of Dyer Street",
        (
            "A short connecting street of no particular character, brick-fronted and briskly walked through rather than lingered in.",
            "It carries the name of an Antarctic geologist the university would prefer not to discuss.",
        ),
    ),
    "high_alley": Voice(
        "the cramped brick of High Alley",
        (
            "An alley barely wide enough for one, brick close on either side, running blind toward Independence Square. What light reaches the ground arrives grey.",
        ),
    ),
    "federal": Voice(
        "the stone stoops of Federal Street",
        (
            "Federal-style houses with fanlight doors and granite stoops keep up the appearance of the republic's better years. The appearance is well maintained.",
            "Boot scrapers stand beside each door, worn deep by use, though the street has been paved for sixty years.",
        ),
    ),
    "noyes": Voice(
        "the flat-fronted houses of Noyes Street",
        (
            "Flat-fronted houses in an unbroken line, their windows all the same size and all the same distance apart. The effect is restful and then, after a moment, not.",
            "A single tree grows midway along, far larger than its allotted square of earth should support.",
        ),
    ),
    "halsey": Voice(
        "the high blank walls of Halsey Street",
        (
            "Warehouse walls rise blank and windowless on the eastern side, the western given over to narrow houses. The street is always in shadow.",
            "Freight doors open onto the walk at intervals, their tracks greased and their padlocks new.",
            "The street ends at Water Street and the embankment, where the rail line cuts the town off from its own river.",
        ),
    ),
    # ----------------------------------------------- north-south, crossings
    "west": Voice(
        "the long straight run of West Street",
        (
            "One of the three streets that runs the whole length of Arkham, north hem to southern boundary. It does not bend once.",
            "The houses change character every few blocks without the street itself changing at all: brick, then frame, then brick again.",
            "Carters use this street by preference, and their traffic has worn the centre paving into a shallow trough.",
            "Streetlamps are newer here than elsewhere, replaced by the town in a fit of civic feeling. They are still not quite bright enough.",
        ),
    ),
    "garrison": Voice(
        "the broad spine of Garrison Street",
        (
            "Arkham's north-south spine, broad and busy, carrying most of what the town moves between its halves.",
            "The street is named for a militia muster that the town histories record twice, with different dates and different outcomes.",
            "Shopfronts and offices front the street in a solid commercial wall, their upper storeys given to clerks and copyists.",
            "Its granite kerbs are set deep and true, laid by men who expected the street to outlast them, and were right.",
        ),
    ),
    "peabody": Voice(
        "the wide eastern artery of Peabody Avenue",
        (
            "A wide avenue running the town's eastern length, laid out for traffic that has not yet materialised. Its footways are generous and empty.",
            "Plane trees line both sides, pollarded into knuckled stumps each winter and each spring putting up more growth than they lost.",
            "The avenue carries the Kingsport road south out of town, and takes on that road's character well before it leaves.",
            "Iron bollards separate walk from carriageway, each cast with the town seal, several of them cast with something else.",
        ),
    ),
    # -------------------------------------------------- north-south, south
    "hill": Voice(
        "the steep pitch of Hill Street",
        (
            "The street climbs Arkham's western rise steeply enough to need steps in its footway. From the top, the town lies grey below.",
            "Retaining walls hold back the hillside, bulging in places where the earth has pressed harder than expected.",
            "Hangman's Hill stands above the street's northern end, and the street does not go up to meet it.",
        ),
    ),
    "boundary": Voice(
        "the old stone wall of Boundary Street",
        (
            "A cobblestone street marking the edge of Miskatonic University's grounds. Ancient stone walls line it, covered in ivy that seems to move with a purpose of its own.",
            "The street's name predates the university, the town charter, and the wall itself. Nobody can say what boundary it originally marked.",
            "Gas lamps are set into the wall at long intervals, their brackets much older than their lamps.",
        ),
    ),
    "parsonage": Voice(
        "the quiet frontage of Parsonage Street",
        (
            "A quiet street of clergy houses and church properties, its frontage uniformly grey and uniformly shut. The street runs the town's length in two separate pieces.",
            "Low iron gates open onto small walled gardens, each with a bench, none of them occupied.",
            "The Sanatorium stands at the street's northern head, and the street approaches it directly and without ornament.",
            "Sound carries strangely here: footsteps arrive before their walker and continue after.",
        ),
    ),
    "walnut": Voice(
        "the deep-shaded run of Walnut Street",
        (
            "Black walnut trees give the street its name and a deep, cool shade that persists well past the hour it should.",
            "Their fallen husks stain the paving black underfoot, and the stain does not wash away.",
            "Modest houses stand back behind small front gardens, well kept and entirely without ornament.",
        ),
    ),
    "powder": Voice(
        "the low brick sheds of Powder Mills Street",
        (
            "The street runs toward the old powder mills, and its buildings are low, thick-walled, and set well apart, as such buildings are.",
            "The mills have been closed for forty years. The walls are still standing and still show no crack.",
            "The ground here is scorched in patches that no amount of rain has faded.",
        ),
    ),
    "frenchhill": Voice(
        "the steep decay of French Hill Street",
        (
            "The street climbs French Hill past houses that were fine once and are now divided, sublet, and sagging. The hill keeps its own hours.",
            "Steps replace paving for a stretch, their treads worn into shallow bowls. The wear is greater than the traffic explains.",
            "This is the oldest-settled ground in Arkham, and the most thoroughly gone to seed.",
        ),
    ),
    "sentinel": Voice(
        "the blind gable ends of Sentinel Street",
        (
            "Houses turn their gable ends to the street, presenting blank triangles of clapboard and no windows at all. The arrangement is said to be traditional.",
            "The street is straight, narrow, and entirely without trees, and one can see along its whole length from either end.",
            "Its name appears on no deed older than 1790, and on every deed since.",
        ),
    ),
    "east": Voice(
        "the frayed eastern edge of East Street",
        (
            "Arkham's eastern limit, where the town gives out into scrub and the odd shed. The paving stops well before the houses do.",
            "Yards back onto open ground here, their fences patched with whatever came to hand.",
            "From this street the marshes are visible on a clear day, and on most days they are not clear.",
        ),
    ),
}


# Intersection prose. ``{a}`` and ``{b}`` take the two streets' ``corner`` fragments.
#
# Corner fragments are a mix of singular and plural noun phrases ("the steep gables",
# "the quiet frontage"), so no template may make one the subject of a verb - that
# produced "the steep gables of Derby Street runs into...". Every template below
# either uses a compound subject with a plural verb or keeps both streets inside a
# prepositional phrase, which is agreement-safe for either number.
CORNER_TEMPLATES: tuple[str, ...] = (
    "{a} and {b} cross here. The corner stone is worn smooth on one face and sharp on the other.",
    "The corner of {a} and {b}. A drain at the kerb takes more water than the street above it sheds.",
    "A crossing of {a} and {b}. The lamp on this corner is lit before dusk and out before dawn.",
    "{a} and {b} meet here, and not quite at a right angle. Nobody has thought it worth correcting.",
    "The junction of {a} and {b}. Someone has chalked a mark on the kerbstone, and someone else has half scrubbed it away.",
)


# The ten rooms that are not on the street lattice.
EXTRA_PROSE: dict[str, str] = {
    "road_to_dunwich": (
        "The paving ends and the Aylesbury road begins, running west between hedgerows toward Dunwich. "
        "Nobody from Arkham goes that way without a reason they are willing to state aloud."
    ),
    "road_to_boston": (
        "Washington Street loses its kerbs here and becomes the Boston road, straight and grey between open fields. "
        "It is the way most people leave Arkham, and the way fewest return."
    ),
    "road_to_kingsport": (
        "Peabody Avenue narrows into the Kingsport road and bends south toward the sea. "
        "The wind along it carries salt, and gulls stand on the milestones without calling."
    ),
    "arkham_station": (
        "The Boston and Maine station is a long brick hall with a vaulted iron roof and a floor worn pale by a century of boots. "
        "The departure board lists a service to Innsmouth that the stationmaster will tell you does not run."
    ),
    "road_to_salem": (
        "The rails run west from the platform's end along a raised embankment, curving out of sight toward Salem and Boston. "
        "Walking the sleepers is forbidden, and the prohibition is enforced by nothing but the drop on either side."
    ),
    "the_island": (
        "A low wooded island in the Miskatonic, reached by a stone stair down the northern embankment. "
        "The trees here are older than anything on either bank, and the river divides around them without hurry."
    ),
    "independence_square": (
        "A civic square of gravel walks and clipped limes, with a bandstand at its centre and benches facing outward. "
        "It is the one open space in Arkham that feels entirely safe, which the older residents find worth remarking on."
    ),
    "hangmans_hill": (
        "Bare ground rises to a flat summit where the gallows stood until 1789, and where nothing has grown since. "
        "The town is laid out below, and from here its streets make a pattern they do not make from within."
    ),
    "wooded_graveyard": (
        "Old stones lean among close-grown trees on the hill's northern slope, most of them unreadable and none of them recent. "
        "The wood has taken the ground back so thoroughly that the paths survive only as absences."
    ),
    "old_arkham_graveyard": (
        "The town's first burying ground, walled in iron and crowded with slate markers whose winged skulls have weathered to blank ovals. "
        "The ground is noticeably higher inside the railings than out."
    ),
}
