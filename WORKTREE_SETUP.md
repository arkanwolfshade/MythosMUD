# MythosMUD Worktree Setup

*"The organization of knowledge is as important as the knowledge itself"* - Dr. Henry Armitage, Miskatonic University

## Overview

This repository has been refactored to use Git worktrees for better organization and parallel development. Each worktree focuses on a specific aspect of the MythosMUD project.

## Worktree Structure

### Main Worktree (`E:/projects/GitHub/MythosMUD`)
- **Branch**: `main`
- **Purpose**: Core development, integration, and project management
- **Focus**: Overall project coordination, merging features, and release management

### Client Worktree (`E:/projects/GitHub/MythosMUD-client`)
- **Branch**: `client`
- **Purpose**: Frontend/React development
- **Focus**:
  - React components and UI/UX
  - Client-side game logic
  - WebSocket connections
  - Terminal emulation
  - Accessibility improvements

### Server Worktree (`E:/projects/GitHub/MythosMUD-server`)
- **Branch**: `server`
- **Purpose**: Backend/Python development
- **Focus**:
  - FastAPI server development
  - Database management
  - Game mechanics
  - Authentication and security
  - Real-time communication

### Documentation Worktree (`E:/projects/GitHub/MythosMUD-docs`)
- **Branch**: `docs`
- **Purpose**: Documentation and planning
- **Focus**:
  - Technical documentation
  - Planning documents
  - API documentation
  - User guides
  - Architecture decisions

### Testing Worktree (`E:/projects/GitHub/MythosMUD-testing`)
- **Branch**: `testing`
- **Purpose**: Test development and debugging
- **Focus**:
  - Unit test development
  - Integration testing
  - Performance testing
  - Debugging tools
  - Test infrastructure

## Development Workflow

### Starting Development
1. Navigate to the appropriate worktree directory
2. Switch to the relevant branch if needed
3. Make changes in the focused area
4. Commit changes to the specific branch
5. Merge back to main when ready

### Example Workflows

#### Client Development
```powershell
cd E:/projects/GitHub/MythosMUD-client
# Make React/UI changes
git add .
git commit -m "feat(client): improve terminal formatting"
git push origin client
```

#### Server Development
```powershell
cd E:/projects/GitHub/MythosMUD-server
# Make backend changes
git add .
git commit -m "feat(server): implement new game mechanics"
git push origin server
```

#### Integration
```powershell
cd E:/projects/GitHub/MythosMUD
git merge client
git merge server
git push origin main
```

## Branch Management

### Current Branches
- `main` - Primary development branch
- `client` - Frontend development
- `server` - Backend development
- `docs` - Documentation
- `testing` - Testing and debugging

### Legacy Branches (To be cleaned up)
- `overall_cleanup` - Previous main development branch
- `arkham_city_generation` - Content generation
- `auth_tests` - Authentication testing
- `feature/issue-62-configurable-game-tick-rate` - Feature development
- `feature/room-pathing-validator` - Room validation
- `realtime` - Real-time features

## Best Practices

1. **Stay Focused**: Each worktree should focus on its specific domain
2. **Regular Integration**: Merge changes back to main regularly
3. **Clear Commit Messages**: Use conventional commit format
4. **Test Before Merge**: Ensure tests pass before merging to main
5. **Documentation**: Update docs worktree when making significant changes

## Troubleshooting

### Common Issues
- **Worktree conflicts**: Ensure you're in the correct worktree directory
- **Branch confusion**: Use `git worktree list` to see all worktrees
- **Merge conflicts**: Resolve conflicts in the main worktree

### Useful Commands
```powershell
# List all worktrees
git worktree list

# Check current branch
git branch

# Switch between worktrees
cd E:/projects/GitHub/MythosMUD-[worktree-name]

# Clean up worktrees (if needed)
git worktree remove [worktree-path]
```

## Integration with GitHub Issues

Each worktree corresponds to specific GitHub issue categories:

- **Client**: Issues #90, #91, #92, #93 (UI/UX issues)
- **Server**: Issues #89, #73, #70, #69, #68 (Backend features)
- **Docs**: Issues #26, #28 (Documentation and planning)
- **Testing**: All test-related issues and debugging

---

*"The proper organization of our eldritch knowledge allows for more efficient research into the forbidden realms."* - Professor Wolfshade
