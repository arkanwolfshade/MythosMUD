# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-09-20-nats-env-config/spec.md

## Technical Requirements

### Environment Variable Integration

Add support for `NATS_SERVER_PATH` environment variable in PowerShell scripts

- Environment variable should accept both absolute and relative paths
- Support for environment variable in both system environment and `.env` files
- Environment variable should be loaded using existing environment loading patterns in `start_server.ps1`

### Path Detection Logic

Implement new function `Get-NatsServerPath` that checks environment variable first

- Maintain existing hardcoded path detection as fallback mechanism
- Validate that specified path exists and points to valid NATS server executable
- Support both Windows paths (backslashes) and Unix-style paths (forward slashes)

### Error Handling and Validation

Validate that `NATS_SERVER_PATH` points to existing file

- Verify that the specified executable is actually a NATS server (version check)
- Provide clear error messages when environment variable is set but path is invalid
- Maintain graceful fallback to hardcoded paths when environment variable is not set

### Script Modifications Required

**nats_manager.ps1**: Replace `$PossiblePaths` array logic with environment-aware detection

**nats_status.ps1**: Update detailed information display to show environment variable source

**start_server.ps1**: Ensure environment variables are loaded before NATS server startup
- Maintain all existing function signatures and return values for backward compatibility

### Configuration Examples

Update `env.production.example` to include `NATS_SERVER_PATH` example

- Document environment variable usage in script help and comments
- Provide examples for common NATS server installation locations

### Testing Requirements

Test with environment variable set to valid path

- Test with environment variable set to invalid path
- Test with environment variable not set (fallback behavior)
- Test with environment variable set to relative path
- Test integration with existing NATS server management functions

### Backward Compatibility

All existing NATS management functionality must continue to work unchanged

- Scripts should behave identically when environment variable is not set
- No breaking changes to function parameters or return values
- Existing hardcoded paths must remain as fallback options
