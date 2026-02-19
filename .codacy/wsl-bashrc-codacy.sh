# Codacy CLI v2 - add to WSL ~/.bashrc (https://github.com/codacy/codacy-cli-v2)
# Paste this block into your WSL terminal, or: cat .codacy/wsl-bashrc-codacy.sh >> ~/.bashrc
# Then run: source ~/.bashrc

if [ -f "$HOME/.cache/codacy/codacy-cli-v2/version.yaml" ]; then
  CODACY_VERSION=$(grep -o 'version: *"[^"]*"' "$HOME/.cache/codacy/codacy-cli-v2/version.yaml" | cut -d'"' -f2)
  CODACY_BIN="$HOME/.cache/codacy/codacy-cli-v2/$CODACY_VERSION/codacy-cli-v2"
  if [ -n "$CODACY_VERSION" ] && [ -x "$CODACY_BIN" ]; then
    export PATH="$HOME/.cache/codacy/codacy-cli-v2/$CODACY_VERSION:$PATH"
    alias codacy-cli=codacy-cli-v2
  fi
fi
