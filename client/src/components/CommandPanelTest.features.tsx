import { FEATURES, SHORTCUTS } from './CommandPanelTest.constants';
import { EldritchIcon } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';

export function CommandPanelTestFeatures() {
  return (
    <MythosPanel title="Enhanced Features" variant="elevated" size="lg">
      <h3>Command Features</h3>
      {FEATURES.map(([icon, title, description]) => (
        <div key={title}>
          <EldritchIcon name={icon} size={14} />
          <strong>{title}</strong> {description}
        </div>
      ))}
      <h3>Keyboard Shortcuts</h3>
      {SHORTCUTS.map(([shortcut, description]) => (
        <div key={shortcut}>
          <kbd>{shortcut}</kbd> {description}
        </div>
      ))}
    </MythosPanel>
  );
}
