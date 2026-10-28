import type { PanelState } from '../types';
import {
  MINIMIZED_BAR_HEIGHT,
  MINIMIZED_DOCK_PADDING,
  preparePanelForMinimize,
  relayoutMinimizedDock,
} from '../PanelSystem/panelMinimizeDock';

// Panel layout utilities for default three-column layout (#1018)
// Based on findings from "Spatial Organization in Non-Euclidean Interfaces" - Dr. Armitage, 1928
// Left: chat / location / room / occupants. Middle: game info, full height. Right: character info,
// map, journal, command input. Command history and inventory start docked. Heights are ratios of the
// available height so the arrangement holds at any viewport.

export const createDefaultPanelLayout = (viewportWidth: number, viewportHeight: number /* lizard: allow nloc */) => {
  const headerHeight = 48;
  const padding = 20;
  const columnWidth = (viewportWidth - padding * 4) / 3;
  const availableHeight = viewportHeight - headerHeight - padding * 2;
  const top = headerHeight + padding;

  const leftColumnX = padding;
  const middleColumnX = padding * 2 + columnWidth;
  const rightColumnX = padding * 3 + columnWidth * 2;

  // Heights are ratios, floored at each panel's minSize so a short viewport (1280x720) can't push a
  // panel past the column bottom: Rnd enforces minSize, so a ratio below it would overflow the viewport
  // (and focusing the command input then scrolls the overflow-hidden root, shifting the dock).
  // One panel per column takes the remainder, so each column totals exactly its available height.
  // ponytail: below ~600px tall the floors alone exceed the column; no further squeezing is attempted.

  // The dock tray hugs the bottom-left, so the left column stops above it.
  const leftHeight = availableHeight - (MINIMIZED_BAR_HEIGHT + MINIMIZED_DOCK_PADDING);
  const chatHeight = Math.max(leftHeight * 0.26, 200);
  const locationHeight = Math.max(leftHeight * 0.12, 80);
  const roomDescHeight = Math.max(leftHeight * 0.27, 100);
  const occupantsHeight = leftHeight - chatHeight - locationHeight - roomDescHeight;

  const minimapHeight = Math.max(availableHeight * 0.17, 120);
  const questLogHeight = Math.max(availableHeight * 0.16, 100);
  const commandInputHeight = Math.max(availableHeight * 0.17, 120);
  const characterInfoHeight = availableHeight - minimapHeight - questLogHeight - commandInputHeight;

  const panels = {
    chatHistory: {
      id: 'chatHistory',
      title: 'Chat History',
      position: { x: leftColumnX, y: top },
      size: { width: columnWidth, height: chatHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1000,
      minSize: { width: 300, height: 200 },
    },
    location: {
      id: 'location',
      title: 'Location',
      position: { x: leftColumnX, y: top + chatHeight },
      size: { width: columnWidth, height: locationHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1001,
      minSize: { width: 200, height: 80 },
    },
    roomDescription: {
      id: 'roomDescription',
      title: 'Room Description',
      position: { x: leftColumnX, y: top + chatHeight + locationHeight },
      size: { width: columnWidth, height: roomDescHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1002,
      minSize: { width: 200, height: 100 },
    },
    occupants: {
      id: 'occupants',
      title: 'Occupants',
      position: { x: leftColumnX, y: top + chatHeight + locationHeight + roomDescHeight },
      size: { width: columnWidth, height: occupantsHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1003,
      minSize: { width: 200, height: 100 },
    },
    gameInfo: {
      id: 'gameInfo',
      title: 'Game Info',
      position: { x: middleColumnX, y: top },
      size: { width: columnWidth, height: availableHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1004,
      minSize: { width: 300, height: 200 },
    },
    characterInfo: {
      id: 'characterInfo',
      title: 'Character Info',
      position: { x: rightColumnX, y: top },
      size: { width: columnWidth, height: characterInfoHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1005,
      minSize: { width: 250, height: 200 },
    },
    minimap: {
      id: 'minimap',
      title: 'Map',
      position: { x: rightColumnX, y: top + characterInfoHeight },
      size: { width: columnWidth, height: minimapHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1006,
      minSize: { width: 150, height: 100 },
      opaque: true,
      minHeight: 100,
    },
    questLog: {
      id: 'questLog',
      title: 'Journal',
      position: { x: rightColumnX, y: top + characterInfoHeight + minimapHeight },
      size: { width: columnWidth, height: questLogHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1009,
      minSize: { width: 250, height: 100 },
    },
    commandInput: {
      id: 'commandInput',
      title: 'Command Input',
      position: { x: rightColumnX, y: top + characterInfoHeight + minimapHeight + questLogHeight },
      size: { width: columnWidth, height: commandInputHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1010,
      minSize: { width: 280, height: 120 },
    },
    // Docked by default and opened on demand. The geometry here is where each opens, floating
    // above its neighbours (hence the high zIndex); the dock slot is applied below.
    commandHistory: {
      id: 'commandHistory',
      title: 'Command History',
      position: { x: rightColumnX, y: top + availableHeight * 0.5 },
      size: { width: columnWidth, height: availableHeight * 0.35 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1012,
      minSize: { width: 200, height: 150 },
    },
    inventory: {
      id: 'inventory',
      title: 'Inventory',
      position: { x: middleColumnX, y: top + availableHeight * 0.4 },
      size: { width: columnWidth, height: availableHeight * 0.4 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1011,
      minSize: { width: 250, height: 180 },
    },
  } satisfies Record<string, PanelState>;

  // Minimize through the same helpers a runtime minimize uses, so each docked panel keeps its
  // open geometry in preMinimizePosition/Size and expanding it restores there, not at the dock slot.
  const docked = relayoutMinimizedDock(
    {
      ...panels,
      commandHistory: preparePanelForMinimize(panels.commandHistory),
      inventory: preparePanelForMinimize(panels.inventory),
    },
    viewportWidth,
    viewportHeight
  );

  return { ...panels, commandHistory: docked.commandHistory, inventory: docked.inventory };
};
