import { MOVEMENT_COMMANDS } from './CommandPanelTest.constants';
import { MythosPanel } from './ui/MythosPanel';

export function CommandStats({ history }: { readonly history: string[] }) {
  const communicationTypes = ['say', 'whisper', 'shout'];
  const eldritchPattern = /invoke|summon|ritual|eldritch|forbidden/i;
  const lookCount = history.filter(command => command.includes('look')).length;
  const moveCount = history.filter(command => MOVEMENT_COMMANDS.includes(command)).length;
  const castCount = history.filter(command => command.startsWith('cast')).length;
  const communicationCount = history.filter(command =>
    communicationTypes.some(type => command.startsWith(type))
  ).length;
  const eldritchCount = history.filter(command => eldritchPattern.test(command)).length;
  const rows: Array<[string, number]> = [
    ['Total Commands:', history.length],
    ['Look Commands:', lookCount],
    ['Movement Commands:', moveCount],
    ['Cast Commands:', castCount],
    ['Communication:', communicationCount],
    ['Eldritch Commands:', eldritchCount],
  ];
  return (
    <MythosPanel title="Command Statistics" variant="outlined" size="lg">
      {rows.map(([label, value]) => (
        <div className="flex justify-between" key={label}>
          {label}
          <span>{value}</span>
        </div>
      ))}
    </MythosPanel>
  );
}
