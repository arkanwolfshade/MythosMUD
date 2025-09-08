// Temporarily commented out due to MUI dependencies
// This component will be migrated to TailwindCSS in a future phase

/*
import React, { useState } from 'react';
import {
  Drawer,
  Box,
  Typography,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Collapse,
  Chip,
  Divider,
} from '@mui/material';
import {
  ExpandLess,
  ExpandMore,
  Help as HelpIcon,
  Visibility as LookIcon,
  DirectionsWalk as GoIcon,
  Chat as SayIcon,
  Settings,
  Group as WhoIcon,
  List as ListIcon,
  VolumeOff as MuteIcon,
  VolumeUp as UnmuteIcon,
} from '@mui/icons-material';

// Custom icon components (these would need to be replaced with Lucide icons)
const EmoteIcon = () => <span>😊</span>;
const AliasIcon = () => <span>🔗</span>;
const HelpCommandIcon = () => <span>❓</span>;

interface Command {
  name: string;
  description: string;
  syntax: string;
  examples: string[];
  category: string;
  icon: React.ReactNode;
}

const commands: Command[] = [
  {
    name: 'look',
    description: 'Look around the current room or at a specific object',
    syntax: 'look [target]',
    examples: ['look', 'look north', 'look at the door'],
    category: 'Exploration',
    icon: <LookIcon />,
  },
  {
    name: 'north/south/east/west',
    description: 'Move in the specified direction',
    syntax: 'north|south|east|west',
    examples: ['north', 's', 'east'],
    category: 'Movement',
    icon: <GoIcon />,
  },
  {
    name: 'say',
    description: 'Speak to everyone in the room',
    syntax: 'say <message>',
    examples: ['say Hello everyone!', 'say "How are you?"'],
    category: 'Communication',
    icon: <SayIcon />,
  },
  {
    name: 'emote',
    description: 'Perform an action or emotion',
    syntax: 'emote <action>',
    examples: ['emote smiles warmly', 'emote looks around nervously'],
    category: 'Communication',
    icon: <EmoteIcon />,
  },
  {
    name: 'whisper',
    description: 'Send a private message to another player',
    syntax: 'whisper <player> <message>',
    examples: ['whisper ArkanWolfshade Hello!', 'whisper "John Doe" "How are you?"'],
    category: 'Communication',
    icon: <EmoteIcon />,
  },
  {
    name: 'reply',
    description: 'Reply to the last whisper received',
    syntax: 'reply <message>',
    examples: ['reply Hello back!', 'reply "Thanks for the info"'],
    category: 'Communication',
    icon: <EmoteIcon />,
  },
  {
    name: 'shout',
    description: 'Shout a message to all connected players',
    syntax: 'shout <message>',
    examples: ['shout "Anyone want to group up?"', 'shout Hello everyone!'],
    category: 'Communication',
    icon: <EmoteIcon />,
  },
  {
    name: 'alias',
    description: 'Create a shortcut for a command',
    syntax: 'alias <shortcut> <command>',
    examples: ['alias n north', 'alias "look door" "look at the door"'],
    category: 'System',
    icon: <AliasIcon />,
  },
  {
    name: 'help',
    description: 'Get help on a specific command',
    syntax: 'help [command]',
    examples: ['help', 'help look', 'help movement'],
    category: 'System',
    icon: <HelpCommandIcon />,
  },
  {
    name: 'who',
    description: 'See who is currently online',
    syntax: 'who',
    examples: ['who'],
    category: 'Information',
    icon: <WhoIcon />,
  },
  {
    name: 'inventory',
    description: 'Check your inventory',
    syntax: 'inventory',
    examples: ['inventory', 'i'],
    category: 'Information',
    icon: <ListIcon />,
  },
  {
    name: 'mute',
    description: 'Mute a specific player or channel',
    syntax: 'mute <target>',
    examples: ['mute ArkanWolfshade', 'mute chat'],
    category: 'System',
    icon: <MuteIcon />,
  },
  {
    name: 'unmute',
    description: 'Unmute a previously muted player or channel',
    syntax: 'unmute <target>',
    examples: ['unmute ArkanWolfshade', 'unmute chat'],
    category: 'System',
    icon: <UnmuteIcon />,
  },
];

interface CommandHelpDrawerProps {
  open: boolean;
  onClose: () => void;
}

export const CommandHelpDrawer: React.FC<CommandHelpDrawerProps> = ({ open, onClose }) => {
  const [expandedCategory, setExpandedCategory] = useState<string | null>(null);

  const handleCategoryClick = (category: string) => {
    setExpandedCategory(expandedCategory === category ? null : category);
  };

  const categories = Array.from(new Set(commands.map(cmd => cmd.category)));

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      PaperProps={{
        sx: {
          width: 400,
          bgcolor: 'background.paper',
        },
      }}
    >
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
          <Typography variant="h6" component="h2">
            <HelpIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
            Command Help
          </Typography>
          <IconButton onClick={onClose} size="small">
            <ExpandLess />
          </IconButton>
        </Box>

        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Browse available commands by category. Click on a category to expand and see detailed information.
        </Typography>

        <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
          {categories.map((category) => {
            const categoryCommands = commands.filter(cmd => cmd.category === category);
            const isExpanded = expandedCategory === category;

            return (
              <React.Fragment key={category}>
                <ListItem disablePadding>
                  <ListItemButton onClick={() => handleCategoryClick(category)}>
                    <ListItemIcon>
                      {category === 'Exploration' && <LookIcon />}
                      {category === 'Movement' && <GoIcon />}
                      {category === 'Communication' && <SayIcon />}
                      {category === 'Information' && <WhoIcon />}
                      {category === 'System' && <Settings />}
                    </ListItemIcon>
                    <ListItemText
                      primary={category}
                      primaryTypographyProps={{ fontWeight: 'bold' }}
                    />
                    {isExpanded ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </ListItem>

                <Collapse in={isExpanded} timeout="auto" unmountOnExit>
                  <List component="div" disablePadding>
                    {categoryCommands.map((command) => (
                      <ListItem key={command.name} sx={{ pl: 4 }}>
                        <Box sx={{ width: '100%' }}>
                          <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                            <ListItemIcon sx={{ minWidth: 36 }}>{command.icon}</ListItemIcon>
                            <Typography variant="subtitle2" component="span" sx={{ fontWeight: 'bold' }}>
                              {command.name}
                            </Typography>
                            <Chip
                              label={command.category}
                              size="small"
                              sx={{ ml: 'auto', fontSize: '0.7rem' }}
                            />
                          </Box>

                          <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                            {command.description}
                          </Typography>

                          <Box>
                            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>
                              Syntax:
                            </Typography>
                            <Chip
                              label={command.syntax}
                              size="small"
                              variant="outlined"
                              sx={{ fontSize: '0.7rem', mb: 1 }}
                            />

                            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>
                              Examples:
                            </Typography>
                            {command.examples.map((example, index) => (
                              <Chip
                                key={index}
                                label={example}
                                size="small"
                                variant="outlined"
                                sx={{ fontSize: '0.7rem', mr: 0.5, mb: 0.5 }}
                              />
                            ))}
                          </Box>
                        </Box>
                      </ListItem>
                    ))}
                  </List>
                </Collapse>
                <Divider />
              </React.Fragment>
            );
          })}
        </List>
      </Box>
    </Drawer>
  );
};
*/

export const CommandHelpDrawer: React.FC<{ open: boolean; onClose: () => void }> = () => {
  return <div>Command Help (Coming Soon)</div>;
};
