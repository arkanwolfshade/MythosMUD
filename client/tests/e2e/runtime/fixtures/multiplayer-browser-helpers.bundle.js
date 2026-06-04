/**
 * Injected into each Playwright page via addInitScript.
 * Defines window.__mythosE2e* helpers (no ES module exports in the browser).
 */
(function installMythosE2eBrowserHelpers() {
  const LOGIN_SUBMIT_BUTTON_LABELS = ['Enter the Void', 'Login'];

  function isValidElement(el) {
    return Boolean(el && el instanceof Element);
  }

  function computedStyleHidesElement(style) {
    if (style.display === 'none') {
      return true;
    }
    if (style.visibility === 'hidden') {
      return true;
    }
    return Number(style.opacity) === 0;
  }

  function isElementVisible(el) {
    if (!isValidElement(el)) {
      return false;
    }
    let current = el;
    while (current && current instanceof Element) {
      const style = window.getComputedStyle(current);
      if (computedStyleHidesElement(style)) {
        return false;
      }
      current = current.parentElement;
    }
    const rects = el.getClientRects();
    if (rects.length > 0) {
      return true;
    }
    return el.isConnected;
  }

  function getBodyInnerText() {
    const body = document.body;
    if (!body) {
      return '';
    }
    return body.innerText ?? body.textContent ?? '';
  }

  function hasUsernameInputInBrowser() {
    const inputs = document.querySelectorAll('input');
    for (const input of inputs) {
      if (!isElementVisible(input)) {
        continue;
      }
      const placeholder = input.getAttribute('placeholder');
      if (placeholder && placeholder.toLowerCase().indexOf('username') >= 0) {
        return true;
      }
      const name = input.getAttribute('name');
      if (name && name.toLowerCase().indexOf('username') >= 0) {
        return true;
      }
      if (input.getAttribute('data-testid') === 'username-input') {
        return true;
      }
    }
    return false;
  }

  function buttonHasLoginSubmitLabel(text) {
    if (!text) {
      return false;
    }
    for (const label of LOGIN_SUBMIT_BUTTON_LABELS) {
      if (text.includes(label)) {
        return true;
      }
    }
    return false;
  }

  function hasLoginSubmitButtonInBrowser() {
    return Array.from(document.querySelectorAll('button')).some(button => {
      if (!isElementVisible(button)) {
        return false;
      }
      return buttonHasLoginSubmitLabel(button.textContent);
    });
  }

  function isLoginFormVisibleInBrowser() {
    return hasUsernameInputInBrowser() && hasLoginSubmitButtonInBrowser();
  }

  function fieldHasCommandPlaceholder(field) {
    const tag = field.tagName;
    if (tag !== 'INPUT' && tag !== 'TEXTAREA') {
      return false;
    }
    const placeholder = field.getAttribute('placeholder');
    return placeholder !== null && placeholder.toLowerCase().indexOf('command') >= 0;
  }

  function hasCommandInputInBrowser() {
    const byTestId = document.querySelector('[data-testid="command-input"]');
    if (byTestId !== null && isElementVisible(byTestId)) {
      return true;
    }
    const fields = document.querySelectorAll('input, textarea');
    for (const field of fields) {
      if (!isElementVisible(field)) {
        continue;
      }
      if (fieldHasCommandPlaceholder(field)) {
        return true;
      }
    }
    return false;
  }

  function elementTextIncludesGameInfo(text) {
    return text !== null && text.indexOf('Game Info') >= 0;
  }

  function hasGameInfoPanelInBrowser() {
    const byTestId = document.querySelector('[data-testid="game-info-panel"]');
    if (byTestId !== null && isElementVisible(byTestId)) {
      return true;
    }
    const elements = document.querySelectorAll('*');
    for (const el of elements) {
      if (!isElementVisible(el)) {
        continue;
      }
      if (elementTextIncludesGameInfo(el.textContent)) {
        return true;
      }
    }
    return false;
  }

  function hasBodyTextGameUiIndicators(bodyText) {
    const hasPlayerHeader = bodyText.includes('Player:') && !bodyText.includes('Enter the Void');
    const hasMythosTime = bodyText.includes('Mythos Time');
    const hasRoomContent = bodyText.includes('Occupants') || bodyText.includes('Location');
    return hasPlayerHeader || hasMythosTime || hasRoomContent;
  }

  function hasPrimaryGameUiMarkersInBrowser() {
    const gameTerminal = document.querySelector('[data-testid="game-terminal"]');
    return (
      hasCommandInputInBrowser() ||
      hasGameInfoPanelInBrowser() ||
      (gameTerminal !== null && isElementVisible(gameTerminal))
    );
  }

  window.__mythosE2eIsGameUiLoaded = function mythosE2eIsGameUiLoaded() {
    if (hasCommandInputInBrowser()) {
      return true;
    }
    if (hasGameInfoPanelInBrowser()) {
      return true;
    }
    const bodyText = getBodyInnerText();
    if (hasBodyTextGameUiIndicators(bodyText)) {
      return true;
    }
    if (isLoginFormVisibleInBrowser()) {
      return false;
    }
    return hasPrimaryGameUiMarkersInBrowser();
  };

  window.__mythosE2eCaptureGameUiDiagnostics = function mythosE2eCaptureGameUiDiagnostics() {
    const bodyText = getBodyInnerText();
    return {
      isGameUiLoaded: window.__mythosE2eIsGameUiLoaded(),
      hasVisibleCommandInput: hasCommandInputInBrowser(),
      hasVisibleGameInfoPanel: hasGameInfoPanelInBrowser(),
      hasVisibleLoginForm: isLoginFormVisibleInBrowser(),
      hasBodyGameUiIndicators: hasBodyTextGameUiIndicators(bodyText),
      bodySnippet: bodyText.slice(0, 400),
    };
  };

  function elementShowsConnectedStatus(text) {
    if (!text) {
      return false;
    }
    if (text.trim() === 'Connected') {
      return true;
    }
    return text.includes('Connected') && !text.includes('linkdead');
  }

  window.__mythosE2eHasConnectedStatus = function mythosE2eHasConnectedStatus() {
    const statusElements = Array.from(document.querySelectorAll('*'));
    return statusElements.some(el => {
      if (!isElementVisible(el)) {
        return false;
      }
      return elementShowsConnectedStatus(el.textContent);
    });
  };

  function hasTickMessageInBrowser() {
    const gameInfoElements = Array.from(document.querySelectorAll('*'));
    return gameInfoElements.some(el => {
      if (!isElementVisible(el)) {
        return false;
      }
      const text = el.textContent;
      return text !== null && text.indexOf('[Tick') >= 0 && text.indexOf(']') >= 0;
    });
  }

  function isEmptyGameInfoPanelText(text) {
    return text.includes('No messages to display') || text.includes('No messages yet');
  }

  function hasGameInfoAnyMessageInBrowser() {
    const gameInfoPanel = Array.from(document.querySelectorAll('*')).find(el => {
      if (!isElementVisible(el)) {
        return false;
      }
      return elementTextIncludesGameInfo(el.textContent);
    });
    const panelText = gameInfoPanel ? gameInfoPanel.textContent : null;
    if (!panelText) {
      return false;
    }
    return !isEmptyGameInfoPanelText(panelText);
  }

  function hasRoomStateIndicatorsInBrowser() {
    const bodyText = getBodyInnerText();
    const hasOccupants = bodyText.includes('Occupants');
    const hasExitsOrDescription = bodyText.includes('Exits:') || bodyText.includes('Room Description');
    return hasOccupants && hasExitsOrDescription;
  }

  window.__mythosE2eHasRoomSubscription = function mythosE2eHasRoomSubscription() {
    return hasTickMessageInBrowser() || hasGameInfoAnyMessageInBrowser() || hasRoomStateIndicatorsInBrowser();
  };

  window.__mythosE2eHasExpectedOccupantCount = function mythosE2eHasExpectedOccupantCount(expected) {
    const bodyText = getBodyInnerText();
    const occupantsMatch = bodyText.match(/Occupants\s*\((\d+)\)/);
    if (occupantsMatch) {
      return parseInt(occupantsMatch[1], 10) >= expected;
    }
    const playersMatch = bodyText.match(/Players\s*\((\d+)\)/);
    if (playersMatch) {
      return parseInt(playersMatch[1], 10) >= expected;
    }
    return false;
  };

  window.__mythosE2eHasOtherPlayerNames = function mythosE2eHasOtherPlayerNames(names) {
    const bodyText = getBodyInnerText();
    return names.every(name => bodyText.includes(name));
  };

  window.__mythosE2eIsDisconnectedBannerVisible = function mythosE2eIsDisconnectedBannerVisible() {
    return !getBodyInnerText().includes('You are disconnected and cannot perform actions');
  };

  window.__mythosE2eCaptureOccupantsSnapshot = function mythosE2eCaptureOccupantsSnapshot() {
    const bodyText = getBodyInnerText();
    const occupantsMatch = bodyText.match(/Occupants\s*\((\d+)\)/);
    const playersMatch = bodyText.match(/Players\s*\((\d+)\)/);
    const occupantLine = bodyText.split('\n').find(line => line.includes('Occupants') || line.includes('Players ('));
    const occupantsSection = occupantLine !== undefined ? occupantLine.slice(0, 200) : undefined;
    return {
      hasOccupantsMatch: !!occupantsMatch,
      occupantsCount: occupantsMatch ? parseInt(occupantsMatch[1], 10) : null,
      hasPlayersMatch: !!playersMatch,
      playersCount: playersMatch ? parseInt(playersMatch[1], 10) : null,
      occupantsSnippet: occupantsSection ?? 'not found',
      hasLinkdead: bodyText.includes('(linkdead)'),
    };
  };
})();
