/**
 * ANSI to HTML converter for terminal-style output
 * Handles color codes, formatting, and escape sequences
 * Text is escaped via security.ts before embedding in HTML for defense-in-depth.
 */

import { inputSanitizer } from './security';

interface AnsiState {
  bold: boolean;
  dim: boolean;
  italic: boolean;
  fgColor: string | null;
  bgColor: string | null;
}

const ANSI_COLORS: { [key: string]: string } = {
  '30': '#000000',
  '31': '#ff4444',
  '32': '#00ff00',
  '33': '#ffaa00',
  '34': '#4488ff',
  '35': '#ff44ff',
  '36': '#44ffff',
  '37': '#ffffff',
  '90': '#666666',
  '91': '#ff6666',
  '92': '#66ff66',
  '93': '#ffcc66',
  '94': '#6699ff',
  '95': '#ff66ff',
  '96': '#66ffff',
  '97': '#ffffff',
  '40': '#000000',
  '41': '#ff4444',
  '42': '#00ff00',
  '43': '#ffaa00',
  '44': '#4488ff',
  '45': '#ff44ff',
  '46': '#44ffff',
  '47': '#ffffff',
  '100': '#666666',
  '101': '#ff6666',
  '102': '#66ff66',
  '103': '#ffcc66',
  '104': '#6699ff',
  '105': '#ff66ff',
  '106': '#66ffff',
  '107': '#ffffff',
};

function resetAnsiState(state: AnsiState): void {
  state.bold = false;
  state.dim = false;
  state.italic = false;
  state.fgColor = null;
  state.bgColor = null;
}

function applyStyleCode(state: AnsiState, num: number): void {
  switch (num) {
    case 0:
      resetAnsiState(state);
      break;
    case 1:
      state.bold = true;
      break;
    case 2:
      state.dim = true;
      break;
    case 3:
      state.italic = true;
      break;
    case 22:
      state.bold = false;
      state.dim = false;
      break;
    case 23:
      state.italic = false;
      break;
    default:
      applyColorCode(state, num);
      break;
  }
}

function applyColorCode(state: AnsiState, num: number): void {
  if ((num >= 30 && num <= 37) || (num >= 90 && num <= 97)) {
    state.fgColor = ANSI_COLORS[String(num)] || null;
    return;
  }
  if ((num >= 40 && num <= 47) || (num >= 100 && num <= 107)) {
    state.bgColor = ANSI_COLORS[String(num)] || null;
  }
}

function updateState(state: AnsiState, code: string): void {
  for (const c of code.split(';')) {
    applyStyleCode(state, parseInt(c, 10));
  }
}

function buildStyleList(state: AnsiState): string[] {
  const styles: string[] = [];
  if (state.bold) {
    styles.push('font-weight: bold');
  }
  if (state.dim) {
    styles.push('opacity: 0.7');
  }
  if (state.italic) {
    styles.push('font-style: italic');
  }
  if (state.fgColor) {
    styles.push(`color: ${state.fgColor}`);
  }
  if (state.bgColor) {
    styles.push(`background-color: ${state.bgColor}`);
  }
  return styles;
}

function wrapText(text: string, state: AnsiState): string {
  const escaped = inputSanitizer.sanitizeIncomingPlainText(text);
  if (!state.bold && !state.dim && !state.italic && !state.fgColor && !state.bgColor) {
    return escaped;
  }

  const styles = buildStyleList(state);
  if (styles.length === 0) {
    return escaped;
  }

  return `<span style="${styles.join('; ')}">${escaped}</span>`;
}

export function ansiToHtml(text: string): string {
  const state: AnsiState = {
    bold: false,
    dim: false,
    italic: false,
    fgColor: null,
    bgColor: null,
  };

  const segments: string[] = [];
  let currentText = '';
  let i = 0;

  while (i < text.length) {
    if (text[i] === '\x1b' && text[i + 1] === '[') {
      if (currentText) {
        segments.push(wrapText(currentText, state));
        currentText = '';
      }

      let j = i + 2;
      while (j < text.length && text[j] !== 'm') {
        j++;
      }

      if (j < text.length) {
        updateState(state, text.substring(i + 2, j));
        i = j + 1;
      } else {
        currentText += text[i];
        i++;
      }
    } else {
      currentText += text[i];
      i++;
    }
  }

  if (currentText) {
    segments.push(wrapText(currentText, state));
  }

  return segments.join('');
}

/**
 * Convert ANSI text to HTML and preserve line breaks
 */
export function ansiToHtmlWithBreaks(text: string): string {
  return text
    .split('\n')
    .map(line => ansiToHtml(line))
    .join('<br>');
}
