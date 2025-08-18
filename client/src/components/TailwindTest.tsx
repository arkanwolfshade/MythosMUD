import React, { useState } from 'react';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';
import { TerminalCard } from './ui/TerminalCard';
import { TerminalInput } from './ui/TerminalInput';

export const TailwindTest: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [passwordValue, setPasswordValue] = useState('');

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-mythos-terminal-primary mb-4">MythosMUD Interface</h1>
          <p className="text-mythos-terminal-text-secondary text-lg">
            Enhanced TailwindCSS Components with Eldritch Aesthetics
          </p>
        </div>

        {/* Enhanced Terminal Components */}
        <MythosPanel title="Enhanced Terminal Components" variant="eldritch" size="lg">
          <div className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <h3 className="text-mythos-terminal-primary font-bold text-lg">Buttons</h3>
                <div className="flex flex-wrap gap-3">
                  <TerminalButton variant="primary" size="sm">
                    Small Primary
                  </TerminalButton>
                  <TerminalButton variant="secondary" size="md">
                    Medium Secondary
                  </TerminalButton>
                  <TerminalButton variant="danger" size="lg">
                    Large Danger
                  </TerminalButton>
                </div>
                <TerminalButton variant="primary" disabled>
                  Disabled Button
                </TerminalButton>
              </div>

              <div className="space-y-4">
                <h3 className="text-mythos-terminal-primary font-bold text-lg">Inputs</h3>
                <div className="space-y-3">
                  <TerminalInput value={inputValue} onChange={setInputValue} placeholder="Enter command..." size="md" />
                  <TerminalInput
                    value={passwordValue}
                    onChange={setPasswordValue}
                    placeholder="Password"
                    type="password"
                    size="sm"
                  />
                  <TerminalInput value="" onChange={() => {}} placeholder="Disabled input" disabled size="lg" />
                </div>
              </div>
            </div>
          </div>
        </MythosPanel>

        {/* Mythos Icons Showcase */}
        <MythosPanel title="Eldritch Icons" subtitle="Mythos-themed icon system" variant="elevated" size="lg">
          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.connection} variant="success" size={24} />
              <span className="text-xs text-center">Connection</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.disconnected} variant="error" size={24} />
              <span className="text-xs text-center">Disconnected</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.connecting} variant="warning" size={24} animated />
              <span className="text-xs text-center">Connecting</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.look} variant="primary" size={24} />
              <span className="text-xs text-center">Look</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.chat} variant="secondary" size={24} />
              <span className="text-xs text-center">Chat</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.attack} variant="error" size={24} />
              <span className="text-xs text-center">Attack</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.inventory} variant="primary" size={24} />
              <span className="text-xs text-center">Inventory</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.character} variant="secondary" size={24} />
              <span className="text-xs text-center">Character</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.room} variant="primary" size={24} />
              <span className="text-xs text-center">Room</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.eldritch} variant="warning" size={24} />
              <span className="text-xs text-center">Eldritch</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.horror} variant="error" size={24} />
              <span className="text-xs text-center">Horror</span>
            </div>
            <div className="flex flex-col items-center space-y-2 p-3 border border-gray-700 rounded">
              <EldritchIcon name={MythosIcons.help} variant="primary" size={24} />
              <span className="text-xs text-center">Help</span>
            </div>
          </div>
        </MythosPanel>

        {/* Panel Variants */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <MythosPanel title="Default Panel" variant="default" size="md">
            <p className="text-mythos-terminal-text">
              This is a default panel with standard styling. Perfect for general content display.
            </p>
          </MythosPanel>

          <MythosPanel title="Elevated Panel" variant="elevated" size="md">
            <p className="text-mythos-terminal-text">
              An elevated panel with enhanced shadows and prominence. Great for important information.
            </p>
          </MythosPanel>

          <MythosPanel title="Outlined Panel" variant="outlined" size="md">
            <p className="text-mythos-terminal-text">
              A transparent panel with primary border. Ideal for overlays and floating content.
            </p>
          </MythosPanel>

          <MythosPanel title="Eldritch Panel" variant="eldritch" size="md" showEldritchBorder>
            <p className="text-mythos-terminal-text">
              The most eldritch of panels, with corner decorations and enhanced styling for forbidden knowledge.
            </p>
          </MythosPanel>
        </div>

        {/* Color Palette and Typography */}
        <MythosPanel title="Color Palette & Typography" variant="elevated" size="lg">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Color Palette</h3>
              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-2">
                  <div className="h-12 bg-mythos-terminal-primary rounded border flex items-center justify-center">
                    <span className="text-black font-bold text-sm">Primary</span>
                  </div>
                  <p className="text-xs text-center">#00ff00</p>
                </div>
                <div className="space-y-2">
                  <div className="h-12 bg-mythos-terminal-secondary rounded border flex items-center justify-center">
                    <span className="text-black font-bold text-sm">Secondary</span>
                  </div>
                  <p className="text-xs text-center">#ff9800</p>
                </div>
                <div className="space-y-2">
                  <div className="h-12 bg-mythos-terminal-surface rounded border flex items-center justify-center">
                    <span className="text-mythos-terminal-text font-bold text-sm">Surface</span>
                  </div>
                  <p className="text-xs text-center">#1a1a1a</p>
                </div>
                <div className="space-y-2">
                  <div className="h-12 bg-mythos-terminal-background rounded border border-gray-700 flex items-center justify-center">
                    <span className="text-mythos-terminal-text font-bold text-sm">Background</span>
                  </div>
                  <p className="text-xs text-center">#0a0a0a</p>
                </div>
              </div>
            </div>

            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Typography</h3>
              <div className="space-y-3">
                <h1 className="text-2xl font-bold text-mythos-terminal-primary">Heading 1</h1>
                <h2 className="text-xl font-bold text-mythos-terminal-primary">Heading 2</h2>
                <h3 className="text-lg font-bold text-mythos-terminal-primary">Heading 3</h3>
                <p className="text-mythos-terminal-text">
                  Regular text in the MythosMUD terminal style. The font should be Courier New (monospace).
                </p>
                <p className="text-mythos-terminal-text-secondary">
                  Secondary text with a slightly different color for hierarchy.
                </p>
                <p className="text-mythos-terminal-error">Error text in red for warnings and alerts.</p>
                <p className="text-mythos-terminal-warning">Warning text in orange for cautions.</p>
                <p className="text-mythos-terminal-success">Success text in green for confirmations.</p>
              </div>
            </div>
          </div>
        </MythosPanel>

        {/* Animation Showcase */}
        <MythosPanel title="Animations & Effects" variant="eldritch" size="lg">
          <div className="space-y-6">
            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Shimmer Animation</h3>
              <div className="animate-shimmer bg-mythos-terminal-primary h-8 rounded opacity-50"></div>
              <p className="text-sm text-mythos-terminal-text-secondary">
                The shimmer animation should be visible on the green bar above.
              </p>
            </div>

            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Interactive Elements</h3>
              <div className="flex flex-wrap gap-4">
                <TerminalButton variant="primary" size="md">
                  Hover Me
                </TerminalButton>
                <TerminalButton variant="secondary" size="md">
                  Focus Me
                </TerminalButton>
                <EldritchIcon name={MythosIcons.eldritch} variant="warning" size={32} animated />
              </div>
            </div>
          </div>
        </MythosPanel>

        {/* Legacy Components for Comparison */}
        <TerminalCard title="Legacy TerminalCard Component" variant="outlined">
          <p className="text-mythos-terminal-text">
            This is the original TerminalCard component for comparison. The new MythosPanel provides enhanced styling
            and eldritch elements.
          </p>
        </TerminalCard>
      </div>
    </div>
  );
};
