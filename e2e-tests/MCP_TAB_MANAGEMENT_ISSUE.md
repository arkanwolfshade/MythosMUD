# MCP Tab Management Configuration Issue

## Problem Summary

The multiplayer E2E test scenarios require browser tab management functions (`browser_tab_new`, `browser_tab_select`,
`browser_tab_list`, `browser_tab_close`) to coordinate multiple players across different browser tabs. However, these
functions are not currently available in the MCP server configuration.

## Current State

### Available MCP Tools

The current MCP browser tools available use the pattern:

- `mcp_cursor-ide-browser_browser_navigate`
- `mcp_cursor-ide-browser_browser_snapshot`
- `mcp_cursor-ide-browser_browser_click`
- `mcp_cursor-ide-browser_browser_type`
- `mcp_cursor-ide-browser_browser_wait_for`
- etc.

**Missing**: Tab management functions are not in the available tool list.

### Expected Function Names (from scenarios)

The test scenarios reference these functions:

1. **Pattern 1** (from scenario-01-basic-connection.md):

   - `mcp_playwright_browser_tab_new({url: "http://localhost:5173"})`
   - `mcp_playwright_browser_tab_select({index: 1})`

2. **Pattern 2** (from scenario-23-container-multi-user-looting.md):

   - `mcp_playwright_browser_tabs({action: "new"})`
   - `mcp_playwright_browser_tabs({action: "select", index: 1})`

3. **Pattern 3** (from CLEANUP.md):

   - `mcp_playwright_browser_tab_list()`
   - `mcp_playwright_browser_tab_close({index: i})`

## Root Cause Analysis

### MCP Server Type

**Current**: Using `cursor-ide-browser` MCP server (Cursor's built-in browser automation)

**Expected**: Should support tab management, but functions may be:

  1. Not enabled in the MCP server configuration
  2. Named differently than expected
  3. Requiring additional capability flags

### Research Findings

According to Playwright MCP documentation, tab management functions are part of the `core-tabs` capability, which should
be enabled by default. However, the scenarios reference functions that suggest a different MCP server configuration.

## Investigation Steps Needed

1. **Check Cursor MCP Configuration**

   - Verify if Cursor IDE has MCP server configuration files
   - Check if `cursor-ide-browser` supports tab management
   - Look for capability flags or settings

2. **Verify Available Tools**

   - List all available MCP tools to see actual function names
   - Check if tab management functions exist under different names

3. **Check Cursor Settings**

   - Look for MCP server configuration in Cursor settings
   - Verify if additional capabilities need to be enabled

## Possible Solutions

### Option 1: Enable core-tabs Capability

If Cursor's browser MCP supports it, enable the `core-tabs` capability:

```json
{
  "capabilities": ["core", "core-tabs"]
}
```

### Option 2: Use Different Function Names

If tab management functions exist but have different names, update all scenarios to use the correct function names.

### Option 3: Use Browser Contexts Instead of Tabs

If tabs aren't supported, consider using multiple browser contexts/pages instead, though this may require significant
scenario updates.

### Option 4: Manual Tab Creation Workaround

As a temporary workaround, we could manually create tabs using browser keyboard shortcuts or JavaScript injection, but
this is not ideal for automated testing.

## Impact

**Blocking**: All 21 multiplayer E2E test scenarios require tab management for:

- Multi-player coordination (2+ browser tabs)
- Real-time message broadcasting verification
- State synchronization testing
- Complex multiplayer interaction patterns

**Workarounds**: Currently none available that would allow automated execution of the scenarios.

## Next Steps

1. ✅ **Document the issue** (this file)
2. ⏳ **Investigate Cursor MCP configuration files**
3. ⏳ **Check Cursor settings/configuration for browser MCP**
4. ⏳ **List all available MCP tools to verify function names**
5. ⏳ **Test if alternative approaches work (contexts, pages, etc.)**
6. ⏳ **Update scenarios or configuration based on findings**

## Related Files

`e2e-tests/MULTIPLAYER_TEST_RULES.md` - Master rules for E2E testing

- `e2e-tests/scenarios/scenario-01-basic-connection.md` - First scenario requiring tabs
- `e2e-tests/CLEANUP.md` - Cleanup procedures referencing tab functions
- `e2e-tests/TROUBLESHOOTING.md` - Troubleshooting guide mentioning tabs

## Status

**Date**: 2025-12-02
**Status**: INVESTIGATION IN PROGRESS
**Blocker**: YES - All multiplayer scenarios blocked
**Priority**: HIGH - Required for E2E testing
