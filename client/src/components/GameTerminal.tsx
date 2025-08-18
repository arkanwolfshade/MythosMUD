import React, { useState } from 'react';
import { DraggablePanel } from './DraggablePanel';
import { MotdContent } from './MotdContent';
import { ChatPanel } from './panels/ChatPanel';
import { CommandPanel } from './panels/CommandPanel';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';

interface GameTerminalProps {
  playerId: string;
  playerName: string;
  authToken: string;
  isConnected: boolean;
}

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

export const GameTerminal: React.FC<GameTerminalProps> = ({ playerId, playerName, isConnected }) => {
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    {
      text: `Welcome to MythosMUD, ${playerName}. The eldritch forces await your command.`,
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'You enter the dimly lit library of Miskatonic University. Ancient tomes line the walls, their leather bindings cracked with age.',
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'system',
    },
  ]);

  const [commandHistory, setCommandHistory] = useState<string[]>([]);
  const [showMotd, setShowMotd] = useState(true);

  const handleSendCommand = (command: string) => {
    // Add command to history
    setCommandHistory(prev => [...prev, command]);

    // Add system response to chat
    const response: ChatMessage = {
      text: `You say: "${command}"`,
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'chat',
    };

    setChatMessages(prev => [...prev, response]);

    // Simulate game response
    setTimeout(() => {
      const gameResponse: ChatMessage = {
        text: `The eldritch forces process your command: "${command}". The forbidden knowledge courses through your mind.`,
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType: 'system',
      };
      setChatMessages(prev => [...prev, gameResponse]);
    }, 500);
  };

  const handleClearChat = () => {
    setChatMessages([]);
  };

  const handleDownloadChat = () => {
    const logContent = chatMessages.map(msg => `[${new Date(msg.timestamp).toLocaleString()}] ${msg.text}`).join('\n');

    const blob = new Blob([logContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `mythosmud-chat-${new Date().toISOString().split('T')[0]}.log`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleClearCommands = () => {
    setCommandHistory([]);
  };

  return (
    <div className="h-full w-full bg-mythos-terminal-background text-mythos-terminal-text font-mono relative overflow-hidden">
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 h-12 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-10">
        <div className="flex items-center gap-3">
          <EldritchIcon name={MythosIcons.connection} size={20} variant={isConnected ? 'success' : 'error'} />
          <h1 className="text-lg font-bold text-mythos-terminal-primary">MythosMUD Terminal</h1>
        </div>
        <div className="flex items-center gap-4 text-sm">
          <span className="text-mythos-terminal-text-secondary">Player: {playerName}</span>
          <span
            className={`px-2 py-1 rounded text-xs ${isConnected ? 'bg-mythos-terminal-success text-black' : 'bg-mythos-terminal-error text-white'}`}
          >
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
      </div>

      {/* MOTD Overlay (preserved styles) */}
      {showMotd && (
        <div className="motd-display">
          <div className="motd-content">
            <MotdContent />
          </div>
          <div className="motd-actions">
            <button onClick={() => setShowMotd(false)}>Continue</button>
          </div>
        </div>
      )}

      {/* Main Content Area */}
      <div className="pt-12 h-full">
        {/* Chat Panel */}
        <DraggablePanel
          id="chat-panel"
          title="Chat"
          initialPosition={{ x: 20, y: 80 }}
          initialSize={{ width: 500, height: 400 }}
          minSize={{ width: 300, height: 200 }}
          maxSize={{ width: 800, height: 600 }}
          variant="eldritch"
          onClose={() => console.log('Chat panel closed')}
          onMinimize={() => console.log('Chat panel minimized')}
          onMaximize={() => console.log('Chat panel maximized')}
        >
          <ChatPanel messages={chatMessages} onClearMessages={handleClearChat} onDownloadLogs={handleDownloadChat} />
        </DraggablePanel>

        {/* Command Panel */}
        <DraggablePanel
          id="command-panel"
          title="Commands"
          initialPosition={{ x: 540, y: 80 }}
          initialSize={{ width: 400, height: 400 }}
          minSize={{ width: 300, height: 200 }}
          maxSize={{ width: 600, height: 600 }}
          variant="elevated"
          onClose={() => console.log('Command panel closed')}
          onMinimize={() => console.log('Command panel minimized')}
          onMaximize={() => console.log('Command panel maximized')}
        >
          <CommandPanel
            commandHistory={commandHistory}
            onSendCommand={handleSendCommand}
            onClearHistory={handleClearCommands}
            placeholder="Enter your eldritch command..."
          />
        </DraggablePanel>

        {/* Status Panel */}
        <DraggablePanel
          id="status-panel"
          title="Status"
          initialPosition={{ x: 20, y: 500 }}
          initialSize={{ width: 300, height: 200 }}
          minSize={{ width: 200, height: 150 }}
          maxSize={{ width: 400, height: 300 }}
          variant="default"
          onClose={() => console.log('Status panel closed')}
          onMinimize={() => console.log('Status panel minimized')}
          onMaximize={() => console.log('Status panel maximized')}
        >
          <div className="p-4 space-y-4">
            <div className="space-y-2">
              <h3 className="text-mythos-terminal-primary font-bold">Player Info</h3>
              <div className="space-y-1 text-sm">
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Name:</span>
                  <span className="text-mythos-terminal-text">{playerName}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">ID:</span>
                  <span className="text-mythos-terminal-text">{playerId}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Status:</span>
                  <span className={`${isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error'}`}>
                    {isConnected ? 'Online' : 'Offline'}
                  </span>
                </div>
              </div>
            </div>

            <div className="space-y-2">
              <h3 className="text-mythos-terminal-primary font-bold">Statistics</h3>
              <div className="space-y-1 text-sm">
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Messages:</span>
                  <span className="text-mythos-terminal-text">{chatMessages.length}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Commands:</span>
                  <span className="text-mythos-terminal-text">{commandHistory.length}</span>
                </div>
              </div>
            </div>
          </div>
        </DraggablePanel>
      </div>
    </div>
  );
};
