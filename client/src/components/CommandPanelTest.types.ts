export interface CommandPanelTestViewModel {
  commandHistory: string[];
  lastCommand: string;
  commandResults: string[];
  onSendCommand: (command: string) => void;
  onClearHistory: () => void;
  onAddSampleCommands: () => void;
  onAddMythosCommands: () => void;
}

export interface CommandControlsProps {
  readonly lastCommand: string;
  readonly commandResults: string[];
  readonly onAddSampleCommands: () => void;
  readonly onAddMythosCommands: () => void;
}
