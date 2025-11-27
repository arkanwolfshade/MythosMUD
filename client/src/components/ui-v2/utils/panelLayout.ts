import type { PanelState } from '../types';

// Panel layout utilities for default three-column layout
// Based on findings from "Spatial Organization in Non-Euclidean Interfaces" - Dr. Armitage, 1928

export const createDefaultPanelLayout = (viewportWidth: number, viewportHeight: number): Record<string, PanelState> => {
  const headerHeight = 48;
  const padding = 20;
  const columnWidth = (viewportWidth - padding * 4) / 3;
  const availableHeight = viewportHeight - headerHeight - padding * 2;

  // Left column panels
  const leftColumnX = padding;
  const leftColumnWidth = columnWidth;

  // Middle column panels
  const middleColumnX = padding * 2 + columnWidth;
  const middleColumnWidth = columnWidth;

  // Right column panels
  const rightColumnX = padding * 3 + columnWidth * 2;
  const rightColumnWidth = columnWidth;

  // Calculate panel heights for left column (chat, location, room desc, occupants)
  const leftPanelHeight = availableHeight / 4;

  return {
    chatHistory: {
      id: 'chatHistory',
      title: 'Chat History',
      position: { x: leftColumnX, y: headerHeight + padding },
      size: { width: leftColumnWidth, height: leftPanelHeight * 2 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1000,
      minSize: { width: 300, height: 200 },
    },
    location: {
      id: 'location',
      title: 'Location',
      position: { x: leftColumnX, y: headerHeight + padding + leftPanelHeight * 2 },
      size: { width: leftColumnWidth, height: leftPanelHeight * 0.5 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1001,
      minSize: { width: 200, height: 80 },
    },
    roomDescription: {
      id: 'roomDescription',
      title: 'Room Description',
      position: { x: leftColumnX, y: headerHeight + padding + leftPanelHeight * 2.5 },
      size: { width: leftColumnWidth, height: leftPanelHeight * 0.75 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1002,
      minSize: { width: 200, height: 100 },
    },
    occupants: {
      id: 'occupants',
      title: 'Occupants',
      position: { x: leftColumnX, y: headerHeight + padding + leftPanelHeight * 3.25 },
      size: { width: leftColumnWidth, height: leftPanelHeight * 0.75 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1003,
      minSize: { width: 200, height: 100 },
    },
    gameInfo: {
      id: 'gameInfo',
      title: 'Game Info',
      position: { x: middleColumnX, y: headerHeight + padding },
      size: { width: middleColumnWidth, height: availableHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1004,
      minSize: { width: 300, height: 200 },
    },
    characterInfo: {
      id: 'characterInfo',
      title: 'Character Info',
      position: { x: rightColumnX, y: headerHeight + padding },
      size: { width: rightColumnWidth, height: availableHeight * 0.6 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1005,
      minSize: { width: 250, height: 200 },
    },
    commandHistory: {
      id: 'commandHistory',
      title: 'Command History',
      position: { x: rightColumnX, y: headerHeight + padding + availableHeight * 0.6 },
      size: { width: rightColumnWidth, height: availableHeight * 0.2 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1006,
      minSize: { width: 200, height: 150 },
    },
    commandInput: {
      id: 'commandInput',
      title: 'Command Input',
      position: { x: rightColumnX, y: headerHeight + padding + availableHeight * 0.8 },
      size: { width: rightColumnWidth, height: availableHeight * 0.2 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1007,
      minSize: { width: 200, height: 100 },
    },
  };
};
