import React from 'react';
import type { MessageSegment } from '../types';
import { getSegmentClass } from '../utils/messageCategoryStyle';

/**
 * A plain-text line as its styled spans (#1025). The spans' text joins back to the line's `message`, so the
 * words are identical to the unsegmented rendering; only NPC names gain colour and weight.
 *
 * Deliberately not `getMessageCategoryClass`: that adds a `::before` glyph and a Text-labels word, which would
 * decorate every name mid-line. A segment is colour and weight only, and carries no aria of its own.
 */
export const SegmentedText: React.FC<{ segments: MessageSegment[] }> = ({ segments }) => (
  <>
    {segments.map((segment, index) => {
      const className = getSegmentClass(segment.category);
      return className ? (
        <span key={index} className={className}>
          {segment.text}
        </span>
      ) : (
        <React.Fragment key={index}>{segment.text}</React.Fragment>
      );
    })}
  </>
);
