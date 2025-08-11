#!/usr/bin/env python3
"""
Setup Data Submodule Script
Helps migrate from local data/ directory to git submodule
"""

import os
import shutil
import subprocess
import sys


def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Command failed: {cmd}")
            print(f"Error: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error running command '{cmd}': {e}")
        return False


def backup_data_directory():
    """Create a backup of the current data directory"""
    print("=== CREATING DATA BACKUP ===")

    if os.path.exists("data"):
        backup_dir = "data_backup"
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)

        shutil.copytree("data", backup_dir)
        print(f"✅ Data backed up to {backup_dir}/")
        return True
    else:
        print("❌ No data/ directory found")
        return False


def remove_data_directory():
    """Remove the current data directory"""
    print("\n=== REMOVING CURRENT DATA DIRECTORY ===")

    if os.path.exists("data"):
        shutil.rmtree("data")
        print("✅ Removed data/ directory")
        return True
    else:
        print("❌ No data/ directory to remove")
        return False


def add_submodule():
    """Add the data submodule"""
    print("\n=== ADDING DATA SUBMODULE ===")

    submodule_url = "https://github.com/arkanwolfshade/mythosmud_data.git"

    # Add the submodule
    if run_command(f"git submodule add {submodule_url} data"):
        print("✅ Added data submodule")
        return True
    else:
        print("❌ Failed to add submodule")
        return False


def update_gitignore():
    """Update .gitignore to exclude data/ but allow submodule"""
    print("\n=== UPDATING .GITIGNORE ===")

    gitignore_path = ".gitignore"
    data_exclude_line = "data/"

    # Read current .gitignore
    if os.path.exists(gitignore_path):
        with open(gitignore_path) as f:
            lines = f.readlines()
    else:
        lines = []

    # Check if data/ is already excluded
    if any(line.strip() == data_exclude_line for line in lines):
        print("✅ data/ already excluded in .gitignore")
    else:
        # Add the exclusion
        lines.append(f"\n# Exclude data directory (now handled by submodule)\n{data_exclude_line}\n")

        with open(gitignore_path, "w") as f:
            f.writelines(lines)
        print("✅ Added data/ exclusion to .gitignore")

    return True


def create_submodule_docs():
    """Create documentation for the submodule setup"""
    print("\n=== CREATING SUBMODULE DOCUMENTATION ===")

    docs_content = """# MythosMUD Data Submodule

This project uses a git submodule for game data to keep sensitive information separate from the main codebase.

## Setup

### Initial Clone
When cloning this repository for the first time, you need to initialize the submodule:

```bash
git clone --recursive https://github.com/arkanwolfshade/MythosMUD.git
```

### Existing Repository
If you already have the repository cloned, initialize the submodule:

```bash
git submodule init
git submodule update
```

## Working with the Data Submodule

### Updating Data
To get the latest data changes:

```bash
git submodule update --remote data
```

### Making Changes to Data
1. Navigate to the data directory: `cd data`
2. Make your changes
3. Commit and push to the data repository: `git add . && git commit -m "Update data" && git push`
4. Return to main repository: `cd ..`
5. Update the submodule reference: `git add data && git commit -m "Update data submodule"`

### Switching Branches
When switching branches that have different submodule references:

```bash
git checkout <branch>
git submodule update
```

## Data Repository
The game data is stored in a private repository: https://github.com/arkanwolfshade/mythosmud_data

This includes:
- Room definitions and layouts
- Player data and aliases
- Game configuration files
- MOTD and other content

## Security
The data repository is private to prevent players from accessing game data that could give them an unfair advantage.
"""

    with open("DATA_SUBMODULE.md", "w") as f:
        f.write(docs_content)

    print("✅ Created DATA_SUBMODULE.md")
    return True


def main():
    """Main setup function"""
    print("=== MYTHOSMUD DATA SUBMODULE SETUP ===\n")

    # Check if we're in a git repository
    if not os.path.exists(".git"):
        print("❌ Not in a git repository. Please run this from the project root.")
        return False

    # Check if data submodule already exists
    if os.path.exists("data/.git"):
        print("✅ Data submodule already exists")
        return True

    # Step 1: Backup current data
    if not backup_data_directory():
        return False

    # Step 2: Remove current data directory
    if not remove_data_directory():
        return False

    # Step 3: Add submodule
    if not add_submodule():
        return False

    # Step 4: Update .gitignore
    if not update_gitignore():
        return False

    # Step 5: Create documentation
    if not create_submodule_docs():
        return False

    print("\n=== SETUP COMPLETE ===")
    print("✅ Data submodule setup complete!")
    print("\nNext steps:")
    print("1. Push the data backup to your private repository")
    print("2. Update any hardcoded paths in your code")
    print("3. Test that everything works correctly")
    print("4. Commit the submodule changes")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
