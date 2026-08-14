import type { CommandControlsProps } from './CommandPanelTest.types';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';

export function CommandControls({
  lastCommand,
  commandResults,
  onAddSampleCommands,
  onAddMythosCommands,
}: CommandControlsProps) {
  return (
    <MythosPanel title="Command Controls" variant="elevated" size="lg">
      <div className="space-y-4">
        <div>
          <div className="text-sm text-mythos-terminal-text-secondary">Last Command:</div>
          <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded text-sm">
            {lastCommand || 'No command sent yet'}
          </div>
        </div>
        <div>
          <div className="text-sm text-mythos-terminal-text-secondary">Command Results:</div>
          <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded text-sm max-h-32 overflow-auto">
            {commandResults.length
              ? commandResults.slice(-5).map(result => <div key={result}>{result}</div>)
              : 'No results yet'}
          </div>
        </div>
        <div className="flex gap-2">
          <TerminalButton variant="primary" onClick={onAddSampleCommands}>
            Add Sample
          </TerminalButton>
          <TerminalButton variant="secondary" onClick={onAddMythosCommands}>
            Add Mythos
          </TerminalButton>
        </div>
      </div>
    </MythosPanel>
  );
}
