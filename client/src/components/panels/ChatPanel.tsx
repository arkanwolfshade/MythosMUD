import React, { useEffect, useRef, useState } from 'react';
import { AVAILABLE_CHANNELS, DEFAULT_CHANNEL } from '../../config/channels';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import { TerminalInput } from '../ui/TerminalInput';

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface ChatPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export const ChatPanel: React.FC<ChatPanelProps> = ({
  messages,
  onSendChatMessage,
  onClearMessages,
  onDownloadLogs,
  disabled = false,
  isConnected = true,
  selectedChannel = DEFAULT_CHANNEL,
  onChannelSelect,
}) => {
  const [chatInput, setChatInput] = useState('');
  const [inputHistory, setInputHistory] = useState<string[]>([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const [showChatHistory, setShowChatHistory] = useState(false);
  const [chatFilter, setChatFilter] = useState<string>('all');
  const [channelActivity, setChannelActivity] = useState<Record<string, { lastActivity: Date; messageCount: number }>>(
    {}
  );
  const [unreadCounts, setUnreadCounts] = useState<Record<string, number>>({});
  const [isTyping, setIsTyping] = useState(false);
  const [showTypingIndicator, setShowTypingIndicator] = useState(false);
  const [showEmotePanel, setShowEmotePanel] = useState(false);
  const [showFormattingPanel, setShowFormattingPanel] = useState(false);
  const [showSettingsPanel, setShowSettingsPanel] = useState(false);
  const [fontSize, setFontSize] = useState<'small' | 'medium' | 'large'>('medium');
  const [soundEnabled, setSoundEnabled] = useState(true);
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);
  const [ignoredUsers, setIgnoredUsers] = useState<string[]>([]);
  const [spamFilterEnabled, setSpamFilterEnabled] = useState(true);
  const [messageRateLimit, setMessageRateLimit] = useState(5); // messages per minute
  const [lastMessageTime, setLastMessageTime] = useState<number>(0);
  const [exportFormat, setExportFormat] = useState<'txt' | 'json' | 'html'>('txt');
  const inputRef = useRef<HTMLInputElement>(null);

  // Focus input on mount
  useEffect(() => {
    // Focus will be handled by autoFocus prop
  }, []);

  // Track channel activity from messages
  useEffect(() => {
    const newActivity: Record<string, { lastActivity: Date; messageCount: number }> = {};

    messages.forEach(message => {
      // Handle both 'chat' and 'command' messages that contain chat content
      if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
        // Extract channel from message content or use the message's channel property
        const channelId = message.channel || extractChannelFromMessage(message.text) || selectedChannel;

        // Debug logging for ChatPanel message processing
        if (process.env.NODE_ENV === 'development') {
          console.log('🔍 ChatPanel Message Processing:', {
            messageText: message.text.substring(0, 100) + (message.text.length > 100 ? '...' : ''),
            messageType: message.messageType,
            messageChannel: message.channel,
            extractedChannel: extractChannelFromMessage(message.text),
            selectedChannel: selectedChannel,
            finalChannelId: channelId,
            isChatContent: isChatContent(message.text),
            timestamp: message.timestamp,
          });
        }

        if (!newActivity[channelId]) {
          newActivity[channelId] = { lastActivity: new Date(message.timestamp), messageCount: 0 };
        }

        newActivity[channelId].messageCount++;
        newActivity[channelId].lastActivity = new Date(message.timestamp);
      }
    });

    setChannelActivity(prev => ({ ...prev, ...newActivity }));

    // Update unread counts using functional update to avoid dependency loop
    setUnreadCounts(prev => {
      const newUnreadCounts = { ...prev };

      messages.forEach(message => {
        // Handle both 'chat' and 'command' messages that contain chat content
        if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
          const channelId = message.channel || extractChannelFromMessage(message.text) || selectedChannel;
          // Increment unread count for other channels
          if (channelId !== selectedChannel) {
            newUnreadCounts[channelId] = (newUnreadCounts[channelId] || 0) + 1;
          }
        }
      });

      return newUnreadCounts;
    });
  }, [messages, selectedChannel]); // Remove unreadCounts dependency

  const handleChatSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!chatInput.trim() || disabled || !isConnected) return;

    const message = chatInput.trim();

    // Check rate limiting
    if (!checkRateLimit()) {
      alert(`Please wait before sending another message. Rate limit: ${messageRateLimit} messages per minute.`);
      return;
    }

    // Check for spam
    if (isSpamMessage(message)) {
      alert('Message appears to be spam and has been blocked.');
      return;
    }

    // Add to input history
    setInputHistory(prev => [...prev, message]);

    // Send chat message
    onSendChatMessage(message, selectedChannel);

    // Clear input and reset history index
    setChatInput('');
    setHistoryIndex(-1);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex < inputHistory.length - 1) {
        const newIndex = historyIndex + 1;
        setHistoryIndex(newIndex);
        setChatInput(inputHistory[inputHistory.length - 1 - newIndex]);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setChatInput(inputHistory[inputHistory.length - 1 - newIndex]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setChatInput('');
      }
    } else if (e.key === 'Tab') {
      e.preventDefault();
      // Auto-complete channel shortcuts
      const channel = AVAILABLE_CHANNELS.find(c => c.id === selectedChannel);
      if (channel?.shortcut && !chatInput.startsWith(`/${channel.shortcut}`)) {
        setChatInput(`/${channel.shortcut} ${chatInput}`);
      }
    }
  };

  const handleInputChange = (value: string) => {
    setChatInput(value);

    // Show typing indicator
    if (value.trim() && !isTyping) {
      setIsTyping(true);
      setShowTypingIndicator(true);
    } else if (!value.trim() && isTyping) {
      setIsTyping(false);
      setShowTypingIndicator(false);
    }
  };

  // Hide typing indicator after delay
  useEffect(() => {
    if (showTypingIndicator) {
      const timer = setTimeout(() => {
        setShowTypingIndicator(false);
      }, 2000);
      return () => clearTimeout(timer);
    }
  }, [showTypingIndicator]);

  const handleQuickCommand = (command: string) => {
    setChatInput(command);
    // Focus will be handled by autoFocus prop
  };

  // Emote definitions
  const emotes = [
    { code: ':smile:', text: '😊', description: 'Happy smile' },
    { code: ':wave:', text: '👋', description: 'Friendly wave' },
    { code: ':laugh:', text: '😄', description: 'Laughing' },
    { code: ':wink:', text: '😉', description: 'Winking' },
    { code: ':sad:', text: '😢', description: 'Sad face' },
    { code: ':angry:', text: '😠', description: 'Angry face' },
    { code: ':surprised:', text: '😲', description: 'Surprised' },
    { code: ':cool:', text: '😎', description: 'Cool' },
    { code: ':heart:', text: '❤️', description: 'Heart' },
    { code: ':thumbsup:', text: '👍', description: 'Thumbs up' },
    { code: ':thumbsdown:', text: '👎', description: 'Thumbs down' },
    { code: ':clap:', text: '👏', description: 'Clapping' },
  ];

  // Formatting options
  const formattingOptions = [
    { code: '**text**', description: 'Bold text', example: '**bold**' },
    { code: '*text*', description: 'Italic text', example: '*italic*' },
    { code: '`text`', description: 'Code/monospace', example: '`code`' },
    { code: '~~text~~', description: 'Strikethrough', example: '~~strike~~' },
  ];

  const insertEmote = (emote: string) => {
    setChatInput(prev => prev + emote);
    setShowEmotePanel(false);
    inputRef.current?.focus();
  };

  const insertFormatting = (format: string) => {
    const selection = window.getSelection();
    if (selection && selection.toString()) {
      const selectedText = selection.toString();
      const formattedText = format.replace('text', selectedText);
      setChatInput(prev => prev.replace(selectedText, formattedText));
    } else {
      setChatInput(prev => prev + format);
    }
    setShowFormattingPanel(false);
    inputRef.current?.focus();
  };

  const getFontSizeClass = () => {
    switch (fontSize) {
      case 'small':
        return 'text-sm';
      case 'large':
        return 'text-lg';
      default:
        return 'text-base';
    }
  };

  const playNotificationSound = () => {
    if (soundEnabled) {
      // Simple beep sound using Web Audio API
      const audioContext = new (window.AudioContext ||
        (window as { webkitAudioContext?: typeof AudioContext }).webkitAudioContext)();
      const oscillator = audioContext.createOscillator();
      const gainNode = audioContext.createGain();

      oscillator.connect(gainNode);
      gainNode.connect(audioContext.destination);

      oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);

      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.1);
    }
  };

  // Moderation functions
  const addIgnoredUser = (username: string) => {
    if (!ignoredUsers.includes(username)) {
      setIgnoredUsers(prev => [...prev, username]);
    }
  };

  const removeIgnoredUser = (username: string) => {
    setIgnoredUsers(prev => prev.filter(user => user !== username));
  };

  const isUserIgnored = (username: string) => {
    return ignoredUsers.includes(username);
  };

  const isSpamMessage = (message: string) => {
    if (!spamFilterEnabled) return false;

    // Simple spam detection: repeated characters, excessive caps, common spam patterns
    const repeatedChars = /(.)\1{4,}/; // 5+ repeated characters
    const excessiveCaps = /[A-Z]{10,}/; // 10+ consecutive caps
    const spamPatterns = /\b(buy|sell|click|free|money|casino|pills|viagra)\b/i;

    return repeatedChars.test(message) || excessiveCaps.test(message) || spamPatterns.test(message);
  };

  const checkRateLimit = () => {
    const now = Date.now();
    const timeSinceLastMessage = now - lastMessageTime;
    const minInterval = (60 * 1000) / messageRateLimit; // Convert to milliseconds

    if (timeSinceLastMessage < minInterval) {
      return false;
    }

    setLastMessageTime(now);
    return true;
  };

  // Filter messages based on moderation settings
  const getFilteredMessages = () => {
    return messages.filter(message => {
      // Filter out ignored users
      if (message.aliasChain && message.aliasChain.length > 0) {
        const username = message.aliasChain[0].original.split(' ')[0]; // Extract username
        if (isUserIgnored(username)) {
          return false;
        }
      }

      // Filter out spam messages
      if (isSpamMessage(message.text)) {
        return false;
      }

      return true;
    });
  };

  // Export and backup functions
  const exportChatLog = (format: 'txt' | 'json' | 'html') => {
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const filename = `mythosmud-chat-${timestamp}`;

    let content = '';
    let mimeType = '';

    switch (format) {
      case 'txt':
        content = getFilteredMessages()
          .map(message => `[${message.timestamp}] ${message.text}`)
          .join('\n');
        mimeType = 'text/plain';
        break;

      case 'json':
        content = JSON.stringify(getFilteredMessages(), null, 2);
        mimeType = 'application/json';
        break;

      case 'html':
        content = `
          <!DOCTYPE html>
          <html>
          <head>
            <title>MythosMUD Chat Log</title>
            <style>
              body { font-family: monospace; background: #0a0a0a; color: #00ff00; padding: 20px; }
              .message { margin-bottom: 10px; }
              .timestamp { color: #888; }
            </style>
          </head>
          <body>
            <h1>MythosMUD Chat Log</h1>
            <p>Exported on: ${new Date().toLocaleString()}</p>
            ${getFilteredMessages()
              .map(
                message => `
                <div class="message">
                  <span class="timestamp">[${message.timestamp}]</span>
                  <span>${message.text}</span>
                </div>
              `
              )
              .join('')}
          </body>
          </html>
        `;
        mimeType = 'text/html';
        break;
    }

    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${filename}.${format}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const backupChatSettings = () => {
    const settings = {
      fontSize,
      soundEnabled,
      notificationsEnabled,
      ignoredUsers,
      spamFilterEnabled,
      messageRateLimit,
      exportFormat,
      timestamp: new Date().toISOString(),
    };

    const content = JSON.stringify(settings, null, 2);
    const blob = new Blob([content], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `mythosmud-chat-settings-${new Date().toISOString().replace(/[:.]/g, '-')}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const importChatSettings = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = e => {
      try {
        const settings = JSON.parse(e.target?.result as string);
        if (settings.fontSize) setFontSize(settings.fontSize);
        if (settings.soundEnabled !== undefined) setSoundEnabled(settings.soundEnabled);
        if (settings.notificationsEnabled !== undefined) setNotificationsEnabled(settings.notificationsEnabled);
        if (settings.ignoredUsers) setIgnoredUsers(settings.ignoredUsers);
        if (settings.spamFilterEnabled !== undefined) setSpamFilterEnabled(settings.spamFilterEnabled);
        if (settings.messageRateLimit) setMessageRateLimit(settings.messageRateLimit);
        if (settings.exportFormat) setExportFormat(settings.exportFormat);
        alert('Chat settings imported successfully!');
      } catch {
        alert('Failed to import settings. Invalid file format.');
      }
    };
    reader.readAsText(file);
  };

  const handleChannelSelect = (channelId: string) => {
    // Clear unread count when switching to a channel
    setUnreadCounts(prev => ({ ...prev, [channelId]: 0 }));
    onChannelSelect?.(channelId);
  };

  const getActivityLevel = (channelId: string): 'high' | 'medium' | 'low' | 'none' => {
    const activity = channelActivity[channelId];
    if (!activity) return 'none';

    const now = new Date();
    const minutesSinceLastActivity = (now.getTime() - activity.lastActivity.getTime()) / (1000 * 60);

    if (minutesSinceLastActivity <= 1) return 'high';
    if (minutesSinceLastActivity <= 5) return 'medium';
    if (minutesSinceLastActivity <= 15) return 'low';
    return 'none';
  };

  const getActivityColor = (level: 'high' | 'medium' | 'low' | 'none'): string => {
    switch (level) {
      case 'high':
        return 'bg-mythos-terminal-success';
      case 'medium':
        return 'bg-mythos-terminal-warning';
      case 'low':
        return 'bg-mythos-terminal-secondary';
      default:
        return 'bg-gray-600';
    }
  };

  // Filter messages by channel and moderation settings
  const filteredMessages = getFilteredMessages().filter(message => {
    // Debug logging for message filtering
    if (process.env.NODE_ENV === 'development') {
      console.log('🔍 ChatPanel Message Filtering:', {
        messageText: message.text.substring(0, 50) + (message.text.length > 50 ? '...' : ''),
        messageType: message.messageType,
        messageChannel: message.channel,
        chatFilter: chatFilter,
        selectedChannel: selectedChannel,
        isChatContent: isChatContent(message.text),
        willShow:
          chatFilter === 'all' ||
          (chatFilter === 'current' &&
            (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text)))),
        timestamp: message.timestamp,
      });
    }

    if (chatFilter === 'all') return true;
    if (chatFilter === 'current') {
      // Filter for current channel messages - handle both 'chat' and 'command' messages with chat content
      const isChatMessage =
        message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text));

      // If it's a chat message, also check if it belongs to the current channel
      if (isChatMessage) {
        const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
        return messageChannel === selectedChannel;
      }

      return false;
    }
    return true;
  });

  // Debug logging for final filtered messages
  console.log('🔍 ChatPanel Final Filtered Messages:', {
    totalMessages: messages.length,
    filteredCount: filteredMessages.length,
    chatFilter,
    selectedChannel,
    filteredMessages: filteredMessages.map(m => ({
      text: m.text.substring(0, 50) + (m.text.length > 50 ? '...' : ''),
      messageType: m.messageType,
      channel: m.channel,
      timestamp: m.timestamp,
    })),
    timestamp: new Date().toISOString(),
  });

  // Calculate chat statistics
  const chatStats = {
    totalMessages: messages.length,
    currentChannelMessages: filteredMessages.length,
    inputHistoryCount: inputHistory.length,
    currentChannelActivity: getActivityLevel(selectedChannel),
    totalUnread: Object.values(unreadCounts).reduce((sum, count) => sum + count, 0),
  };

  const getChannelQuickCommands = () => {
    const channel = AVAILABLE_CHANNELS.find(c => c.id === selectedChannel);
    if (!channel || channel.disabled) return [];

    return [
      {
        command: `/${channel.shortcut} Hello!`,
        icon: channel.icon,
        description: `Send greeting to ${channel.name} channel`,
      },
      {
        command: `/${channel.shortcut} How is everyone?`,
        icon: channel.icon,
        description: `Greet ${channel.name} channel`,
      },
      {
        command: `/${channel.shortcut} Goodbye!`,
        icon: channel.icon,
        description: `Say goodbye to ${channel.name} channel`,
      },
    ];
  };

  const commonQuickCommands = [
    { command: 'Hello everyone!', icon: MythosIcons.chat, description: 'General greeting', category: 'greetings' },
    {
      command: 'How is everyone doing?',
      icon: MythosIcons.chat,
      description: 'Check on players',
      category: 'greetings',
    },
    { command: 'Goodbye!', icon: MythosIcons.chat, description: 'Farewell message', category: 'farewells' },
    { command: 'Thanks!', icon: MythosIcons.chat, description: 'Thank you message', category: 'courtesy' },
    { command: 'Nice to meet you!', icon: MythosIcons.chat, description: 'Introduction', category: 'greetings' },
    { command: 'See you later!', icon: MythosIcons.chat, description: 'Casual goodbye', category: 'farewells' },
    { command: "You're welcome!", icon: MythosIcons.chat, description: 'Response to thanks', category: 'courtesy' },
    { command: 'Excuse me', icon: MythosIcons.chat, description: 'Get attention', category: 'courtesy' },
  ];

  const getQuickCommandsByCategory = () => {
    const categories = {
      greetings: commonQuickCommands.filter(cmd => cmd.category === 'greetings'),
      courtesy: commonQuickCommands.filter(cmd => cmd.category === 'courtesy'),
      farewells: commonQuickCommands.filter(cmd => cmd.category === 'farewells'),
    };
    return categories;
  };

  const formatTimestamp = (timestamp: string): string => {
    try {
      const date = new Date(timestamp);
      return date.toLocaleTimeString('en-US', {
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    } catch {
      return timestamp;
    }
  };

  const getMessageClass = (messageType?: string): string => {
    switch (messageType) {
      case 'emote':
        return 'text-mythos-terminal-primary italic';
      case 'system':
        return 'text-mythos-terminal-warning font-bold';
      case 'error':
        return 'text-mythos-terminal-error font-bold';
      case 'whisper':
        return 'text-mythos-terminal-secondary italic';
      case 'shout':
        return 'text-mythos-terminal-warning font-bold';
      default:
        return 'text-mythos-terminal-text';
    }
  };

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Chat</h3>
        </div>
        <div className="flex items-center gap-2">
          {onClearMessages && (
            <TerminalButton variant="secondary" size="sm" onClick={onClearMessages} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
            </TerminalButton>
          )}
          {onDownloadLogs && (
            <TerminalButton variant="secondary" size="sm" onClick={onDownloadLogs} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.download} size={14} variant="primary" />
            </TerminalButton>
          )}
        </div>
      </div>

      {/* Channel Selector */}
      <div
        className="p-3 border-b border-gray-700 bg-mythos-terminal-surface"
        role="region"
        aria-label="Channel Selection"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-2">
          <span className="text-sm text-mythos-terminal-text-secondary font-mono">Channel:</span>
          <ChannelSelector
            channels={AVAILABLE_CHANNELS}
            selectedChannel={selectedChannel}
            onChannelSelect={handleChannelSelect}
            disabled={disabled || !isConnected}
            className="flex-1 w-full sm:w-auto"
          />
        </div>

        {/* Channel Activity Indicators */}
        <div
          className="flex flex-col sm:flex-row items-start sm:items-center gap-2 sm:gap-4 mt-2"
          role="region"
          aria-label="Channel Activity Indicators"
        >
          <span className="text-xs text-mythos-terminal-text-secondary">Activity:</span>
          <div className="flex flex-wrap items-center gap-2">
            {AVAILABLE_CHANNELS.map(channel => {
              const activityLevel = getActivityLevel(channel.id);
              const unreadCount = unreadCounts[channel.id] || 0;

              return (
                <div
                  key={channel.id}
                  className="flex items-center gap-1 group cursor-pointer hover:bg-mythos-terminal-background/50 rounded px-1 transition-all duration-200"
                  role="button"
                  tabIndex={0}
                  aria-label={`${channel.name} channel - ${activityLevel} activity${unreadCount > 0 ? `, ${unreadCount} unread messages` : ''}`}
                  onKeyDown={e => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      handleChannelSelect(channel.id);
                    }
                  }}
                >
                  <div
                    className={`w-2 h-2 rounded-full ${getActivityColor(activityLevel)} transition-all duration-300 ${activityLevel === 'high' ? 'animate-pulse' : ''}`}
                  ></div>
                  <span className="text-xs text-mythos-terminal-text-secondary group-hover:text-mythos-terminal-primary transition-colors duration-200">
                    {channel.name}
                  </span>
                  {unreadCount > 0 && (
                    <div className="bg-mythos-terminal-error text-white text-xs rounded-full px-1 min-w-[16px] h-4 flex items-center justify-center animate-bounce">
                      {unreadCount > 99 ? '99+' : unreadCount}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Chat Input Area */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface" role="region" aria-label="Chat Input">
        <form onSubmit={handleChatSubmit} className="space-y-3">
          {/* Input Controls */}
          <div className="flex flex-wrap items-center gap-2 mb-2">
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setShowEmotePanel(!showEmotePanel)}
              className="flex items-center gap-1 text-xs"
              aria-label={`${showEmotePanel ? 'Hide' : 'Show'} emote panel`}
              aria-expanded={showEmotePanel}
            >
              <span>😊</span>
              <span className="hidden sm:inline">Emotes</span>
            </TerminalButton>
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setShowFormattingPanel(!showFormattingPanel)}
              className="flex items-center gap-1 text-xs"
              aria-label={`${showFormattingPanel ? 'Hide' : 'Show'} formatting panel`}
              aria-expanded={showFormattingPanel}
            >
              <EldritchIcon name={MythosIcons.system} size={12} variant="primary" />
              <span className="hidden sm:inline">Format</span>
            </TerminalButton>
            <TerminalButton
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setShowSettingsPanel(!showSettingsPanel)}
              className="flex items-center gap-1 text-xs"
              aria-label={`${showSettingsPanel ? 'Hide' : 'Show'} settings panel`}
              aria-expanded={showSettingsPanel}
            >
              <EldritchIcon name={MythosIcons.system} size={12} variant="primary" />
              <span className="hidden sm:inline">Settings</span>
            </TerminalButton>
          </div>

          {/* Emote Panel */}
          {showEmotePanel && (
            <div
              className="p-2 bg-mythos-terminal-background border border-gray-700 rounded mb-2"
              role="region"
              aria-label="Emote Selection"
            >
              <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-2">
                {emotes.map(emote => (
                  <TerminalButton
                    key={emote.code}
                    type="button"
                    variant="secondary"
                    size="sm"
                    onClick={() => insertEmote(emote.text)}
                    className="flex items-center justify-center text-sm p-2 hover:scale-110 transition-all duration-200"
                  >
                    {emote.text}
                  </TerminalButton>
                ))}
              </div>
            </div>
          )}

          {/* Formatting Panel */}
          {showFormattingPanel && (
            <div
              className="p-2 bg-mythos-terminal-background border border-gray-700 rounded mb-2"
              role="region"
              aria-label="Text Formatting Options"
            >
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {formattingOptions.map(format => (
                  <TerminalButton
                    key={format.code}
                    type="button"
                    variant="secondary"
                    size="sm"
                    onClick={() => insertFormatting(format.code)}
                    className="flex items-center gap-1 text-xs"
                  >
                    <span className="font-mono">{format.example}</span>
                  </TerminalButton>
                ))}
              </div>
            </div>
          )}

          {/* Settings Panel */}
          {showSettingsPanel && (
            <div
              className="p-3 bg-mythos-terminal-background border border-gray-700 rounded mb-2"
              role="region"
              aria-label="Chat Settings"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Font Size:</span>
                  <select
                    value={fontSize}
                    onChange={e => setFontSize(e.target.value as 'small' | 'medium' | 'large')}
                    className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-sm"
                  >
                    <option value="small">Small</option>
                    <option value="medium">Medium</option>
                    <option value="large">Large</option>
                  </select>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Sound Notifications:</span>
                  <input
                    type="checkbox"
                    checked={soundEnabled}
                    onChange={e => setSoundEnabled(e.target.checked)}
                    className="w-4 h-4"
                  />
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Desktop Notifications:</span>
                  <input
                    type="checkbox"
                    checked={notificationsEnabled}
                    onChange={e => setNotificationsEnabled(e.target.checked)}
                    className="w-4 h-4"
                  />
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Spam Filter:</span>
                  <input
                    type="checkbox"
                    checked={spamFilterEnabled}
                    onChange={e => setSpamFilterEnabled(e.target.checked)}
                    className="w-4 h-4"
                  />
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-mythos-terminal-text-secondary">Message Rate Limit:</span>
                  <select
                    value={messageRateLimit}
                    onChange={e => setMessageRateLimit(Number(e.target.value))}
                    className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-sm"
                  >
                    <option value={3}>3 per minute</option>
                    <option value={5}>5 per minute</option>
                    <option value={10}>10 per minute</option>
                    <option value={20}>20 per minute</option>
                  </select>
                </div>
                <div className="flex gap-2">
                  <TerminalButton
                    type="button"
                    variant="secondary"
                    size="sm"
                    onClick={() => {
                      if ('Notification' in window) {
                        Notification.requestPermission();
                      }
                    }}
                    className="flex-1 text-xs"
                  >
                    Request Notification Permission
                  </TerminalButton>
                  <TerminalButton
                    type="button"
                    variant="secondary"
                    size="sm"
                    onClick={playNotificationSound}
                    className="flex-1 text-xs"
                  >
                    Test Sound
                  </TerminalButton>
                </div>

                {/* Ignored Users Management */}
                <div className="border-t border-gray-600 pt-3">
                  <h4 className="text-sm font-bold text-mythos-terminal-text-primary mb-2">Ignored Users</h4>
                  <div className="space-y-2">
                    {ignoredUsers.length === 0 ? (
                      <p className="text-xs text-mythos-terminal-text-secondary">No ignored users</p>
                    ) : (
                      ignoredUsers.map(user => (
                        <div
                          key={user}
                          className="flex items-center justify-between bg-mythos-terminal-background p-2 rounded"
                        >
                          <span className="text-xs text-mythos-terminal-text-secondary">{user}</span>
                          <TerminalButton
                            type="button"
                            variant="secondary"
                            size="sm"
                            onClick={() => removeIgnoredUser(user)}
                            className="text-xs px-2 py-1"
                          >
                            Unignore
                          </TerminalButton>
                        </div>
                      ))
                    )}
                  </div>
                </div>

                {/* Export and Backup */}
                <div className="border-t border-gray-600 pt-3">
                  <h4 className="text-sm font-bold text-mythos-terminal-text-primary mb-2">Export & Backup</h4>
                  <div className="space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="text-sm text-mythos-terminal-text-secondary">Export Format:</span>
                      <select
                        value={exportFormat}
                        onChange={e => setExportFormat(e.target.value as 'txt' | 'json' | 'html')}
                        className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-sm"
                      >
                        <option value="txt">Text (.txt)</option>
                        <option value="json">JSON (.json)</option>
                        <option value="html">HTML (.html)</option>
                      </select>
                    </div>
                    <div className="flex gap-2">
                      <TerminalButton
                        type="button"
                        variant="secondary"
                        size="sm"
                        onClick={() => exportChatLog(exportFormat)}
                        className="flex-1 text-xs"
                      >
                        Export Chat Log
                      </TerminalButton>
                      <TerminalButton
                        type="button"
                        variant="secondary"
                        size="sm"
                        onClick={backupChatSettings}
                        className="flex-1 text-xs"
                      >
                        Backup Settings
                      </TerminalButton>
                    </div>
                    <div className="flex gap-2">
                      <label className="flex-1">
                        <input type="file" accept=".json" onChange={importChatSettings} className="hidden" />
                        <TerminalButton
                          type="button"
                          variant="secondary"
                          size="sm"
                          className="w-full text-xs"
                          onClick={() => (document.querySelector('input[type="file"]') as HTMLInputElement)?.click()}
                        >
                          Import Settings
                        </TerminalButton>
                      </label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}

          <div className="flex flex-col sm:flex-row gap-2">
            <div className="flex-1 relative">
              <TerminalInput
                value={chatInput}
                onChange={handleInputChange}
                onKeyDown={handleKeyDown}
                placeholder="Type your message here..."
                disabled={disabled || !isConnected}
                className="w-full transition-all duration-200 focus:ring-2 focus:ring-mythos-terminal-primary/50"
                autoFocus={true}
              />
              {showTypingIndicator && (
                <div className="absolute -bottom-6 left-0 text-xs text-mythos-terminal-secondary animate-pulse">
                  <EldritchIcon name={MythosIcons.chat} size={12} className="mr-1" />
                  Typing...
                </div>
              )}
            </div>
            <TerminalButton
              type="submit"
              variant="primary"
              disabled={!chatInput.trim() || disabled || !isConnected}
              className="px-4 transition-all duration-200 hover:scale-105 disabled:hover:scale-100"
            >
              <EldritchIcon name={MythosIcons.chat} size={16} className="mr-2" />
              <span className="hidden sm:inline">Send</span>
            </TerminalButton>
          </div>
        </form>
      </div>

      {/* Quick Chat Commands */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <EldritchIcon name={MythosIcons.move} size={14} variant="primary" />
            <span className="text-sm text-mythos-terminal-text-secondary font-bold">Quick Commands:</span>
          </div>

          {/* Categorized Quick Commands */}
          {Object.entries(getQuickCommandsByCategory()).map(([category, commands]) => (
            <div key={category} className="space-y-2">
              <div className="flex items-center gap-2">
                <EldritchIcon name={MythosIcons.chat} size={12} variant="primary" />
                <span className="text-xs text-mythos-terminal-text-secondary font-bold capitalize">{category}:</span>
              </div>
              <div className="grid grid-cols-2 gap-2">
                {commands.map(({ command, icon }) => (
                  <TerminalButton
                    key={command}
                    variant="secondary"
                    size="sm"
                    onClick={() => handleQuickCommand(command)}
                    disabled={disabled || !isConnected}
                    className="flex items-center gap-2 text-xs transition-all duration-200 hover:scale-105 hover:shadow-lg disabled:hover:scale-100"
                  >
                    <EldritchIcon name={icon} size={12} variant="primary" />
                    <span className="truncate">{command}</span>
                  </TerminalButton>
                ))}
              </div>
            </div>
          ))}

          {/* Channel-specific quick commands */}
          {getChannelQuickCommands().length > 0 && (
            <>
              <div className="flex items-center gap-2 mt-4">
                <EldritchIcon name={MythosIcons.chat} size={14} variant="primary" />
                <span className="text-sm text-mythos-terminal-text-secondary font-bold">
                  {AVAILABLE_CHANNELS.find(c => c.id === selectedChannel)?.name} Channel:
                </span>
              </div>
              <div className="grid grid-cols-1 gap-2">
                {getChannelQuickCommands().map(({ command, icon }) => (
                  <TerminalButton
                    key={command}
                    variant="secondary"
                    size="sm"
                    onClick={() => handleQuickCommand(command)}
                    disabled={disabled || !isConnected}
                    className="flex items-center gap-2 text-xs"
                  >
                    <EldritchIcon name={icon} size={12} variant="primary" />
                    <span className="truncate">{command}</span>
                  </TerminalButton>
                ))}
              </div>
            </>
          )}

          <div className="text-xs text-mythos-terminal-text-secondary">
            <span className="font-bold">Tip:</span> Use Tab for channel shortcuts, ↑↓ for history navigation
          </div>
        </div>
      </div>

      {/* Chat History Toggle */}
      <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={() => setShowChatHistory(!showChatHistory)}
              className="flex items-center gap-2 text-xs"
            >
              <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
              <span>Chat History</span>
            </TerminalButton>
            <select
              value={chatFilter}
              onChange={e => setChatFilter(e.target.value)}
              className="bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text"
            >
              <option value="all">All Messages</option>
              <option value="current">Current Channel</option>
            </select>
          </div>
          <div className="text-xs text-mythos-terminal-text-secondary">{chatStats.currentChannelMessages} messages</div>
        </div>
      </div>

      {/* Chat Messages Display */}
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        {filteredMessages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center space-y-2">
              <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
              <p className="text-mythos-terminal-text-secondary text-sm">
                No messages yet. Start chatting to see messages here.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {filteredMessages.map((message, index) => (
              <div
                key={index}
                className="p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30 hover:shadow-lg animate-fade-in"
                style={{ animationDelay: `${index * 50}ms` }}
              >
                {/* Alias Expansion Information */}
                {message.aliasChain && message.aliasChain.length > 0 && (
                  <div className="mb-3 p-2 bg-mythos-terminal-background border border-mythos-terminal-primary/50 rounded text-xs">
                    <div className="flex items-center gap-2 mb-2">
                      <EldritchIcon name={MythosIcons.move} size={12} variant="warning" />
                      <span className="text-mythos-terminal-warning font-bold">Alias Expansion:</span>
                    </div>
                    <div className="space-y-1">
                      {message.aliasChain.map((alias, chainIndex) => (
                        <div key={chainIndex} className="flex items-center gap-2">
                          <span className="text-mythos-terminal-warning font-bold">{alias.original}</span>
                          <EldritchIcon name={MythosIcons.exit} size={10} variant="primary" />
                          <span className="text-mythos-terminal-success italic">{alias.expanded}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Message Timestamp */}
                <div className="mb-2">
                  <span className="text-xs text-mythos-terminal-text-secondary font-mono">
                    {formatTimestamp(message.timestamp)}
                  </span>
                </div>

                {/* Message Content */}
                <div
                  className={`${getFontSizeClass()} leading-relaxed ${getMessageClass(message.messageType)}`}
                  dangerouslySetInnerHTML={{
                    __html: message.isHtml
                      ? message.isCompleteHtml
                        ? message.text
                        : ansiToHtmlWithBreaks(message.text)
                      : message.text,
                  }}
                  onContextMenu={e => {
                    e.preventDefault();
                    const username = message.aliasChain?.[0]?.original.split(' ')[0];
                    if (username && !isUserIgnored(username)) {
                      if (confirm(`Ignore messages from ${username}?`)) {
                        addIgnoredUser(username);
                      }
                    }
                  }}
                  title="Right-click to ignore user"
                />
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Chat Statistics */}
      <div
        className="p-2 border-t border-gray-700 bg-mythos-terminal-surface"
        role="status"
        aria-label="Chat Statistics"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs text-mythos-terminal-text-secondary gap-2 sm:gap-0">
          <div className="flex flex-wrap items-center gap-2 sm:gap-4">
            <div className="flex items-center gap-1">
              <div className="w-2 h-2 bg-mythos-terminal-success rounded-full"></div>
              <span>Connected</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.chat} size={12} variant="secondary" />
              <span>{chatStats.currentChannelMessages} messages</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.connection} size={12} variant="secondary" />
              <span>Channel: {AVAILABLE_CHANNELS.find(c => c.id === selectedChannel)?.name}</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.clock} size={12} variant="secondary" />
              <span>{chatStats.inputHistoryCount} sent</span>
            </div>
            <div className="flex items-center gap-1">
              <div className={`w-2 h-2 rounded-full ${getActivityColor(chatStats.currentChannelActivity)}`}></div>
              <span>Activity: {chatStats.currentChannelActivity}</span>
            </div>
            {chatStats.totalUnread > 0 && (
              <div className="flex items-center gap-1">
                <EldritchIcon name={MythosIcons.chat} size={12} variant="error" />
                <span>{chatStats.totalUnread} unread</span>
              </div>
            )}
          </div>
          <div className="text-xs opacity-75">MythosMUD Terminal</div>
        </div>
      </div>
    </div>
  );
};
