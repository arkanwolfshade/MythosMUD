import { CommandCategories } from './CommandPanelTest.categories';
import { CommandControls } from './CommandPanelTest.controls';
import { CommandStats } from './CommandPanelTest.stats';
import type { CommandPanelTestViewModel } from './CommandPanelTest.types';

export function CommandPanelTestSidebar({ viewModel }: { readonly viewModel: CommandPanelTestViewModel }) {
  const { commandHistory, lastCommand, commandResults, onAddSampleCommands, onAddMythosCommands } = viewModel;
  return (
    <div className="space-y-6">
      <CommandControls
        lastCommand={lastCommand}
        commandResults={commandResults}
        onAddSampleCommands={onAddSampleCommands}
        onAddMythosCommands={onAddMythosCommands}
      />
      <CommandStats history={commandHistory} />
      <CommandCategories />
    </div>
  );
}
