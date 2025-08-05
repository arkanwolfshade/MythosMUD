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
  '30': '#000000', // black
  '31': '#ff0000', // red
  '32': '#00ff00', // green
  '33': '#ffff00', // yellow
  '34': '#0000ff', // blue
  '35': '#ff00ff', // magenta
  '36': '#00ffff', // cyan
  '37': '#ffffff', // white
  '90': '#808080', // bright black
  '91': '#ff8080', // bright red
  '92': '#80ff80', // bright green
  '93': '#ffff80', // bright yellow
  '94': '#8080ff', // bright blue
  '95': '#ff80ff', // bright magenta
  '96': '#80ffff', // bright cyan
  '97': '#ffffff', // bright white
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
