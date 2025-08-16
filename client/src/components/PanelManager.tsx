import { Add, GridOff, GridOn, Settings } from '@mui/icons-material';
import { Box, Button, IconButton, Menu, MenuItem, Tooltip } from '@mui/material';
import { styled } from '@mui/material/styles';
import React, { useCallback, useEffect, useState } from 'react';
import { DraggablePanel } from './DraggablePanel';
import { ChatPanel } from './panels/ChatPanel';
import { CommandPanel } from './panels/CommandPanel';
import { ConnectionPanel } from './panels/ConnectionPanel';
import { PlayerPanel } from './panels/PlayerPanel';
import { RoomPanel } from './panels/RoomPanel';

// Game data interfaces
interface Player {
  name: string;
  stats?: {
    current_health: number;
    max_health?: number;
    sanity: number;
    max_sanity?: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    intelligence?: number;
    wisdom?: number;
    charisma?: number;
  };
  level?: number;
}

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits?: Record<string, string | null>;
  occupants?: string[];
  occupant_count?: number;
}

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

// Styled components

const WorkspaceToolbar = styled(Box)(({ theme }) => ({
  position: 'absolute',
  top: theme.spacing(2),
  right: theme.spacing(2),
  zIndex: 2000,
  display: 'flex',
  gap: theme.spacing(1),
  backgroundColor: theme.palette.background.paper,
  borderRadius: theme.shape.borderRadius,
  padding: theme.spacing(1),
  boxShadow: theme.shadows[4],
}));

interface PanelConfig {
  id: string;
  title: string;
  type: string;
  position: { x: number; y: number };
  size: { width: number; height: number };
  isMinimized: boolean;
  isMaximized: boolean;
  zIndex: number;
}

interface PanelManagerProps {
  children?: React.ReactNode;
  onPanelChange?: (panels: PanelConfig[]) => void;
  initialPanels?: PanelConfig[];
  enableGrid?: boolean;
  gridSize?: number;
  className?: string;
  // Game data props
  isConnected?: boolean;
  isConnecting?: boolean;
  error?: string | null;
  reconnectAttempts?: number;
  room?: Room | null;
  player?: Player | null;
  messages?: ChatMessage[];
  commandHistory?: string[];
  // Game handlers
  onConnect?: () => void;
  onDisconnect?: () => void;
  onLogout?: () => void;
  onDownloadLogs?: () => void;
  onSendCommand?: (command: string) => void;
  onClearMessages?: () => void;
  onClearHistory?: () => void;
}

export const PanelManager: React.FC<PanelManagerProps> = ({
  children,
  onPanelChange,
  initialPanels = [],
  enableGrid = true,
  gridSize = 20,
  className,
  // Game data props
  isConnected = false,
  isConnecting = false,
  error = null,
  reconnectAttempts = 0,
  room = null,
  player = null,
  messages = [],
  commandHistory = [],
  // Game handlers
  onConnect,
  onDisconnect,
  onLogout,
  onDownloadLogs,
  onSendCommand,
  onClearMessages,
  onClearHistory,
}) => {
  // Default panel configuration
  const getDefaultPanels = (): PanelConfig[] => [
    {
      id: 'connection-default',
      title: 'Connection Status',
      type: 'connection',
      position: { x: 20, y: 20 },
      size: { width: 300, height: 200 },
      isMinimized: false,
      isMaximized: false,
      zIndex: 1000,
    },
    {
      id: 'room-default',
      title: 'Room Information',
      type: 'room',
      position: { x: 20, y: 240 },
      size: { width: 350, height: 400 },
      isMinimized: false,
      isMaximized: false,
      zIndex: 1001,
    },
    {
      id: 'player-default',
      title: 'Player Stats',
      type: 'player',
      position: { x: 390, y: 20 },
      size: { width: 300, height: 300 },
      isMinimized: false,
      isMaximized: false,
      zIndex: 1002,
    },
    {
      id: 'chat-default',
      title: 'Chat Log',
      type: 'chat',
      position: { x: 710, y: 20 },
      size: { width: 600, height: 500 },
      isMinimized: false,
      isMaximized: false,
      zIndex: 1003,
    },
    {
      id: 'commands-default',
      title: 'Command History',
      type: 'commands',
      position: { x: 390, y: 340 },
      size: { width: 400, height: 300 },
      isMinimized: false,
      isMaximized: false,
      zIndex: 1004,
    },
  ];

  const [panels, setPanels] = useState<PanelConfig[]>(initialPanels.length > 0 ? initialPanels : getDefaultPanels());
  const [showGrid, setShowGrid] = useState(enableGrid);
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const [nextZIndex, setNextZIndex] = useState(1000);

  // Load panels from localStorage on mount
  useEffect(() => {
    const savedPanels = localStorage.getItem('mythosmud-panels');
    if (savedPanels) {
      try {
        const parsedPanels = JSON.parse(savedPanels);
        // Only use saved panels if they exist and are valid
        if (parsedPanels && Array.isArray(parsedPanels) && parsedPanels.length > 0) {
          setPanels(parsedPanels);
          // Set next z-index to be higher than the highest existing panel
          const maxZIndex = Math.max(...parsedPanels.map((p: PanelConfig) => p.zIndex), 999);
          setNextZIndex(maxZIndex + 1);
        } else {
          // If no valid saved panels, use defaults and save them
          const defaultPanels = getDefaultPanels();
          setPanels(defaultPanels);
          setNextZIndex(1005);
          localStorage.setItem('mythosmud-panels', JSON.stringify(defaultPanels));
        }
      } catch (error) {
        console.error('Failed to load saved panels:', error);
        // On error, use defaults
        const defaultPanels = getDefaultPanels();
        setPanels(defaultPanels);
        setNextZIndex(1005);
        localStorage.setItem('mythosmud-panels', JSON.stringify(defaultPanels));
      }
    } else {
      // No saved panels, use defaults and save them
      const defaultPanels = getDefaultPanels();
      setPanels(defaultPanels);
      setNextZIndex(1005);
      localStorage.setItem('mythosmud-panels', JSON.stringify(defaultPanels));
    }
  }, []);

  // Save panels to localStorage whenever they change
  useEffect(() => {
    localStorage.setItem('mythosmud-panels', JSON.stringify(panels));
    onPanelChange?.(panels);
  }, [panels, onPanelChange]);

  // Update grid visibility
  useEffect(() => {
    setShowGrid(enableGrid);
  }, [enableGrid]);

  // Bring panel to front
  const bringToFront = useCallback(
    (panelId: string) => {
      setPanels(prev =>
        prev.map(panel => ({
          ...panel,
          zIndex: panel.id === panelId ? nextZIndex : panel.zIndex,
        }))
      );
      setNextZIndex(prev => prev + 1);
    },
    [nextZIndex]
  );

  // Update panel position
  const handlePanelPositionChange = useCallback(
    (panelId: string, position: { x: number; y: number }) => {
      setPanels(prev => prev.map(panel => (panel.id === panelId ? { ...panel, position } : panel)));
      bringToFront(panelId);
    },
    [bringToFront]
  );

  // Update panel size
  const handlePanelSizeChange = useCallback(
    (panelId: string, size: { width: number; height: number }) => {
      setPanels(prev => prev.map(panel => (panel.id === panelId ? { ...panel, size } : panel)));
      bringToFront(panelId);
    },
    [bringToFront]
  );

  // Minimize panel
  const handlePanelMinimize = useCallback((panelId: string) => {
    setPanels(prev =>
      prev.map(panel => (panel.id === panelId ? { ...panel, isMinimized: true, isMaximized: false } : panel))
    );
  }, []);

  // Maximize panel
  const handlePanelMaximize = useCallback((panelId: string) => {
    setPanels(prev =>
      prev.map(panel =>
        panel.id === panelId ? { ...panel, isMaximized: !panel.isMaximized, isMinimized: false } : panel
      )
    );
  }, []);

  // Close panel
  const handlePanelClose = useCallback((panelId: string) => {
    setPanels(prev => prev.filter(panel => panel.id !== panelId));
  }, []);

  // Add new panel
  const addPanel = useCallback(
    (type: string) => {
      const newPanel: PanelConfig = {
        id: `${type}-${Date.now()}`,
        title: getPanelTitle(type),
        type,
        position: { x: 50 + panels.length * 30, y: 50 + panels.length * 30 },
        size: getDefaultPanelSize(type),
        isMinimized: false,
        isMaximized: false,
        zIndex: nextZIndex,
      };

      setPanels(prev => [...prev, newPanel]);
      setNextZIndex(prev => prev + 1);
      setAnchorEl(null);
    },
    [panels.length, nextZIndex]
  );

  // Get panel title based on type
  const getPanelTitle = (type: string): string => {
    switch (type) {
      case 'connection':
        return 'Connection Status';
      case 'room':
        return 'Room Information';
      case 'player':
        return 'Player Stats';
      case 'chat':
        return 'Chat Log';
      case 'commands':
        return 'Command History';
      default:
        return 'Panel';
    }
  };

  // Get default panel size based on type
  const getDefaultPanelSize = (type: string): { width: number; height: number } => {
    switch (type) {
      case 'connection':
        return { width: 300, height: 200 };
      case 'room':
        return { width: 350, height: 400 };
      case 'player':
        return { width: 300, height: 300 };
      case 'chat':
        return { width: 600, height: 500 };
      case 'commands':
        return { width: 400, height: 300 };
      default:
        return { width: 300, height: 400 };
    }
  };

  // Reset layout
  const resetLayout = useCallback(() => {
    const defaultPanels: PanelConfig[] = [
      {
        id: 'connection-default',
        title: 'Connection Status',
        type: 'connection',
        position: { x: 20, y: 20 },
        size: { width: 300, height: 200 },
        isMinimized: false,
        isMaximized: false,
        zIndex: 1000,
      },
      {
        id: 'room-default',
        title: 'Room Information',
        type: 'room',
        position: { x: 20, y: 240 },
        size: { width: 350, height: 400 },
        isMinimized: false,
        isMaximized: false,
        zIndex: 1001,
      },
      {
        id: 'player-default',
        title: 'Player Stats',
        type: 'player',
        position: { x: 390, y: 20 },
        size: { width: 300, height: 300 },
        isMinimized: false,
        isMaximized: false,
        zIndex: 1002,
      },
      {
        id: 'chat-default',
        title: 'Chat Log',
        type: 'chat',
        position: { x: 710, y: 20 },
        size: { width: 600, height: 500 },
        isMinimized: false,
        isMaximized: false,
        zIndex: 1003,
      },
    ];

    setPanels(defaultPanels);
    setNextZIndex(1004);
  }, []);

  // Handle menu open
  const handleMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  // Handle menu close
  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <div
      className={className}
      style={{
        position: 'relative',
        width: '100%',
        height: '100%',
        minWidth: '100%',
        minHeight: '100%',
        flex: '1 1 auto',
        backgroundColor: '#0a0a0a',
        overflow: 'hidden',
        backgroundImage: showGrid
          ? `
          linear-gradient(rgba(0, 0, 0, 0.1) 1px, transparent 1px),
          linear-gradient(90deg, rgba(0, 0, 0, 0.1) 1px, transparent 1px)
        `
          : 'none',
        backgroundSize: `${gridSize}px ${gridSize}px`,
      }}
    >
      {/* Workspace Toolbar */}
      <WorkspaceToolbar>
        <Tooltip title="Add Panel">
          <Button variant="contained" startIcon={<Add />} onClick={handleMenuOpen} size="small">
            Add Panel
          </Button>
        </Tooltip>

        <Tooltip title={showGrid ? 'Hide Grid' : 'Show Grid'}>
          <IconButton onClick={() => setShowGrid(!showGrid)} color={showGrid ? 'primary' : 'default'} size="small">
            {showGrid ? <GridOff /> : <GridOn />}
          </IconButton>
        </Tooltip>

        <Tooltip title="Reset Layout">
          <IconButton onClick={resetLayout} size="small">
            <Settings />
          </IconButton>
        </Tooltip>
      </WorkspaceToolbar>

      {/* Panel Menu */}
      <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleMenuClose}>
        <MenuItem onClick={() => addPanel('connection')}>Connection Status</MenuItem>
        <MenuItem onClick={() => addPanel('room')}>Room Information</MenuItem>
        <MenuItem onClick={() => addPanel('player')}>Player Stats</MenuItem>
        <MenuItem onClick={() => addPanel('chat')}>Chat Log</MenuItem>
        <MenuItem onClick={() => addPanel('commands')}>Command History</MenuItem>
      </Menu>

      {/* Render Panels */}
      {panels.map(panel => (
        <DraggablePanel
          key={panel.id}
          id={panel.id}
          title={panel.title}
          initialPosition={panel.position}
          initialSize={panel.size}
          isMinimized={panel.isMinimized}
          isMaximized={panel.isMaximized}
          snapToGrid={showGrid}
          gridSize={gridSize}
          onPositionChange={position => handlePanelPositionChange(panel.id, position)}
          onSizeChange={size => handlePanelSizeChange(panel.id, size)}
          onMinimize={() => handlePanelMinimize(panel.id)}
          onMaximize={() => handlePanelMaximize(panel.id)}
          onClose={() => handlePanelClose(panel.id)}
          style={{ zIndex: panel.zIndex }}
        >
          {/* Panel content based on type */}
          {panel.type === 'connection' && (
            <ConnectionPanel
              isConnected={isConnected}
              isConnecting={isConnecting}
              error={error}
              reconnectAttempts={reconnectAttempts}
              onConnect={onConnect || (() => {})}
              onDisconnect={onDisconnect || (() => {})}
              onLogout={onLogout || (() => {})}
              onDownloadLogs={onDownloadLogs || (() => {})}
            />
          )}
          {panel.type === 'room' && <RoomPanel room={room} />}
          {panel.type === 'player' && <PlayerPanel player={player} />}
          {panel.type === 'chat' && (
            <ChatPanel messages={messages} onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
          )}
          {panel.type === 'commands' && (
            <CommandPanel
              commandHistory={commandHistory}
              onSendCommand={onSendCommand || (() => {})}
              onClearHistory={onClearHistory || (() => {})}
              disabled={!isConnected}
              placeholder="Enter command..."
            />
          )}
        </DraggablePanel>
      ))}

      {/* Children content (if any) */}
      {children}
    </div>
  );
};
