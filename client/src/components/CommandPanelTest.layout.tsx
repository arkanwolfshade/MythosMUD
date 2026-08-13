import type { ReactNode } from 'react';
import type { CommandPanelTestViewModel } from './CommandPanelTest.types';
import { CommandPanel } from './panels/CommandPanel';
import { MythosPanel } from './ui/MythosPanel';

interface CommandPanelTestLayoutProps {
  readonly viewModel: CommandPanelTestViewModel;
  readonly sidebar: ReactNode;
  readonly features: ReactNode;
  readonly examples: ReactNode;
}

export function CommandPanelTestLayout({ viewModel, sidebar, features, examples }: CommandPanelTestLayoutProps) {
  const { commandHistory, onSendCommand, onClearHistory } = viewModel;
  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-mythos-terminal-primary mb-4">Enhanced Command Panel</h1>
          <p className="text-mythos-terminal-text-secondary text-lg">
            Mythos-themed command interface with improved history and suggestions
          </p>
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <MythosPanel title="Command Interface" variant="eldritch" size="lg" className="min-h-panel-test">
              <CommandPanel
                commandHistory={commandHistory}
                onSendCommand={onSendCommand}
                onClearHistory={onClearHistory}
                placeholder="Enter your eldritch command..."
              />
            </MythosPanel>
          </div>
          {sidebar}
        </div>
        {features}
        {examples}
      </div>
    </div>
  );
}
