param(
	[string]$PlayersDbPath = "data/local/players/local_players.db.bak",
	[string]$OutDir = "data/migration/csv"
)

if (-not (Test-Path $PlayersDbPath)) {
	Write-Error "SQLite players DB not found: $PlayersDbPath"
	exit 1
}

New-Item -ItemType Directory -Path $OutDir -Force | Out-Null

# Ensure sqlite3 is available
$sqlite = "sqlite3.exe"
if (-not (Get-Command $sqlite -ErrorAction SilentlyContinue)) {
	Write-Error "sqlite3.exe not found on PATH. Please install or add to PATH."
	exit 1
}

# Export helpers
function Export-QueryCsv {
	param([string]$Db, [string]$Sql, [string]$CsvPath)
	$cmd = ".mode csv`n.headers on`n.output $CsvPath`n$Sql`n.output stdout"
	$cmd | & $sqlite $Db | Out-Null
}

# NOTE: Adjust column selection according to actual SQLite schema if needed.
# Users (columns per SQLite schema)
$usersSql = @"
SELECT
	id AS old_sqlite_id,
	email,
	username,
	hashed_password,
	CASE WHEN is_active IN (1,'1','t','true') THEN 1 ELSE 0 END AS is_active,
	CASE WHEN is_superuser IN (1,'1','t','true') THEN 1 ELSE 0 END AS is_superuser,
	CASE WHEN is_verified IN (1,'1','t','true') THEN 1 ELSE 0 END AS is_verified,
	created_at,
	updated_at
FROM users;
"@
Export-QueryCsv -Db $PlayersDbPath -Sql $usersSql -CsvPath (Join-Path $OutDir "users.csv")

# Players (columns per SQLite schema)
$playersSql = @"
SELECT
	player_id AS old_sqlite_id,
	user_id,
	name,
	CASE WHEN is_admin IN (1,'1','t','true') THEN 1 ELSE 0 END AS is_admin,
	profession_id AS profession_sqlite_id,
	stats AS stats_json,
	inventory AS inventory_json,
	status_effects AS status_effects_json,
	current_room_id,
	respawn_room_id,
	experience_points,
	level,
	created_at,
	last_active
FROM players;
"@
Export-QueryCsv -Db $PlayersDbPath -Sql $playersSql -CsvPath (Join-Path $OutDir "players.csv")

Write-Host "Exported CSVs to $OutDir"
