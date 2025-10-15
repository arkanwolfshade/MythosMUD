# Spec Requirements Document

> Spec: E2E Playwright CLI Conversion
> Created: 2025-10-08

## Overview

Convert 10 of 21 multiplayer E2E test scenarios from AI Agent + Playwright MCP execution to automated Playwright CLI tests that can run in CI/CD pipelines, while maintaining the 11 scenarios that require true multiplayer real-time coordination in the MCP-based test suite. This conversion will enable faster feedback loops, reduce AI Agent execution costs, and improve test coverage for error handling, accessibility, and integration scenarios.

## User Stories

### Automated E2E Test Execution

As a **developer**, I want to run automated E2E tests locally and in CI/CD pipelines, so that I can get immediate feedback on code changes without requiring AI Agent coordination or manual test execution.

**Workflow**: Developer makes changes to error handling code, runs `make test-client-runtime` locally, receives immediate feedback on test results. On PR creation, GitHub Actions automatically runs the full E2E test suite and reports results. Developer fixes any issues and pushes updates. Tests re-run automatically and gate the PR merge.

**Problem Solved**: Currently all 21 scenarios require manual AI Agent execution via Playwright MCP, which is slow, expensive, and cannot run in automated pipelines. This blocks rapid iteration and increases time-to-feedback for developers.

### Test Data Management for Automated Tests

As a **QA engineer**, I want automated test data seeding and cleanup between test runs, so that tests are reliable, repeatable, and don't interfere with each other or with development data.

**Workflow**: QA engineer runs full E2E test suite. Before tests start, test database is seeded with known players, rooms, and state. Each test runs against clean, predictable data. After tests complete, test data is cleaned up. Next test run starts fresh with same seeded data. Tests pass consistently regardless of previous test runs or development database state.

**Problem Solved**: Current manual MCP tests require manual database verification and cleanup. This leads to flaky tests, unpredictable failures, and wasted time debugging environment issues rather than actual bugs.

### Focused MCP Testing for Real Multiplayer Scenarios

As a **test automation engineer**, I want to focus Playwright MCP scenarios on only the features that truly require real-time multi-player coordination, so that I can minimize AI Agent execution time and costs while maintaining comprehensive test coverage.

**Workflow**: Engineer reviews scenario playbook, identifies which scenarios test single-player features (errors, accessibility, etc.) versus true multiplayer interaction (message broadcasting, state synchronization). Converts single-player scenarios to automated Playwright CLI tests. Refactors multiplayer scenarios to be more focused and efficient. Results in 11 focused MCP scenarios instead of 21, reducing execution time by ~50%.

**Problem Solved**: Current MCP playbook contains scenarios that don't actually need multi-tab real-time coordination, wasting AI Agent resources on tests that could be automated. This increases costs and reduces the efficiency of manual test execution.

## Spec Scope

1. **Test Infrastructure Setup** - Create Playwright runtime test configuration, fixtures for authentication and player management, and directory structure for organized test files.

2. **Category A Full Conversion** - Convert 6 scenarios (Local Channel Errors, Whisper Errors, Whisper Rate Limiting, Whisper Logging, Logout Errors, Logout Accessibility) to fully automated Playwright CLI tests.

3. **Category B Partial Conversion** - Split 4 scenarios (Who Command, Logout Button, Local Channel Integration, Whisper Integration) into automated tests for single-player functionality plus simplified MCP scenarios for multi-player verification.

4. **Test Database Seeding** - Implement test data seeding strategy using the existing `data/` directory structure with test-specific players, rooms, and NPCs for predictable test execution.

5. **Database Cleanup Mechanisms** - Create before/after hooks for test data cleanup and reset to ensure test isolation and repeatability.

6. **GitHub Actions Integration** - Update CI/CD workflows to run automated Playwright CLI tests on PR creation and merge, with proper test reporting and failure handling.

7. **Makefile Target Updates** - Add `test-client-runtime` and `test-server-runtime` targets for easy local test execution and CI/CD integration.

8. **MCP Scenario Refactoring** - Refactor the 11 remaining MCP scenarios to be more focused, efficient, and clearly documented as requiring multi-player coordination.

## Out of Scope

- Converting any scenarios that require true multi-player real-time coordination (11 scenarios remain in MCP)
- Changes to server-side code or API endpoints
- Modifications to existing Playwright MCP infrastructure
- Performance optimization of test execution speed
- Visual regression testing or screenshot comparison
- Load testing or stress testing scenarios
- Integration with external test reporting services beyond GitHub Actions
- Automated test data generation beyond basic seeding

## Expected Deliverable

1. **Fully Automated Test Suite** - 10 scenarios (6 full + 4 partial) converted to automated Playwright CLI tests that run successfully in local development and CI/CD without manual intervention.

2. **Test Data Seeding System** - Automated database seeding and cleanup mechanisms that provide predictable, isolated test data for each test run using the `data/` directory structure.

3. **CI/CD Integration** - GitHub Actions workflow updates that automatically run the new Playwright CLI tests on PR creation and merge, with clear pass/fail reporting and test artifacts.

4. **Refactored MCP Playbook** - Updated multiplayer scenario playbook containing only the 11 scenarios that truly require multi-player coordination, with improved documentation and execution efficiency.

5. **Developer Documentation** - Updated testing documentation explaining when to use automated Playwright CLI tests versus MCP scenarios, how to run tests locally, and how to add new test scenarios.
