import { COMMAND_CATEGORIES } from './CommandPanelTest.constants';
import { MythosPanel } from './ui/MythosPanel';

export function CommandCategories() {
  return (
    <MythosPanel title="Command Categories" variant="default" size="lg">
      {Object.entries(COMMAND_CATEGORIES).map(([category, commands]) => (
        <div key={category}>
          <h4>{category}</h4>
          <div>
            {commands.map(command => (
              <span key={command}>{command}</span>
            ))}
          </div>
        </div>
      ))}
    </MythosPanel>
  );
}
