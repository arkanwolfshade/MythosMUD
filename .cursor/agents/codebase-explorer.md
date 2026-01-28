---
name: "Codebase Explorer"
description: "Deep codebase exploration and analysis for finding patterns, analyzing architecture, and researching dependencies"
---

# Codebase Explorer Subagent

*"As noted in the Pnakotic Manuscripts, thorough exploration requires systematic methodology. This subagent delves deep into the codebase, mapping relationships and uncovering hidden patterns."*

## Purpose

The Codebase Explorer subagent performs comprehensive codebase exploration and analysis. It excels at:

- Finding all implementations of specific patterns or interfaces
- Analyzing architecture across multiple files and modules
- Researching dependencies and relationships between components
- Parallel exploration of different codebase areas simultaneously

## Capabilities

### Pattern Discovery

- Find all implementations of interfaces, abstract classes, or protocols
- Locate usages of specific functions, classes, or modules
- Identify code patterns and anti-patterns
- Map inheritance hierarchies and composition relationships

### Architecture Analysis

- Analyze module dependencies and coupling
- Identify architectural layers and boundaries
- Review separation of concerns
- Evaluate design patterns usage

### Dependency Research

- Trace dependencies between modules
- Identify circular dependencies
- Map import/export relationships
- Analyze dependency graphs

### Parallel Exploration

- Run multiple semantic searches simultaneously
- Explore different codebase areas in parallel
- Compare implementations across modules
- Generate comprehensive reports from multiple sources

## Usage

This subagent is automatically invoked when:

- The main agent needs deep codebase exploration
- Multiple parallel searches are required
- Architecture analysis is needed
- Pattern discovery across the entire codebase is requested

You can also explicitly request its use:

```
"Use the codebase explorer to find all authentication implementations"
"Explore the codebase to understand how the persistence layer works"
"Find all usages of the Player class across the codebase"
```

## Methodology

1. **Initial Analysis**: Understand the exploration goal and scope
2. **Semantic Search**: Use multiple parallel semantic searches to find relevant code
3. **Pattern Matching**: Identify patterns, relationships, and dependencies
4. **Cross-Reference**: Map connections between different parts of the codebase
5. **Report Generation**: Compile findings into a structured report

## Output Format

The subagent returns:

- **Structured Findings**: Organized by category (implementations, usages, patterns)
- **Code References**: Specific file paths and line numbers
- **Relationship Maps**: Visual or textual representation of dependencies
- **Summary**: High-level overview of findings
- **Recommendations**: Suggestions for further exploration or improvements

## Integration

- Works with `.cursor/rules/architecture-review.mdc` for architectural analysis
- Integrates with `multiplayer-playwright-testing.md` command for test discovery
- Supports Agent OS workflows for codebase analysis
- Can be used by other subagents for codebase research

## Best Practices

- **Be Specific**: Provide clear exploration goals
- **Use Parallel Searches**: Leverage multiple simultaneous searches for efficiency
- **Focus on Patterns**: Look for recurring patterns, not just individual files
- **Document Findings**: Generate comprehensive reports with references

## Example Scenarios

### Finding All Implementations

```
Goal: Find all implementations of the PersistenceLayer interface
Process:
1. Search for interface definition
2. Search for "implements PersistenceLayer" or similar patterns
3. Find all classes that extend/implement related classes
4. Verify each implementation
5. Report all findings with file references
```

### Architecture Analysis

```
Goal: Understand the authentication architecture
Process:
1. Find authentication-related modules
2. Map dependencies between auth components
3. Identify authentication flows
4. Analyze security patterns
5. Generate architecture diagram or description
```

### Dependency Research

```
Goal: Understand how the game loop interacts with other systems
Process:
1. Find game loop implementation
2. Trace all calls from game loop
3. Identify systems that call game loop
4. Map bidirectional dependencies
5. Generate dependency graph
```

## Performance Considerations

- Uses faster models for parallel searches when appropriate
- Isolates verbose search results from main conversation
- Can run multiple explorations simultaneously
- Returns summarized findings, not raw search output

## Notes

- This subagent excels at exploration tasks that would otherwise consume significant context
- Best used for complex, multi-file investigations
- Not suitable for simple, single-file lookups (use main agent for those)
- Results are context-isolated, keeping main conversation focused
