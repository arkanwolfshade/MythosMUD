import React, { useState } from 'react';
import { buildClasses } from './designTokens';
import {
  AllStats,
  Channel,
  ChannelSelector,
  ConnectionStatus,
  EldritchIcon,
  HealthStat,
  LucidityStat,
  MessagesCount,
  MythosPanel,
  PlayerName,
  StatusPanel,
  TerminalButton,
  TerminalCard,
  TerminalInput,
} from './index';

/**
 * Style Guide Component
 *
 * This component demonstrates all available UI components and their variants.
 * It serves as both documentation and a testing ground for the design system.
 */
export const StyleGuide: React.FC = () => {
  const [inputValue, setInputValue] = useState('');
  const [selectedChannel, setSelectedChannel] = useState('local');
  const [disabledInputValue, setDisabledInputValue] = useState('');
  const [errorInputValue, setErrorInputValue] = useState('');
  const [sizeSmValue, setSizeSmValue] = useState('');
  const [sizeMdValue, setSizeMdValue] = useState('');
  const [sizeLgValue, setSizeLgValue] = useState('');
  const [formInputValue, setFormInputValue] = useState('');

  const mockPlayer = {
    id: 'player-1',
    name: 'TestPlayer',
    stats: {
      current_db: 100,
      lucidity: 80,
      strength: 10,
      dexterity: 12,
      constitution: 14,
      intelligence: 16,
      wisdom: 13,
      charisma: 15,
      occult_knowledge: 5,
      fear: 2,
      corruption: 1,
      cult_affiliation: 0,
    },
    level: 5,
  };

  const channels: Channel[] = [
    {
      id: 'local',
      name: 'Local',
      description: 'Chat with players in your current room',
      icon: 'local',
      color: '#10b981',
      shortcut: 'say',
    },
    {
      id: 'global',
      name: 'Global',
      description: 'Chat with all players across the game',
      icon: 'global',
      color: '#3b82f6',
      shortcut: 'chat',
    },
    {
      id: 'whisper',
      name: 'Whisper',
      description: 'Send a private message to a specific player',
      icon: 'whisper',
      color: '#8b5cf6',
      shortcut: 'whisper',
    },
  ];

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-6">
      <div className="max-w-7xl mx-auto space-y-8">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-4xl font-bold text-mythos-terminal-primary mb-2">MythosMUD UI Style Guide</h1>
          <p className="text-mythos-terminal-text-secondary">Comprehensive component library and design system</p>
        </div>

        {/* Buttons Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Buttons</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
            {/* Button Variants */}
            <div className="space-y-2">
              <h3 className="text-lg font-semibold">Variants</h3>
              <div className="space-y-2">
                <TerminalButton variant="primary">Primary</TerminalButton>
                <TerminalButton variant="secondary">Secondary</TerminalButton>
                <TerminalButton variant="danger">Error</TerminalButton>
                <TerminalButton variant="success">Success</TerminalButton>
                <TerminalButton variant="warning">Warning</TerminalButton>
              </div>
            </div>

            {/* Button Sizes */}
            <div className="space-y-2">
              <h3 className="text-lg font-semibold">Sizes</h3>
              <div className="space-y-2">
                <TerminalButton size="sm">Small</TerminalButton>
                <TerminalButton size="md">Medium</TerminalButton>
                <TerminalButton size="lg">Large</TerminalButton>
              </div>
            </div>

            {/* Button States */}
            <div className="space-y-2">
              <h3 className="text-lg font-semibold">States</h3>
              <div className="space-y-2">
                <TerminalButton>Normal</TerminalButton>
                <TerminalButton disabled>Disabled</TerminalButton>
                <TerminalButton className="opacity-75">Loading</TerminalButton>
              </div>
            </div>

            {/* Button with Icons */}
            <div className="space-y-2">
              <h3 className="text-lg font-semibold">With Icons</h3>
              <div className="space-y-2">
                <TerminalButton>
                  <EldritchIcon name="chat" size={16} className="mr-2" />
                  Chat
                </TerminalButton>
                <TerminalButton variant="danger">
                  <EldritchIcon name="horror" size={16} className="mr-2" />
                  Error
                </TerminalButton>
              </div>
            </div>

            {/* Custom Classes */}
            <div className="space-y-2">
              <h3 className="text-lg font-semibold">Custom</h3>
              <div className="space-y-2">
                <button className={buildClasses.button('primary', 'md')}>Built Class</button>
                <button className={buildClasses.button('secondary', 'sm', true)}>Disabled Built</button>
              </div>
            </div>
          </div>
        </section>

        {/* Inputs Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Inputs</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Basic Inputs */}
            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Basic Inputs</h3>
              <div className="space-y-3">
                <TerminalInput
                  placeholder="Enter text..."
                  value={inputValue}
                  onChange={e => setInputValue(e.target.value)}
                />
                <TerminalInput
                  placeholder="Disabled input"
                  value={disabledInputValue}
                  onChange={e => setDisabledInputValue(e.target.value)}
                  disabled
                />
                <TerminalInput
                  placeholder="Error state"
                  value={errorInputValue}
                  onChange={e => setErrorInputValue(e.target.value)}
                  className="border-red-500 focus:border-red-500 focus:ring-red-500"
                />
              </div>
            </div>

            {/* Input Sizes */}
            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Sizes</h3>
              <div className="space-y-3">
                <TerminalInput
                  size="sm"
                  placeholder="Small input"
                  value={sizeSmValue}
                  onChange={e => setSizeSmValue(e.target.value)}
                />
                <TerminalInput
                  size="md"
                  placeholder="Medium input"
                  value={sizeMdValue}
                  onChange={e => setSizeMdValue(e.target.value)}
                />
                <TerminalInput
                  size="lg"
                  placeholder="Large input"
                  value={sizeLgValue}
                  onChange={e => setSizeLgValue(e.target.value)}
                />
              </div>
            </div>

            {/* Custom Inputs */}
            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Custom Classes</h3>
              <div className="space-y-3">
                <input className={buildClasses.input('default', 'md')} placeholder="Built class input" />
                <input className={buildClasses.input('error', 'md', true)} placeholder="Disabled built class" />
              </div>
            </div>
          </div>
        </section>

        {/* Cards Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Cards & Panels</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Basic Cards */}
            <TerminalCard>
              <h3 className="text-lg font-semibold mb-2">Basic Card</h3>
              <p className="text-sm text-mythos-terminal-text-secondary">
                This is a basic card component with default styling.
              </p>
            </TerminalCard>

            {/* Mythos Panels */}
            <MythosPanel variant="default" title="Default Panel">
              <p className="text-sm">Default panel variant</p>
            </MythosPanel>

            <MythosPanel variant="elevated" title="Elevated Panel">
              <p className="text-sm">Elevated panel with shadow</p>
            </MythosPanel>

            <MythosPanel variant="eldritch" title="Eldritch Panel">
              <p className="text-sm">Eldritch panel with special styling</p>
            </MythosPanel>

            {/* Custom Panels */}
            <div className={buildClasses.panel('default', 'md')}>
              <h3 className="text-lg font-semibold mb-2">Built Panel</h3>
              <p className="text-sm">Panel built with design tokens</p>
            </div>
          </div>
        </section>

        {/* Compound Components Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Compound Components</h2>

          {/* Status Panel */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Status Panel</h3>
              <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-4">
                <StatusPanel
                  player={mockPlayer}
                  isConnected={true}
                  isConnecting={false}
                  playerName="TestPlayer"
                  messagesCount={5}
                  commandsCount={10}
                >
                  <AllStats />
                </StatusPanel>
              </div>
            </div>

            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Custom Status Composition</h3>
              <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-4">
                <StatusPanel
                  player={mockPlayer}
                  isConnected={true}
                  isConnecting={false}
                  playerName="TestPlayer"
                  messagesCount={5}
                  commandsCount={10}
                >
                  <ConnectionStatus />
                  <PlayerName />
                  <HealthStat />
                  <LucidityStat />
                  <MessagesCount />
                </StatusPanel>
              </div>
            </div>
          </div>
        </section>

        {/* Form Components Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Form Components</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Channel Selector</h3>
              <ChannelSelector
                channels={channels}
                selectedChannel={selectedChannel}
                onChannelSelect={setSelectedChannel}
              />
            </div>

            <div className="space-y-4">
              <h3 className="text-lg font-semibold">Form Example</h3>
              <form className="space-y-3">
                <TerminalInput
                  placeholder="Player name"
                  value={inputValue}
                  onChange={e => setInputValue(e.target.value)}
                />
                <TerminalInput
                  placeholder="Character name"
                  value={formInputValue}
                  onChange={e => setFormInputValue(e.target.value)}
                />
                <div className="flex gap-2">
                  <TerminalButton type="submit" variant="primary">
                    Submit
                  </TerminalButton>
                  <TerminalButton type="button" variant="secondary">
                    Cancel
                  </TerminalButton>
                </div>
              </form>
            </div>
          </div>
        </section>

        {/* Icons Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Icons</h2>
          <div className="grid grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-4">
            <div className="text-center">
              <EldritchIcon name="chat" size={24} variant="primary" />
              <p className="text-xs mt-1">chat</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="command" size={24} variant="secondary" />
              <p className="text-xs mt-1">command</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="connection" size={24} variant="success" />
              <p className="text-xs mt-1">connection</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="horror" size={24} variant="error" />
              <p className="text-xs mt-1">error</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="eye" size={24} variant="warning" />
              <p className="text-xs mt-1">warning</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="log" size={24} variant="secondary" />
              <p className="text-xs mt-1">log</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="clear" size={24} variant="error" />
              <p className="text-xs mt-1">clear</p>
            </div>
            <div className="text-center">
              <EldritchIcon name="download" size={24} variant="primary" />
              <p className="text-xs mt-1">download</p>
            </div>
          </div>
        </section>

        {/* Color Palette Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Color Palette</h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="space-y-2">
              <div className="bg-mythos-terminal-primary h-16 rounded"></div>
              <p className="text-sm">Primary</p>
            </div>
            <div className="space-y-2">
              <div className="bg-mythos-terminal-success h-16 rounded"></div>
              <p className="text-sm">Success</p>
            </div>
            <div className="space-y-2">
              <div className="bg-mythos-terminal-error h-16 rounded"></div>
              <p className="text-sm">Error</p>
            </div>
            <div className="space-y-2">
              <div className="bg-mythos-terminal-warning h-16 rounded"></div>
              <p className="text-sm">Warning</p>
            </div>
          </div>
        </section>

        {/* Typography Section */}
        <section className="space-y-4">
          <h2 className="text-2xl font-bold text-mythos-terminal-primary">Typography</h2>
          <div className="space-y-4">
            <div>
              <h1 className="text-4xl font-bold">Heading 1</h1>
              <h2 className="text-3xl font-bold">Heading 2</h2>
              <h3 className="text-2xl font-bold">Heading 3</h3>
              <h4 className="text-xl font-bold">Heading 4</h4>
              <h5 className="text-lg font-bold">Heading 5</h5>
              <h6 className="text-base font-bold">Heading 6</h6>
            </div>
            <div className="space-y-2">
              <p className="text-base">Base paragraph text</p>
              <p className="text-sm">Small paragraph text</p>
              <p className="text-xs">Extra small paragraph text</p>
              <p className="text-base text-mythos-terminal-text-secondary">Secondary text color</p>
              <p className="text-base text-mythos-terminal-primary">Primary text color</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};
