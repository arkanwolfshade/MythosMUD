# Cursor IDE Quick Reference - Worktree Integration

*"Efficiency in our eldritch research requires mastery of our tools"* - Professor Wolfshade

## 🚀 Essential Commands

### Worktree Navigation

| Action | Command | Description |
|--------|---------|-------------|
| **Switch to Main** | `.\scripts\worktree-manager.ps1 -Action main` | Core integration work |
| **Switch to Client** | `.\scripts\worktree-manager.ps1 -Action client` | React/UI development |
| **Switch to Server** | `.\scripts\worktree-manager.ps1 -Action server` | Python/Backend work |
| **Switch to Docs** | `.\scripts\worktree-manager.ps1 -Action docs` | Documentation |
| **Switch to Testing** | `.\scripts\worktree-manager.ps1 -Action testing` | Testing & debugging |
| **Show Status** | `.\scripts\worktree-manager.ps1 -Action status` | View all worktrees |
| **Cleanup Branches** | `.\scripts\worktree-manager.ps1 -Action cleanup` | Remove legacy branches |

### Alternative Methods

| Method | Command | Description |
|--------|---------|-------------|
| **Tasks Menu** | `Ctrl+Shift+P` → `Tasks: Run Task` | Select worktree tasks |
| **Direct CD** | `cd ../MythosMUD-server` | Manual navigation |
| **Worktree Ops** | `python scripts/worktree-ops.py status` | Python-based status |

### File Navigation

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Go to File** | `Ctrl+P` | Quick file navigation |
| **Go to Symbol** | `Ctrl+Shift+O` | Navigate to functions/classes |
| **Go to Line** | `Ctrl+G` | Jump to specific line |
| **Recent Files** | `Ctrl+E` | Recently opened files |

### Search & Replace

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Find in Files** | `Ctrl+Shift+F` | Search across all worktrees |
| **Find in Current File** | `Ctrl+F` | Search in current file |
| **Replace in Files** | `Ctrl+Shift+H` | Replace across files |
| **Find References** | `Shift+F12` | Find all references |

## 🎯 Development Workflows

### Client Development

```
1. Focus: ⚛️ Client (React/UI) folder
2. Edit: React/TypeScript files
3. Terminal: npm run dev
4. Test: npm test
5. Commit: git add . && git commit -m "feat(client): ..."
```

### Server Development

```
1. Focus: 🐍 Server (Python/Backend) folder
2. Edit: Python/FastAPI files
3. Terminal: python -m pytest
4. Test: make test
5. Commit: git add . && git commit -m "feat(server): ..."
```

### Documentation

```
1. Focus: 📚 Documentation folder
2. Edit: Markdown files
3. Preview: Ctrl+Shift+V
4. Commit: git add . && git commit -m "docs: ..."
```

### Testing

```
1. Focus: 🧪 Testing & Debug folder
2. Write: Test files
3. Run: pytest or npm test
4. Debug: F5 for debugging
5. Commit: git add . && git commit -m "test: ..."
```

## 🔧 Git Operations

### Branch Management

| Action | Command | Description |
|--------|---------|-------------|
| **Check Status** | `Ctrl+Shift+G` | View source control |
| **Stage Changes** | `Ctrl+Shift+G` → `+` | Stage modified files |
| **Commit** | `Ctrl+Enter` | Commit staged changes |
| **Push** | `Ctrl+Shift+P` → `Git: Push` | Push to remote |
| **Pull** | `Ctrl+Shift+P` → `Git: Pull` | Pull from remote |

### Worktree Status

| Action | Command | Description |
|--------|---------|-------------|
| **Show Status** | `Ctrl+Shift+P` → `📊 Show Worktree Status` | All worktree status |
| **Cleanup** | `Ctrl+Shift+P` → `🧹 Cleanup Legacy Branches` | Legacy branch cleanup |

## 🧪 Testing & Debugging

### Python Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=server

# Run specific test
pytest server/tests/test_auth.py::test_login

# Debug test
pytest --pdb server/tests/test_auth.py::test_login
```

### Client Testing

```bash
# Run tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test
npm test -- --testNamePattern="login"

# Debug test
npm test -- --inspect-brk
```

### Debugging

| Action | Shortcut | Description |
|--------|----------|-------------|
| **Start Debugging** | `F5` | Start debug session |
| **Continue** | `F5` | Continue execution |
| **Step Over** | `F10` | Step over line |
| **Step Into** | `F11` | Step into function |
| **Step Out** | `Shift+F11` | Step out of function |
| **Toggle Breakpoint** | `F9` | Set/remove breakpoint |

## 📊 Performance Tips

### File Exclusions

- **Build artifacts**: `node_modules`, `__pycache__`, `.venv`
- **Test artifacts**: `.pytest_cache`, `htmlcov`, `.coverage`
- **Git artifacts**: `.git`, temporary files

### Search Optimization

- **Filter by folder**: Click folder icon in search
- **Filter by file type**: Use `*.py` or `*.tsx`
- **Exclude patterns**: Use `-node_modules` in search

### Extension Management

- **Disable unused extensions** per worktree
- **Use workspace-specific settings**
- **Monitor extension performance**

## 🎨 Visual Customization

### Color Theme

- **Activity Bar**: Mythos-inspired dark theme
- **Status Bar**: Worktree-aware status
- **Editor**: Syntax highlighting per language

### Icons & Organization

- **Material Icons**: Domain-specific folder icons
- **File Nesting**: Intelligent file grouping
- **Explorer**: Clean, organized structure

## 🚨 Troubleshooting

### Common Issues

#### Worktree Not Visible

```powershell
# Check worktree status
git worktree list

# Recreate if needed
git worktree add ../MythosMUD-client client
```

#### Extension Conflicts

- **Disable conflicting extensions**
- **Use workspace-specific settings**
- **Check extension compatibility**

#### Performance Issues

- **Exclude large folders** from search
- **Limit file watchers**
- **Use workspace-specific settings**

### Debug Commands

```powershell
# Check worktree paths
.\scripts\worktree-manager.ps1 -Action status

# Verify workspace
code --list-extensions --show-versions

# Check Python
python --version
```

## 📈 Productivity Metrics

### Success Indicators

- **Reduced context switching** time
- **Faster file navigation**
- **Improved code organization**
- **Better debugging efficiency**

### Tracking Improvements

- **Development velocity** increase
- **Code quality** improvements
- **Team collaboration** enhancement
- **Documentation** completeness

---

*"Mastery of our tools amplifies our eldritch research capabilities."* - Professor Wolfshade

## 🎯 Quick Start Checklist

- [ ] **Open workspace**: `MythosMUD.code-workspace`
- [ ] **Install extensions**: Accept recommended extensions
- [ ] **Test navigation**: Switch between worktrees
- [ ] **Verify Git**: Check source control integration
- [ ] **Test debugging**: Run debug configurations
- [ ] **Customize settings**: Adjust to preferences
- [ ] **Share configuration**: Commit workspace files

The enhanced IDE integration provides a powerful, organized development environment that maximizes productivity while maintaining the scholarly rigor expected at Miskatonic University.
