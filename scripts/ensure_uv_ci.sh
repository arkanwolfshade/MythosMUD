#!/usr/bin/env bash
# CI only: download pinned uv (linux x86_64) from GitHub releases and verify SHA256.
# Avoids executing https://astral.sh/uv/install.sh at runtime (supply-chain / integrity).
# Installs to $HOME/.local/bin/uv and prints that directory on stdout (add to PATH).
#
# To bump: set VERSION, then copy the digest from the release asset
#   https://github.com/astral-sh/uv/releases/download/<VERSION>/uv-x86_64-unknown-linux-gnu.tar.gz.sha256
set -euo pipefail

VERSION="0.11.2"
ASSET="uv-x86_64-unknown-linux-gnu.tar.gz"
EXPECTED_SHA256="7ac2ca0449c8d68dae9b99e635cd3bc9b22a4cb1de64b7c43716398447d42981"
BASE_URL="https://github.com/astral-sh/uv/releases/download/${VERSION}"
ROOT="${GITHUB_WORKSPACE:-$(pwd)}"
CACHE_DIR="${ROOT}/.cache/uv-ci"
TAR_PATH="${CACHE_DIR}/${ASSET}"
INSTALL_DIR="${HOME}/.local/bin"
UV_EXTRACT_SUBDIR="uv-x86_64-unknown-linux-gnu"

mkdir -p "${CACHE_DIR}"
mkdir -p "${INSTALL_DIR}"

need_download=1
if [[ -f "${TAR_PATH}" ]]; then
  ACTUAL=$(sha256sum "${TAR_PATH}" | awk '{print $1}')
  if [[ "${ACTUAL}" == "${EXPECTED_SHA256}" ]]; then
    need_download=0
  else
    echo "Cached uv tarball failed SHA256 check; re-downloading." >&2
    rm -f "${TAR_PATH}"
  fi
fi

if [[ "${need_download}" -eq 1 ]]; then
  curl -fsSL "${BASE_URL}/${ASSET}" -o "${TAR_PATH}"
  ACTUAL=$(sha256sum "${TAR_PATH}" | awk '{print $1}')
  if [[ "${ACTUAL}" != "${EXPECTED_SHA256}" ]]; then
    echo "::error::SHA256 mismatch for uv tarball (expected ${EXPECTED_SHA256}, got ${ACTUAL})" >&2
    exit 1
  fi
fi

rm -rf "${CACHE_DIR:?}/${UV_EXTRACT_SUBDIR:?}"
tar xzf "${TAR_PATH}" -C "${CACHE_DIR}"
SRC_BIN="${CACHE_DIR}/${UV_EXTRACT_SUBDIR}/uv"
if [[ ! -f "${SRC_BIN}" ]]; then
  echo "::error::uv binary missing after extract: ${SRC_BIN}" >&2
  exit 1
fi
cp -f "${SRC_BIN}" "${INSTALL_DIR}/uv"
chmod +x "${INSTALL_DIR}/uv"
printf '%s\n' "${INSTALL_DIR}"
