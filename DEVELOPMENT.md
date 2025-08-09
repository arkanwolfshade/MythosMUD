# 🛠️ MythosMUD – Development Environment Setup

This guide will help you bootstrap your workspace for developing MythosMUD.

---

## Prerequisites

- **Git**
- **Python 3.12+** (managed via [pyenv-win](https://github.com/pyenv-win/pyenv-win) recommended)
- **Node.js 18+** and **npm** (for client)
- **[uv](https://github.com/astral-sh/uv)** (for Python dependency management - **required**)
- **VSCode** or Cursor.ai (recommended editor)
- **React Developer Tools** (Firefox/Chrome extension for debugging React components)

---

## 1. Install uv

**On macOS/Linux:**

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify installation:**

```sh
uv --version
```

---

## 2. Clone the Repository

```sh
git clone <your-repo-url>
cd MythosMUD
```

---

## 3. Set Up the Python Server

### a. Set Python Version (if using pyenv-win)

```sh
pyenv install 3.12.11  # if not already installed
pyenv local 3.12.11
```

### b. Install Dependencies

```sh
cd server
uv sync
```

### c. Set Up Pre-commit Hooks

```sh
uv run pre-commit install -f
```

### d. Run the Server

```sh
uv run uvicorn main:app --reload
```

The server should now be running at [http://localhost:54731](http://localhost:54731)

---

## 4. Set Up the React Client

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

## 5. Development Scripts

We provide convenient scripts for common development tasks:

### **Install Everything:**

```sh
python scripts/install.py
```

### **Run the Server:**

```sh
python scripts/run.py
```

### **Run Tests:**

```sh
python scripts/test.py
```

### **Lint Code:**

```sh
python scripts/lint.py
```

### **Format Code:**

```sh
python scripts/format.py
```

---

## 6. Manual Commands

### **Python Development:**

```sh
cd server

# Install dependencies
uv sync

# Run server
uv run uvicorn main:app --reload

# Run tests
uv run pytest tests/ -v

# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Add new dependency
uv add package-name

# Add development dependency
uv add --dev package-name
```

### **Client Development:**

```sh
cd client

# Install dependencies
npm install

# Start development server
npm start

# Run tests
npm test

# Build for production
npm run build
```

---

## 7. Why uv?

- **🚀 Faster**: 10-100x faster than pip/poetry
- **🔒 Reliable**: Deterministic dependency resolution
- **🛠️ Modern**: Built-in virtual environment management
- **📦 Compatible**: Works with existing pyproject.toml
- **🔄 Simple**: Single tool for all Python operations

---

## 8. Troubleshooting

### **uv not found:**

```sh
# Reinstall uv following the installation instructions above
# Make sure to restart your terminal after installation
```

### **Python version issues:**

```sh
# Ensure you have Python 3.12+ installed
python --version

# If using pyenv, set the local version
pyenv local 3.12.11
```

### **Dependency conflicts:**

```sh
# Clean and reinstall
cd server
uv sync --reinstall
```

### **Client-Server Connection Issues:**

```sh
# Check if server is running on correct port
curl http://localhost:54731/game/status

# Verify Vite proxy configuration in client/vite.config.ts
# Ensure target ports match server configuration

# Use React Developer Tools to debug component state
# - Install React Developer Tools extension in Firefox/Chrome
# - Check component props, state, and network requests
# - Monitor authentication state and API calls
```

### **React Component Debugging:**

- **React Developer Tools**: Use the Firefox/Chrome extension to inspect component state
- **Network Tab**: Check API requests and responses in browser dev tools
- **Console**: Monitor authentication flow and error messages
- **Component State**: Verify `isAuthenticated`, `playerId`, and `authToken` values

---

## 9. Next Steps

- Read the [PLANNING.md](PLANNING.md) for project architecture
- Check [GitHub Issues](https://github.com/arkanwolfshade/MythosMUD/issues) for current development priorities
- Review [SECURITY.md](SECURITY.md) for security guidelines
