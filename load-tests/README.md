# Load Tests for MythosMUD

This directory contains load testing tools and scripts for MythosMUD.

## Overview

The load test suite is designed to test the server under concurrent load with 10 players performing various actions. The test covers:

- Concurrent registration of 10 new players
- Concurrent login of all 10 players
- Execution of 20 different actions (2 per player) covering most available commands
- 5-minute idle period to test connection stability
- Log analysis to identify issues

## Files

- **`load_test_10_players.spec.ts`** - TypeScript/Playwright test specification (reference implementation)
- **`LOAD_TEST_EXECUTION_GUIDE.md`** - Step-by-step execution guide using Playwright MCP tools
- **`get_invite_codes.py`** - Helper script to fetch 10 active invite codes from database
- **`analyze_logs.py`** - Helper script to analyze errors.log and warnings.log files

## Quick Start

### Prerequisites

1. Ensure server is stopped: `./scripts/stop_server.ps1`
2. Verify ports 54731 and 5173 are free
3. Get 10 active invite codes: `python load-tests/get_invite_codes.py`
4. Start server: `./scripts/start_local.ps1`

### Execution

The load test should be executed using Playwright MCP tools following the step-by-step guide in `LOAD_TEST_EXECUTION_GUIDE.md`. This approach is required because:

- The test requires 10 concurrent browser tabs
- Real-time coordination between multiple players
- Verification of message broadcasting and state synchronization

### Log Analysis

After completing the load test and shutting down the server:

```bash
python load-tests/analyze_logs.py
```

This will:
- Analyze `logs/local/errors.log` for ERROR and CRITICAL level entries
- Analyze `logs/local/warnings.log` for WARNING level entries
- Categorize issues by type
- Generate a summary report
- Save the report to `logs/local/load_test_analysis_report.txt`

## Player Configuration

The load test uses 10 players with the following profession distribution:

| Player | Username | Profession | Profession ID | Actions |
|--------|----------|------------|---------------|---------|
| 1 | loadtest_player_1 | Tramp | 0 | look, say Hello everyone |
| 2 | loadtest_player_2 | Antiquarian | 1 | go north, who |
| 3 | loadtest_player_3 | Author | 2 | local Testing local channel, status |
| 4 | loadtest_player_4 | Dilettante | 3 | global Testing global channel, whoami |
| 5 | loadtest_player_5 | Doctor of Medicine | 4 | whisper Player1 Hello, inventory |
| 6 | loadtest_player_6 | Journalist | 5 | reply Thanks, time |
| 7 | loadtest_player_7 | Police Detective | 6 | emote waves, me stretches |
| 8 | loadtest_player_8 | Private Investigator | 7 | pose standing, help |
| 9 | loadtest_player_9 | Professor | 8 | alias test look, aliases |
| 10 | loadtest_player_10 | Tramp | 0 | sit, stand |

**Note**: Two players (Player 1 and Player 10) are assigned Tramp profession to cover all 9 available professions with 10 players.

## Test Phases

1. **Registration Phase**: Register 10 players concurrently
2. **Character Creation Phase**: Select professions and create characters
3. **Login Phase**: Log in all 10 players concurrently
4. **Action Execution Phase**: Execute 2 actions per player (20 total actions)
5. **Idle Phase**: Maintain all players connected for 5 minutes
6. **Shutdown Phase**: Gracefully shut down the server
7. **Analysis Phase**: Analyze log files for errors and warnings

## Expected Duration

- Registration: ~2-3 minutes (concurrent)
- Character Creation: ~3-5 minutes (sequential per player)
- Login: ~1-2 minutes (concurrent)
- Action Execution: ~2-3 minutes (sequential per player)
- Idle Period: 5 minutes
- **Total**: ~15-20 minutes

## Success Criteria

- ✅ All 10 players register successfully
- ✅ All 10 players log in concurrently
- ✅ All 20 actions execute successfully
- ✅ All players remain connected during 5-minute idle period
- ✅ Server shuts down gracefully
- ✅ Log files are analyzed and issues documented

## Troubleshooting

### Not Enough Invite Codes

If `get_invite_codes.py` reports fewer than 10 active invite codes:

```bash
# Generate more invite codes
python tools/invite_tools/generate_invites_db.py
```

### Connection Issues During Test

If players disconnect during the idle period:
- Check server logs for connection errors
- Verify WebSocket connection stability
- Check for rate limiting issues

### Log Analysis Shows Errors

Review the generated report in `logs/local/load_test_analysis_report.txt` and:
- Categorize errors by type
- Identify patterns (e.g., all connection errors at specific time)
- Document issues that need to be addressed

## Notes

- The test uses a consistent password for all players: `LoadTest123!`
- All players start in the default starting room
- Some commands (like `whisper`) require coordination between players
- Some commands (like `go north`) may fail if no exit exists - this is expected and should be handled gracefully
