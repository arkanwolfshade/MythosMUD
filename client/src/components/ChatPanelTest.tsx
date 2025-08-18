import React, { useState } from 'react';
import { ChatPanel } from './panels/ChatPanel';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { MythosPanel } from './ui/MythosPanel';
import { TerminalButton } from './ui/TerminalButton';
import { TerminalInput } from './ui/TerminalInput';

type ChatMessageType = 'chat' | 'whisper' | 'shout' | 'emote' | 'system' | 'error';

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: ChatMessageType;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

export const ChatPanelTest: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      text: 'Welcome to MythosMUD, Professor Wolfshade. The eldritch forces await your command.',
      timestamp: new Date(Date.now() - 300000).toISOString(),
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'You enter the dimly lit library of Miskatonic University. Ancient tomes line the walls, their leather bindings cracked with age.',
      timestamp: new Date(Date.now() - 240000).toISOString(),
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'Professor Armitage says: "Ah, Professor Wolfshade! I trust your research into the Necronomicon is proceeding well?"',
      timestamp: new Date(Date.now() - 180000).toISOString(),
      isHtml: false,
      messageType: 'chat',
    },
    {
      text: 'You whisper to Professor Armitage: "The forbidden knowledge grows stronger each day. I fear what I have uncovered."',
      timestamp: new Date(Date.now() - 120000).toISOString(),
      isHtml: false,
      messageType: 'whisper',
    },
    {
      text: 'Professor Armitage whispers to you: "Be careful, my friend. Some doors, once opened, cannot be closed."',
      timestamp: new Date(Date.now() - 90000).toISOString(),
      isHtml: false,
      messageType: 'whisper',
    },
    {
      text: 'You SHOUT: "The stars are right! The time is now!"',
      timestamp: new Date(Date.now() - 60000).toISOString(),
      isHtml: false,
      messageType: 'shout',
    },
    {
      text: 'You *adjusts spectacles nervously while examining the ancient manuscript*',
      timestamp: new Date(Date.now() - 45000).toISOString(),
      isHtml: false,
      messageType: 'emote',
    },
    {
      text: 'You cast the spell "Eldritch Sight" and your vision becomes clouded with otherworldly knowledge.',
      timestamp: new Date(Date.now() - 30000).toISOString(),
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'ERROR: Your sanity has decreased by 5 points due to exposure to forbidden knowledge.',
      timestamp: new Date(Date.now() - 15000).toISOString(),
      isHtml: false,
      messageType: 'error',
    },
    {
      text: 'You say: "n"',
      timestamp: new Date(Date.now() - 10000).toISOString(),
      isHtml: false,
      messageType: 'chat',
      aliasChain: [
        {
          original: 'n',
          expanded: 'north',
          alias_name: 'direction',
        },
      ],
    },
    {
      text: 'You move north through the ancient corridors.',
      timestamp: new Date(Date.now() - 5000).toISOString(),
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'You say: "look"',
      timestamp: new Date(Date.now() - 2000).toISOString(),
      isHtml: false,
      messageType: 'chat',
      aliasChain: [
        {
          original: 'look',
          expanded: 'look around',
          alias_name: 'action',
        },
      ],
    },
    {
      text: "You are in the Restricted Section of the library. The air is thick with the scent of old parchment and something... else. The walls seem to shift when you're not looking directly at them.",
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'system',
    },
  ]);

  const [newMessage, setNewMessage] = useState('');
  const [messageType, setMessageType] = useState<ChatMessageType>('chat');

  const addMessage = () => {
    if (newMessage.trim()) {
      const message: ChatMessage = {
        text: newMessage,
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType,
      };
      setMessages(prev => [...prev, message]);
      setNewMessage('');
    }
  };

  const clearMessages = () => {
    setMessages([]);
  };

  const downloadLogs = () => {
    const logContent = messages.map(msg => `[${new Date(msg.timestamp).toLocaleString()}] ${msg.text}`).join('\n');

    const blob = new Blob([logContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `mythosmud-chat-${new Date().toISOString().split('T')[0]}.log`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const addSampleMessage = (type: ChatMessageType, text: string) => {
    const message: ChatMessage = {
      text,
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: type,
    };
    setMessages(prev => [...prev, message]);
  };

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text font-mono p-8">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-mythos-terminal-primary mb-4">Enhanced Chat Panel</h1>
          <p className="text-mythos-terminal-text-secondary text-lg">
            Mythos-themed chat interface with improved message organization and styling
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Chat Panel */}
          <div className="lg:col-span-2">
            <MythosPanel title="Chat Interface" variant="eldritch" size="lg" className="h-[600px]">
              <ChatPanel messages={messages} onClearMessages={clearMessages} onDownloadLogs={downloadLogs} />
            </MythosPanel>
          </div>

          {/* Controls Panel */}
          <div className="space-y-6">
            <MythosPanel title="Message Controls" variant="elevated" size="lg">
              <div className="space-y-4">
                <div className="space-y-2">
                  <label className="text-sm text-mythos-terminal-text-secondary">Message Type:</label>
                  <select
                    value={messageType}
                    onChange={e => setMessageType(e.target.value as ChatMessageType)}
                    className="w-full p-2 bg-mythos-terminal-surface border border-gray-700 rounded text-mythos-terminal-text focus:border-mythos-terminal-primary focus:outline-none"
                  >
                    <option value="chat">Chat</option>
                    <option value="whisper">Whisper</option>
                    <option value="shout">Shout</option>
                    <option value="emote">Emote</option>
                    <option value="system">System</option>
                    <option value="error">Error</option>
                  </select>
                </div>

                <div className="space-y-2">
                  <label className="text-sm text-mythos-terminal-text-secondary">New Message:</label>
                  <TerminalInput
                    value={newMessage}
                    onChange={setNewMessage}
                    placeholder="Type your message..."
                    onKeyDown={e => e.key === 'Enter' && addMessage()}
                  />
                </div>

                <TerminalButton variant="primary" onClick={addMessage} disabled={!newMessage.trim()} className="w-full">
                  <EldritchIcon name={MythosIcons.chat} size={16} className="mr-2" />
                  Send Message
                </TerminalButton>
              </div>
            </MythosPanel>

            <MythosPanel title="Sample Messages" variant="outlined" size="lg">
              <div className="space-y-3">
                <TerminalButton
                  variant="secondary"
                  size="sm"
                  onClick={() =>
                    addSampleMessage(
                      'system',
                      'A cold wind blows through the corridors, carrying whispers of ancient secrets.'
                    )
                  }
                  className="w-full"
                >
                  Add System Message
                </TerminalButton>

                <TerminalButton
                  variant="secondary"
                  size="sm"
                  onClick={() =>
                    addSampleMessage('emote', 'You *shudders as the eldritch knowledge courses through your mind*')
                  }
                  className="w-full"
                >
                  Add Emote
                </TerminalButton>

                <TerminalButton
                  variant="secondary"
                  size="sm"
                  onClick={() =>
                    addSampleMessage('whisper', 'You whisper to yourself: "The stars are almost right..."')
                  }
                  className="w-full"
                >
                  Add Whisper
                </TerminalButton>

                <TerminalButton
                  variant="secondary"
                  size="sm"
                  onClick={() => addSampleMessage('error', 'WARNING: Your sanity is dangerously low!')}
                  className="w-full"
                >
                  Add Error
                </TerminalButton>

                <TerminalButton
                  variant="secondary"
                  size="sm"
                  onClick={() => {
                    const message: ChatMessage = {
                      text: 'You say: "n"',
                      timestamp: new Date().toISOString(),
                      isHtml: false,
                      messageType: 'chat',
                      aliasChain: [
                        {
                          original: 'n',
                          expanded: 'north',
                          alias_name: 'direction',
                        },
                      ],
                    };
                    setMessages(prev => [...prev, message]);
                  }}
                  className="w-full"
                >
                  Add Alias Expansion
                </TerminalButton>
              </div>
            </MythosPanel>

            <MythosPanel title="Statistics" variant="default" size="lg">
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Total Messages:</span>
                  <span className="text-mythos-terminal-text font-bold">{messages.length}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">System Messages:</span>
                  <span className="text-mythos-terminal-warning">
                    {messages.filter(m => m.messageType === 'system').length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Chat Messages:</span>
                  <span className="text-mythos-terminal-text">
                    {messages.filter(m => m.messageType === 'chat').length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Whispers:</span>
                  <span className="text-mythos-terminal-secondary">
                    {messages.filter(m => m.messageType === 'whisper').length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Emotes:</span>
                  <span className="text-mythos-terminal-primary">
                    {messages.filter(m => m.messageType === 'emote').length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">Errors:</span>
                  <span className="text-mythos-terminal-error">
                    {messages.filter(m => m.messageType === 'error').length}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-mythos-terminal-text-secondary">With Aliases:</span>
                  <span className="text-mythos-terminal-success">
                    {messages.filter(m => m.aliasChain && m.aliasChain.length > 0).length}
                  </span>
                </div>
              </div>
            </MythosPanel>
          </div>
        </div>

        {/* Features Showcase */}
        <MythosPanel title="Enhanced Features" variant="elevated" size="lg">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Message Types</h3>
              <div className="space-y-2 text-sm">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-text rounded"></div>
                  <span>
                    <strong>Chat:</strong> Regular conversation messages
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-secondary rounded"></div>
                  <span>
                    <strong>Whisper:</strong> Private messages in italic
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-warning rounded"></div>
                  <span>
                    <strong>Shout:</strong> Loud messages in bold
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-primary rounded"></div>
                  <span>
                    <strong>Emote:</strong> Character actions in italic
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-warning rounded"></div>
                  <span>
                    <strong>System:</strong> Game information in bold
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-mythos-terminal-error rounded"></div>
                  <span>
                    <strong>Error:</strong> Error messages in red
                  </span>
                </div>
              </div>
            </div>

            <div className="space-y-4">
              <h3 className="text-mythos-terminal-primary font-bold text-lg">Enhanced Features</h3>
              <ul className="space-y-2 text-sm">
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.move} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Alias Expansion:</strong> Visual display of command aliases
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.clock} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Formatted Timestamps:</strong> Clean, readable time display
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.chat} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Auto-scroll:</strong> Automatically scrolls to new messages
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.download} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Log Export:</strong> Download chat logs as text files
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.clear} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Clear Messages:</strong> One-click message clearing
                  </span>
                </li>
                <li className="flex items-start gap-2">
                  <EldritchIcon name={MythosIcons.connection} size={14} variant="primary" className="mt-0.5" />
                  <span>
                    <strong>Status Footer:</strong> Connection status and message count
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </MythosPanel>
      </div>
    </div>
  );
};
