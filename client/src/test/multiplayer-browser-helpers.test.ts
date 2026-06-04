/**
 * @vitest-environment jsdom
 */

import { afterEach, describe, expect, it } from 'vitest';

import {
  captureGameUiDiagnosticsInBrowser,
  isGameUiLoadedInBrowser,
} from '../../tests/e2e/runtime/fixtures/multiplayer-browser-helpers.js';

function setBodyHtml(html: string): void {
  document.body.innerHTML = html;
}

afterEach(() => {
  document.body.innerHTML = '';
});

describe('multiplayer-browser-helpers', () => {
  it('returns true when visible command input is present', () => {
    setBodyHtml(`
      <div style="display:none">
        <input data-testid="username-input" placeholder="Username" />
        <button>Enter the Void</button>
      </div>
      <input data-testid="command-input" placeholder="Enter game command..." />
    `);

    expect(isGameUiLoadedInBrowser()).toBe(true);
    expect(captureGameUiDiagnosticsInBrowser().hasVisibleLoginForm).toBe(false);
  });

  it('returns true when game UI indicators exist but login form is hidden in DOM', () => {
    setBodyHtml(`
      <div style="display:none">
        <input data-testid="username-input" placeholder="Username" />
        <button>Enter the Void</button>
      </div>
      <div>
        <span>Player: ArkanWolfshade</span>
        <span>Connected</span>
        <span>Mythos Time</span>
        <span>Occupants (1)</span>
        <span>Exits: North</span>
      </div>
    `);

    expect(isGameUiLoadedInBrowser()).toBe(true);
  });

  it('returns false when visible login form is shown', () => {
    setBodyHtml(`
      <input data-testid="username-input" placeholder="Username" />
      <button>Enter the Void</button>
    `);

    expect(isGameUiLoadedInBrowser()).toBe(false);
    expect(captureGameUiDiagnosticsInBrowser().hasVisibleLoginForm).toBe(true);
  });
});
