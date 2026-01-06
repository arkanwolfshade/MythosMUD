/**
 * SafeHtml component wrapper for dangerouslySetInnerHTML
 * Automatically sanitizes HTML content using DOMPurify before rendering
 *
 * This component provides a safe way to render HTML content from the server
 * while preventing XSS attacks. All HTML is sanitized using DOMPurify.sanitize()
 * before being rendered via dangerouslySetInnerHTML.
 *
 * Note: Uses DOMPurify directly (rather than inputSanitizer wrapper) so that
 * CodeQL can recognize the sanitization flow and understand the data is safe.
 */

import DOMPurify, { type Config as DOMPurifyConfig } from 'dompurify';
import React from 'react';

interface SafeHtmlProps extends React.HTMLAttributes<HTMLElement> {
  /**
   * HTML content to render (will be sanitized automatically)
   */
  html: string;

  /**
   * Tag name for the wrapper element (default: 'span')
   */
  tag?: React.ElementType;
}

/**
 * SafeHtml component that automatically sanitizes HTML before rendering
 *
 * Usage:
 * ```tsx
 * <SafeHtml html={serverHtml} className="message-content" />
 * ```
 *
 * This replaces direct usage of dangerouslySetInnerHTML with automatic
 * XSS protection via DOMPurify sanitization.
 *
 * CodeQL recognizes DOMPurify.sanitize() as a sanitization function,
 * so using it directly here ensures CodeQL understands the sanitization flow.
 */
export const SafeHtml: React.FC<SafeHtmlProps> = ({ html, className, tag: Tag = 'span', ...props }) => {
  // Sanitize HTML content using DOMPurify before rendering
  // CodeQL tracks DOMPurify.sanitize() data flow and recognizes this as safe sanitization
  // Using the same configuration as inputSanitizer.sanitizeIncomingHtml() for consistency
  // nosemgrep: typescript.lang.security.audit.xss.xss
  // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
  const sanitizedHtml = DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'br', 'p', 'span', 'div', 'ul', 'ol', 'li', 'code', 'pre'],
    ALLOWED_ATTR: ['class'],
    ALLOW_DATA_ATTR: false,
    ALLOW_UNKNOWN_PROTOCOLS: false,
    SAFE_FOR_TEMPLATES: true,
  } as DOMPurifyConfig);

  // HTML content has been sanitized via DOMPurify.sanitize() - CodeQL recognizes this pattern
  // and understands that sanitizedHtml is safe for dangerouslySetInnerHTML
  // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
  return <Tag className={className} dangerouslySetInnerHTML={{ __html: sanitizedHtml }} {...props} />;
};
