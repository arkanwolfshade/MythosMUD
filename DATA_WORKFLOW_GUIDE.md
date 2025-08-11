# MythosMUD Data Workflow Guide

## Overview
With the git submodule setup, your workflow for managing game data changes slightly. This guide explains the new process and provides tools to make it seamless.

## Your New Workflow

### 🔄 Before (Single Repository)
1. **Generate new rooms** → Edit files in `data/rooms/`
2. **Run server locally** → Test with local data
3. **Commit and push** → Single `git push`

### 🔄 After (Submodule Setup)
1. **Generate new rooms** → Edit files in `data/rooms/` *(same)*
2. **Run server locally** → Test with local data *(same)*
3. **Commit data changes** → Push to private data repo
4. **Update submodule reference** → Push to main repo

## 🛠️ Automated Workflow (Recommended)

### Using the Commit Script
```bash
# After making room changes, simply run:
python scripts/commit_data_changes.py

# Or with a commit message:
python scripts/commit_data_changes.py commit "Add new Arkham downtown rooms"
```

### What the Script Does
1. **Checks for changes** in the data directory
2. **Commits and pushes** data changes to private repo
3. **Updates submodule reference** in main repo
4. **Pushes main repo** changes

## 🛠️ Manual Workflow

### Step-by-Step Process
```bash
# 1. Make your room changes (same as before)
# Edit files in data/rooms/earth/arkham_city/

# 2. Test locally (same as before)
python scripts/start_dev.ps1

# 3. Commit data changes
cd data
git add .
git commit -m "Add new Arkham downtown rooms"
git push origin main
cd ..

# 4. Update submodule reference
git add data
git commit -m "Update data submodule with new rooms"
git push origin main
```

## 📋 Common Scenarios

### Adding New Rooms
```bash
# 1. Create new room files in data/rooms/
# 2. Test with server
python scripts/start_dev.ps1

# 3. Commit changes
python scripts/commit_data_changes.py commit "Add new campus buildings"
```

### Updating Existing Rooms
```bash
# 1. Edit room files in data/rooms/
# 2. Test changes
python scripts/start_dev.ps1

# 3. Commit changes
python scripts/commit_data_changes.py commit "Update downtown room descriptions"
```

### Checking Status
```bash
# See what changes are pending
python scripts/commit_data_changes.py status
```

## 🔧 Troubleshooting

### Submodule Not Initialized
```bash
# If data/ directory is empty
git submodule init
git submodule update
```

### Data Changes Not Detected
```bash
# Check if you're in the right directory
cd data
git status
cd ..
```

### Push Failed
```bash
# Check if you have access to the private repo
# Ensure you're authenticated with GitHub
git remote -v
```

## 🎯 Benefits of This Setup

### Security
- **Private data repository** prevents player cheating
- **Separate access controls** for data vs code
- **No sensitive data in public repo**

### Development
- **Independent versioning** of data and code
- **Easier collaboration** on data without code changes
- **Clean separation** of concerns

### Deployment
- **Production servers** can pull latest data independently
- **Rollback capability** for data changes
- **Audit trail** for all data modifications

## 📝 Best Practices

### Commit Messages
- **Be descriptive** about what rooms/areas you're adding/modifying
- **Include context** about the changes (e.g., "Add new campus buildings for Miskatonic University")
- **Reference issues** if applicable (e.g., "Fix room connectivity issues #123")

### Testing
- **Always test locally** before committing
- **Use the map builder** to verify room connectivity
- **Run the room validator** to check for issues

### Frequency
- **Commit frequently** rather than large batches
- **Group related changes** in single commits
- **Keep data and code changes separate**

## 🚀 Quick Reference

### Daily Workflow
```bash
# 1. Make changes to data/rooms/
# 2. Test: python scripts/start_dev.ps1
# 3. Commit: python scripts/commit_data_changes.py
```

### Status Check
```bash
python scripts/commit_data_changes.py status
```

### Manual Commit
```bash
python scripts/commit_data_changes.py commit "Your commit message"
```

### Submodule Issues
```bash
git submodule update --remote data
```

This workflow maintains the simplicity of your current process while adding the security benefits of the submodule setup!
