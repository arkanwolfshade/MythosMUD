/**
 * Unit tests for asciiMapViewerUtils (viewport key handler).
 * Guards against regressions of map viewport keyboard navigation.
 */
/* global KeyboardEvent, document -- provided by Vitest happy-dom test environment */

import { describe, expect, it, vi } from 'vitest';
import { VIEWPORT_BUTTON_CLASS, createViewportKeyHandler } from '../asciiMapViewerUtils';

describe('asciiMapViewerUtils', () => {
  describe('VIEWPORT_BUTTON_CLASS', () => {
    it('is a non-empty string for tailwind classes', () => {
      expect(VIEWPORT_BUTTON_CLASS).toBeTypeOf('string');
      expect(VIEWPORT_BUTTON_CLASS.length).toBeGreaterThan(0);
    });
  });

  describe('createViewportKeyHandler', () => {
    it('ArrowUp decrements viewport Y', () => {
      const setViewportX = vi.fn();
      const setViewportY = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, setViewportY);
      const event = new KeyboardEvent('keydown', { key: 'ArrowUp', bubbles: true });
      Object.defineProperty(event, 'target', { value: document.body });

      handler(event);

      expect(setViewportY).toHaveBeenCalledWith(expect.any(Function));
      const updater = setViewportY.mock.calls[0][0];
      expect(updater(10)).toBe(9);
    });

    it('ArrowDown increments viewport Y', () => {
      const setViewportY = vi.fn();
      const handler = createViewportKeyHandler(vi.fn(), setViewportY);
      const event = new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true });
      Object.defineProperty(event, 'target', { value: document.body });

      handler(event);

      expect(setViewportY).toHaveBeenCalledWith(expect.any(Function));
      const updater = setViewportY.mock.calls[0][0];
      expect(updater(10)).toBe(11);
    });

    it('ArrowLeft decrements viewport X', () => {
      const setViewportX = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, vi.fn());
      const event = new KeyboardEvent('keydown', { key: 'ArrowLeft', bubbles: true });
      Object.defineProperty(event, 'target', { value: document.body });

      handler(event);

      expect(setViewportX).toHaveBeenCalledWith(expect.any(Function));
      const updater = setViewportX.mock.calls[0][0];
      expect(updater(5)).toBe(4);
    });

    it('ArrowRight increments viewport X', () => {
      const setViewportX = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, vi.fn());
      const event = new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true });
      Object.defineProperty(event, 'target', { value: document.body });

      handler(event);

      expect(setViewportX).toHaveBeenCalledWith(expect.any(Function));
      const updater = setViewportX.mock.calls[0][0];
      expect(updater(5)).toBe(6);
    });

    it('Home resets viewport X and Y to 0', () => {
      const setViewportX = vi.fn();
      const setViewportY = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, setViewportY);
      const event = new KeyboardEvent('keydown', { key: 'Home', bubbles: true });
      Object.defineProperty(event, 'target', { value: document.body });

      handler(event);

      expect(setViewportX).toHaveBeenCalledWith(0);
      expect(setViewportY).toHaveBeenCalledWith(0);
    });

    it('does not handle key when target is input', () => {
      const setViewportX = vi.fn();
      const setViewportY = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, setViewportY);
      const input = document.createElement('input');
      const event = new KeyboardEvent('keydown', { key: 'ArrowUp', bubbles: true });
      Object.defineProperty(event, 'target', { value: input });

      handler(event);

      expect(setViewportX).not.toHaveBeenCalled();
      expect(setViewportY).not.toHaveBeenCalled();
    });

    it('does not handle key when target is textarea', () => {
      const setViewportX = vi.fn();
      const setViewportY = vi.fn();
      const handler = createViewportKeyHandler(setViewportX, setViewportY);
      const textarea = document.createElement('textarea');
      const event = new KeyboardEvent('keydown', { key: 'ArrowRight', bubbles: true });
      Object.defineProperty(event, 'target', { value: textarea });

      handler(event);

      expect(setViewportX).not.toHaveBeenCalled();
      expect(setViewportY).not.toHaveBeenCalled();
    });
  });
});
