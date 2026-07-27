/**
 * SafeHtml: render server/chat HTML only after DOMPurify sanitization.
 *
 * Avoids React's dangerouslySetInnerHTML prop (Opengrep XSS rule) by writing
 * sanitized markup onto a host element via useLayoutEffect.
 */

import React, { useLayoutEffect, useRef } from 'react';

import { getDomPurify } from '../../utils/domPurifyClient';
import { INCOMING_HTML_DOMPURIFY_CONFIG } from '../../utils/security';

interface SafeHtmlProps extends React.HTMLAttributes<HTMLElement> {
  /**
   * HTML content to render (will be sanitized automatically)
   */
  html: string;

  /**
   * Host element tag name (default: 'span'). Intrinsic tags only.
   */
  tag?: keyof JSX.IntrinsicElements;
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
export const SafeHtml: React.FC<SafeHtmlProps> = ({ html, className, tag = 'span', ...props }) => {
  const hostRef = useRef<HTMLElement | null>(null);
  const dirty = typeof html === 'string' ? html : '';
  const sanitizedHtml = getDomPurify().sanitize(dirty, INCOMING_HTML_DOMPURIFY_CONFIG);

  useLayoutEffect(() => {
    const host = hostRef.current;
    if (!host) {
      return;
    }
    // DOMPurify output only; not raw user HTML.
    host.innerHTML = sanitizedHtml;
  }, [sanitizedHtml]);

  return React.createElement(tag, { ...props, className, ref: hostRef });
};
