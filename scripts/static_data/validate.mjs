import { readFile } from 'node:fs/promises';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const root = resolve(__dirname, '..', '..');

const ajv = new Ajv2020({ allErrors: true, strict: true, allowUnionTypes: true });
addFormats(ajv);

async function loadJson(path) {
	const raw = await readFile(path, 'utf-8');
	return JSON.parse(raw);
}

async function validateFile(schemaPath, dataPath, what) {
	const schema = await loadJson(schemaPath);
	const data = await loadJson(dataPath);
	const validate = ajv.compile(schema);
	const ok = validate(data);
	if (!ok) {
		console.error(`Validation failed for ${what}`);
		console.error(ajv.errorsText(validate.errors, { dataVar: what }));
		process.exitCode = 1;
	} else {
		console.log(`Validated ${what}`);
	}
}

async function main() {
	await validateFile(
		resolve(root, 'db/static/schemas/holidays.schema.json'),
		resolve(root, 'data/local/calendar/holidays.json'),
		'holidays'
	);
	await validateFile(
		resolve(root, 'db/static/schemas/npc_schedules.schema.json'),
		resolve(root, 'data/local/calendar/schedules/npc.json'),
		'npc schedules'
	);
	await validateFile(
		resolve(root, 'db/static/schemas/emotes.schema.json'),
		resolve(root, 'data/local/emotes.json'),
		'emotes'
	);
	// Rooms: validate a sample set quickly; full validation can be added later if needed
	console.log('Room schema ready; generation step will validate per-file before use.');
}

main().catch((err) => {
	console.error('Validator error', err);
	process.exit(1);
});
