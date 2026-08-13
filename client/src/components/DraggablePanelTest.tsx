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
    <DraggablePanelTestView
      panels={panels}
      onAddPanel={addPanel}
      onClosePanel={closePanel}
      onClearPanels={() => setPanels([])}
    />
  );
};

type DraggablePanel = {
  id: string;
  title: string;
  variant: 'default' | 'elevated' | 'eldritch';
  position: { x: number; y: number };
  size: { width: number; height: number };
};

function PanelControls({ onAddPanel, onClearPanels }: { onAddPanel: () => void; onClearPanels: () => void }) {
  return (
    <MythosPanel title="Panel Controls" variant="elevated" size="lg">
      <div className="space-y-4">
        <div className="flex flex-wrap gap-4">
          <TerminalButton variant="primary" onClick={onAddPanel}>
            <EldritchIcon name={MythosIcons.maximize} size={16} className="mr-2" />
            Add New Panel
          </TerminalButton>
          <TerminalButton variant="secondary" onClick={onClearPanels}>
            <EldritchIcon name={MythosIcons.clear} size={16} className="mr-2" />
            Clear All Panels
          </TerminalButton>
        </div>
        <p className="text-sm text-mythos-terminal-text-secondary">
          Drag panels by their headers, resize using the edges and corners. Try minimizing and maximizing!
        </p>
      </div>
    </MythosPanel>
  );
}

function PanelContent({ panel }: { panel: DraggablePanel }) {
  return (
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
  );
}

function DraggablePanelItem({ panel, onClose }: { panel: DraggablePanel; onClose: (id: string) => void }) {
  return (
    <DraggablePanel
      title={panel.title}
      variant={panel.variant}
      defaultPosition={panel.position}
      defaultSize={panel.size}
      onClose={() => onClose(panel.id)}
      onMinimize={() => {
        console.log({ action: 'Minimize panel', panelId: panel.id });
      }}
      onMaximize={() => {
        console.log({ action: 'Maximize panel', panelId: panel.id });
      }}
    >
      <PanelContent panel={panel} />
    </DraggablePanel>
  );
}

const PANEL_VARIANTS = [
  { label: 'Default', detail: 'Standard panel with subtle styling', swatch: 'border-gray-700' },
  {
    label: 'Elevated',
    detail: 'Enhanced shadows and prominence',
    swatch: 'border-mythos-terminal-primary shadow-lg',
  },
  {
    label: 'Eldritch',
    detail: 'Maximum eldritch styling with enhanced effects',
    swatch: 'border-mythos-terminal-primary shadow-xl',
  },
] as const;

const PANEL_CONTROLS = [
  { label: 'Drag', detail: 'Click and drag the header to move panels' },
  { label: 'Resize', detail: 'Hover over edges/corners and drag to resize' },
  { label: 'Minimize', detail: 'Click the minimize button to collapse' },
  { label: 'Maximize', detail: 'Click the maximize button to expand' },
  { label: 'Close', detail: 'Click the X button to remove panels' },
  { label: 'Grid Snap', detail: 'Panels snap to a 20px grid by default' },
] as const;

function PanelInstructions() {
  return (
    <MythosPanel title="Instructions" variant="eldritch" size="lg">
      <div className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="space-y-3">
            <h3 className="text-mythos-terminal-primary font-bold">Panel Variants</h3>
            <ul className="space-y-2 text-sm">
              {PANEL_VARIANTS.map(v => (
                <li key={v.label} className="flex items-center gap-2">
                  <div className={`w-3 h-3 bg-mythos-terminal-surface border rounded ${v.swatch}`} />
                  <span>
                    <strong>{v.label}:</strong> {v.detail}
                  </span>
                </li>
              ))}
            </ul>
          </div>
          <div className="space-y-3">
            <h3 className="text-mythos-terminal-primary font-bold">Controls</h3>
            <ul className="space-y-2 text-sm">
              {PANEL_CONTROLS.map(c => (
                <li key={c.label}>
                  <strong>{c.label}:</strong> {c.detail}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </MythosPanel>
  );
}

function DraggablePanelTestView({
  panels,
  onAddPanel,
  onClosePanel,
  onClearPanels,
}: {
  panels: DraggablePanel[];
  onAddPanel: () => void;
  onClosePanel: (id: string) => void;
  onClearPanels: () => void;
}) {
  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-mythos-terminal-primary mb-4">DraggablePanel Test</h1>
          <p className="text-mythos-terminal-text-secondary text-lg">
            Enhanced Mythos-themed draggable panels with full functionality
          </p>
        </div>

        <PanelControls onAddPanel={onAddPanel} onClearPanels={onClearPanels} />

        {panels.map(panel => (
          <DraggablePanelItem key={panel.id} panel={panel} onClose={onClosePanel} />
        ))}

        <PanelInstructions />
      </div>
    </div>
  );
}
