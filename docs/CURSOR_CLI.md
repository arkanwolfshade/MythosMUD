# Cursor CLI Documentation

*"In the restricted archives, we learn that automation requires proper tools. The Cursor CLI provides powerful coding assistance directly from the terminal, enabling both interactive sessions and automated workflows."*

## Overview

Cursor CLI lets you interact with AI agents directly from your terminal to write, review, and modify code. Whether you prefer an interactive terminal interface or print automation for scripts and CI pipelines, the CLI provides powerful coding assistance right where you work.

## Installation

### Windows PowerShell
```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

### macOS/Linux/WSL
```bash
curl https://cursor.com/install -fsS | bash
```

### Verification
```powershell
cursor --version
```

Expected output:
```
2.4.22
618c607a249dd7fd2ffc662c6531143833bebd40
x64
```

## Core Commands

### Interactive Mode
Start a conversational session with the agent:
```powershell
cursor agent
```

Start with an initial prompt:
```powershell
cursor agent "refactor the auth module to use JWT tokens"
```

### Non-Interactive Mode (Print Mode)
Run with specific prompt and model:
```powershell
cursor agent -p "find and fix performance issues" --model "gpt-5.2"
```

Use with git changes included for review:
```powershell
cursor agent -p "review these changes for security issues" --output-format text
```

## Modes

The CLI supports the same modes as the editor:

| Mode      | Description                                                  | Shortcut      |
| --------- | ------------------------------------------------------------ | ------------- |
| **Agent** | Full access to all tools for complex coding tasks            | Default       |
| **Plan**  | Design your approach before coding with clarifying questions | `--mode=plan` |
| **Ask**   | Read-only exploration without making changes                 | `--mode=ask`  |

### Using Modes

**Plan Mode**:
```powershell
cursor agent --mode=plan -p "refactor the persistence layer"
```

**Ask Mode**:
```powershell
cursor agent --mode=ask -p "explore the authentication flow"
```

## Project Scripts

MythosMUD includes PowerShell scripts that wrap Cursor CLI for common workflows:

### cursor-cli-agent.ps1
Wrapper script for common CLI agent tasks:
```powershell
.\scripts\cursor-cli-agent.ps1 "analyze test failures in server/tests/unit"
.\scripts\cursor-cli-agent.ps1 -NonInteractive -Prompt "review security of auth module"
.\scripts\cursor-cli-agent.ps1 -Plan -Prompt "refactor the persistence layer"
```

### cursor-cli-review.ps1
Automated code review:
```powershell
.\scripts\cursor-cli-review.ps1 -GitChanges
.\scripts\cursor-cli-review.ps1 -Path server/services/auth.py -Focus security
.\scripts\cursor-cli-review.ps1 -Path server/ -Focus all -OutputReport
```

### cursor-cli-test-fix.ps1
Test failure remediation:
```powershell
.\scripts\cursor-cli-test-fix.ps1 -TestPath server/tests/unit
.\scripts\cursor-cli-test-fix.ps1 -TestFile server/tests/unit/test_auth.py
.\scripts\cursor-cli-test-fix.ps1 -TestName test_login_failure -AnalyzeOnly
```

## Common Options

### Model Selection
```powershell
cursor agent -p "analyze code" --model "gpt-5.2"
cursor agent -p "analyze code" --model "claude-4.5-opus"
```

### Output Format
```powershell
cursor agent -p "review code" --output-format text
cursor agent -p "review code" --output-format json
```

### Non-Interactive Mode
```powershell
cursor agent -p "fix bugs"  # Print mode (non-interactive)
```

## Sessions

Resume previous conversations to maintain context:

```powershell
# List all previous chats
cursor agent ls

# Resume latest conversation
cursor agent resume

# Resume specific conversation
cursor agent --resume="chat-id-here"
```

## Cloud Agent Handoff

Push your conversation to a Cloud Agent to continue running while you're away:

```powershell
# Send a task to Cloud Agent
cursor agent "&refactor the auth module and add comprehensive tests"
```

Pick up your Cloud Agent tasks on web or mobile at [cursor.com/agents](https://cursor.com/agents).

## Use Cases

### Code Writing/Review
```powershell
cursor agent -p "review the authentication module for security issues"
cursor agent -p "refactor the persistence layer to use dependency injection"
```

### Terminal Command Execution
```powershell
cursor agent "run the test suite and analyze failures"
```

### Codebase Searching
```powershell
cursor agent "find all implementations of the Player class"
```

### File Generation
```powershell
cursor agent "generate a new API endpoint for user management"
```

### Automation Workflows
```powershell
# In CI/CD pipeline
cursor agent -p "review these changes for security issues" --output-format text > review.txt
```

## Integration with Project Workflows

### Test Failure Remediation
```powershell
.\scripts\cursor-cli-test-fix.ps1 -TestPath server/tests/unit -OutputReport
```

### Security Review
```powershell
.\scripts\cursor-cli-review.ps1 -GitChanges -Focus security
```

### Performance Analysis
```powershell
.\scripts\cursor-cli-review.ps1 -Path server/services/ -Focus performance
```

## Best Practices

### Interactive vs Non-Interactive
- **Interactive**: Use for exploratory work, complex refactoring, learning
- **Non-Interactive**: Use for automation, CI/CD, scripts, quick reviews

### Model Selection
- **Default**: Works well for most tasks
- **GPT-5.2**: Good for code generation and refactoring
- **Claude-4.5-Opus**: Good for analysis and review

### Output Format
- **Text**: Human-readable output for reviews and reports
- **JSON**: Structured output for automation and parsing

## Troubleshooting

### CLI Not Found
```powershell
# Verify installation
cursor --version

# Reinstall if needed
irm 'https://cursor.com/install?win32=true' | iex
```

### Permission Issues
```powershell
# Check execution policy
Get-ExecutionPolicy

# Set execution policy if needed (requires admin)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Model Not Available
```powershell
# List available models
cursor agent --help

# Use default model if specific model unavailable
cursor agent -p "your prompt"
```

## References

- [Cursor CLI Documentation](https://cursor.com/docs/cli/overview)
- [Cursor CLI Reference](https://docs.cursor.com/en/cli/reference/parameters)
- Project scripts: `scripts/cursor-cli-*.ps1`
- Workflow examples: `docs/CURSOR_WORKFLOWS.md`

## Notes

- The CLI is currently in beta and should only be used in trusted environments
- CLI usage consumes API credits based on your Cursor plan
- Non-interactive mode is best for automation and CI/CD
- Interactive mode provides better context and conversation flow
