import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import { installLocalStorageShim } from '../localStorageShim';

describe('installLocalStorageShim', () => {
  let globalDescriptor: PropertyDescriptor | undefined;
  let globalWindowDescriptor: PropertyDescriptor | undefined;
  let windowDescriptor: PropertyDescriptor | undefined;

  beforeEach(() => {
    globalDescriptor = Object.getOwnPropertyDescriptor(globalThis, 'localStorage');
    globalWindowDescriptor = Object.getOwnPropertyDescriptor(globalThis, 'window');
    if (typeof globalThis.window !== 'undefined') {
      windowDescriptor = Object.getOwnPropertyDescriptor(globalThis.window, 'localStorage');
    } else {
      windowDescriptor = undefined;
    }
  });

  afterEach(() => {
    if (globalWindowDescriptor) {
      Object.defineProperty(globalThis, 'window', globalWindowDescriptor);
    } else {
      Reflect.deleteProperty(globalThis, 'window');
    }
    if (typeof globalThis.window !== 'undefined') {
      if (windowDescriptor) {
        Object.defineProperty(globalThis.window, 'localStorage', windowDescriptor);
      } else {
        Reflect.deleteProperty(globalThis.window, 'localStorage');
      }
    }
    if (globalDescriptor) {
      Object.defineProperty(globalThis, 'localStorage', globalDescriptor);
    } else {
      Reflect.deleteProperty(globalThis, 'localStorage');
    }
  });

  it('does not replace storage when clear, removeItem, setItem, and getItem are functions', () => {
    const mockStorage = {
      clear: vi.fn(),
      removeItem: vi.fn(),
      setItem: vi.fn(),
      getItem: vi.fn(),
      key: vi.fn(),
      length: 0,
    };
    Object.defineProperty(globalThis, 'localStorage', {
      value: mockStorage,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    expect(globalThis.localStorage).toBe(mockStorage);
    expect(mockStorage.setItem).not.toHaveBeenCalled();
  });

  it('replaces broken storage missing clear', () => {
    const broken = {
      removeItem: vi.fn(),
      setItem: vi.fn(),
      getItem: vi.fn(),
    };
    Object.defineProperty(globalThis, 'localStorage', {
      value: broken,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    const storage = globalThis.localStorage;
    expect(storage).not.toBe(broken);
    storage.setItem('k', 'v');
    expect(storage.getItem('k')).toBe('v');
    storage.clear();
    expect(storage.getItem('k')).toBeNull();
  });

  it('replaces broken storage missing removeItem', () => {
    const broken = {
      clear: vi.fn(),
      setItem: vi.fn(),
      getItem: vi.fn(),
    };
    Object.defineProperty(globalThis, 'localStorage', {
      value: broken,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    const storage = globalThis.localStorage;
    expect(storage).not.toBe(broken);
    storage.setItem('k', 'v');
    expect(storage.getItem('k')).toBe('v');
    storage.removeItem('k');
    expect(storage.getItem('k')).toBeNull();
  });

  it('replaces broken storage missing setItem', () => {
    const broken = {
      clear: vi.fn(),
      removeItem: vi.fn(),
      getItem: vi.fn(),
    };
    Object.defineProperty(globalThis, 'localStorage', {
      value: broken,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    const storage = globalThis.localStorage;
    expect(storage).not.toBe(broken);
    storage.setItem('x', 'y');
    expect(storage.getItem('x')).toBe('y');
  });

  it('replaces broken storage missing getItem', () => {
    const broken = {
      clear: vi.fn(),
      removeItem: vi.fn(),
      setItem: vi.fn(),
    };
    Object.defineProperty(globalThis, 'localStorage', {
      value: broken,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    const storage = globalThis.localStorage;
    expect(storage).not.toBe(broken);
    storage.setItem('a', 'b');
    expect(storage.getItem('a')).toBe('b');
  });

  it('installs when localStorage is undefined', () => {
    Reflect.deleteProperty(globalThis, 'localStorage');

    installLocalStorageShim();

    globalThis.localStorage.setItem('a', '1');
    expect(globalThis.localStorage.getItem('a')).toBe('1');
  });

  it('installs when localStorage is null', () => {
    Object.defineProperty(globalThis, 'localStorage', {
      value: null,
      configurable: true,
      writable: true,
    });

    installLocalStorageShim();

    globalThis.localStorage.setItem('n', '1');
    expect(globalThis.localStorage.getItem('n')).toBe('1');
  });

  it('coerces keys and values with setItem/getItem', () => {
    Reflect.deleteProperty(globalThis, 'localStorage');
    installLocalStorageShim();
    const storage = globalThis.localStorage;

    storage.setItem(1 as unknown as string, 2 as unknown as string);
    expect(storage.getItem('1')).toBe('2');
  });

  it('supports length, key order, and removeItem', () => {
    Reflect.deleteProperty(globalThis, 'localStorage');
    installLocalStorageShim();
    const storage = globalThis.localStorage;

    expect(storage.length).toBe(0);
    storage.setItem('first', 'a');
    storage.setItem('second', 'b');
    expect(storage.length).toBe(2);
    expect(storage.key(0)).toBe('first');
    expect(storage.key(1)).toBe('second');
    storage.removeItem('first');
    expect(storage.length).toBe(1);
    expect(storage.getItem('first')).toBeNull();
    expect(storage.key(0)).toBe('second');
  });

  it('aliases window.localStorage to the same instance when window exists', () => {
    Reflect.deleteProperty(globalThis, 'localStorage');
    if (typeof globalThis.window === 'undefined') {
      return;
    }
    Reflect.deleteProperty(globalThis.window, 'localStorage');

    installLocalStorageShim();

    expect(globalThis.window.localStorage).toBe(globalThis.localStorage);
    globalThis.localStorage.setItem('w', 'x');
    expect(globalThis.window.localStorage.getItem('w')).toBe('x');
  });

  it('installs only on globalThis when globalThis.window is absent', () => {
    if (typeof globalThis.window === 'undefined') {
      return;
    }

    Reflect.deleteProperty(globalThis, 'window');
    Reflect.deleteProperty(globalThis, 'localStorage');

    installLocalStorageShim();

    expect(typeof globalThis.window).toBe('undefined');
    globalThis.localStorage.setItem('nowin', '1');
    expect(globalThis.localStorage.getItem('nowin')).toBe('1');
  });
});
