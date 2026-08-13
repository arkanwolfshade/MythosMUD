import React from 'react';
import type { Channel } from './ChannelSelector';
import { ChannelSelector } from './ChannelSelector';
import { EldritchIcon } from './EldritchIcon';
import { MythosPanel } from './MythosPanel';
import {
  AllStats,
  ConnectionStatus,
  HealthStat,
  LucidityStat,
  MessagesCount,
  PlayerName,
  StatusPanel,
  type StatusPanelProps,
} from './StatusPanel';
import { TerminalButton } from './TerminalButton';
import { TerminalCard } from './TerminalCard';
import { TerminalInput } from './TerminalInput';
import { buildClasses } from './designTokens';

// Match StatusPanel player shape (requires stats.lucidity) so mock fixtures stay assignable.
export type StyleGuideMockPlayer = NonNullable<StatusPanelProps['player']>;

type StyleGuideInputState = {
  value: string;
  setValue: (v: string) => void;
};

export type StyleGuideInputsProps = {
  basic: StyleGuideInputState;
  disabled: StyleGuideInputState;
  error: StyleGuideInputState;
  sizeSm: StyleGuideInputState;
  sizeMd: StyleGuideInputState;
  sizeLg: StyleGuideInputState;
};

export function StyleGuideButtonsSection() {
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Buttons</h2>
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
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
        <div className="space-y-2">
          <h3 className="text-lg font-semibold">Sizes</h3>
          <div className="space-y-2">
            <TerminalButton size="sm">Small</TerminalButton>
            <TerminalButton size="md">Medium</TerminalButton>
            <TerminalButton size="lg">Large</TerminalButton>
          </div>
        </div>
        <div className="space-y-2">
          <h3 className="text-lg font-semibold">States</h3>
          <div className="space-y-2">
            <TerminalButton>Normal</TerminalButton>
            <TerminalButton disabled>Disabled</TerminalButton>
            <TerminalButton className="opacity-75">Loading</TerminalButton>
          </div>
        </div>
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
        <div className="space-y-2">
          <h3 className="text-lg font-semibold">Custom</h3>
          <div className="space-y-2">
            <button className={buildClasses.button('primary', 'md')}>Built Class</button>
            <button className={buildClasses.button('secondary', 'sm', true)}>Disabled Built</button>
          </div>
        </div>
      </div>
    </section>
  );
}

export function StyleGuideInputsSection({ inputs }: { inputs: StyleGuideInputsProps }) {
  const { basic, disabled, error, sizeSm, sizeMd, sizeLg } = inputs;
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Inputs</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Basic Inputs</h3>
          <div className="space-y-3">
            <TerminalInput
              placeholder="Enter text..."
              value={basic.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                basic.setValue(e.target.value);
              }}
            />
            <TerminalInput
              placeholder="Disabled input"
              value={disabled.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                disabled.setValue(e.target.value);
              }}
              disabled
            />
            <TerminalInput
              placeholder="Error state"
              value={error.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                error.setValue(e.target.value);
              }}
              className="border-red-500 focus:border-red-500 focus:ring-red-500"
            />
          </div>
        </div>
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Sizes</h3>
          <div className="space-y-3">
            <TerminalInput
              size="sm"
              placeholder="Small input"
              value={sizeSm.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                sizeSm.setValue(e.target.value);
              }}
            />
            <TerminalInput
              size="md"
              placeholder="Medium input"
              value={sizeMd.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                sizeMd.setValue(e.target.value);
              }}
            />
            <TerminalInput
              size="lg"
              placeholder="Large input"
              value={sizeLg.value}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                sizeLg.setValue(e.target.value);
              }}
            />
          </div>
        </div>
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Custom Classes</h3>
          <div className="space-y-3">
            <input className={buildClasses.input('default', 'md')} placeholder="Built class input" />
            <input className={buildClasses.input('error', 'md', true)} placeholder="Disabled built class" />
          </div>
        </div>
      </div>
    </section>
  );
}

export function StyleGuideCardsSection() {
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Cards & Panels</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <TerminalCard>
          <h3 className="text-lg font-semibold mb-2">Basic Card</h3>
          <p className="text-sm text-mythos-terminal-text-secondary">
            This is a basic card component with default styling.
          </p>
        </TerminalCard>
        <MythosPanel variant="default" title="Default Panel">
          <p className="text-sm">Default panel variant</p>
        </MythosPanel>
        <MythosPanel variant="elevated" title="Elevated Panel">
          <p className="text-sm">Elevated panel with shadow</p>
        </MythosPanel>
        <MythosPanel variant="eldritch" title="Eldritch Panel">
          <p className="text-sm">Eldritch panel with special styling</p>
        </MythosPanel>
        <div className={buildClasses.panel('default', 'md')}>
          <h3 className="text-lg font-semibold mb-2">Built Panel</h3>
          <p className="text-sm">Panel built with design tokens</p>
        </div>
      </div>
    </section>
  );
}

type StyleGuideCompoundSectionProps = {
  mockPlayer: StyleGuideMockPlayer;
};

export function StyleGuideCompoundSection({ mockPlayer }: StyleGuideCompoundSectionProps) {
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Compound Components</h2>
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
  );
}

type FormsSectionProps = {
  channels: Channel[];
  selectedChannel: string;
  setSelectedChannel: (v: string) => void;
  inputValue: string;
  setInputValue: (v: string) => void;
  formInputValue: string;
  setFormInputValue: (v: string) => void;
};

export function StyleGuideFormsSection(props: FormsSectionProps) {
  const {
    channels,
    selectedChannel,
    setSelectedChannel,
    inputValue,
    setInputValue,
    formInputValue,
    setFormInputValue,
  } = props;
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Form Components</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Channel Selector</h3>
          <ChannelSelector channels={channels} selectedChannel={selectedChannel} onChannelSelect={setSelectedChannel} />
        </div>
        <div className="space-y-4">
          <h3 className="text-lg font-semibold">Form Example</h3>
          <form className="space-y-3">
            <TerminalInput
              placeholder="Player name"
              value={inputValue}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                setInputValue(e.target.value);
              }}
            />
            <TerminalInput
              placeholder="Character name"
              value={formInputValue}
              onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                setFormInputValue(e.target.value);
              }}
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
  );
}

export function StyleGuideIconsSection() {
  const icons = [
    { name: 'chat', variant: 'primary' },
    { name: 'command', variant: 'secondary' },
    { name: 'connection', variant: 'success' },
    { name: 'horror', variant: 'error' },
    { name: 'eye', variant: 'warning' },
    { name: 'log', variant: 'secondary' },
    { name: 'clear', variant: 'error' },
    { name: 'download', variant: 'primary' },
  ] as const;
  return (
    <section className="space-y-4">
      <h2 className="text-2xl font-bold text-mythos-terminal-primary">Icons</h2>
      <div className="grid grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-4">
        {icons.map(icon => (
          <div key={icon.name} className="text-center">
            <EldritchIcon name={icon.name} size={24} variant={icon.variant} />
            <p className="text-xs mt-1">
              {icon.name === 'horror' ? 'error' : icon.name === 'eye' ? 'warning' : icon.name}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

export function StyleGuideColorsSection() {
  return (
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
  );
}

export function StyleGuideTypographySection() {
  return (
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
  );
}
