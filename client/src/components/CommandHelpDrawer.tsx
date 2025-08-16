import {
  Settings as AliasIcon,
  ExpandLess,
  ExpandMore,
  DirectionsWalk as GoIcon,
  Info as HelpCommandIcon,
  Help as HelpIcon,
  List as ListIcon,
  Visibility as LookIcon,
  VolumeOff as MuteIcon,
  Chat as SayIcon,
  Settings,
  VolumeUp as UnmuteIcon,
  Person as WhoIcon,
} from '@mui/icons-material';
import {
  Box,
  Chip,
  Collapse,
  Divider,
  Drawer,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from '@mui/material';
import React, { useState } from 'react';

interface Command {
  name: string;
  category: string;
  description: string;
  usage: string;
  examples: string[];
  icon: React.ReactNode;
}

const commands: Command[] = [
  {
    name: 'look',
    category: 'Exploration',
    description: 'Examine your surroundings or look in a specific direction',
    usage: 'look [direction]',
    examples: ['look', 'look north', 'look east'],
    icon: <LookIcon />,
  },
  {
    name: 'go',
    category: 'Movement',
    description: 'Move in a specific direction',
    usage: 'go <direction>',
    examples: ['go north', 'go south', 'go east', 'go west'],
    icon: <GoIcon />,
  },
  {
    name: 'say',
    category: 'Communication',
    description: 'Speak to other players in the room',
    usage: 'say <message>',
    examples: ['say Hello everyone!', 'say How are you?'],
    icon: <SayIcon />,
  },
  {
    name: 'alias',
    category: 'System',
    description: 'Create shortcuts for commonly used commands',
    usage: 'alias <shortcut> <command>',
    examples: ['alias n go north', 'alias s go south'],
    icon: <AliasIcon />,
  },
  {
    name: 'help',
    category: 'System',
    description: 'Get detailed help for a specific command',
    usage: 'help [command]',
    examples: ['help', 'help look', 'help go'],
    icon: <HelpCommandIcon />,
  },
  {
    name: 'who',
    category: 'Information',
    description: 'See who is currently online',
    usage: 'who',
    examples: ['who'],
    icon: <WhoIcon />,
  },
  {
    name: 'mutes',
    category: 'Communication',
    description: 'View your current mute list',
    usage: 'mutes',
    examples: ['mutes'],
    icon: <ListIcon />,
  },
  {
    name: 'mute',
    category: 'Communication',
    description: 'Mute a player (personal or global if admin)',
    usage: 'mute <player>',
    examples: ['mute PlayerName'],
    icon: <MuteIcon />,
  },
  {
    name: 'unmute',
    category: 'Communication',
    description: 'Unmute a previously muted player',
    usage: 'unmute <player>',
    examples: ['unmute PlayerName'],
    icon: <UnmuteIcon />,
  },
];

const categories = ['Exploration', 'Movement', 'Communication', 'Information', 'System'];

interface CommandHelpDrawerProps {
  open: boolean;
  onClose: () => void;
}

export function CommandHelpDrawer({ open, onClose }: CommandHelpDrawerProps) {
  const [expandedCategory, setExpandedCategory] = useState<string | null>(null);

  const handleCategoryClick = (category: string) => {
    setExpandedCategory(expandedCategory === category ? null : category);
  };

  const getCommandsByCategory = (category: string) => {
    return commands.filter(cmd => cmd.category === category);
  };

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      sx={{
        '& .MuiDrawer-paper': {
          width: 400,
          maxWidth: '90vw',
        },
      }}
    >
      <Box sx={{ p: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
          <Typography variant="h6" component="h2">
            <HelpIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
            Command Reference
          </Typography>
          <IconButton onClick={onClose} size="small">
            <ExpandLess />
          </IconButton>
        </Box>

        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Click on a category to see available commands and their usage.
        </Typography>

        <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
          {categories.map(category => {
            const categoryCommands = getCommandsByCategory(category);
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
                      secondary={`${categoryCommands.length} command${categoryCommands.length !== 1 ? 's' : ''}`}
                    />
                    {isExpanded ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                </ListItem>

                <Collapse in={isExpanded} timeout="auto" unmountOnExit>
                  <List component="div" disablePadding>
                    {categoryCommands.map(command => (
                      <ListItem key={command.name} sx={{ pl: 4 }}>
                        <Box sx={{ width: '100%' }}>
                          <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                            <ListItemIcon sx={{ minWidth: 36 }}>{command.icon}</ListItemIcon>
                            <Typography variant="subtitle2" component="span" sx={{ fontWeight: 'bold' }}>
                              {command.name}
                            </Typography>
                            <Chip
                              label={command.usage}
                              size="small"
                              variant="outlined"
                              sx={{ ml: 1, fontSize: '0.7rem' }}
                            />
                          </Box>

                          <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                            {command.description}
                          </Typography>

                          <Box>
                            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>
                              Examples:
                            </Typography>
                            {command.examples.map((example, index) => (
                              <Chip
                                key={index}
                                label={example}
                                size="small"
                                variant="filled"
                                sx={{
                                  mr: 0.5,
                                  mb: 0.5,
                                  fontSize: '0.7rem',
                                  bgcolor: 'action.hover',
                                  '&:hover': {
                                    bgcolor: 'action.selected',
                                  },
                                }}
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
}
