import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';

interface Message {
  id?: string | number;
  text: string;
  timestamp: string;
  [key: string]: unknown;
}

interface VirtualizedMessageListProps {
  messages: Message[];
  itemHeight: number;
  containerHeight: number;
  renderItem: (item: Message, index: number) => React.ReactNode;
  overscan?: number;
}

export const VirtualizedMessageList: React.FC<VirtualizedMessageListProps> = ({
  messages,
  itemHeight,
  containerHeight,
  renderItem,
  overscan = 5,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [scrollTop, setScrollTop] = useState(0);

  // Calculate visible range
  const visibleRange = useMemo(() => {
    const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - overscan);
    const endIndex = Math.min(messages.length - 1, Math.ceil((scrollTop + containerHeight) / itemHeight) + overscan);
    return { startIndex, endIndex };
  }, [scrollTop, containerHeight, itemHeight, messages.length, overscan]);

  // Calculate total height and offset
  const totalHeight = messages.length * itemHeight;
  const offsetY = visibleRange.startIndex * itemHeight;

  // Handle scroll events
  const handleScroll = useCallback((event: React.UIEvent<HTMLDivElement>) => {
    setScrollTop(event.currentTarget.scrollTop);
  }, []);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (containerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = containerRef.current;
      const isAtBottom = scrollTop + clientHeight >= scrollHeight - 10; // 10px threshold

      if (isAtBottom) {
        containerRef.current.scrollTop = scrollHeight;
      }
    }
  }, [messages.length]);

  // Get visible messages
  const visibleMessages = useMemo(() => {
    return messages.slice(visibleRange.startIndex, visibleRange.endIndex + 1);
  }, [messages, visibleRange.startIndex, visibleRange.endIndex]);

  return (
    <div
      ref={containerRef}
      style={{
        height: containerHeight,
        overflow: 'auto',
        position: 'relative',
      }}
      onScroll={handleScroll}
    >
      <div style={{ height: totalHeight, position: 'relative' }}>
        <div
          style={{
            position: 'absolute',
            top: offsetY,
            left: 0,
            right: 0,
          }}
        >
          {visibleMessages.map((message, index) => {
            const actualIndex = visibleRange.startIndex + index;
            return (
              <div key={actualIndex} style={{ height: itemHeight }}>
                {renderItem(message, actualIndex)}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
