import { useState, type Dispatch, type SetStateAction } from 'react';
import { DEFAULT_COMMAND_HISTORY, MYTHOS_COMMANDS, SAMPLE_COMMANDS } from './CommandPanelTest.constants';
import {
  CommandPanelTestExamples,
  CommandPanelTestFeatures,
  CommandPanelTestLayout,
  CommandPanelTestSidebar,
} from './CommandPanelTest.panels';
import type { CommandPanelTestViewModel } from './CommandPanelTest.types';

export type { CommandPanelTestViewModel };

function appendCommands(setCommandHistory: Dispatch<SetStateAction<string[]>>, commands: string[]) {
  setCommandHistory(previous => [...previous, ...commands]);
}

export function CommandPanelTest() {
  const [commandHistory, setCommandHistory] = useState<string[]>(DEFAULT_COMMAND_HISTORY);
  const [lastCommand, setLastCommand] = useState('');
  const [commandResults, setCommandResults] = useState<string[]>([]);

  const handleSendCommand = (command: string) => {
    setLastCommand(command);
    setCommandHistory(previous => [...previous, command]);
    setCommandResults(previous => [
      ...previous,
      `Command executed: ${command}`,
      'Processing eldritch knowledge...',
      'The forbidden knowledge courses through your mind.',
    ]);
  };

  const viewModel: CommandPanelTestViewModel = {
    commandHistory,
    lastCommand,
    commandResults,
    onSendCommand: handleSendCommand,
    onClearHistory: () => {
      setCommandHistory([]);
      setCommandResults([]);
    },
    onAddSampleCommands: () => appendCommands(setCommandHistory, SAMPLE_COMMANDS),
    onAddMythosCommands: () => appendCommands(setCommandHistory, MYTHOS_COMMANDS),
  };

  return (
    <CommandPanelTestLayout
      viewModel={viewModel}
      sidebar={<CommandPanelTestSidebar viewModel={viewModel} />}
      features={<CommandPanelTestFeatures />}
      examples={<CommandPanelTestExamples />}
    />
  );
}
