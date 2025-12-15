import React, { useState } from 'react';
import { DraggablePanel } from './DraggablePanel';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';
import { TerminalInput } from './ui/TerminalInput';

export const DraggablePanelTest: React.FC = () => {
  const [panels, setPanels] = useState([
    {
      id: '1',
      title: 'Chat Panel',
      variant: 'default' as const,
      position: { x: 50, y: 50 },
      size: { width: 300, height: 400 },
    },
    {
      id: '2',
      title: 'Command Panel',
      variant: 'elevated' as const,
      position: { x: 400, y: 50 },
      size: { width: 350, height: 300 },
    },
    {
      id: '3',
      title: 'Eldritch Panel',
      variant: 'eldritch' as const,
      position: { x: 50, y: 500 },
      size: { width: 400, height: 300 },
    },
  ]);

  const closePanel = (id: string) => {
    setPanels(prev => prev.filter(panel => panel.id !== id));
  };

  const addPanel = () => {
    const newId = (panels.length + 1).toString();
    const variants = ['default', 'elevated', 'eldritch'] as const;
    const variant = variants[panels.length % 3];

    setPanels(prev => [
      ...prev,
      {
        id: newId,
        title: `New ${variant.charAt(0).toUpperCase() + variant.slice(1)} Panel`,
        variant,
        position: { x: 100 + panels.length * 50, y: 100 + panels.length * 50 },
        size: { width: 300, height: 250 },
      },
    ]);
  };

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-mythos-terminal-primary mb-4">DraggablePanel Test</h1>
          <p className="text-mythos-terminal-text-secondary text-lg">
            Enhanced Mythos-themed draggable panels with full functionality
          </p>
        </div>

        {/* Control Panel */}
        <MythosPanel title="Panel Controls" variant="elevated" size="lg">
          <div className="space-y-4">
            <div className="flex flex-wrap gap-4">
              <TerminalButton variant="primary" onClick={addPanel}>
                <EldritchIcon name={MythosIcons.maximize} size={16} className="mr-2" />
                Add New Panel
              </TerminalButton>
              <TerminalButton
                variant="secondary"
                onClick={() => {
                  setPanels([]);
                }}
              >
                <EldritchIcon name={MythosIcons.clear} size={16} className="mr-2" />
                Clear All Panels
              </TerminalButton>
            </div>
            <p className="text-sm text-mythos-terminal-text-secondary">
              Drag panels by their headers, resize using the edges and corners. Try minimizing and maximizing!
            </p>
          </div>
        </MythosPanel>

        {/* Draggable Panels */}
        {panels.map(panel => (
          <DraggablePanel
            key={panel.id}
            title={panel.title}
            variant={panel.variant}
            defaultPosition={panel.position}
            defaultSize={panel.size}
            onClose={() => {
              closePanel(panel.id);
            }}
            onMinimize={() => {
              console.log({ action: 'Minimize panel', panelId: panel.id });
            }}
            onMaximize={() => {
              console.log({ action: 'Maximize panel', panelId: panel.id });
            }}
          >
            <div className="space-y-4">
              <MythosPanel
                title={`${panel.variant.charAt(0).toUpperCase() + panel.variant.slice(1)} Content`}
                variant="outlined"
              >
                <div className="space-y-3">
                  <p className="text-mythos-terminal-text">
                    This is a {panel.variant} panel with enhanced Mythos styling. The panel can be dragged and resized.
                  </p>

                  <div className="space-y-2">
                    <label className="text-sm text-mythos-terminal-text-secondary">Sample Input:</label>
                    <TerminalInput value="" onChange={() => {}} placeholder="Type something..." />
                  </div>

                  <div className="flex flex-wrap gap-2">
                    <TerminalButton variant="primary" size="sm">
                      <EldritchIcon name={MythosIcons.chat} size={14} className="mr-1" />
                      Action
                    </TerminalButton>
                    <TerminalButton variant="secondary" size="sm">
                      <EldritchIcon name={MythosIcons.settings} size={14} className="mr-1" />
                      Settings
                    </TerminalButton>
                  </div>
                </div>
              </MythosPanel>

              <div className="grid grid-cols-2 gap-4 text-xs">
                <div className="space-y-1">
                  <div className="flex justify-between">
                    <span className="text-mythos-terminal-text-secondary">Position:</span>
                    <span className="text-mythos-terminal-text">
                      ({panel.position.x}, {panel.position.y})
                    </span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-mythos-terminal-text-secondary">Size:</span>
                    <span className="text-mythos-terminal-text">
                      {panel.size.width} × {panel.size.height}
                    </span>
                  </div>
                </div>
                <div className="space-y-1">
                  <div className="flex justify-between">
                    <span className="text-mythos-terminal-text-secondary">Variant:</span>
                    <span className="text-mythos-terminal-text capitalize">{panel.variant}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-mythos-terminal-text-secondary">ID:</span>
                    <span className="text-mythos-terminal-text">{panel.id}</span>
                  </div>
                </div>
              </div>
            </div>
          </DraggablePanel>
        ))}

        {/* Instructions */}
        <MythosPanel title="Instructions" variant="eldritch" size="lg">
          <div className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-3">
                <h3 className="text-mythos-terminal-primary font-bold">Panel Variants</h3>
                <ul className="space-y-2 text-sm">
                  <li className="flex items-center gap-2">
                    <div className="w-3 h-3 bg-mythos-terminal-surface border border-gray-700 rounded"></div>
                    <span>
                      <strong>Default:</strong> Standard panel with subtle styling
                    </span>
                  </li>
                  <li className="flex items-center gap-2">
                    <div className="w-3 h-3 bg-mythos-terminal-surface border border-mythos-terminal-primary rounded shadow-lg"></div>
                    <span>
                      <strong>Elevated:</strong> Enhanced shadows and prominence
                    </span>
                  </li>
                  <li className="flex items-center gap-2">
                    <div className="w-3 h-3 bg-mythos-terminal-surface border border-mythos-terminal-primary rounded shadow-xl"></div>
                    <span>
                      <strong>Eldritch:</strong> Maximum eldritch styling with enhanced effects
                    </span>
                  </li>
                </ul>
              </div>

              <div className="space-y-3">
                <h3 className="text-mythos-terminal-primary font-bold">Controls</h3>
                <ul className="space-y-2 text-sm">
                  <li>
                    <strong>Drag:</strong> Click and drag the header to move panels
                  </li>
                  <li>
                    <strong>Resize:</strong> Hover over edges/corners and drag to resize
                  </li>
                  <li>
                    <strong>Minimize:</strong> Click the minimize button to collapse
                  </li>
                  <li>
                    <strong>Maximize:</strong> Click the maximize button to expand
                  </li>
                  <li>
                    <strong>Close:</strong> Click the X button to remove panels
                  </li>
                  <li>
                    <strong>Grid Snap:</strong> Panels snap to a 20px grid by default
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </MythosPanel>
      </div>
    </div>
  );
};
