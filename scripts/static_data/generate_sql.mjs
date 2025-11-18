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

	// Build SQL in dependency order
	const parts = [];
	parts.push('-- Generated from rooms directory');

	// Zones
	for (const [zoneStable, zoneName] of insertZones.entries()) {
		const zid = v5('zones', zoneStable);
		zoneIdByStable.set(zoneStable, zid);
		parts.push(
			`INSERT INTO zones (id, stable_id, name) VALUES ('${zid}'::uuid, '${ql(zoneStable)}', '${ql(zoneName)}') ON CONFLICT (stable_id) DO NOTHING;`
		);
	}

	// Subzones
	for (const s of insertSubzones) {
		const zid = zoneIdByStable.get(s.zoneStable);
		const key = subzoneIdKey(s.zoneStable, s.subStable);
		if (!subzoneIdByStable.has(key)) {
			const szId = v5('subzones', `${s.zoneStable}:${s.subStable}`);
			subzoneIdByStable.set(key, szId);
			parts.push(
				`INSERT INTO subzones (id, zone_id, stable_id, name) VALUES ('${szId}'::uuid, '${zid}'::uuid, '${ql(s.subStable)}', '${ql(s.name)}') ` +
					`ON CONFLICT (zone_id, stable_id) DO NOTHING;`
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

	// Generate zone configurations
	// Deduplicate: only keep one config per zone
	// Ensure we're using the actual zone_config.json file (not accidentally picking up subzone configs)
	const zoneConfigsByZone = new Map();
	for (const zc of zoneConfigs) {
		const zoneStable = `${zc.plane}/${zc.zone}`;
		// Only add if we don't have one yet, or if this one has zone_type (which indicates it's a proper zone config)
		if (!zoneConfigsByZone.has(zoneStable)) {
			zoneConfigsByZone.set(zoneStable, zc);
		} else {
			// If we already have one, prefer the one with zone_type field (proper zone config)
			const existing = zoneConfigsByZone.get(zoneStable);
			if (zc.config.zone_type && !existing.config.zone_type) {
				zoneConfigsByZone.set(zoneStable, zc);
			}
		}
	}

	for (const [zoneStable, zc] of zoneConfigsByZone) {
		const zoneId = zoneIdByStable.get(zoneStable);
		const configId = v5('zone_configurations', `${zoneStable}:zone`);

		const weatherPatterns = JSON.stringify(zc.config.weather_patterns || []);
		const specialRules = JSON.stringify(zc.config.special_rules || {});
		const description = zc.config.description ? `'${ql(zc.config.description)}'` : 'NULL';
		const environment = zc.config.environment ? `'${ql(zc.config.environment)}'` : 'NULL';

		parts.push(
			`INSERT INTO zone_configurations (id, zone_id, subzone_id, configuration_type, environment, description, weather_patterns, special_rules) VALUES (` +
				`'${configId}'::uuid, '${zoneId}'::uuid, NULL, 'zone', ${environment}, ${description}, '${weatherPatterns.replaceAll("'", "''")}'::jsonb, '${specialRules.replaceAll("'", "''")}'::jsonb) ` +
				`ON CONFLICT (zone_id, subzone_id, configuration_type) DO NOTHING;`
		);
	}

	// Generate subzone configurations
	console.log(`DEBUG: Generating ${subzoneConfigs.length} subzone configs`);
	console.log(`DEBUG: subzoneIdByStable has ${subzoneIdByStable.size} entries`);
	for (const szc of subzoneConfigs) {
		const zoneStable = `${szc.plane}/${szc.zone}`;
		const zoneId = zoneIdByStable.get(zoneStable);
		const key = `${zoneStable}::${szc.subzone}`;
		const subzoneId = subzoneIdByStable.get(key);

		console.log(`DEBUG: Processing subzone config: ${key}, zoneId=${zoneId ? 'found' : 'NOT FOUND'}, subzoneId=${subzoneId ? 'found' : 'NOT FOUND'}`);

		if (!subzoneId) {
			console.warn(`Warning: Subzone ID not found for ${key}, skipping subzone config`);
			continue;
		}
		if (!zoneId) {
			console.warn(`Warning: Zone ID not found for ${zoneStable}, skipping subzone config`);
			continue;
		}

		const configId = v5('zone_configurations', `${key}:subzone`);

		const weatherPatterns = JSON.stringify(szc.config.weather_patterns || []);
		const specialRules = JSON.stringify(szc.config.special_rules || {});
		const description = szc.config.description ? `'${ql(szc.config.description)}'` : 'NULL';
		const environment = szc.config.environment ? `'${ql(szc.config.environment)}'` : 'NULL';

		parts.push(
			`INSERT INTO zone_configurations (id, zone_id, subzone_id, configuration_type, environment, description, weather_patterns, special_rules) VALUES (` +
				`'${configId}'::uuid, '${zoneId}'::uuid, '${subzoneId}'::uuid, 'subzone', ${environment}, ${description}, '${weatherPatterns.replaceAll("'", "''")}'::jsonb, '${specialRules.replaceAll("'", "''")}'::jsonb) ` +
				`ON CONFLICT (zone_id, subzone_id, configuration_type) DO NOTHING;`
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
