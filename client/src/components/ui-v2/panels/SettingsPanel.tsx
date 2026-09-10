import React from 'react';
import {
  useAccessibilityPreference,
  useAnimationPreference,
  useChatGrainPreference,
  useCompactModePreference,
  useDebugInfoPreference,
} from '../../../contexts/hooks/useThemeContext';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';

function SettingsToggleRow(props: {
  label: string;
  description: string;
  checked: boolean;
  onChange: (next: boolean) => void;
}) {
  return (
    <label className="flex items-start justify-between gap-3 py-2 border-b border-mythos-terminal-border cursor-pointer">
      <span>
        <span className="block text-sm text-mythos-terminal-text">{props.label}</span>
        <span className="block text-xs text-mythos-terminal-text-secondary">{props.description}</span>
      </span>
      <input
        type="checkbox"
        checked={props.checked}
        onChange={event => props.onChange(event.target.checked)}
        className="mt-1 accent-mythos-terminal-primary"
        aria-label={props.label}
      />
    </label>
  );
}

/**
 * UI preferences panel (#804). `ThemeProvider`'s preferences existed but had nowhere to be set --
 * this is that surface, built to land the `chatGrain` toggle. The other rows are already-typed,
 * already-persisted preferences (`ThemeContext.tsx`) that simply had no control until now.
 *
 * Server-side chat effects (garbling, hallucinations) are NOT toggleable here, and never will be
 * -- they're game state under ADR-024, and a client opt-out would be a combat advantage
 * (SUBSYSTEM_CHAT_EFFECT_ACCESSIBILITY_DESIGN.md §2). `chatGrain` is the one exception: it's
 * presentation-only per ADR-025, so toggling it carries no fairness concern.
 */
export const SettingsPanel: React.FC = () => {
  const { chatGrain, setChatGrain } = useChatGrainPreference();
  const { animations, setAnimations } = useAnimationPreference();
  const { compactMode, setCompactMode } = useCompactModePreference();
  const { showDebugInfo, setShowDebugInfo } = useDebugInfoPreference();
  const { highContrast, setHighContrast, reducedMotion, setReducedMotion } = useAccessibilityPreference();

  return (
    <div className="h-full flex flex-col font-mono" data-testid="settings-panel">
      <div className="flex items-center gap-2 p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <EldritchIcon name={MythosIcons.chat} size={18} variant="primary" />
        <h3 className="text-mythos-terminal-primary font-bold">Settings</h3>
      </div>
      <div className="flex-1 overflow-auto p-3 bg-mythos-terminal-background">
        <SettingsToggleRow
          label="Corruption grain"
          description="Decorative texture over chat as corruption rises. Presentation-only."
          checked={chatGrain}
          onChange={setChatGrain}
        />
        <SettingsToggleRow
          label="Animations"
          description="UI transition and motion effects."
          checked={animations}
          onChange={setAnimations}
        />
        <SettingsToggleRow
          label="Compact mode"
          description="Denser panel spacing."
          checked={compactMode}
          onChange={setCompactMode}
        />
        <SettingsToggleRow
          label="High contrast"
          description="Increase UI contrast."
          checked={highContrast}
          onChange={setHighContrast}
        />
        <SettingsToggleRow
          label="Reduced motion"
          description="Minimize non-essential animation, honoring your OS setting too."
          checked={reducedMotion}
          onChange={setReducedMotion}
        />
        <SettingsToggleRow
          label="Debug info"
          description="Show developer diagnostics in the UI."
          checked={showDebugInfo}
          onChange={setShowDebugInfo}
        />
      </div>
    </div>
  );
};
