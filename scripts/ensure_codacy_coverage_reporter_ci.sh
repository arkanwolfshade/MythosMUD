#!/usr/bin/env bash
# CI only: download a pinned codacy-coverage-reporter (linux amd64) from GitHub
# releases and verify SHA256. Avoids executing https://coverage.codacy.com/get.sh
# at runtime (supply-chain / integrity). Prints the reporter binary path on stdout;
# diagnostics go to stderr.
#
# Pin: https://github.com/codacy/codacy-coverage-reporter/releases/tag/14.1.2
# SHA256: GitHub release asset digest for codacy-coverage-reporter-linux (API).
set -euo pipefail

VERSION="14.1.2"
ASSET_NAME="codacy-coverage-reporter-linux"
EXPECTED_SHA256="3fde3d10921cb545d86c06cc7950323f9482ca55ce1c9b9ce9ac805334afd656"
BASE_URL="https://github.com/codacy/codacy-coverage-reporter/releases/download/${VERSION}"

ROOT="${GITHUB_WORKSPACE:-$(pwd)}"
CACHE_DIR="${ROOT}/.cache/codacy-coverage-reporter"
BIN="${CACHE_DIR}/${ASSET_NAME}"

mkdir -p "${CACHE_DIR}"

if [[ -f "${BIN}" ]]; then
  ACTUAL=$(sha256sum "${BIN}" | awk '{print $1}')
  if [[ "${ACTUAL}" == "${EXPECTED_SHA256}" ]]; then
    chmod +x "${BIN}"
    printf '%s\n' "${BIN}"
    exit 0
  fi
  echo "Cached Codacy reporter failed SHA256 check; re-downloading." >&2
  rm -f "${BIN}"
fi

curl -fsSL "${BASE_URL}/${ASSET_NAME}" -o "${BIN}"
chmod +x "${BIN}"

ACTUAL=$(sha256sum "${BIN}" | awk '{print $1}')
if [[ "${ACTUAL}" != "${EXPECTED_SHA256}" ]]; then
  echo "::error::SHA256 mismatch for Codacy coverage reporter (expected ${EXPECTED_SHA256}, got ${ACTUAL})" >&2
  exit 1
fi

printf '%s\n' "${BIN}"
