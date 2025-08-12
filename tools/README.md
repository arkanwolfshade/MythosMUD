# MythosMUD Room Toolkit

A unified command-line toolkit for room management, validation, mapping, and analysis in MythosMUD.

## Overview

This toolkit consolidates functionality from the original `validator.py` and `mapbuilder.py` tools into a single, powerful command-line interface. It provides comprehensive room management capabilities including validation, mapping, analysis, and automated fixing.

## Installation

The toolkit is part of the MythosMUD project and uses the same dependencies:

```bash
# Install optional dependencies for enhanced features
uv add tcod rich
```

## Usage

### Basic Commands

```bash
# Run the toolkit
python -m tools.room_toolkit [COMMAND] [OPTIONS]

# Get help
python -m tools.room_toolkit --help
python -m tools.room_toolkit validate --help
```

### Available Commands

#### `validate` - Room Validation
Validates room connectivity and structure.

```bash
# Validate all rooms
python -m tools.room_toolkit validate

# Validate specific zone
python -m tools.room_toolkit validate --zone arkham_city

# Validate with auto-fixing
python -m tools.room_toolkit validate --fix --backup

# Schema-only validation
python -m tools.room_toolkit validate --schema-only
```

#### `map` - Map Building & Visualization
Builds and renders room maps.

```bash
# Build and render map with tcod
python -m tools.room_toolkit map --start-room earth_arkham_city_northside_intersection_derby_high --render tcod

# Export map to file
python -m tools.room_toolkit map --start-room earth_arkham_city_northside_intersection_derby_high --output map.txt

# Text-only rendering
python -m tools.room_toolkit map --start-room earth_arkham_city_northside_intersection_derby_high --render text
```

#### `analyze` - Room Analysis
Analyzes room data and generates reports.

```bash
# Analyze connectivity
python -m tools.room_toolkit analyze --connectivity

# Analyze environment distribution
python -m tools.room_toolkit analyze --environment

# Generate HTML report
python -m tools.room_toolkit analyze --connectivity --environment --format html --output analysis.html
```

#### `fix` - Automated Fixing
Automatically fixes common room issues.

```bash
# Fix ID mismatches
python -m tools.room_toolkit fix --id-mismatches --backup

# Fix environment types
python -m tools.room_toolkit fix --environment-types --backup

# Dry run (show what would be fixed)
python -m tools.room_toolkit fix --id-mismatches --dry-run
```

#### `report` - Comprehensive Reports
Generates comprehensive room reports.

```bash
# Generate console report
python -m tools.room_toolkit report

# Generate HTML report with maps
python -m tools.room_toolkit report --format html --include-maps --output report.html
```

## Global Options

- `--base-path PATH`: Base directory for room files (default: `./data/rooms`)
- `--verbose, -v`: Detailed output
- `--no-colors`: Disable colored output

## Features

### Enhanced Room Loading
- Recursive file discovery
- Automatic metadata extraction
- Caching for performance
- Coordinate inference

### Comprehensive Validation
- JSON schema validation
- Connectivity analysis
- Environment type validation
- Room ID consistency checks

### Advanced Mapping
- Multiple rendering backends (tcod, text)
- Coordinate inference with BFS
- Export to various formats
- MythosMUD-specific tile palette

### Automated Fixing
- ID mismatch correction
- Environment type categorization
- Intersection room ID fixes
- Backup creation

### Rich Analysis
- Connectivity pattern analysis
- Environment distribution analysis
- Zone structure analysis
- Multiple output formats (console, JSON, HTML)

## Architecture

The toolkit is organized into modular components:

```
tools/room_toolkit/
├── __init__.py          # Package initialization
├── __main__.py          # Entry point
├── cli.py              # Main CLI interface
├── core/               # Core functionality
│   ├── loader.py       # Room loading
│   ├── validator.py    # Validation engine
│   ├── mapper.py       # Map building
│   ├── analyzer.py     # Analysis engine
│   ├── fixer.py        # Auto-fixing
│   └── reporter.py     # Output formatting
├── schemas/            # JSON schemas
├── rules/              # Validation rules
└── scripts/            # Enhanced analysis scripts
    ├── arkham_connectivity_analyzer.py
    └── room_id_mismatch_analyzer.py
```

## Migration from Old Tools

### From `validator.py`
```bash
# Old
python room_validator/validator.py --base-path ./data/rooms --zone arkham_city

# New
python -m tools.room_toolkit validate --base-path ./data/rooms --zone arkham_city
```

### From `mapbuilder.py`
```bash
# Old
python data/mythos_mud_mapbuilder.py --rooms-dir data/rooms/earth/arkham_city --start-room earth_arkham_city_northside_intersection_derby_high --render tcod

# New
python -m tools.room_toolkit map --start-room earth_arkham_city_northside_intersection_derby_high --render tcod
```

## Examples

### Complete Workflow

```bash
# 1. Validate rooms
python -m tools.room_toolkit validate --zone arkham_city

# 2. Fix issues automatically
python -m tools.room_toolkit fix --id-mismatches --environment-types --backup

# 3. Generate analysis report
python -m tools.room_toolkit analyze --connectivity --environment --format html --output analysis.html

# 4. Build and view map
python -m tools.room_toolkit map --start-room earth_arkham_city_northside_intersection_derby_high --render tcod
```

### Batch Processing

```bash
# Process multiple zones
for zone in arkham_city innsmouth; do
    python -m tools.room_toolkit validate --zone $zone
    python -m tools.room_toolkit analyze --connectivity --output ${zone}_analysis.json
done
```

## Configuration

The toolkit uses the same configuration as the main MythosMUD project. Room files should be organized in the standard directory structure:

```
data/rooms/
├── earth/
│   ├── arkham_city/
│   │   ├── downtown/
│   │   ├── northside/
│   │   └── ...
│   └── innsmouth/
└── yeng/
    └── katmandu/
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure you're running from the project root directory
2. **Missing Dependencies**: Install optional dependencies with `uv add tcod rich`
3. **File Not Found**: Check the `--base-path` option points to the correct directory
4. **Permission Errors**: Ensure write permissions for backup and output files

### Debug Mode

Use the `--verbose` flag for detailed output:

```bash
python -m tools.room_toolkit validate --verbose
```

## Enhanced Scripts

The toolkit includes enhanced analysis scripts that integrate with the core functionality:

### Arkham Connectivity Analyzer
```bash
# Analyze Arkham City connectivity
python tools/room_toolkit/scripts/arkham_connectivity_analyzer.py

# Save detailed report
python tools/room_toolkit/scripts/arkham_connectivity_analyzer.py --output arkham_analysis.json
```

### Room ID Mismatch Analyzer
```bash
# Analyze room ID mismatches
python tools/room_toolkit/scripts/room_id_mismatch_analyzer.py

# Save detailed report
python tools/room_toolkit/scripts/room_id_mismatch_analyzer.py --output mismatch_analysis.json
```

These scripts provide enhanced analysis capabilities beyond the basic CLI commands, with detailed reporting and pattern recognition.

## Contributing

The toolkit is designed to be extensible. New commands can be added to `cli.py`, new functionality can be implemented in the appropriate core module, and enhanced scripts can be added to the `scripts/` directory.

## License

Part of the MythosMUD project. See the main project license for details.
