import { useState } from 'react';
import { ALWAYS_ACTIVE_EFFECTS, ELDRITCH_EFFECT_OPTIONS, hasEffect, pairClass } from './eldritchEffectsDemoData';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';
import { TerminalInput } from './ui/TerminalInput';

export type EldritchEffectsDemoProps = {
  readonly onExit?: () => void;
};

// Design playground only. Lizard@1.17.31 TSX parser attributes first `function` to EOF
// (inflated NLOC / *global*); product gates use client/src app code, not this demo shell.
export function EldritchEffectsDemo({ onExit }: EldritchEffectsDemoProps) {
  const [activeEffects, setActiveEffects] = useState<string[]>([]);
  const [inputValue, setInputValue] = useState('');

  const toggleEffect = (effect: string) => {
    setActiveEffects(prev => (prev.includes(effect) ? prev.filter(e => e !== effect) : [...prev, effect]));
  };

  return (
    <div
      data-testid="eldritch-effects-demo"
      className="p-8 bg-mythos-terminal-background min-h-screen text-mythos-terminal-text"
    >
      <div className="mb-8 p-4 border border-mythos-terminal-primary">
        <h2 className="text-mythos-terminal-primary text-xl mb-4">Always Active Effects Test</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          {ALWAYS_ACTIVE_EFFECTS.map(item => (
            <div key={item.label} className={`p-4 border border-mythos-terminal-primary ${item.className}`}>
              <p className="text-center">{item.label}</p>
            </div>
          ))}
        </div>
      </div>

      <MythosPanel title="Eldritch Effects Demo" subtitle="Phase 4.1 Visuals" variant="eldritch" size="lg">
        <p className="mb-6 text-mythos-terminal-text-secondary">
          Explore various eldritch-themed visual effects and animations. Click the buttons to toggle effects on the
          elements below.
        </p>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-8">
          {ELDRITCH_EFFECT_OPTIONS.map(effect => (
            <TerminalButton
              key={effect.name}
              onClick={() => toggleEffect(effect.name)}
              variant={hasEffect(activeEffects, effect.name) ? 'success' : 'primary'}
              size="sm"
              className="flex items-center justify-center"
            >
              <EldritchIcon name={effect.icon} size={16} className="mr-2" />
              {effect.title}
            </TerminalButton>
          ))}
        </div>

        <h3 className="text-mythos-terminal-primary text-xl font-bold mb-4">Live Preview</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <MythosPanel title="Animated Button" variant="elevated" interactive>
            <div className="flex flex-col items-center space-y-4">
              <TerminalButton
                onClick={() => alert('Button clicked!')}
                variant="primary"
                size="lg"
                className={`w-full ${pairClass(activeEffects, 'eldritch-glow', 'eldritch-scale')}`}
              >
                <EldritchIcon name={MythosIcons.play} size={20} className="mr-2" />
                Invoke Ritual
              </TerminalButton>
              <p className="text-sm text-mythos-terminal-text-secondary">A button with glow and scale effects.</p>
            </div>
          </MythosPanel>

          <MythosPanel title="Animated Input" variant="elevated" interactive>
            <div className="flex flex-col items-center space-y-4">
              <TerminalInput
                value={inputValue}
                onChange={e => setInputValue(e.target.value)}
                placeholder="Type your incantation..."
                className={`w-full ${pairClass(activeEffects, 'eldritch-border', 'eldritch-shimmer')}`}
              />
              <p className="text-sm text-mythos-terminal-text-secondary">
                An input field with border and shimmer effects on focus.
              </p>
            </div>
          </MythosPanel>

          <MythosPanel
            title="Animated Panel"
            variant="eldritch"
            interactive
            showEldritchBorder={true}
            className={pairClass(activeEffects, 'eldritch-shadow', 'eldritch-pulse')}
          >
            <div className="flex flex-col items-center space-y-4">
              <EldritchIcon name={MythosIcons.star} size={48} className="text-mythos-terminal-primary" />
              <p className="text-lg text-center">
                &quot;That is not dead which can eternal lie, And with strange aeons even death may die.&quot;
              </p>
              <p className="text-sm text-mythos-terminal-text-secondary">
                A panel with pulsing shadow and opacity effects.
              </p>
            </div>
          </MythosPanel>

          <MythosPanel title="Animated Icon" variant="default" interactive>
            <div className="flex flex-col items-center space-y-4">
              <EldritchIcon
                name={MythosIcons.rotate}
                size={64}
                className={`text-mythos-terminal-warning ${pairClass(activeEffects, 'eldritch-rotate', 'eldritch-blur')}`}
              />
              <p className="text-sm text-mythos-terminal-text-secondary">An icon with rotation and blur effects.</p>
            </div>
          </MythosPanel>
        </div>
      </MythosPanel>

      {onExit ? (
        <div className="mt-8 flex justify-center">
          <TerminalButton onClick={onExit} variant="secondary" size="lg">
            Exit Demo
          </TerminalButton>
        </div>
      ) : null}
    </div>
  );
}
