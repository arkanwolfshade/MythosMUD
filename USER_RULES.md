# USER RULES - CRITICAL SERVER MANAGEMENT

## MANDATORY SERVER RULES

### NEVER use is_background: true for server startup commands
- Server startup must be visible to catch errors
- Background mode hides critical startup information
- Always use `is_background: false` for server operations

### ALWAYS use is_background: false for server startup so you can see the output
- You need to see "Press any key to exit" to know the server is running
- Error messages are only visible in foreground mode
- Server startup is a critical operation requiring full attention

### If you need to start a server, you MUST first run ./scripts/stop_server.ps1
- Never assume no server is running
- Always stop first, then start
- This prevents multiple server instances

### After running stop_server.ps1, you MUST verify ports are free with netstat
- Run: `netstat -an | findstr :54731`
- Run: `netstat -an | findstr :5173`
- Both should return empty results before starting server

### Only THEN can you run ./scripts/start_dev.ps1 with is_background: false
- One start command only
- Use `is_background: false` to see output
- Wait for "Press any key to exit" message

### If start_dev.ps1 fails or shows errors, DO NOT run it again - investigate the error first
- Don't try multiple starts
- Read the error message carefully
- Fix the underlying issue before retrying

## VIOLATION CONSEQUENCES
- Multiple server instances running simultaneously
- Port conflicts and connection failures
- Unpredictable behavior in multiplayer scenarios
- Complete failure of the testing process

## EXISTING RULES (REINFORCED)
- DO NOT START THE SERVER WITHOUT MAKING SURE THERE ARE NO RUNNING INSTANCES!
- Always verify that there is not an existing instance of the server running before trying to start the server
- Only kill tasks that are part of this project by name
- Never use taskkill on node.exe
