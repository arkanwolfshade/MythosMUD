# OpenSSF Best Practices Badge Application Guide

This guide provides step-by-step instructions for applying to the OpenSSF Best Practices Badge for MythosMUD.

## Application URL
<https://www.bestpractices.dev/>/>

## Step 1: Initial Setup

1. Visit <https://www.bestpractices.dev/>/>
2. Click "Get a Badge"
3. Enter repository URL: `https://github.com/arkanwolfshade/MythosMUD`
4. Click "Get Badge"

## Step 2: Self-Assessment Questionnaire

### Basic Information


- **Project Name**: My<https://github.com/arkanwolfshade/MythosMUD>
- **Repository URL**: <https://github.com/arkanwolfshade/MythosMUD>
- **Badge Level**: Gold (10 points)

### Passing Level Criteria (5 points)


#### 1. Basic Project Website Content ✅

- **Question**: Does the project have a basic project website?
- **Answer**: Yes
- **Evidence**: README.md with comprehensive project overview, setup instructions, and documentation links


#### 2. Open Source License ✅

- **Question**: Does the project have an open source license?
- **Answer**: Yes

- **Evidence**: MIT License in LICENSE file and referenced in README.md

#### 3. Documenation ✅

- **Question**: Does the project have documentation?
- **Answer**: Yes
- **Evidence**:
  - README.md - Project overview and quickstart
  - DEVELOPMENT.md - Development setup instructions
  - docs/PRD.md - Product requirements document
  - PLANNING.md - Architecture and planning

  - SECURITY.md - Security documentation
  - TASKS.md - Development tasks

#### 4. Change Control ✅


- **Question**: Does the project use change control?
- **Answer**: Yes
- **Evidence**: Git repository with full history, GitHub Issues for task tracking, pull request workflow

#### 5. Reporting ✅

- **Question**: Does the project have a reporting process?

- **Answer**: Yes
- **Evidence**: Security vulnerability reporting process documented in SECURITY.md, contact information in README.md, GitHub Issues for bug reports

### Silver Level Criteria (7 points)

#### 6. Quality ✅

- **Question**: Does the project have quality assurance?
- **Answer**: Yes

- **Evidence**:
  - Automated testing with pytest (70%+ coverage requirement)
  - CI/CD pipeline with GitHub Actions (.github/workflows/ci.yml)
  - Code linting with ruff for Python, ESLint for JavaScript/TypeScript
  - Pre-commit hooks for quality checks

#### 7. Security ✅

- **Question**: Does the project have security practices?
- **Answer**: Yes
- **Evidence**:
  - Comprehensive security documentation in SECURITY.md

  - CodeQL static analysis (.github/workflows/codeql.yml)
  - Semgrep security scanning (.github/workflows/semgrep.yml)
  - Dependency vulnerability scanning (.github/workflows/dependency-review.yml)
  - Known vulnerabilities tracked and fixed (documented in SECURITY.md)

### Gold Level Criteria (10 points)

#### 8. Analysis ✅


- **Question**: Does the project use static analysis?
- **Answer**: Yes
- **Evidence**:
  - CodeQL static analysis for Python security
  - Semgrep multi-language security scanning
  - Scorecard supply chain security analysis (.github/workflows/scorecards.yml)
  - Automated vulnerability detection in CI/CD

#### 9. Security Review ✅


- **Question**: Does the project have security reviews?
- **Answer**: Yes
- **Evidence**:
  - Regular security audits documented in SECURITY.md
  - Known vulnerabilities tracked and fixed
  - Security best practices implemented (input validation, path validation, XSS prevention)
  - Secure authentication system with JWT and bcrypt

#### 10. Build Reproducibility ✅


- **Question**: Does the project have reproducible builds?
- **Answer**: Yes
- **Evidence**:
  - Locked dependencies (uv.lock for Python, package-lock.json for Node.js)
  - Pinned GitHub Actions versions in CI workflows
  - Deterministic builds via CI/CD pipeline

  - Environment-specific configurations (server_config.yaml)

## Step 3: Supporting Documentation

### Key Documents to Reference

1. **docs/OPENSSF_BEST_PRACTICES.md** - Comprehensive compliance documentation
2. **SECURITY.md** - Security practices and vulnerability reporting
3. **README.md** - Project overview and documentation links
4. **.github/workflows/** - CI/CD and security scanning workflows

### Evidence Files

- `.github/workflows/ci.yml` - Automated testing and quality checks
- `.github/workflows/codeql.yml` - Static security analysis
- `.github/workflows/semgrep.yml` - Security scanning
- `.github/workflows/scorecards.yml` - Supply chain security analysis
- `.github/workflows/dependency-review.yml` - Dependency vulnerability scanning
- `SECURITY.md` - Security documentation and practices
- `uv.lock` and `client/package-lock.json` - Locked dependencies


## Step 4: Submission

1. Review all answers for accuracy
2. Submit the application
3. Wait for OpenSSF team review (typically 1-2 weeks)
4. Receive badge notification

## Step 5: Badge Display

Once the badge is awarded:


1. Add the badge to README.md:

   ```markdown
   [![OpenSSF Best Practices](https://www.bestpractices.dev/projects/XXXX/badge)](https://www.bestpractices.dev/projects/XXXX)

   ```<https://www.bestpractices.dev/>
<https://www.bestpractices.dev/criteria/2>
2. Update the badge <https://github.com/ossf/scorecard/blob/main/docs/checks.md>

3. Commit and push the changes

## Troubleshooting

### Common Issues

- **Missing Documentation**: Ensure all referenced documents exist and are accessible
- **Broken Links**: Verify all GitHub workflow links are working
- **Incomplete Evidence**: Make sure all security practices are documented

### Support

- OpenSSF Best Practices: <https://www.bestpractices.dev/>
- Badge Criteria: <https://www.bestpractices.dev/criteria/2>
- Scorecard Checks: <https://github.com/ossf/scorecard/blob/main/docs/checks.md>

---

*This guide should be updated after the badge application is completed with the actual project ID and badge URL.*
