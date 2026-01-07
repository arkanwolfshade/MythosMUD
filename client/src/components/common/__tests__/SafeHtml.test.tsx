/**
 * Tests for SafeHtml component
 * Verifies that XSS payloads are properly sanitized before rendering
 */

import { render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { SafeHtml } from '../SafeHtml';

describe('SafeHtml', () => {
  it('should sanitize script tags', () => {
    const maliciousHtml = '<script>alert("XSS")</script><p>Safe content</p>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    // nosemgrep: typescript.lang.security.audit.xss.xss
    // This test intentionally uses malicious HTML to verify that SafeHtml component properly sanitizes it
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    // Script tag should be removed
    expect(container.querySelector('script')).toBeNull();
    // Safe content should remain
    expect(container.textContent).toContain('Safe content');
  });

  it('should sanitize event handlers', () => {
    const maliciousHtml = '<div onclick="alert(\'XSS\')">Click me</div>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    const div = container.querySelector('div');
    expect(div).not.toBeNull();
    // onclick attribute should be removed
    expect(div?.getAttribute('onclick')).toBeNull();
    expect(div?.textContent).toContain('Click me');
  });

  it('should sanitize javascript: protocol', () => {
    const maliciousHtml = '<a href="javascript:alert(\'XSS\')">Link</a>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    // Anchor tags are not in ALLOWED_TAGS, so they are removed entirely (safer than just stripping javascript:)
    const link = container.querySelector('a');
    expect(link).toBeNull();
    // The malicious link should be completely removed, leaving only safe content
    expect(container.textContent).toBe('Link'); // Text content remains but link is removed
  });

  it('should preserve allowed HTML tags', () => {
    const safeHtml = '<b>Bold</b> <i>Italic</i> <em>Emphasis</em> <strong>Strong</strong>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={safeHtml} />);

    expect(container.querySelector('b')).not.toBeNull();
    expect(container.querySelector('i')).not.toBeNull();
    expect(container.querySelector('em')).not.toBeNull();
    expect(container.querySelector('strong')).not.toBeNull();
  });

  it('should preserve allowed attributes', () => {
    const htmlWithClass = '<div class="test-class">Content</div>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={htmlWithClass} />);

    const div = container.querySelector('div');
    expect(div?.getAttribute('class')).toBe('test-class');
  });

  it('should handle empty HTML', () => {
    const { container } = render(<SafeHtml html="" />);
    expect(container.textContent).toBe('');
  });

  it('should handle null/undefined HTML gracefully', () => {
    const { container: container1 } = render(<SafeHtml html={null as unknown as string} />);
    expect(container1.textContent).toBe('');

    const { container: container2 } = render(<SafeHtml html={undefined as unknown as string} />);
    expect(container2.textContent).toBe('');
  });

  it('should support custom tag prop', () => {
    const html = '<p>Content</p>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={html} tag="div" />);

    // Should render as div, not span
    const wrapper = container.firstChild;
    expect(wrapper?.nodeName.toLowerCase()).toBe('div');
  });

  it('should support className prop', () => {
    const { container } = render(<SafeHtml html="Content" className="test-class" />);
    const wrapper = container.firstChild as HTMLElement;
    expect(wrapper.className).toBe('test-class');
  });

  it('should sanitize nested script tags', () => {
    const maliciousHtml = '<div><script>alert("XSS")</script>Content</div>';
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    expect(container.querySelector('script')).toBeNull();
    expect(container.textContent).toContain('Content');
  });

  it('should sanitize iframe tags', () => {
    const maliciousHtml = '<iframe src="evil.com"></iframe><p>Safe</p>';
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    expect(container.querySelector('iframe')).toBeNull();
    expect(container.textContent).toContain('Safe');
  });

  it('should sanitize style attributes with javascript', () => {
    const maliciousHtml = '<div style="background: url(javascript:alert(1))">Content</div>';
    const { container } = render(<SafeHtml html={maliciousHtml} />);

    const div = container.querySelector('div');
    // Style attribute should be removed (not in ALLOWED_ATTR)
    expect(div?.getAttribute('style')).toBeNull();
  });

  it('should handle ANSI-to-HTML converted content', () => {
    // Simulate content from ansiToHtmlWithBreaks
    const ansiHtml = '<span style="color: #ff4444">Red text</span>';
    // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
    const { container } = render(<SafeHtml html={ansiHtml} />);

    // Style attributes are not allowed, so span should exist but without style
    const span = container.querySelector('span');
    expect(span).not.toBeNull();
    expect(span?.getAttribute('style')).toBeNull();
    expect(span?.textContent).toContain('Red text');
  });
});
