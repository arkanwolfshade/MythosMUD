# Spec Requirements Document

> Spec: E2E Test Suite Refactor
> Created: 2025-09-18

## Overview

Refactor the monolithic MULTIPLAYER_SCENARIOS_PLAYBOOK.md into a structured, modular E2E test suite with individual scenario files, master rules, and hybrid Playwright testing approach to improve maintainability, reduce AI context requirements, and enable selective scenario execution.

## User Stories

### Test Suite Maintainability

As a developer, I want to work with individual scenario files instead of a massive 2900+ line playbook, so that I can focus on specific test scenarios without overwhelming AI context limits and can easily modify or add new tests.

The current playbook has grown beyond practical AI context limits, making it difficult to execute individual scenarios or make targeted modifications. A modular structure will allow developers to work with specific scenarios while maintaining shared execution rules.

### Selective Test Execution

As a QA engineer, I want to run individual test scenarios or groups of related scenarios, so that I can test specific functionality without executing the entire test suite.

The modular structure will enable running specific scenarios (e.g., just whisper channel tests) or subsets of tests based on development needs, reducing test execution time and improving debugging efficiency.

### Hybrid Testing Approach

As a test automation engineer, I want to use the most appropriate testing tool for each scenario, so that simple tests use standard Playwright while complex multi-tab interactions use Playwright MCP.

Different scenarios have different complexity requirements - some can use standard Playwright tests for CI/CD integration, while others need the advanced multi-tab capabilities of Playwright MCP for realistic user simulation.

## Spec Scope

1. **Master Rules File** - Extract common execution procedures, database verification, server management, and configurable timeout settings into a reusable MULTIPLAYER_TEST_RULES.md file
2. **Individual Scenario Files** - Create 21 separate scenario files with execution steps, expected results, and success criteria for each multiplayer test case
3. **Supporting Documentation** - Create separate CLEANUP.md and TROUBLESHOOTING.md files for post-execution procedures and error handling
4. **Hybrid Testing Implementation** - Implement both standard Playwright and Playwright MCP approaches based on scenario complexity requirements
5. **Cursor Rules Integration** - Update the run-multiplayer-playbook rule to reference the new modular structure

## Out of Scope

- Modifying the actual test scenarios or expected behaviors
- Changing the server or client code being tested
- Implementing new testing frameworks beyond Playwright
- Creating CI/CD pipeline integration (separate task)
- Performance optimization of the test execution itself

## Expected Deliverable

1. A complete modular E2E test suite with 21 individual scenario files, master rules, and supporting documentation that can be executed individually or as groups
2. Updated cursor rules that reference the new modular structure and maintain backward compatibility with existing workflows
3. Hybrid testing implementation that uses the most appropriate Playwright approach for each scenario's complexity level
