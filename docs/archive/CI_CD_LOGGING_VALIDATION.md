# CI/CD Enhanced Logging Validation

## Overview

This document describes how enhanced logging validation is integrated into the CI/CD pipeline to ensure all code uses the enhanced logging system correctly and doesn't use deprecated logging patterns.

## Pipeline Integration

### GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml

name: CI/CD Pipeline with Enhanced Logging Validation

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  enhanced-logging-validation:
    name: Enhanced Logging Pattern Validation
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install uv
          uv sync

      - name: Run enhanced logging pattern linter
        run: |
          python scripts/lint_logging_patterns.py

      - name: Validate pre-commit hooks
        run: |
          pre-commit run --all-files

      - name: Run tests with enhanced logging
        run: |
          make test
          make test-comprehensive

      - name: Generate logging coverage report
        run: |
          python scripts/generate_logging_coverage.py

      - name: Upload logging validation results
        uses: actions/upload-artifact@v3
        with:
          name: logging-validation-results
          path: |
            logs/
            coverage.xml
            logging-coverage-report.html

  security-validation:
    name: Security and Privacy Validation
    runs-on: ubuntu-latest
    needs: enhanced-logging-validation

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          pip install uv
          uv sync

      - name: Run security scanning
        run: |
          python scripts/security_scan.py

      - name: Validate COPPA compliance
        run: |
          python scripts/coppa_compliance_check.py

      - name: Check for sensitive data in logs
        run: |
          python scripts/sensitive_data_scan.py
```

### Pre-commit Hook Integration

```yaml
# .pre-commit-config.yaml

repos:
  - repo: local
    hooks:
      - id: logging-pattern-lint
        name: Enhanced Logging Pattern Linter
        entry: python scripts/lint_logging_patterns.py
        language: system
        types: [python]
        pass_filenames: false
        always_run: true
        stages: [pre-commit]

      - id: security-scan
        name: Security and Privacy Scanner
        entry: python scripts/security_scan.py
        language: system
        types: [python]
        pass_filenames: false
        always_run: true
        stages: [pre-commit]
```

## Validation Scripts

### Enhanced Logging Pattern Linter

```python
# scripts/lint_logging_patterns.py
#!/usr/bin/env python3
"""
Enhanced Logging Pattern Linter

This script validates that all Python files use the enhanced logging system
and don't use deprecated logging patterns.
"""

import ast
import sys
from pathlib import Path
from typing import List, Tuple

class LoggingPatternLinter(ast.NodeVisitor):
    """AST visitor to detect deprecated logging patterns."""

    def __init__(self):
        self.errors: List[Tuple[int, str]] = []
        self.imports = {}
        self.uses_enhanced_logging = False

    def visit_Import(self, node: ast.Import) -> None:
        """Check for deprecated logging imports."""
        for alias in node.names:
            if alias.name == "logging":
                self.errors.append((node.lineno, "FORBIDDEN: import logging - Use enhanced logging instead"))
            elif alias.name == "structlog" and not self.uses_enhanced_logging:
                self.errors.append((node.lineno, "FORBIDDEN: import structlog - Use enhanced logging instead"))

        self.imports[node.lineno] = [alias.name for alias in node.names]
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Check for deprecated logging imports."""
        if node.module == "logging":
            for alias in node.names:
                if alias.name in ["getLogger", "Logger"]:
                    self.errors.append((node.lineno, f"FORBIDDEN: from logging import {alias.name} - Use enhanced logging instead"))
        elif node.module == "server.logging.enhanced_logging_config":
            self.uses_enhanced_logging = True

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        """Check for deprecated logging patterns."""
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ["info", "debug", "warning", "error", "critical"]:
                # Check for context parameter (deprecated)

                for keyword in node.keywords:
                    if keyword.arg == "context":
                        self.errors.append((node.lineno, "FORBIDDEN: context parameter - Use direct key-value pairs instead"))

        self.generic_visit(node)

def lint_file(file_path: Path) -> List[Tuple[int, str]]:
    """Lint a single Python file for logging patterns."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content)
        linter = LoggingPatternLinter()
        linter.visit(tree)

        return linter.errors
    except Exception as e:
        return [(0, f"Error parsing file: {e}")]

def main():
    """Main function to run the linter."""
    project_root = Path(__file__).parent.parent
    python_files = list(project_root.rglob("*.py"))

    errors_found = False

    print("Checking Python files for enhanced logging patterns...")

    for file_path in python_files:
        # Skip __pycache__, test files, and virtual environment files

        if ("__pycache__" in str(file_path) or
            "test" in str(file_path).lower() or
            ".venv" in str(file_path) or
            "site-packages" in str(file_path)):
            continue

        errors = lint_file(file_path)

        if errors:
            errors_found = True
            print(f"\n{file_path.relative_to(project_root)}")
            for line_num, error_msg in errors:
                print(f"  Line {line_num}: {error_msg}")

    if errors_found:
        print("\nEnhanced logging pattern violations found!")
        print("\nFor correct usage, see:")
        print("  - docs/LOGGING_BEST_PRACTICES.md")
        print("  - docs/LOGGING_QUICK_REFERENCE.md")
        print("  - docs/examples/logging/")
        print("\nCorrect usage example:")
        print("  from server.logging.enhanced_logging_config import get_logger")
        print("  logger = get_logger(__name__)")
        print("  logger.info('message', key=value)")
        sys.exit(1)
    else:
        print("All files use enhanced logging correctly!")

if __name__ == "__main__":
    main()
```

### Security and Privacy Scanner

```python
# scripts/security_scan.py
#!/usr/bin/env python3
"""
Security and Privacy Scanner

This script scans for potential security and privacy issues in the codebase.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

class SecurityScanner:
    """Scanner for security and privacy issues."""

    def __init__(self):
        self.issues: List[Tuple[str, int, str]] = []

        # Patterns to detect sensitive data

        self.sensitive_patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', "Potential hardcoded password"),
            (r'token\s*=\s*["\'][^"\']+["\']', "Potential hardcoded token"),
            (r'secret\s*=\s*["\'][^"\']+["\']', "Potential hardcoded secret"),
            (r'api_key\s*=\s*["\'][^"\']+["\']', "Potential hardcoded API key"),
        ]

        # Patterns to detect logging of sensitive data

        self.logging_sensitive_patterns = [
            (r'logger\.(info|debug|warning|error|critical)\s*\(\s*[^)]*password[^)]*\)', "Logging sensitive data: password"),
            (r'logger\.(info|debug|warning|error|critical)\s*\(\s*[^)]*token[^)]*\)', "Logging sensitive data: token"),
            (r'logger\.(info|debug|warning|error|critical)\s*\(\s*[^)]*secret[^)]*\)', "Logging sensitive data: secret"),
        ]

    def scan_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """Scan a single file for security issues."""
        issues = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                # Check for sensitive data patterns

                for pattern, message in self.sensitive_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        issues.append((str(file_path), line_num, message))

                # Check for logging sensitive data

                for pattern, message in self.logging_sensitive_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        issues.append((str(file_path), line_num, message))

        except Exception as e:
            issues.append((str(file_path), 0, f"Error scanning file: {e}"))

        return issues

    def scan_directory(self, directory: Path) -> List[Tuple[str, int, str]]:
        """Scan a directory for security issues."""
        all_issues = []

        for file_path in directory.rglob("*.py"):
            if ("__pycache__" in str(file_path) or
                ".venv" in str(file_path) or
                "site-packages" in str(file_path)):
                continue

            issues = self.scan_file(file_path)
            all_issues.extend(issues)

        return all_issues

def main():
    """Main function to run the security scanner."""
    project_root = Path(__file__).parent.parent
    scanner = SecurityScanner()

    print("Scanning for security and privacy issues...")

    issues = scanner.scan_directory(project_root)

    if issues:
        print(f"\nFound {len(issues)} security/privacy issues:")
        for file_path, line_num, message in issues:
            print(f"  {file_path}:{line_num} - {message}")

        print("\nSecurity recommendations:")
        print("  - Use environment variables for sensitive data")
        print("  - Never log passwords, tokens, or secrets")
        print("  - Use enhanced logging security sanitization")
        print("  - Review docs/SECURITY.md for best practices")

        sys.exit(1)
    else:
        print("No security or privacy issues found!")

if __name__ == "__main__":
    main()
```

### COPPA Compliance Checker

```python
# scripts/coppa_compliance_check.py
#!/usr/bin/env python3
"""
COPPA Compliance Checker

This script validates COPPA compliance requirements for the MythosMUD project.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

class COPPAComplianceChecker:
    """Checker for COPPA compliance requirements."""

    def __init__(self):
        self.violations: List[Tuple[str, int, str]] = []

        # COPPA compliance patterns

        self.compliance_patterns = [
            (r'age\s*[<>=]\s*\d+', "Potential age-based logic - ensure COPPA compliance"),
            (r'birthdate|birth_date|date_of_birth', "Personal information collection - COPPA violation"),
            (r'email\s*=\s*[^@]+@[^@]+\.[^@]+', "Email collection - requires parental consent"),
            (r'phone|telephone|mobile', "Phone number collection - COPPA violation"),
            (r'address|street|city|state|zip', "Address collection - COPPA violation"),
            (r'parent|guardian|adult', "Parent/guardian references - ensure proper consent"),
        ]

        # Required COPPA compliance patterns

        self.required_patterns = [
            (r'coppa|COPPA', "COPPA compliance reference"),
            (r'parental.*consent|consent.*parental', "Parental consent mechanism"),
            (r'age.*verification|verification.*age', "Age verification mechanism"),
        ]

    def check_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """Check a single file for COPPA compliance."""
        violations = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                # Check for compliance violations

                for pattern, message in self.compliance_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append((str(file_path), line_num, message))

        except Exception as e:
            violations.append((str(file_path), 0, f"Error checking file: {e}"))

        return violations

    def check_directory(self, directory: Path) -> List[Tuple[str, int, str]]:
        """Check a directory for COPPA compliance."""
        all_violations = []

        for file_path in directory.rglob("*.py"):
            if ("__pycache__" in str(file_path) or
                ".venv" in str(file_path) or
                "site-packages" in str(file_path)):
                continue

            violations = self.check_file(file_path)
            all_violations.extend(violations)

        return all_violations

def main():
    """Main function to run the COPPA compliance checker."""
    project_root = Path(__file__).parent.parent
    checker = COPPAComplianceChecker()

    print("Checking COPPA compliance...")

    violations = checker.check_directory(project_root)

    if violations:
        print(f"\nFound {len(violations)} potential COPPA compliance issues:")
        for file_path, line_num, message in violations:
            print(f"  {file_path}:{line_num} - {message}")

        print("\nCOPPA compliance recommendations:")
        print("  - Never collect personal information from minors")
        print("  - Implement parental consent mechanisms")
        print("  - Use age verification systems")
        print("  - Review docs/SECURITY.md for COPPA guidelines")

        sys.exit(1)
    else:
        print("No COPPA compliance issues found!")

if __name__ == "__main__":
    main()
```

## Production Deployment

### Enhanced Logging in Production

```python
# server/config/production_logging.py

from server.logging.enhanced_logging_config import configure_production_logging

def setup_production_logging():
    """Configure enhanced logging for production environment."""

    # Configure structured logging for production

    configure_production_logging(
        log_level="INFO",
        enable_correlation_ids=True,
        enable_security_sanitization=True,
        enable_performance_monitoring=True,
        log_aggregation_endpoint="https://logs.mythosmud.com/api/v1/logs"
    )

    # Configure log rotation

    configure_log_rotation(
        max_file_size="100MB",
        backup_count=10,
        rotation_interval="daily"
    )

    # Configure security sanitization

    configure_security_sanitization(
        redact_fields=["password", "token", "secret", "key"],
        hash_sensitive_data=True,
        enable_audit_logging=True
    )
```

### Docker Configuration

```dockerfile
# Dockerfile.production

FROM python:3.12-slim

# Install dependencies

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application

COPY . /app
WORKDIR /app

# Configure enhanced logging

ENV LOG_LEVEL=INFO
ENV ENABLE_CORRELATION_IDS=true
ENV ENABLE_SECURITY_SANITIZATION=true
ENV ENABLE_PERFORMANCE_MONITORING=true

# Run application

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Monitoring and Alerting

### Log Aggregation

```yaml
# docker-compose.monitoring.yml

version: '3.8'
services:
  loki:
    image: grafana/loki:2.9.0
    ports:
      - "3100:3100"
    volumes:
      - ./monitoring/loki-config.yml:/etc/loki/local-config.yaml
    command: -config.file=/etc/loki/local-config.yaml

  promtail:
    image: grafana/promtail:2.9.0
    volumes:
      - ./logs:/var/log/mythosmud
      - ./monitoring/promtail-config.yml:/etc/promtail/config.yml
    command: -config.file=/etc/promtail/config.yml

  grafana:
    image: grafana/grafana:10.0.0
    ports:
      - "3000:3000"
    volumes:
      - ./monitoring/grafana-dashboards:/var/lib/grafana/dashboards
      - ./monitoring/grafana-provisioning:/etc/grafana/provisioning
    environment:
      GF_SECURITY_ADMIN_PASSWORD=admin
```

### Health Checks

```python
# server/monitoring/health.py

from fastapi import APIRouter, HTTPException
from server.logging.enhanced_logging_config import get_logger, bind_request_context

logger = get_logger(__name__)
router = APIRouter()

@router.get("/health")
async def health_check():
    """Comprehensive health check endpoint with enhanced logging."""
    # Bind request context for correlation tracking

    bind_request_context(
        correlation_id=f"health_check_{datetime.utcnow().timestamp()}",
        endpoint="/health",
        method="GET"
    )

    try:
        # Check database connectivity

        db_status = await check_database_health()

        # Check WebSocket connections

        ws_status = await check_websocket_health()

        # Check SSE connections

        sse_status = await check_sse_health()

        # Enhanced structured logging

        logger.info("Health check completed",
                   db_status=db_status,
                   ws_status=ws_status,
                   sse_status=sse_status,
                   endpoint="/health",
                   response_time_ms=calculate_response_time())

        return {
            "status": "healthy",
            "database": db_status,
            "websocket": ws_status,
            "sse": sse_status,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        # Enhanced error logging with context

        logger.error("Health check failed",
                    error=str(e),
                    error_type=type(e).__name__,
                    endpoint="/health",
                    stack_trace=traceback.format_exc())
        raise HTTPException(status_code=503, detail="Service unhealthy")
```

## Troubleshooting

### Common Issues

#### Logging Pattern Violations

**Issue**: Enhanced logging pattern violations in CI/CD

**Solution**: Run `python scripts/lint_logging_patterns.py` locally before committing

#### Security Violations

**Issue**: Sensitive data detected in code

**Solution**: Use environment variables and enhanced logging security sanitization

#### COPPA Compliance Issues

**Issue**: Potential COPPA violations detected

**Solution**: Review and implement proper consent mechanisms

### Debugging Commands

```bash
# Run enhanced logging pattern linter

python scripts/lint_logging_patterns.py

# Run security scan

python scripts/security_scan.py

# Run COPPA compliance check

python scripts/coppa_compliance_check.py

# Run all validation scripts

make validate-all
```

## Documentation References

**Enhanced Logging Guide**: [LOGGING_BEST_PRACTICES.md](LOGGING_BEST_PRACTICES.md)

**Quick Reference**: [LOGGING_QUICK_REFERENCE.md](LOGGING_QUICK_REFERENCE.md)

**Pre-commit Validation**: [PRE_COMMIT_LOGGING_VALIDATION.md](PRE_COMMIT_LOGGING_VALIDATION.md)
- **Security Guide**: [SECURITY.md](SECURITY.md)
- **Testing Examples**: [docs/examples/logging/](examples/logging/)
