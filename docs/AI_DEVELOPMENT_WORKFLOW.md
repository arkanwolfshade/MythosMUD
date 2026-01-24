# 🐙 MythosMUD AI Development Workflow

*"The boundaries between human and artificial intelligence blur in the pursuit of eldritch knowledge."* - Dr. Herbert
West, Miskatonic University

---

## Table of Contents

1. [Overview](#overview)
2. [AI Tool Selection](#ai-tool-selection)
3. [Effective Prompting Strategies](#effective-prompting-strategies)
4. [Command Development Workflow](#command-development-workflow)
5. [Code Review with AI](#code-review-with-ai)
6. [Testing with AI](#testing-with-ai)
7. [Debugging with AI](#debugging-with-ai)
8. [Documentation with AI](#documentation-with-ai)
9. [Best Practices](#best-practices)
10. [Common Pitfalls](#common-pitfalls)
11. [Example Workflows](#example-workflows)

---

## Overview

AI tools can significantly accelerate MythosMUD command development when used effectively. This guide provides
strategies for leveraging AI to write better code, catch bugs, and maintain consistency with project patterns.

### Benefits of AI-Assisted Development

**Faster Implementation**: Generate boilerplate code and common patterns

**Consistency**: Ensure adherence to project conventions

**Bug Prevention**: Catch common errors and security issues

**Learning**: Understand patterns and best practices

**Documentation**: Generate comprehensive documentation

### When to Use AI

**New Command Implementation**: Generate initial structure and patterns

**Code Review**: Identify potential issues and improvements

**Testing**: Generate test cases and edge case scenarios

**Documentation**: Create or update documentation

**Refactoring**: Improve existing code structure

- **Debugging**: Analyze error patterns and suggest fixes

---

## AI Tool Selection

### Primary Tools

1. **GitHub Copilot**: IDE integration for real-time code suggestions
2. **Claude/GPT**: General-purpose AI for complex reasoning and code generation
3. **Cursor AI**: Specialized for code understanding and generation
4. **Code Review Tools**: Automated code analysis and suggestions

### Tool-Specific Strategies

#### GitHub Copilot

```python
# Use descriptive comments to guide Copilot

async def handle_whisper_command(
    command_data: dict, current_user: dict, request: Any, alias_storage: AliasStorage, player_name: str
) -> dict[str, str]:
    """
    Handle the whisper command for private messaging.

    This command allows players to send private messages to other players in the same room.
    Only the target player should see the message.
    """
    # Copilot will suggest the implementation based on the comment

```

#### Claude/GPT

Use detailed prompts with context:

```
I'm implementing a new command called "whisper" for MythosMUD.
The command should allow players to send private messages to other players.

Requirements:
- Syntax: whisper <player> <message>
- Only the target player should see the message
- Players can't whisper to themselves
- Invalid player names should return an error
- Messages should be logged for moderation

Here's the existing command structure:
[Include relevant code examples]

Can you help me implement this command following the project's patterns?
```

---

## Effective Prompting Strategies

### 1. Provide Context

Always include relevant context about the project:

```
I'm working on MythosMUD, a Cthulhu Mythos-themed MUD built with:
- Python/FastAPI backend
- React/TypeScript frontend
- SQLite database
- Pydantic for validation
- Async command handlers

The project follows these patterns:
[Include specific patterns and conventions]
```

### 2. Be Specific About Requirements

```
I need a command handler that:
1. Validates the target player exists
2. Checks if the target is in the same room
3. Sends a private message only to the target
4. Logs the interaction for moderation
5. Returns appropriate error messages for invalid inputs
6. Follows the project's logging and error handling patterns
```

### 3. Include Examples

```
Here are examples of similar commands in the project:

[Include 2-3 relevant command examples]

Please follow the same patterns and conventions.
```

### 4. Specify Output Format

```
Please provide:
1. The command model (Pydantic class)
2. The command handler function
3. Test cases for the handler
4. Any necessary updates to the command parser
5. Brief explanation of the implementation
```

---

## Command Development Workflow

### Step 1: Planning with AI

**Prompt:**

```
I want to implement a new command called "whisper" for MythosMUD.
Can you help me plan the implementation?

Requirements:
- Players can whisper to other players in the same room
- Only the target player sees the message
- Syntax: whisper <player> <message>
- Should handle edge cases and errors gracefully

What components do I need to implement and what should I consider?
```

**Expected Response:**

- Command model structure
- Handler function requirements
- Integration points
- Security considerations
- Testing scenarios

### Step 2: Model Generation

**Prompt:**

```
Based on the MythosMUD command patterns, create a Pydantic model for a whisper command.

The command should have:
- target_player: required string (player to whisper to)
- message: required string (message content)

Include proper validation and follow the project's patterns.
```

### Step 3: Handler Implementation

**Prompt:**

```
Create a command handler for the whisper command following these patterns:

[Include existing handler examples]

The handler should:
1. Get the persistence layer from request.app.state.persistence
2. Validate the target player exists and is in the same room
3. Send the message only to the target player
4. Log the interaction
5. Handle all error cases gracefully
```

### Step 4: Integration

**Prompt:**

```
I have implemented the whisper command model and handler.
What other files do I need to update to integrate this command?

Please show me the specific changes needed for:
1. Command service registration
2. Command parser updates
3. Command type enum
```

### Step 5: Testing

**Prompt:**

```
Generate comprehensive test cases for the whisper command handler.

Include tests for:
- Successful whisper to valid player
- Whisper to non-existent player
- Whisper to player not in same room
- Whisper to self
- Missing parameters
- Empty message
- Very long message
- Security edge cases
```

---

## Code Review with AI

### Review Prompts

#### General Code Review

```
Please review this command handler for MythosMUD:

[Include code]

Check for:
1. Security issues
2. Error handling
3. Logging consistency
4. Performance concerns
5. Adherence to project patterns
6. Missing edge cases
```

#### Security-Focused Review

```
Please perform a security review of this command handler:

[Include code]

Focus on:
1. Input validation
2. Authorization checks
3. Injection vulnerabilities
4. Rate limiting considerations
5. Logging sensitive information
6. Error message information disclosure
```

#### Performance Review

```
Please review this command handler for performance issues:

[Include code]

Check for:
1. Unnecessary database queries
2. Inefficient algorithms
3. Memory leaks
4. Blocking operations
5. Caching opportunities
6. Batch processing possibilities
```

### Review Response Format

```
## Security Issues

[Issue 1]: Description and fix
- [Issue 2]: Description and fix

## Code Quality

[Issue 1]: Description and improvement
- [Issue 2]: Description and improvement

## Performance

[Issue 1]: Description and optimization
- [Issue 2]: Description and optimization

## Recommendations

[Recommendation 1]
- [Recommendation 2]
```

---

## Testing with AI

### Test Generation

#### Unit Test Generation

```
Generate unit tests for this command handler:

[Include handler code]

Requirements:
- Use pytest and unittest.mock
- Test all success and error paths
- Mock all external dependencies
- Include edge cases
- Follow project testing patterns
```

#### Integration Test Generation

```
Generate integration tests for the whisper command:

[Include command details]

Test scenarios:
- End-to-end command execution
- Database interactions
- Event system integration
- Error handling in real environment
```

#### Edge Case Testing

```
What edge cases should I test for the whisper command?

Consider:
- Input validation
- Database failures
- Network issues
- Concurrent access
- Resource limits
- Security scenarios
```

### Test Review

```
Please review these tests for the whisper command:

[Include test code]

Check for:
1. Test coverage completeness
2. Proper mocking
3. Edge case coverage
4. Test readability
5. Performance considerations
6. Maintainability
```

---

## Debugging with AI

### Error Analysis

#### Stack Trace Analysis

```
I'm getting this error in my command handler:

[Include error and stack trace]

Can you help me understand what's causing this and how to fix it?

Context:
- Command: whisper
- Handler: [Include relevant code]
- Environment: [Include relevant details]
```

#### Logic Debugging

```
My whisper command isn't working as expected:

Expected: Message sent only to target player
Actual: Message sent to all players in room

[Include handler code]

Can you help me identify the issue?
```

### Performance Debugging

```
My command handler is running slowly:

[Include handler code and performance metrics]

Can you help me identify performance bottlenecks and suggest optimizations?
```

---

## Documentation with AI

### Code Documentation

```
Please add comprehensive docstrings to this command handler:

[Include code]

Follow the project's documentation style and include:
- Function purpose
- Parameter descriptions
- Return value description
- Usage examples
- Error conditions
```

### README Updates

```
I've implemented a new whisper command.
Can you help me update the project documentation?

[Include command details]

Please suggest updates for:
1. Command reference documentation
2. User guide
3. Developer documentation
4. Changelog entry
```

---

## Best Practices

### 1. Iterative Development

```
Don't try to generate everything at once. Use AI for:
1. Initial structure and patterns
2. Review and refinement
3. Testing and edge cases
4. Documentation and cleanup
```

### 2. Context Preservation

```
Always provide sufficient context:
- Project structure and patterns
- Existing code examples
- Specific requirements and constraints
- Error messages and stack traces
```

### 3. Validation and Review

```
Never use AI-generated code without:
1. Understanding what it does
2. Reviewing for security issues
3. Testing thoroughly
4. Ensuring it follows project patterns
```

### 4. Learning and Improvement

```
Use AI to learn:
- Ask for explanations of generated code
- Request alternative approaches
- Get feedback on your implementations
- Understand best practices and patterns
```

### 5. Security First

```
Always review AI-generated code for:
- Input validation
- Authorization checks
- Injection vulnerabilities
- Information disclosure
- Resource exhaustion
```

---

## Common Pitfalls

### 1. Over-Reliance on AI

```
❌ Don't: Use AI-generated code without understanding it
✅ Do: Use AI as a tool to accelerate your development, not replace your thinking
```

### 2. Insufficient Context

```
❌ Don't: Ask AI to implement without providing project context
✅ Do: Include relevant code examples, patterns, and requirements
```

### 3. Ignoring Security

```
❌ Don't: Assume AI-generated code is secure
✅ Do: Always review for security issues and validate inputs
```

### 4. Poor Testing

```
❌ Don't: Skip testing AI-generated code
✅ Do: Write comprehensive tests and verify functionality
```

### 5. Inconsistent Patterns

```
❌ Don't: Mix different coding styles and patterns
✅ Do: Ensure AI-generated code follows project conventions
```

---

## Example Workflows

### Complete Command Implementation

#### Step 1: Planning

**Prompt:**

```
I want to implement a "whisper" command for MythosMUD.
Can you help me plan the implementation?

Requirements:
- Players can whisper to other players in the same room
- Only the target player sees the message
- Syntax: whisper <player> <message>
- Should handle edge cases and errors gracefully

What components do I need to implement?
```

#### Step 2: Model Creation

**Prompt:**

```
Create a Pydantic model for the whisper command following these patterns:

[Include existing command models]

Requirements:
- target_player: required string
- message: required string
- Proper validation for both fields
```

#### Step 3: Handler Implementation

**Prompt:**

```
Create a command handler for the whisper command:

[Include handler examples and requirements]

The handler should validate the target player exists and is in the same room,
send the message only to the target, and handle all error cases.
```

#### Step 4: Integration

**Prompt:**

```
What files do I need to update to integrate the whisper command?

[Include current implementation]

Please show the specific changes needed.
```

#### Step 5: Testing

**Prompt:**

```
Generate comprehensive tests for the whisper command:

[Include handler code]

Include tests for all success and error scenarios.
```

#### Step 6: Review

**Prompt:**

```
Please review this complete whisper command implementation:

[Include all code]

Check for security, performance, and adherence to project patterns.
```

### Bug Fixing Workflow

#### Step 1: Error Analysis

**Prompt:**

```
I'm getting this error in my command handler:

[Include error and context]

Can you help me understand what's causing this?
```

#### Step 2: Solution Generation

**Prompt:**

```
Based on the error analysis, can you suggest a fix?

[Include current code and error details]

Please provide the corrected implementation.
```

#### Step 3: Testing the Fix

**Prompt:**

```
I've implemented the fix. Can you help me create tests to verify it works?

[Include fixed code]

Generate tests that would have caught this bug.
```

### Refactoring Workflow

#### Step 1: Code Review

**Prompt:**

```
Please review this command handler for improvement opportunities:

[Include code]

Focus on:
- Code organization
- Error handling
- Performance
- Security
- Maintainability
```

#### Step 2: Refactoring

**Prompt:**

```
Based on the review, can you help me refactor this code?

[Include current code and review feedback]

Please provide an improved version that addresses the issues.
```

#### Step 3: Validation

**Prompt:**

```
I've refactored the code. Can you help me verify the changes are correct?

[Include before and after code]

Check that:
- Functionality is preserved
- Issues are resolved
- New issues weren't introduced
```

---

## AI Tool Configuration

### IDE Settings

```json
// VS Code settings for AI development
{
    "github.copilot.enable": {
        "*": true,
        "plaintext": false,
        "markdown": true,
        "scminput": false
    },
    "github.copilot.chat.enable": true,
    "github.copilot.chat.autoComplete": true
}
```

### Prompt Templates

#### Command Implementation Template

```
I'm implementing a new command called "{command_name}" for MythosMUD.

Requirements:
{requirements}

Project Context:
- Python/FastAPI backend
- Pydantic validation
- Async command handlers
- SQLite database
- Event-driven architecture

Existing Patterns:
{existing_patterns}

Please help me implement this command following the project's conventions.
```

#### Code Review Template

```
Please review this {component_type} for MythosMUD:

{code}

Focus on:
- Security issues
- Error handling
- Performance concerns
- Adherence to project patterns
- Code quality and maintainability

Please provide specific recommendations for improvement.
```

#### Testing Template

```
Generate tests for this {component_type}:

{code}

Requirements:
- Use pytest and unittest.mock
- Test all success and error paths
- Include edge cases
- Follow project testing patterns
- Ensure good coverage
```

---

## Conclusion

AI tools can be powerful allies in MythosMUD development when used thoughtfully and responsibly. Remember:

**AI is a tool, not a replacement** for understanding and critical thinking

**Always review and validate** AI-generated code

**Provide sufficient context** for better results

**Focus on security and testing** when using AI assistance

**Learn from AI suggestions** to improve your own skills

By following these guidelines, you can leverage AI to accelerate development while maintaining code quality and
security.

---

*This guide should be updated as AI tools evolve and new best practices emerge.*
