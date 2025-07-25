import shutil
from pathlib import Path

# List of directories to remove
DIRS_TO_REMOVE = [
    Path('server/__pycache__'),
    Path('server/.pytest_cache'),
    Path('server/htmlcov'),
    Path('client/dist'),
    Path('client/node_modules'),
]


def remove_dir(path: Path):
    if path.exists() and path.is_dir():
        print(f"Removing {path}")
        shutil.rmtree(path, ignore_errors=True)
    else:
        print(f"Skipping {path} (not found)")


if __name__ == "__main__":
    for d in DIRS_TO_REMOVE:
        remove_dir(d)
