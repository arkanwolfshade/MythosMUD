import { EXAMPLES } from './CommandPanelTest.constants';
import { MythosPanel } from './ui/MythosPanel';

export function CommandPanelTestExamples() {
  return (
    <MythosPanel title="Command Examples" variant="eldritch" size="lg">
      {Object.entries(EXAMPLES).map(([category, examples]) => (
        <div key={category}>
          <h4>{category}</h4>
          {examples.map(([command, description]) => (
            <div key={command}>
              <div>&gt; {command}</div>
              <div>{description}</div>
            </div>
          ))}
        </div>
      ))}
    </MythosPanel>
  );
}
