/**
 * Browser-side helpers for Playwright waitForFunction / page.evaluate().
 * Plain JavaScript so Codacy Lizard can parse complexity (TS syntax confuses lizard 1.17.x).
 */

const LOGIN_SUBMIT_BUTTON_LABELS = ['Enter the Void', 'Login'];

function hasUsernameInputInBrowser() {
  const inputs = document.querySelectorAll('input');
  for (const input of inputs) {
    const placeholder = input.getAttribute('placeholder');
    if (placeholder && placeholder.toLowerCase().indexOf('username') >= 0) {
      return true;
    }
    const name = input.getAttribute('name');
    if (name && name.toLowerCase().indexOf('username') >= 0) {
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
  return Array.from(document.querySelectorAll('button')).some(button => buttonHasLoginSubmitLabel(button.textContent));
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
  if (document.querySelector('[data-testid="command-input"]') !== null) {
    return true;
  }
  const fields = document.querySelectorAll('input, textarea');
  for (const field of fields) {
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
  if (document.querySelector('[data-testid="game-info-panel"]') !== null) {
    return true;
  }
  const elements = document.querySelectorAll('*');
  for (const el of elements) {
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
  return (
    hasCommandInputInBrowser() ||
    hasGameInfoPanelInBrowser() ||
    document.querySelector('[data-testid="game-terminal"]') !== null
  );
}

function getBodyInnerText() {
  const body = document.body;
  return body ? body.innerText : '';
}

export function isGameUiLoadedInBrowser() {
  if (isLoginFormVisibleInBrowser()) {
    return false;
  }
  if (hasPrimaryGameUiMarkersInBrowser()) {
    return true;
  }
  return hasBodyTextGameUiIndicators(getBodyInnerText());
}

function elementShowsConnectedStatus(text) {
  if (!text) {
    return false;
  }
  if (text.trim() === 'Connected') {
    return true;
  }
  return text.includes('Connected') && !text.includes('linkdead');
}

export function hasConnectedStatusInBrowser() {
  const statusElements = Array.from(document.querySelectorAll('*'));
  return statusElements.some(el => elementShowsConnectedStatus(el.textContent));
}

function hasTickMessageInBrowser() {
  const gameInfoElements = Array.from(document.querySelectorAll('*'));
  return gameInfoElements.some(el => {
    const text = el.textContent;
    return text !== null && text.indexOf('[Tick') >= 0 && text.indexOf(']') >= 0;
  });
}

function isEmptyGameInfoPanelText(text) {
  return text.includes('No messages to display') || text.includes('No messages yet');
}

function hasGameInfoAnyMessageInBrowser() {
  const gameInfoPanel = Array.from(document.querySelectorAll('*')).find(el =>
    elementTextIncludesGameInfo(el.textContent)
  );
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

export function hasRoomSubscriptionInBrowser() {
  return hasTickMessageInBrowser() || hasGameInfoAnyMessageInBrowser() || hasRoomStateIndicatorsInBrowser();
}

export function hasExpectedOccupantCountInBrowser(expected) {
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
}

export function hasOtherPlayerNamesInBrowser(names) {
  const bodyText = getBodyInnerText();
  return names.every(name => bodyText.includes(name));
}

export function isDisconnectedBannerVisibleInBrowser() {
  return !getBodyInnerText().includes('You are disconnected and cannot perform actions');
}

export function captureOccupantsSnapshotInBrowser() {
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
}
