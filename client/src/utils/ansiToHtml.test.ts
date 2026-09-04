import { describe, expect, it } from 'vitest';
import { ansiToHtml, ansiToHtmlWithBreaks } from './ansiToHtml';

describe('ansiToHtml', () => {
  it('should return plain text unchanged', () => {
    const input = 'Hello, World!';
    const result = ansiToHtml(input);
    expect(result).toBe(input);
  });

  it('should handle bold text', () => {
    const input = '\x1b[1mBold Text\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="font-weight: bold">Bold Text</span>');
  });

  it('should handle dim text', () => {
    const input = '\x1b[2mDim Text\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="opacity: 0.7">Dim Text</span>');
  });

  it('should handle italic text', () => {
    const input = '\x1b[3mItalic Text\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="font-style: italic">Italic Text</span>');
  });

  it('should handle foreground colors', () => {
    const input = '\x1b[31mRed Text\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="color: #ff4444">Red Text</span>');
  });

  it('should handle background colors', () => {
    const input = '\x1b[41mRed Background\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="background-color: #ff4444">Red Background</span>');
  });

  it('should handle multiple styles', () => {
    const input = '\x1b[1;31;43mBold Red Text on Yellow Background\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe(
      '<span style="font-weight: bold; color: #ff4444; background-color: #ffaa00">Bold Red Text on Yellow Background</span>'
    );
  });

  it('should handle reset codes', () => {
    const input = '\x1b[1;31mBold Red\x1b[0m Normal Text';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="font-weight: bold; color: #ff4444">Bold Red</span> Normal Text');
  });

  it('should handle partial reset codes', () => {
    const input = '\x1b[1;31mBold Red\x1b[22mNot Bold Red\x1b[0m Normal';
    const result = ansiToHtml(input);
    expect(result).toBe(
      '<span style="font-weight: bold; color: #ff4444">Bold Red</span><span style="color: #ff4444">Not Bold Red</span> Normal'
    );
  });

  it('should handle bright colors', () => {
    const input = '\x1b[91mBright Red\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="color: #ff6666">Bright Red</span>');
  });

  it('should handle bright background colors', () => {
    const input = '\x1b[101mBright Red Background\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('<span style="background-color: #ff6666">Bright Red Background</span>');
  });

  it('should handle malformed escape sequences', () => {
    const input = '\x1b[31mRed\x1b[Invalid';
    const result = ansiToHtml(input);
    expect(result).toContain('<span style="color: #ff4444">Red</span>');
    expect(result).toContain('Invalid');
  });

  it('should handle empty string', () => {
    const result = ansiToHtml('');
    expect(result).toBe('');
  });

  it('should handle text with literal escape characters', () => {
    const input = 'Text with \\x1b literal';
    const result = ansiToHtml(input);
    expect(result).toBe(input);
  });

  it('should handle multiple color codes in sequence', () => {
    const input = '\x1b[31mRed\x1b[32mGreen\x1b[33mYellow\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe(
      '<span style="color: #ff4444">Red</span><span style="color: #00ff00">Green</span><span style="color: #ffaa00">Yellow</span>'
    );
  });

  it('should handle unknown color codes gracefully', () => {
    const input = '\x1b[99mUnknown Color\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toBe('Unknown Color');
  });

  it('should escape HTML entities in text for defense-in-depth', () => {
    const input = '\x1b[31m<script>alert(1)</script>\x1b[0m';
    const result = ansiToHtml(input);
    expect(result).toContain('&lt;script&gt;');
    expect(result).not.toContain('<script>');
  });

  it('should escape angle brackets and ampersand in plain text', () => {
    const input = 'a<b>c & d';
    const result = ansiToHtml(input);
    expect(result).toBe('a&lt;b&gt;c &amp; d');
  });
});

describe('ansiToHtmlWithBreaks', () => {
  it('should convert ANSI text and preserve line breaks', () => {
    const input = '\x1b[31mRed Line\x1b[0m\nNormal Line\n\x1b[32mGreen Line\x1b[0m';
    const result = ansiToHtmlWithBreaks(input);
    expect(result).toBe(
      '<span style="color: #ff4444">Red Line</span><br>Normal Line<br><span style="color: #00ff00">Green Line</span>'
    );
  });

  it('should handle empty string', () => {
    const result = ansiToHtmlWithBreaks('');
    expect(result).toBe('');
  });

  it('should handle single line', () => {
    const input = '\x1b[31mRed Text\x1b[0m';
    const result = ansiToHtmlWithBreaks(input);
    expect(result).toBe('<span style="color: #ff4444">Red Text</span>');
  });

  it('should handle multiple consecutive line breaks', () => {
    const input = 'Line 1\n\nLine 3';
    const result = ansiToHtmlWithBreaks(input);
    expect(result).toBe('Line 1<br><br>Line 3');
  });
});
