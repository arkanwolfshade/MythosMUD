/**
 * Ensures a full Web Storage API surface on globalThis (and window when present).
 *
 * Node 25+ may enable experimental Web Storage via --localstorage-file; an invalid or empty path
 * yields a broken global `localStorage` (e.g. clear/removeItem missing). Vitest + happy-dom need a
 * complete Storage implementation for code and tests that touch localStorage.
 */
export function installLocalStorageShim(): void {
  const current = globalThis.localStorage;
  const looksUsable =
    current &&
    typeof current.clear === 'function' &&
    typeof current.removeItem === 'function' &&
    typeof current.setItem === 'function' &&
    typeof current.getItem === 'function';
  if (looksUsable) {
    return;
  }
  const map = new Map<string, string>();
  const storage: Storage = {
    get length() {
      return map.size;
    },
    clear(): void {
      map.clear();
    },
    getItem(key: string): string | null {
      return map.get(String(key)) ?? null;
    },
    key(index: number): string | null {
      const keys = Array.from(map.keys());
      return keys[index] ?? null;
    },
    removeItem(key: string): void {
      map.delete(String(key));
    },
    setItem(key: string, value: string): void {
      map.set(String(key), String(value));
    },
  };
  Object.defineProperty(globalThis, 'localStorage', { value: storage, configurable: true, writable: true });
  if (typeof globalThis.window !== 'undefined') {
    Object.defineProperty(globalThis.window, 'localStorage', {
      value: storage,
      configurable: true,
      writable: true,
    });
  }
}
