/**
 * SafeHtml component wrapper for dangerouslySetInnerHTML
 * Sanitizes with DOMPurify at this call site (same config as inputSanitizer.sanitizeIncomingHtml) so static
 * analyzers such as CodeQL recognize the sanitizer before the React XSS sink.
 */

import React from 'react';

import { getDomPurify } from '../../utils/domPurifyClient';
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
  const dirty = typeof html === 'string' ? html : '';
  // Sanitize adjacent to the sink for CodeQL; Opengrep still flags dynamic HTML (ignored in .codacy.yml).
  return (
    <Tag
      className={className}
      dangerouslySetInnerHTML={{
        // nosemgrep: codacy.tools-configs.typescript.react.security.audit.react-dangerouslysetinnerhtml.react-dangerouslysetinnerhtml
        // Reason: value is always getDomPurify().sanitize(..., INCOMING_HTML_DOMPURIFY_CONFIG)
        __html: getDomPurify().sanitize(dirty, INCOMING_HTML_DOMPURIFY_CONFIG),
      }}
      {...props}
    />
  );
};
