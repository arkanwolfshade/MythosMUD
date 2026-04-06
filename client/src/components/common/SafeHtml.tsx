/**
 * SafeHtml component wrapper for dangerouslySetInnerHTML
 * Sanitizes with DOMPurify at this call site (same config as inputSanitizer.sanitizeIncomingHtml) so static
 * analyzers such as CodeQL recognize the sanitizer before the React XSS sink.
 */

import DOMPurify from 'dompurify';
import React from 'react';

import { INCOMING_HTML_DOMPURIFY_CONFIG } from '../../utils/security';

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
 * Content is passed through DOMPurify.sanitize with INCOMING_HTML_DOMPURIFY_CONFIG before rendering.
 */
export const SafeHtml: React.FC<SafeHtmlProps> = ({ html, className, tag: Tag = 'span', ...props }) => {
  const sanitizedHtml =
    !html || typeof html !== 'string' ? '' : DOMPurify.sanitize(html, INCOMING_HTML_DOMPURIFY_CONFIG);
  return <Tag className={className} dangerouslySetInnerHTML={{ __html: sanitizedHtml }} {...props} />;
};
