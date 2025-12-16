/**
 * Tests for inputSanitizer module.
 */

import { describe, expect, it } from 'vitest';
import { inputSanitizer } from '../security';

describe('Input Sanitization', () => {
  it('should sanitize HTML input', () => {
    const maliciousInput = '<script>alert("xss")</script>Hello World';
    const sanitized = inputSanitizer.sanitizeHtml(maliciousInput);

    expect(sanitized).toBe('Hello World');
    expect(sanitized).not.toContain('<script>');
  });

  it('should strip style attributes and be safe for templates', () => {
    const input = '<span style="color:red">Hello</span>';
    const sanitized = inputSanitizer.sanitizeHtml(input);
    expect(sanitized).toBe('<span>Hello</span>');
    expect(sanitized).not.toContain('style=');
  });

  it('should sanitize user commands', () => {
    const maliciousCommand = 'say <img src=x onerror=alert(1)>';
    const sanitized = inputSanitizer.sanitizeCommand(maliciousCommand);

    expect(sanitized).toBe('say');
    expect(sanitized).not.toContain('<img');
    expect(sanitized).not.toContain('onerror');
  });

  it('should remove javascript: protocol from commands', () => {
    const command = 'say javascript:alert(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).not.toContain('javascript:');
    expect(sanitized).toContain('say');
  });

  it('should remove vbscript: protocol from commands', () => {
    const command = 'say vbscript:msgbox(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).not.toContain('vbscript:');
    expect(sanitized).toContain('say');
  });

  it('should handle commands with mixed case protocols', () => {
    const command = 'say JavaScript:alert(1) VBScript:msgbox(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized.toLowerCase()).not.toContain('javascript:');
    expect(sanitized.toLowerCase()).not.toContain('vbscript:');
  });

  it('should trim whitespace from commands', () => {
    const command = '  say hello  ';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).toBe('say hello');
  });

  it('should preserve safe HTML tags', () => {
    const safeInput = '<b>Bold text</b> and <i>italic text</i>';
    const sanitized = inputSanitizer.sanitizeHtml(safeInput);

    expect(sanitized).toContain('<b>Bold text</b>');
    expect(sanitized).toContain('<i>italic text</i>');
  });

  it('should escape special characters in usernames', () => {
    const username = 'user<script>alert("xss")</script>';
    const sanitized = inputSanitizer.sanitizeUsername(username);

    expect(sanitized).toBe('userscriptalertxsssc');
    expect(sanitized).not.toContain('<script>');
    expect(sanitized).not.toContain('>');
    expect(sanitized).not.toContain('"');
  });

  it('should limit username length to 20 characters', () => {
    const longUsername = 'a'.repeat(30);
    const sanitized = inputSanitizer.sanitizeUsername(longUsername);
    expect(sanitized.length).toBe(20);
  });

  it('should handle null, undefined, and empty string inputs', () => {
    expect(inputSanitizer.sanitizeHtml(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeHtml(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeHtml('')).toBe('');

    expect(inputSanitizer.sanitizeCommand(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeCommand(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeCommand('')).toBe('');

    expect(inputSanitizer.sanitizeUsername(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeUsername(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeUsername('')).toBe('');
  });

  it('should sanitize chat messages', () => {
    const maliciousMessage = '<script>alert("xss")</script><b>Bold</b> text';
    const sanitized = inputSanitizer.sanitizeChatMessage(maliciousMessage);

    expect(sanitized).not.toContain('<script>');
    expect(sanitized).toContain('<b>Bold</b>');
    expect(sanitized).toContain('text');
  });

  it('should handle null, undefined, and empty string in sanitizeChatMessage', () => {
    expect(inputSanitizer.sanitizeChatMessage(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeChatMessage(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeChatMessage('')).toBe('');
  });

  it('should limit chat message length to 500 characters', () => {
    const longMessage = 'a'.repeat(600);
    const sanitized = inputSanitizer.sanitizeChatMessage(longMessage);
    expect(sanitized.length).toBeLessThanOrEqual(500);
  });

  it('should sanitize incoming plain text', () => {
    const text = 'Hello & <world> & "test"';
    const sanitized = inputSanitizer.sanitizeIncomingPlainText(text);

    expect(sanitized).toBe('Hello &amp; &lt;world&gt; &amp; "test"');
    expect(sanitized).not.toContain('<');
    expect(sanitized).not.toContain('>');
    expect(sanitized).toContain('&amp;');
  });

  it('should handle empty and null plain text', () => {
    expect(inputSanitizer.sanitizeIncomingPlainText('')).toBe('');
    expect(inputSanitizer.sanitizeIncomingPlainText(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeIncomingPlainText(undefined as unknown as string)).toBe('');
  });

  it('should sanitize incoming HTML', () => {
    const maliciousHtml = '<script>alert("xss")</script><b>Bold</b> <span class="test">text</span>';
    const sanitized = inputSanitizer.sanitizeIncomingHtml(maliciousHtml);

    expect(sanitized).not.toContain('<script>');
    expect(sanitized).toContain('<b>Bold</b>');
    expect(sanitized).toContain('<span class="test">text</span>');
  });

  it('should preserve allowed HTML tags in incoming HTML', () => {
    const html =
      '<b>Bold</b> <i>Italic</i> <em>Emphasis</em> <strong>Strong</strong> <br> <p>Paragraph</p> <ul><li>Item</li></ul> <code>code</code> <pre>pre</pre>';
    const sanitized = inputSanitizer.sanitizeIncomingHtml(html);

    expect(sanitized).toContain('<b>');
    expect(sanitized).toContain('<i>');
    expect(sanitized).toContain('<em>');
    expect(sanitized).toContain('<strong>');
    expect(sanitized).toContain('<br>');
    expect(sanitized).toContain('<p>');
    expect(sanitized).toContain('<ul>');
    expect(sanitized).toContain('<li>');
    expect(sanitized).toContain('<code>');
    expect(sanitized).toContain('<pre>');
  });

  it('should handle empty and null incoming HTML', () => {
    expect(inputSanitizer.sanitizeIncomingHtml('')).toBe('');
    expect(inputSanitizer.sanitizeIncomingHtml(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeIncomingHtml(undefined as unknown as string)).toBe('');
  });
});
