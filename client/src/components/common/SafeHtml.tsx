/**
 * SafeHtml component wrapper for dangerouslySetInnerHTML
 * Automatically sanitizes HTML content using DOMPurify before rendering
 *
 * This component provides a safe way to render HTML content from the server
 * while preventing XSS attacks. All HTML is sanitized using inputSanitizer
 * before being rendered via dangerouslySetInnerHTML.
 */

import React from 'react';
import { inputSanitizer } from '../../utils/security';

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
 */
export const SafeHtml: React.FC<SafeHtmlProps> = ({ html, className, tag: Tag = 'span', ...props }) => {
  // Sanitize HTML content before rendering
  // nosemgrep: typescript.lang.security.audit.xss.xss
  // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
  const sanitizedHtml = inputSanitizer.sanitizeIncomingHtml(html);

  // nosemgrep: typescript.react.security.audit.dangerouslysetinnerhtml.dangerouslysetinnerhtml
  return <Tag className={className} dangerouslySetInnerHTML={{ __html: sanitizedHtml }} {...props} />;
};
