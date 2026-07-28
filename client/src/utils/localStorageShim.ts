/**
 * Ensures a full Web Storage API surface on globalThis (and window when present).
 *
 * Node 22+ exposes experimental Web Storage as an accessor on globalThis. Reading
 * that getter without --localstorage-file emits ExperimentalWarning and returns
 * undefined / a broken Storage. Never invoke that accessor; inspect the descriptor
 * and install a Map-backed Storage when the existing value is missing or incomplete.
 * Vitest + happy-dom need a complete Storage for code and tests that touch localStorage.
 */

function isUsableStorage(value: unknown): value is Storage {
  if (!value || typeof value !== 'object') {
    return false;
  }
  const storage = value as Storage;
  // Single loop keeps lizard CCN under the project gate (was 11 with && chain).
  const methods: Array<keyof Storage> = ['clear', 'removeItem', 'setItem', 'getItem'];
  return methods.every(name => typeof storage[name] === 'function');
}

/**
 * Peek localStorage without triggering Node's experimental webstorage getter warning.
 */
function peekExistingLocalStorage(): Storage | undefined {
  const desc = Object.getOwnPropertyDescriptor(globalThis, 'localStorage');
  if (!desc) {
    return undefined;
  }
  // Data property (jsdom / happy-dom / our shim / tests): safe to read.
  if ('value' in desc) {
    return desc.value as Storage | undefined;
  }
  // Accessor on globalThis under Node is experimental webstorage; invoking it
  // without --localstorage-file emits ExperimentalWarning.
  if (typeof process !== 'undefined' && process.versions?.node && typeof desc.get === 'function') {
    return undefined;
  }
  try {
    return globalThis.localStorage;
  } catch {
    return undefined;
  }
}

export function installLocalStorageShim(): void {
  if (isUsableStorage(peekExistingLocalStorage())) {
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
