# 🛠️ MythosMUD – Development Environment Setup

This guide will help you bootstrap your workspace for developing MythosMUD.

---

## Prerequisites

- **Git**
- **Python 3.11+** (managed via [pyenv-win](https://github.com/pyenv-win/pyenv-win) recommended)
- **Node.js 18+** and **npm** (for client)
- **Poetry** (for Python dependency management, optional but recommended)
- **VSCode** or Cursor.ai (recommended editor)

---

## 1. Clone the Repository

```sh
git clone <your-repo-url>
cd MythosMUD
```

---

## 2. Set Up the Python Server

### a. Set Python Version (if using pyenv-win)
```sh
pyenv install 3.11.8  # if not already installed
pyenv local 3.11.8
```

### b. Install Dependencies

**Option 1: Using Poetry (recommended)**
```sh
cd server
poetry install
```

**Option 2: Using pip**
```sh
cd server
pip install -r requirements.txt
```

### c. Set Up Pre-commit Hooks (optional, recommended)
```sh
pre-commit install
```

### d. Run the Server

**With Poetry:**
```sh
poetry run uvicorn main:app --reload
```

**With pip:**
```sh
uvicorn main:app --reload
```

The server should now be running at [http://localhost:8000](http://localhost:8000)

---

## 3. Set Up the React Client

### a. Install Dependencies
```sh
cd ../client
npm install
```

### b. Start the Development Server
```sh
npm start
```

The client should now be running at [http://localhost:3000](http://localhost:3000)

---

## 4. Linting & Formatting

- **Python:**
  - Run `black .` and `flake8 .` in `/server`
- **JS/TS:**
  - Run `npx prettier --check .` and `npx eslint .` in `/client`

---

## 5. Running Tests

- **Python:** (to be added)
- **JS/TS:** (to be added)

---

## 6. Troubleshooting

- Ensure you are using the correct Python and Node.js versions.
- If you encounter issues with dependencies, try deleting `node_modules` or the Python virtual environment and reinstalling.
- For Windows users, use PowerShell or Git Bash for best results.

---

## 7. Useful Commands

- `pre-commit run --all-files` – Run all pre-commit hooks
- `poetry shell` – Spawn a shell with Poetry's virtual environment
- `npm run lint` – Lint JS/TS code

---

_If you have suggestions or run into issues, please update this file or open an issue!_ 