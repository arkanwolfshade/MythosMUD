import React, { useState } from 'react';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';
import { TerminalInput } from './ui/TerminalInput';

export const EldritchEffectsDemo: React.FC = () => {
  const [activeEffects, setActiveEffects] = useState<string[]>([]);
  const [inputValue, setInputValue] = useState('');

  const toggleEffect = (effect: string) => {
    setActiveEffects(prev => (prev.includes(effect) ? prev.filter(e => e !== effect) : [...prev, effect]));
  };

  const effects = [
    {
      name: 'eldritch-glow',
      title: 'Eldritch Glow',
      description: 'Pulsing green glow effect',
      icon: MythosIcons.lightbulb,
    },
    {
      name: 'eldritch-pulse',
      title: 'Eldritch Pulse',
      description: 'Subtle opacity pulse',
      icon: MythosIcons.heart,
    },
    {
      name: 'eldritch-shimmer',
      title: 'Eldritch Shimmer',
      description: 'Horizontal light shimmer',
      icon: MythosIcons.sparkles,
    },
    {
      name: 'eldritch-fade',
      title: 'Eldritch Fade',
      description: 'Fading in and out',
      icon: MythosIcons.eye,
    },
    {
      name: 'eldritch-slide',
      title: 'Eldritch Slide',
      description: 'Subtle horizontal movement',
      icon: MythosIcons.move,
    },
    {
      name: 'eldritch-scale',
      title: 'Eldritch Scale',
      description: 'Slight scaling effect',
      icon: MythosIcons.maximize,
    },
    {
      name: 'eldritch-rotate',
      title: 'Eldritch Rotate',
      description: 'Slow, continuous rotation',
      icon: MythosIcons.rotate,
    },
    {
      name: 'eldritch-blur',
      title: 'Eldritch Blur',
      description: 'Blurring and unblurring',
      icon: MythosIcons.eyeOff,
    },
    {
      name: 'eldritch-shadow',
      title: 'Eldritch Shadow',
      description: 'Pulsing shadow effect',
      icon: MythosIcons.shadow,
    },
    {
      name: 'eldritch-border',
      title: 'Eldritch Border',
      description: 'Pulsing border color',
      icon: MythosIcons.square,
    },
  ];

  return (
    <div className="p-8 bg-mythos-terminal-background min-h-screen text-mythos-terminal-text">
      {/* Simple Test Section - Always Visible Effects */}
      <div className="mb-8 p-4 border border-mythos-terminal-primary">
        <h2 className="text-mythos-terminal-primary text-xl mb-4">Always Active Effects Test</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="p-4 border border-mythos-terminal-primary animate-eldritch-glow">
            <p className="text-center">Glow Effect</p>
          </div>
          <div className="p-4 border border-mythos-terminal-primary animate-eldritch-pulse">
            <p className="text-center">Pulse Effect</p>
          </div>
          <div className="p-4 border border-mythos-terminal-primary animate-eldritch-rotate">
            <p className="text-center">Rotate Effect</p>
          </div>
          <div className="p-4 border border-mythos-terminal-primary animate-eldritch-scale">
            <p className="text-center">Scale Effect</p>
          </div>
          <div className="p-4 border border-mythos-terminal-primary animate-eldritch-border">
            <p className="text-center">Border Effect</p>
          </div>
        </div>
      </div>

      <MythosPanel title="Eldritch Effects Demo" subtitle="Phase 4.1 Visuals" variant="eldritch" size="lg">
        <p className="mb-6 text-mythos-terminal-text-secondary">
          Explore various eldritch-themed visual effects and animations. Click the buttons to toggle effects on the
          elements below.
        </p>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-8">
          {effects.map(effect => (
            <TerminalButton
              key={effect.name}
              onClick={() => toggleEffect(effect.name)}
              variant={activeEffects.includes(effect.name) ? 'success' : 'primary'}
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
          {/* Example 1: Animated Button */}
          <MythosPanel title="Animated Button" variant="elevated" interactive>
            <div className="flex flex-col items-center space-y-4">
              <TerminalButton
                onClick={() => alert('Button clicked!')}
                variant="primary"
                size="lg"
                className={`w-full ${activeEffects.includes('eldritch-glow') ? 'animate-eldritch-glow' : ''} ${activeEffects.includes('eldritch-scale') ? 'animate-eldritch-scale' : ''}`}
              >
                <EldritchIcon name={MythosIcons.play} size={20} className="mr-2" />
                Invoke Ritual
              </TerminalButton>
              <p className="text-sm text-mythos-terminal-text-secondary">A button with glow and scale effects.</p>
            </div>
          </MythosPanel>

          {/* Example 2: Animated Input */}
          <MythosPanel title="Animated Input" variant="elevated" interactive>
            <div className="flex flex-col items-center space-y-4">
              <TerminalInput
                value={inputValue}
                onChange={setInputValue}
                placeholder="Type your incantation..."
                className={`w-full ${activeEffects.includes('eldritch-border') ? 'animate-eldritch-border' : ''} ${activeEffects.includes('eldritch-shimmer') ? 'animate-eldritch-shimmer' : ''}`}
              />
              <p className="text-sm text-mythos-terminal-text-secondary">
                An input field with border and shimmer effects on focus.
              </p>
            </div>
          </MythosPanel>

          {/* Example 3: Animated Panel */}
          <MythosPanel
            title="Animated Panel"
            variant="eldritch"
            interactive
            showEldritchBorder={true}
            className={`${activeEffects.includes('eldritch-shadow') ? 'animate-eldritch-shadow' : ''} ${activeEffects.includes('eldritch-pulse') ? 'animate-eldritch-pulse' : ''}`}
          >
            <div className="flex flex-col items-center space-y-4">
              <EldritchIcon name={MythosIcons.star} size={48} className="text-mythos-terminal-primary" />
              <p className="text-lg text-center">
                "That is not dead which can eternal lie, And with strange aeons even death may die."
              </p>
              <p className="text-sm text-mythos-terminal-text-secondary">
                A panel with pulsing shadow and opacity effects.
              </p>
            </div>
          </MythosPanel>

          {/* Example 4: Animated Icon */}
          <MythosPanel title="Animated Icon" variant="default" interactive>
            <div className="flex flex-col items-center space-y-4">
              <EldritchIcon
                name={MythosIcons.rotate}
                size={64}
                className={`text-mythos-terminal-warning ${activeEffects.includes('eldritch-rotate') ? 'animate-eldritch-rotate' : ''} ${activeEffects.includes('eldritch-blur') ? 'animate-eldritch-blur' : ''}`}
              />
              <p className="text-sm text-mythos-terminal-text-secondary">An icon with rotation and blur effects.</p>
            </div>
          </MythosPanel>
        </div>
      </MythosPanel>
    </div>
  );
};
