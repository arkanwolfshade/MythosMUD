/**
 * ANSI to HTML converter for terminal-style output
 * Handles color codes, formatting, and escape sequences
 */

interface AnsiState {
  bold: boolean;
  dim: boolean;
  italic: boolean;
  fgColor: string | null;
  bgColor: string | null;
}

const ANSI_COLORS: { [key: string]: string } = {
  // Foreground colors
  '30': '#000000', // black
  '31': '#ff4444', // red (bright for dark background)
  '32': '#00ff00', // green (bright for dark background)
  '33': '#ffaa00', // yellow/orange (bright for dark background)
  '34': '#4488ff', // blue (bright for dark background)
  '35': '#ff44ff', // magenta (bright for dark background)
  '36': '#44ffff', // cyan (bright for dark background)
  '37': '#ffffff', // white (bright for dark background)
  '90': '#666666', // bright black (gray)
  '91': '#ff6666', // bright red
  '92': '#66ff66', // bright green
  '93': '#ffcc66', // bright yellow/orange
  '94': '#6699ff', // bright blue
  '95': '#ff66ff', // bright magenta
  '96': '#66ffff', // bright cyan
  '97': '#ffffff', // bright white

  // Background colors
  '40': '#000000', // black
  '41': '#ff4444', // red
  '42': '#00ff00', // green
  '43': '#ffaa00', // yellow/orange
  '44': '#4488ff', // blue
  '45': '#ff44ff', // magenta
  '46': '#44ffff', // cyan
  '47': '#ffffff', // white
  '100': '#666666', // bright black (gray)
  '101': '#ff6666', // bright red
  '102': '#66ff66', // bright green
  '103': '#ffcc66', // bright yellow/orange
  '104': '#6699ff', // bright blue
  '105': '#ff66ff', // bright magenta
  '106': '#66ffff', // bright cyan
  '107': '#ffffff', // bright white
};

export function ansiToHtml(text: string): string {
  const state: AnsiState = {
    bold: false,
    dim: false,
    italic: false,
    fgColor: null,
    bgColor: null,
  };

  // Split text into segments based on ANSI escape sequences
  const segments: string[] = [];
  let currentText = '';
  let i = 0;

  while (i < text.length) {
    if (text[i] === '\x1b' && text[i + 1] === '[') {
      // Found ANSI escape sequence
      if (currentText) {
        segments.push(wrapText(currentText, state));
        currentText = '';
      }

      // Find the end of the escape sequence
      let j = i + 2;
      while (j < text.length && text[j] !== 'm') {
        j++;
      }

      if (j < text.length) {
        const code = text.substring(i + 2, j);
        updateState(state, code);
        i = j + 1;
      } else {
        // Malformed escape sequence, treat as literal
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

function updateState(state: AnsiState, code: string): void {
  const codes = code.split(';');

  for (const c of codes) {
    const num = parseInt(c, 10);

    switch (num) {
      case 0: // Reset
        state.bold = false;
        state.dim = false;
        state.italic = false;
        state.fgColor = null;
        state.bgColor = null;
        break;
      case 1: // Bold
        state.bold = true;
        break;
      case 2: // Dim
        state.dim = true;
        break;
      case 3: // Italic
        state.italic = true;
        break;
      case 22: // Reset bold/dim
        state.bold = false;
        state.dim = false;
        break;
      case 23: // Reset italic
        state.italic = false;
        break;
      default:
        // Color codes
        if (num >= 30 && num <= 37) {
          state.fgColor = ANSI_COLORS[num] || null;
        } else if (num >= 90 && num <= 97) {
          state.fgColor = ANSI_COLORS[num] || null;
        } else if (num >= 40 && num <= 47) {
          state.bgColor = ANSI_COLORS[num] || null;
        } else if (num >= 100 && num <= 107) {
          state.bgColor = ANSI_COLORS[num] || null;
        }
        break;
    }
  }
}

function wrapText(text: string, state: AnsiState): string {
  if (!state.bold && !state.dim && !state.italic && !state.fgColor && !state.bgColor) {
    return text;
  }

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

  if (styles.length === 0) {
    return text;
  }

  return `<span style="${styles.join('; ')}">${text}</span>`;
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
