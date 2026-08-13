# Codacy High/Critical Baseline – MythosMUD

This document captures a snapshot of the **High** and **Critical** issues reported by Codacy for the
`MythosMUD` repository, using the Codacy UI filtered to `Severities = High, Error`.

## Summary (from Codacy UI snapshot)

- **Total High + Critical issues**: ~8161
- **Repository**: `arkanwolfshade/MythosMUD`
- **View**: `Issues > Current > Severities: High, Error`

### Top code patterns by issue count

From the Codacy UI summary:

- **Detect Common Security Issues in Python Code** – 7938 issues
- **Disallow Unnecessary Conditions** – 84 issues
- **Disallow Non-Null Assertion Operator** – 53 issues
- **Enforce Access to RAC\_\* Tables in SQL Queries** – 50 issues
- **Prohibit CSS Syntax Errors** – 13 issues
- **Audit Dangerous Subprocess Use** – 6 issues
- **Detect CRLF Injection in Logs** – 5 issues
- **Enforce ANSI SQL Syntax Compliance** – 2 issues
- **Detect Base64 High Entropy Strings** – 2 issues
- **Detect Insecure Dependencies (High Severity)** – 2 issues
- **Avoid Using Non-Literal Values in RegExp Constructor** – 2 issues
- **Others** – 2 issues

### Example issue types

- **Python security (Bandit/Semgrep)**:
  - Example shown in Codacy UI: High severity \"Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.\" in
    `server/tests/unit/persistence/test_player_effect_repository.py` (and many other test files).
- **CSS syntax**:
  - Critical error in `client/src/index.css` around `grid-template-columns` with token `1fr 1fr` (reported as an
    unexpected token at line 983, column 28 in the snapshot).

### Distribution notes

- The vast majority of High issues come from the generic Python security pattern bucket
  (**\"Detect Common Security Issues in Python Code\"**), which likely aggregates several underlying rules
  (e.g. use of `assert`, dangerous modules/APIs, subprocess usage, etc.).
- A smaller number of issues relate to:
  - Frontend code (CSS syntax, RegExp constructor usage).
  - SQL / ANSI / RAC\_\* table rules.
  - Dependency security (high severity vulnerabilities).

This baseline should be updated after each major remediation wave to track progress in reducing High and Critical
issues for MythosMUD.
