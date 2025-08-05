# Cursor IDE Worktree Integration Guide

*"The proper integration of tools and knowledge amplifies our eldritch research capabilities"* - Professor Wolfshade

## Overview

This guide explains how to maximize the value of our Git worktree setup within Cursor IDE, creating a powerful development environment that enhances productivity and maintains clear separation of concerns.

## 🎯 Key Benefits of Worktree + Cursor Integration

### 1. **Multi-Folder Workspace Organization**

- **Visual Separation**: Each worktree appears as a distinct folder in the explorer
- **Focused Development**: Work on specific domains without distraction
- **Parallel Development**: Multiple worktrees open simultaneously
- **Context Switching**: Easy navigation between different development areas

### 2. **Enhanced IDE Features**

- **IntelliSense**: Language-specific suggestions for each worktree
- **Debugging**: Separate debug configurations per worktree
- **Testing**: Focused test runners for each domain
- **Git Integration**: Branch-aware features for each worktree

### 3. **Productivity Boosters**

- **Quick Tasks**: Pre-configured tasks for worktree switching
- **File Nesting**: Organized file structure with intelligent grouping
- **Search**: Cross-worktree search with domain filtering
- **Extensions**: Domain-specific extensions per worktree

## 🚀 Getting Started

### Opening the Enhanced Workspace

1. **Open Cursor IDE**
2. **File → Open Workspace**
3. **Select**: `MythosMUD.code-workspace`
4. **Enjoy**: All worktrees visible in the explorer

### Workspace Structure

```
📁 MythosMUD (Workspace)
├── 📁 Main (Integration)          # Core development & integration
├── ⚛️ Client (React/UI)          # Frontend development
├── 🐍 Server (Python/Backend)     # Backend development
├── 📚 Documentation               # Docs & planning
└── 🧪 Testing & Debug            # Testing & debugging
```

## 🎨 Visual Enhancements

### Color Theme

- **Dark Theme**: Mythos-inspired color scheme
- **Activity Bar**: Distinct colors for each worktree
- **Status Bar**: Worktree-aware status information

### Icons & Organization

- **Material Icons**: Domain-specific folder icons
- **File Nesting**: Intelligent file grouping
- **Explorer**: Clean, organized file structure

## ⚡ Quick Actions

### Task Palette (Ctrl+Shift+P)

```
🔄 Switch to Main Worktree
⚛️ Switch to Client Worktree
🐍 Switch to Server Worktree
📚 Switch to Docs Worktree
🧪 Switch to Testing Worktree
📊 Show Worktree Status
🧹 Cleanup Legacy Branches
```

### Keyboard Shortcuts

- **Ctrl+Shift+P**: Open command palette
- **Ctrl+Shift+E**: Focus explorer
- **Ctrl+Shift+G**: Focus source control
- **Ctrl+Shift+X**: Focus extensions

## 🔧 Advanced Configuration

### Language-Specific Settings

#### Python (Server Worktree)

```json
{
  "python.defaultInterpreterPath": "./.venv/Scripts/python.exe",
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "ruff"
}
```

#### TypeScript/React (Client Worktree)

```json
{
  "typescript.preferences.includePackageJsonAutoImports": "on",
  "eslint.enable": true,
  "prettier.requireConfig": true
}
```

### File Exclusions

- **Build artifacts**: `node_modules`, `__pycache__`, `.venv`
- **Test artifacts**: `.pytest_cache`, `htmlcov`, `.coverage`
- **Git artifacts**: `.git`, temporary files

## 🎯 Development Workflows

### 1. **Client Development Workflow**

```
1. Focus on "⚛️ Client (React/UI)" folder
2. Make React/TypeScript changes
3. Use integrated terminal for npm commands
4. Commit to client branch
5. Switch to main for integration
```

### 2. **Server Development Workflow**

```
1. Focus on "🐍 Server (Python/Backend)" folder
2. Make Python/FastAPI changes
3. Use integrated terminal for Python commands
4. Run tests with coverage
5. Commit to server branch
6. Switch to main for integration
```

### 3. **Documentation Workflow**

```
1. Focus on "📚 Documentation" folder
2. Edit Markdown files
3. Use Markdown preview
4. Commit to docs branch
5. Switch to main for integration
```

### 4. **Testing Workflow**

```
1. Focus on "🧪 Testing & Debug" folder
2. Write/run tests
3. Debug issues
4. Use test explorer
5. Commit to testing branch
6. Switch to main for integration
```

## 🔍 Search & Navigation

### Cross-Worktree Search

- **Ctrl+Shift+F**: Search across all worktrees
- **Filter by folder**: Focus search on specific worktrees
- **File type filtering**: Search specific file types

### Navigation Features

- **Go to File**: Ctrl+P for quick file navigation
- **Go to Symbol**: Ctrl+Shift+O for symbol navigation
- **Go to Line**: Ctrl+G for line navigation
- **Recent Files**: Ctrl+E for recent file access

## 🧪 Testing Integration

### Test Explorer

- **Unit Tests**: Python tests in server worktree
- **Integration Tests**: Cross-worktree tests
- **Client Tests**: React component tests
- **Coverage**: Integrated coverage reporting

### Debug Configurations

```json
{
  "name": "Debug Server",
  "type": "python",
  "request": "launch",
  "program": "${workspaceFolder}/server/main.py",
  "cwd": "${workspaceFolder}/server"
}
```

## 🔄 Git Integration

### Source Control Features

- **Branch Awareness**: Each worktree shows its branch
- **Diff View**: Side-by-side diff comparisons
- **Blame**: Line-by-line commit history
- **Graph**: Visual branch history

### GitLens Integration

- **Inline Blame**: See commit info inline
- **File History**: Complete file change history
- **Branch Comparison**: Compare branches visually
- **Remote Integration**: GitHub integration

## 📊 Monitoring & Status

### Worktree Status

- **Branch Information**: Current branch per worktree
- **File Changes**: Modified files per worktree
- **Sync Status**: Push/pull status
- **Conflicts**: Merge conflict indicators

### Performance Monitoring

- **CPU Usage**: Per-worktree resource usage
- **Memory Usage**: Memory consumption tracking
- **Extension Impact**: Extension performance per worktree

## 🛠️ Troubleshooting

### Common Issues

#### Worktree Not Visible

```powershell
# Check worktree status
git worktree list

# Recreate worktree if needed
git worktree add ../MythosMUD-client client
```

#### Extension Conflicts

- **Disable conflicting extensions** per worktree
- **Use workspace-specific settings**
- **Check extension compatibility**

#### Performance Issues

- **Exclude large folders** from search
- **Limit file watchers** per worktree
- **Use workspace-specific settings**

### Debug Commands

```powershell
# Check worktree paths
.\scripts\worktree-manager.ps1 -Action status

# Verify workspace configuration
code --list-extensions --show-versions

# Check Python interpreter
python --version
```

## 🎯 Best Practices

### 1. **Stay Focused**

- Work in the appropriate worktree for your task
- Use folder-specific settings when needed
- Avoid cross-worktree file editing

### 2. **Regular Integration**

- Merge worktree branches to main regularly
- Keep worktrees in sync with main
- Resolve conflicts in main worktree

### 3. **Extension Management**

- Install domain-specific extensions per worktree
- Use workspace-specific extension recommendations
- Disable unnecessary extensions per worktree

### 4. **Performance Optimization**

- Exclude build artifacts from search
- Use file nesting for better organization
- Limit file watchers in large worktrees

## 🚀 Advanced Features

### Custom Tasks

```json
{
  "label": "🧪 Run All Tests",
  "dependsOn": ["Test Server", "Test Client"],
  "group": "test"
}
```

### Debug Configurations

```json
{
  "name": "Debug Full Stack",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/client/src/main.tsx",
  "serverReadyAction": {
    "pattern": "Server running",
    "uriFormat": "http://localhost:8000"
  }
}
```

### Snippets

```json
{
  "React Component": {
    "prefix": "rfc",
    "body": [
      "import React from 'react';",
      "",
      "interface ${1:ComponentName}Props {",
      "  $2",
      "}",
      "",
      "export const ${1:ComponentName}: React.FC<${1:ComponentName}Props> = ({ $3 }) => {",
      "  return (",
      "    <div>",
      "      $0",
      "    </div>",
      "  );",
      "};"
    ]
  }
}
```

## 📈 Productivity Metrics

### Tracking Improvements

- **Development Velocity**: Faster feature development
- **Context Switching**: Reduced time between tasks
- **Code Quality**: Better organization leads to better code
- **Team Collaboration**: Clearer separation of concerns

### Success Indicators

- **Reduced Merge Conflicts**: Better branch management
- **Faster Debugging**: Focused debugging environments
- **Improved Code Reviews**: Clearer change boundaries
- **Better Documentation**: Dedicated docs worktree

---

*"The integration of our eldritch knowledge with modern tools creates a development environment worthy of the Miskatonic archives."* - Professor Wolfshade

## 🎯 Next Steps

1. **Install Recommended Extensions**: All extensions will be suggested when opening the workspace
2. **Customize Settings**: Adjust workspace settings to your preferences
3. **Create Custom Tasks**: Add project-specific tasks as needed
4. **Share Configuration**: Commit workspace configuration to the repository
5. **Team Onboarding**: Share this guide with team members

The enhanced workspace configuration provides a powerful, organized development environment that maximizes the value of our worktree setup while maintaining the scholarly rigor expected at Miskatonic University.
