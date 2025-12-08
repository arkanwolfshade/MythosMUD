import React, { useState } from 'react';
import { CommandPanel } from './panels/CommandPanel';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';

export const CommandPanelTest: React.FC = () => {
  const [commandHistory, setCommandHistory] = useState<string[]>([
    'look',
    'inventory',
    'get ancient tome',
    'read tome',
    'cast eldritch sight',
    'n',
    'look',
    'examine wall',
    'search for secret door',
    'whisper to Professor Armitage "The stars are right"',
    'shout "Beware the Yellow Sign!"',
    'flee',
    's',
    'look',
    'help',
    'who',
    'say "Has anyone seen the Necronomicon?"',
    'wear amulet',
    'cast protection spell',
    'attack cultist',
  ]);

  const [lastCommand, setLastCommand] = useState<string>('');
  const [commandResults, setCommandResults] = useState<string[]>([]);

  const handleSendCommand = (command: string) => {
    setLastCommand(command);
    setCommandHistory(prev => [...prev, command]);

    // Simulate command results
    const results = [
      `Command executed: ${command}`,
      `Processing eldritch knowledge...`,
      `The forbidden knowledge courses through your mind.`,
    ];
    setCommandResults(prev => [...prev, ...results]);
  };

  const handleClearHistory = () => {
    setCommandHistory([]);
    setCommandResults([]);
  };

  const addSampleCommands = () => {
    const sampleCommands = [
      'examine corpse',
      'cast detect magic',
      'search for clues',
      'whisper "The ritual begins"',
      'get ritual dagger',
      'read forbidden scroll',
      'cast summon horror',
      'flee in terror',
    ];
    setCommandHistory(prev => [...prev, ...sampleCommands]);
  };

  const addMythosCommands = () => {
    const mythosCommands = [
      'invoke Cthulhu',
      'read Necronomicon',
      'cast call of the void',
      'whisper to Yog-Sothoth',
      'perform eldritch ritual',
      'summon deep ones',
      'cast lucidity drain',
      'flee from madness',
    ];
    setCommandHistory(prev => [...prev, ...mythosCommands]);
  };

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
          {/* Command Panel */}
          <div className="lg:col-span-2">
            <MythosPanel title="Command Interface" variant="eldritch" size="lg" className="h-[600px]">
              <CommandPanel
                commandHistory={commandHistory}
                onSendCommand={handleSendCommand}
                onClearHistory={handleClearHistory}
                placeholder="Enter your eldritch command..."
              />
            </MythosPanel>
          </div>

          {/* Controls Panel */}
          <div className="space-y-6">
            <MythosPanel title="Command Controls" variant="elevated" size="lg">
              <div className="space-y-4">
                <div className="space-y-2">
                  <label className="text-sm text-mythos-terminal-text-secondary">Last Command:</label>
                  <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded text-sm">
                    {lastCommand || 'No command sent yet'}
                  </div>
                </div>

                <div className="space-y-2">
                  <label className="text-sm text-mythos-terminal-text-secondary">Command Results:</label>
                  <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded text-sm max-h-32 overflow-auto">
                    {commandResults.length > 0 ? (
                      commandResults.slice(-5).map((result, index) => (
                        <div key={index} className="text-mythos-terminal-text-secondary">
                          {result}
                        </div>
                      ))
                    ) : (
                      <div className="text-mythos-terminal-text-secondary">No results yet</div>
                    )}
                  </div>
                </div>

                <div className="flex gap-2">
                  <TerminalButton variant="primary" onClick={addSampleCommands} className="flex-1">
                    <EldritchIcon name={MythosIcons.move} size={16} className="mr-2" />
                    Add Sample
                  </TerminalButton>
                  <TerminalButton variant="secondary" onClick={addMythosCommands} className="flex-1">
                    <EldritchIcon name={MythosIcons.eldritch} size={16} className="mr-2" />
                    Add Mythos
                  </TerminalButton>
                </div>
              </div>
            </MythosPanel>

            <MythosPanel title="Command Statistics" variant="outlined" size="lg">
              <div className="space-y-3 text-sm">
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Total Commands:</span>
                  <span className="text-mythos-terminal-text font-bold">{commandHistory.length}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Look Commands:</span>
                  <span className="text-mythos-terminal-primary">
                    {commandHistory.filter(cmd => cmd.includes('look')).length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Movement Commands:</span>
                  <span className="text-mythos-terminal-secondary">
                    {
                      commandHistory.filter(cmd =>
                        ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'up', 'down'].includes(cmd)
                      ).length
                    }
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Cast Commands:</span>
                  <span className="text-mythos-terminal-warning">
                    {commandHistory.filter(cmd => cmd.startsWith('cast')).length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Communication:</span>
                  <span className="text-mythos-terminal-success">
                    {
                      commandHistory.filter(cmd => ['say', 'whisper', 'shout'].some(type => cmd.startsWith(type)))
                        .length
                    }
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Eldritch Commands:</span>
                  <span className="text-mythos-terminal-error">
                    {
                      commandHistory.filter(cmd =>
                        ['invoke', 'summon', 'ritual', 'eldritch', 'forbidden'].some(word =>
                          cmd.toLowerCase().includes(word)
                        )
                      ).length
                    }
                  </span>
                </div>
              </div>
            </MythosPanel>

            <MythosPanel title="Command Categories" variant="default" size="lg">
              <div className="space-y-3">
                <div className="space-y-2">
                  <h4 className="text-mythos-terminal-primary font-bold text-sm">Movement</h4>
                  <div className="grid grid-cols-2 gap-1 text-xs">
                    {['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'up', 'down'].map(cmd => (
                      <div key={cmd} className="text-mythos-terminal-text-secondary">
                        {cmd}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="space-y-2">
                  <h4 className="text-mythos-terminal-primary font-bold text-sm">Combat</h4>
                  <div className="grid grid-cols-2 gap-1 text-xs">
                    {['attack', 'defend', 'flee', 'cast', 'get', 'drop', 'wear', 'remove'].map(cmd => (
                      <div key={cmd} className="text-mythos-terminal-text-secondary">
                        {cmd}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="space-y-2">
                  <h4 className="text-mythos-terminal-primary font-bold text-sm">Communication</h4>
                  <div className="grid grid-cols-2 gap-1 text-xs">
                    {['say', 'whisper', 'shout', 'tell', 'reply', 'emote'].map(cmd => (
                      <div key={cmd} className="text-mythos-terminal-text-secondary">
                        {cmd}
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </MythosPanel>
          </div>
        </div>

        {/* Features Showcase */}
        <MythosPanel title="Enhanced Features" variant="elevated" size="lg">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Command Features</h3>
              <ul className="space-y-2 text-sm">
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.search} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Auto-suggestions:</strong> Command completion as you type
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.clock} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>History Navigation:</strong> Use ↑↓ arrows to browse past commands
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.move} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Quick Commands:</strong> One-click access to common commands
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.clear} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>History Management:</strong> Clear command history with one click
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.help} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Help Integration:</strong> Quick access to command help
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.stats} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Command Statistics:</strong> Track your command usage
                  </span>
                </li>
              </ul>
            </div>

            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Keyboard Shortcuts</h3>
              <div className="space-y-3 text-sm">
                <div className="space-y-2">
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">↑</kbd>
                    <span>Navigate up in command history</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">↓</kbd>
                    <span>Navigate down in command history</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">
                      Tab
                    </kbd>
                    <span>Auto-complete command (future feature)</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">
                      Enter
                    </kbd>
                    <span>Send command</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">
                      Ctrl+L
                    </kbd>
                    <span>Clear input (future feature)</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <kbd className="px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded text-xs">
                      Ctrl+R
                    </kbd>
                    <span>Search history (future feature)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </MythosPanel>

        {/* Command Examples */}
        <MythosPanel title="Command Examples" variant="eldritch" size="lg">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="space-y-3">
              <h4 className="text-mythos-terminal-primary font-bold">Basic Commands</h4>
              <div className="space-y-2 text-sm">
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; look</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Examine your surroundings</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; inventory</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Check your possessions</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; help</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Get command help</div>
                </div>
              </div>
            </div>

            <div className="space-y-3">
              <h4 className="text-mythos-terminal-primary font-bold">Movement</h4>
              <div className="space-y-2 text-sm">
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; n</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Move north</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; s</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Move south</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; up</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Climb up</div>
                </div>
              </div>
            </div>

            <div className="space-y-3">
              <h4 className="text-mythos-terminal-primary font-bold">Eldritch Commands</h4>
              <div className="space-y-2 text-sm">
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; cast eldritch sight</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">See the unseen</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; read Necronomicon</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Study forbidden lore</div>
                </div>
                <div className="p-2 bg-mythos-terminal-background border border-gray-700 rounded">
                  <div className="text-mythos-terminal-text font-mono">&gt; invoke Cthulhu</div>
                  <div className="text-mythos-terminal-text-secondary text-xs">Summon the Great Old One</div>
                </div>
              </div>
            </div>
          </div>
        </MythosPanel>
      </div>
    </div>
  );
};
