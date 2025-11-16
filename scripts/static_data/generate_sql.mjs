import { promises as fs } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';
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

async function main() {
	const outDir = resolve(root, 'data/static/generated_sql');
	await ensureDir(outDir);

	const sections = [];
	sections.push('\\set ON_ERROR_STOP on');
	sections.push('BEGIN;');
	sections.push('-- world first (zones, subzones, rooms, links)');
	sections.push(await generateRooms());
	sections.push('-- calendars and emotes');
	sections.push(await generateHolidays());
	sections.push(await generateNpcSchedules());
	sections.push(await generateEmotes());
	sections.push('COMMIT;');

	const sql = sections.join('\n');
	const target = resolve(outDir, 'static_seed.sql');
	await fs.writeFile(target, sql, 'utf-8');
	console.log(`Wrote ${target}`);
}

main().catch((err) => {
	console.error('SQL generation failed', err);
	process.exit(1);
});
