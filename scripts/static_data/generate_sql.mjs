import addFormats from 'ajv-formats';
import Ajv2020 from 'ajv/dist/2020.js';
import { promises as fs } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { v5 as uuidv5 } from 'uuid';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const root = resolve(__dirname, '..', '..');

const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
addFormats(ajv);

// Project namespace UUID for deterministic v5 IDs (documented constant)
const NAMESPACE = 'c8e7f86d-b1c9-4074-8b2e-9f3c6c8a9f2a';

async function readJson(path) {
	const raw = await fs.readFile(path, 'utf-8');
	return JSON.parse(raw);
}

async function ensureDir(path) {
	await fs.mkdir(path, { recursive: true });
}

function ql(str) {
	return str.replaceAll("'", "''");
}

function v5(table, stableId) {
	return uuidv5(`${table}:${stableId}`, NAMESPACE);
}

async function generateHolidays() {
	const schema = await readJson(resolve(root, 'db/static/schemas/holidays.schema.json'));
	const validate = ajv.compile(schema);
	const data = await readJson(resolve(root, 'data/local/calendar/holidays.json'));
	if (!validate(data)) {
		throw new Error(ajv.errorsText(validate.errors, { dataVar: 'holidays' }));
	}
	const parts = [];
	parts.push('-- Generated from holidays.json');
	for (const h of data.holidays) {
		const id = v5('calendar_holidays', h.id);
		const bonus = '{' + h.bonus_tags.map(ql).map((x) => `"${x}"`).join(',') + '}';
		parts.push(
			`INSERT INTO calendar_holidays (id, stable_id, name, tradition, month, day, duration_hours, season, bonus_tags) VALUES (` +
				`'${id}'::uuid, '${ql(h.id)}', '${ql(h.name)}', '${ql(h.tradition)}', ${h.month}, ${h.day}, ${h.duration_hours}, '${h.season}', '${bonus}'::text[]) ` +
				`ON CONFLICT (stable_id) DO NOTHING;`
		);
	}
	return parts.join('\n') + '\n';
}

async function generateNpcSchedules() {
	const schema = await readJson(resolve(root, 'db/static/schemas/npc_schedules.schema.json'));
	const validate = ajv.compile(schema);
	const data = await readJson(resolve(root, 'data/local/calendar/schedules/npc.json'));
	if (!validate(data)) {
		throw new Error(ajv.errorsText(validate.errors, { dataVar: 'schedules' }));
	}
	const parts = [];
	parts.push('-- Generated from npc.json schedules');
	for (const s of data.schedules) {
		const id = v5('calendar_npc_schedules', s.id);
		const days = '{' + s.days.map(ql).map((x) => `"${x}"`).join(',') + '}';
		const applies = '{' + s.applies_to.map(ql).map((x) => `"${x}"`).join(',') + '}';
		const effects = '{' + s.effects.map(ql).map((x) => `"${x}"`).join(',') + '}';
		const notes = s.notes ? `'${ql(s.notes)}'` : 'NULL';
		parts.push(
			`INSERT INTO calendar_npc_schedules (id, stable_id, name, category, start_hour, end_hour, days, applies_to, effects, notes) VALUES (` +
				`'${id}'::uuid, '${ql(s.id)}', '${ql(s.name)}', '${ql(s.category)}', ${s.start_hour}, ${s.end_hour}, '${days}'::text[], '${applies}'::text[], '${effects}'::text[], ${notes}) ` +
				`ON CONFLICT (stable_id) DO NOTHING;`
		);
	}
	return parts.join('\n') + '\n';
}

async function generateEmotes() {
	const schema = await readJson(resolve(root, 'db/static/schemas/emotes.schema.json'));
	const validate = ajv.compile(schema);
	const data = await readJson(resolve(root, 'data/local/emotes.json'));
	if (!validate(data)) {
		throw new Error(ajv.errorsText(validate.errors, { dataVar: 'emotes' }));
	}
	const parts = [];
	parts.push('-- Generated from emotes.json');
	for (const [stableId, val] of Object.entries(data.emotes)) {
		const id = v5('emotes', stableId);
		parts.push(
			`INSERT INTO emotes (id, stable_id, self_message, other_message) VALUES (` +
				`'${id}'::uuid, '${ql(stableId)}', '${ql(val.self_message)}', '${ql(val.other_message)}') ` +
				`ON CONFLICT (stable_id) DO NOTHING;`
		);
		for (const alias of val.aliases || []) {
			parts.push(
				`INSERT INTO emote_aliases (emote_id, alias) VALUES ('${id}'::uuid, '${ql(alias)}') ` +
					`ON CONFLICT DO NOTHING;`
			);
		}
	}
	return parts.join('\n') + '\n';
}

async function walk(dir) {
	const out = [];
	const entries = await fs.readdir(dir, { withFileTypes: true });
	for (const e of entries) {
		const p = resolve(dir, e.name);
		if (e.isDirectory()) out.push(...(await walk(p)));
		else if (e.isFile() && e.name.endsWith('.json')) out.push(p);
	}
	return out;
}

async function generateRooms() {
	const schema = await readJson(resolve(root, 'db/static/schemas/room.schema.json'));
	const validate = ajv.compile(schema);
	const base = resolve(root, 'data/local/rooms');
	const files = await walk(base);

	const insertZones = new Map();   // stable_id -> name
	const zoneIdByStable = new Map();
	const insertSubzones = [];       // tuples {zoneStable, subStable, name}
	const subzoneIdKey = (zs, ss) => `${zs}::${ss}`;
	const subzoneIdByStable = new Map();
	const rooms = [];                // room objects with computed ids
	const links = [];                // from,to,direction

	// First pass: collect subzones from room files
	for (const file of files) {
		const base = file.toLowerCase();
		if (base.endsWith('subzone_config.json') || base.endsWith('zone_config.json')) {
			continue; // skip config files
		}
		const room = JSON.parse(await fs.readFile(file, 'utf-8'));
		if (!room.plane && typeof room.id === 'string' && room.id.includes('_')) {
			// infer plane from id prefix (e.g., 'earth_...')
			room.plane = room.id.split('_', 1)[0];
		}
		if (!validate(room)) {
			throw new Error(`Room validation failed for ${file}: ${ajv.errorsText(validate.errors, { dataVar: 'room' })}`);
		}
		const zoneStable = `${room.plane}/${room.zone}`;
		const subStable = room.sub_zone;
		insertZones.set(zoneStable, room.zone);
		insertSubzones.push({ zoneStable, subStable, name: subStable });
		rooms.push(room);
	}

	// Second pass: also create subzones that have config files but no rooms
	for (const file of files) {
		const base = file.toLowerCase();
		if (!base.endsWith('subzone_config.json')) {
			continue; // only process subzone config files
		}
		// Extract plane, zone, subzone from path: data/local/rooms/plane/zone/subzone/subzone_config.json
		const parts = file.split(/[/\\]/);
		const roomsIndex = parts.indexOf('rooms');
		const planeIndex = roomsIndex + 1;
		if (roomsIndex >= 0 && planeIndex > 0 && planeIndex < parts.length - 3) {
			const plane = parts[planeIndex];
			const zone = parts[planeIndex + 1];
			const subzone = parts[planeIndex + 2];
			if (plane && zone && subzone) {
				const zoneStable = `${plane}/${zone}`;
				const subStable = subzone;
				insertZones.set(zoneStable, zone);
				// Only add if not already in list (deduplicate)
				const key = subzoneIdKey(zoneStable, subStable);
				if (!insertSubzones.find(s => subzoneIdKey(s.zoneStable, s.subStable) === key)) {
					insertSubzones.push({ zoneStable, subStable, name: subStable });
				}
			}
		}
	}

	// Build SQL in dependency order
	const parts = [];
	parts.push('-- Generated from rooms directory');

	// Load zone configs for populating zone fields
	const zoneConfigsByKey = new Map();
	for (const file of files) {
		const base = file.toLowerCase();
		if (base.endsWith('zone_config.json') && !base.endsWith('subzone_config.json')) {
			const config = JSON.parse(await fs.readFile(file, 'utf-8'));
			// Extract plane, zone from path: data/local/rooms/plane/zone/zone_config.json
			const parts = file.split(/[/\\]/);
			const roomsIndex = parts.indexOf('rooms');
			const planeIndex = roomsIndex + 1;
			if (roomsIndex >= 0 && planeIndex > 0 && planeIndex < parts.length - 2) {
				const plane = parts[planeIndex];
				const zone = parts[planeIndex + 1];
				if (plane && zone) {
					const zoneStable = `${plane}/${zone}`;
					zoneConfigsByKey.set(zoneStable, config);
				}
			}
		}
	}

	// Zones
	for (const [zoneStable, zoneName] of insertZones.entries()) {
		const zid = v5('zones', zoneStable);
		zoneIdByStable.set(zoneStable, zid);

		// Get zone config if available
		const zoneConfig = zoneConfigsByKey.get(zoneStable);
		const zoneType = zoneConfig?.zone_type ? `'${ql(zoneConfig.zone_type)}'` : 'NULL';
		const environment = zoneConfig?.environment ? `'${ql(zoneConfig.environment)}'` : 'NULL';
		const description = zoneConfig?.description ? `'${ql(zoneConfig.description)}'` : 'NULL';
		const weatherPatterns = zoneConfig?.weather_patterns ? JSON.stringify(zoneConfig.weather_patterns).replaceAll("'", "''") : '[]';
		const specialRules = zoneConfig?.special_rules ? JSON.stringify(zoneConfig.special_rules).replaceAll("'", "''") : '{}';

		parts.push(
			`INSERT INTO zones (id, stable_id, name, zone_type, environment, description, weather_patterns, special_rules) VALUES (` +
				`'${zid}'::uuid, '${ql(zoneStable)}', '${ql(zoneName)}', ${zoneType}, ${environment}, ${description}, '${weatherPatterns}'::jsonb, '${specialRules}'::jsonb) ` +
				`ON CONFLICT (stable_id) DO UPDATE SET ` +
				`zone_type = EXCLUDED.zone_type, ` +
				`environment = EXCLUDED.environment, ` +
				`description = EXCLUDED.description, ` +
				`weather_patterns = EXCLUDED.weather_patterns, ` +
				`special_rules = EXCLUDED.special_rules;`
		);
	}

	// Load subzone configs for populating subzone fields
	const subzoneConfigsByKey = new Map();
	for (const file of files) {
		const base = file.toLowerCase();
		if (base.endsWith('subzone_config.json')) {
			const config = JSON.parse(await fs.readFile(file, 'utf-8'));
			// Extract plane, zone, subzone from path: data/local/rooms/plane/zone/subzone/subzone_config.json
			const parts = file.split(/[/\\]/);
			const roomsIndex = parts.indexOf('rooms');
			const planeIndex = roomsIndex + 1;
			if (roomsIndex >= 0 && planeIndex > 0 && planeIndex < parts.length - 3) {
				const plane = parts[planeIndex];
				const zone = parts[planeIndex + 1];
				const subzone = parts[planeIndex + 2];
				if (plane && zone && subzone) {
					const zoneStable = `${plane}/${zone}`;
					const key = subzoneIdKey(zoneStable, subzone);
					subzoneConfigsByKey.set(key, config);
				}
			}
		}
	}

	// Subzones
	for (const s of insertSubzones) {
		const zid = zoneIdByStable.get(s.zoneStable);
		const key = subzoneIdKey(s.zoneStable, s.subStable);
		if (!subzoneIdByStable.has(key)) {
			const szId = v5('subzones', `${s.zoneStable}:${s.subStable}`);
			subzoneIdByStable.set(key, szId);

			// Get subzone config if available
			const subzoneConfig = subzoneConfigsByKey.get(key);
			const environment = subzoneConfig?.environment ? `'${ql(subzoneConfig.environment)}'` : 'NULL';
			const description = subzoneConfig?.description ? `'${ql(subzoneConfig.description)}'` : 'NULL';
			const specialRules = subzoneConfig?.special_rules ? JSON.stringify(subzoneConfig.special_rules).replaceAll("'", "''") : '{}';

			parts.push(
				`INSERT INTO subzones (id, zone_id, stable_id, name, environment, description, special_rules) VALUES (` +
					`'${szId}'::uuid, '${zid}'::uuid, '${ql(s.subStable)}', '${ql(s.name)}', ${environment}, ${description}, '${specialRules}'::jsonb) ` +
					`ON CONFLICT (zone_id, stable_id) DO UPDATE SET ` +
					`environment = EXCLUDED.environment, ` +
					`description = EXCLUDED.description, ` +
					`special_rules = EXCLUDED.special_rules;`
			);
		}
	}

	// Rooms
	const roomIdByStable = new Map();
	for (const r of rooms) {
		const key = subzoneIdKey(`${r.plane}/${r.zone}`, r.sub_zone);
		const subId = subzoneIdByStable.get(key);
		const rid = v5('rooms', r.id);
		roomIdByStable.set(r.id, rid);
		const attrs = {
			environment: r.environment ?? null
		};
		parts.push(
			`INSERT INTO rooms (id, subzone_id, stable_id, name, description, attributes) VALUES (` +
				`'${rid}'::uuid, '${subId}'::uuid, '${ql(r.id)}', '${ql(r.name)}', '${ql(r.description)}', '${JSON.stringify(attrs).replaceAll("'", "''")}'::jsonb)` +
				` ON CONFLICT (subzone_id, stable_id) DO NOTHING;`
		);
		// Links
		for (const [dir, target] of Object.entries(r.exits || {})) {
			if (target && typeof target === 'string') {
				links.push({ from: r.id, to: target, direction: dir });
			}
		}
	}

	// Room links
	for (const l of links) {
		// Only create links where both endpoints exist in loaded dataset
		if (!roomIdByStable.has(l.from) || !roomIdByStable.has(l.to)) {
			continue;
		}
		const fromId = roomIdByStable.get(l.from);
		const toId = roomIdByStable.get(l.to);
		const linkId = v5('room_links', `${l.from}:${l.direction}`);
		parts.push(
			`INSERT INTO room_links (id, from_room_id, to_room_id, direction, attributes) VALUES (` +
				`'${linkId}'::uuid, '${fromId}'::uuid, '${toId}'::uuid, '${ql(l.direction)}', '{}'::jsonb) ` +
				`ON CONFLICT (from_room_id, direction) DO NOTHING;`
		);
	}

	return parts.join('\n') + '\n';
}

async function generateZoneConfigs() {
	const base = resolve(root, 'data/local/rooms');
	const files = await walk(base);

	const zoneConfigs = [];  // {plane, zone, config}
	const subzoneConfigs = [];  // {plane, zone, subzone, config}

	// Load zone and subzone configs
	for (const file of files) {
		const base = file.toLowerCase();
		// Check subzone_config.json FIRST because it ends with zone_config.json
		// This prevents subzone configs from being incorrectly matched as zone configs
		if (base.endsWith('subzone_config.json')) {
			const config = JSON.parse(await fs.readFile(file, 'utf-8'));
			// Extract plane, zone, subzone from path: data/local/rooms/plane/zone/subzone/subzone_config.json
			const parts = file.split(/[/\\]/);
			const roomsIndex = parts.indexOf('rooms');
			const planeIndex = roomsIndex + 1;
			// Need: plane (planeIndex), zone (planeIndex+1), subzone (planeIndex+2), filename (planeIndex+3)
			// So we need at least planeIndex + 4 parts total (0-indexed, so parts.length >= planeIndex + 4)
			// Which means: planeIndex < parts.length - 3
			if (roomsIndex >= 0 && planeIndex > 0 && planeIndex < parts.length - 3) {
				const plane = parts[planeIndex];
				const zone = parts[planeIndex + 1];
				const subzone = parts[planeIndex + 2];
				if (plane && zone && subzone) {
					subzoneConfigs.push({ plane, zone, subzone, config });
				} else {
					console.warn(`Warning: Missing plane/zone/subzone in path: ${file} (plane=${plane}, zone=${zone}, subzone=${subzone})`);
				}
			} else {
				console.warn(`Warning: Could not parse subzone config path: ${file} (roomsIndex=${roomsIndex}, planeIndex=${planeIndex}, parts.length=${parts.length})`);
			}
		} else if (base.endsWith('zone_config.json')) {
			const config = JSON.parse(await fs.readFile(file, 'utf-8'));
			// Extract plane and zone from path: data/local/rooms/plane/zone/zone_config.json
			const parts = file.split(/[/\\]/);
			const planeIndex = parts.indexOf('rooms') + 1;
			if (planeIndex > 0 && planeIndex < parts.length - 2) {
				const plane = parts[planeIndex];
				const zone = parts[planeIndex + 1];
				zoneConfigs.push({ plane, zone, config });
			}
		}
	}

	const parts = [];
	parts.push('-- Generated from zone_config.json and subzone_config.json files');

	console.log(`Found ${zoneConfigs.length} zone configs and ${subzoneConfigs.length} subzone configs`);

	// Need to load zone and subzone IDs from existing data
	// We'll use the same UUID generation as in generateRooms
	const zoneIdByStable = new Map();
	const subzoneIdByStable = new Map();

	// First, collect all zones and subzones we need
	const zoneStables = new Set();
	const subzoneKeys = new Set();

	for (const zc of zoneConfigs) {
		zoneStables.add(`${zc.plane}/${zc.zone}`);
	}

	for (const szc of subzoneConfigs) {
		zoneStables.add(`${szc.plane}/${szc.zone}`);
		subzoneKeys.add(`${szc.plane}/${szc.zone}::${szc.subzone}`);
	}

	// Generate zone IDs
	for (const zoneStable of zoneStables) {
		const zid = v5('zones', zoneStable);
		zoneIdByStable.set(zoneStable, zid);
	}

	// Generate subzone IDs
	// Use the same UUID generation format as generateRooms(): zoneStable:subStable (single colon)
	for (const szc of subzoneConfigs) {
		const zoneStable = `${szc.plane}/${szc.zone}`;
		const key = `${zoneStable}::${szc.subzone}`;  // Map key uses double colon
		if (!subzoneIdByStable.has(key)) {
			// UUID generation uses single colon to match generateRooms()
			const szId = v5('subzones', `${zoneStable}:${szc.subzone}`);
			subzoneIdByStable.set(key, szId);
		}
	}

	// Generate zone configurations (mapping table only - data is in zones and subzones tables)
	// Create mapping entries for each subzone to its parent zone
	console.log(`DEBUG: Generating ${subzoneConfigs.length} zone-configuration mappings`);
	for (const szc of subzoneConfigs) {
		const zoneStable = `${szc.plane}/${szc.zone}`;
		const zoneId = zoneIdByStable.get(zoneStable);
		const key = `${zoneStable}::${szc.subzone}`;
		const subzoneId = subzoneIdByStable.get(key);

		if (!subzoneId) {
			console.warn(`Warning: Subzone ID not found for ${key}, skipping zone configuration mapping`);
			continue;
		}
		if (!zoneId) {
			console.warn(`Warning: Zone ID not found for ${zoneStable}, skipping zone configuration mapping`);
			continue;
		}

		const configId = v5('zone_configurations', key);

		parts.push(
			`INSERT INTO zone_configurations (id, zone_id, subzone_id) VALUES (` +
				`'${configId}'::uuid, '${zoneId}'::uuid, '${subzoneId}'::uuid) ` +
				`ON CONFLICT (zone_id, subzone_id) DO NOTHING;`
		);
	}

	return parts.join('\n') + '\n';
}

async function main() {
	const outDir = resolve(root, 'data/seed');
	await ensureDir(outDir);

	const sections = [];
	sections.push('\\set ON_ERROR_STOP on');
	sections.push('BEGIN;');
	sections.push('-- world first (zones, subzones, rooms, links)');
	sections.push(await generateRooms());
	sections.push('-- zone configurations');
	sections.push(await generateZoneConfigs());
	sections.push('-- calendars and emotes');
	sections.push(await generateHolidays());
	sections.push(await generateNpcSchedules());
	sections.push(await generateEmotes());
	sections.push('COMMIT;');

	const sql = sections.join('\n');
	const target = resolve(outDir, '00_world_and_emotes.sql');
	await fs.writeFile(target, sql, 'utf-8');
	console.log(`Wrote ${target}`);
}

main().catch((err) => {
	console.error('SQL generation failed', err);
	process.exit(1);
});
