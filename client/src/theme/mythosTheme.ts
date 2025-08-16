import { createTheme } from '@mui/material/styles';

// Custom MythosMUD theme with proper contrast for terminal-style interface
export const mythosTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#00ff00', // Bright green for primary elements
      light: '#4caf50', // Softer green for light variants
      dark: '#2e7d32', // Darker green for dark variants
      contrastText: '#000000', // Black text on green backgrounds
    },
    secondary: {
      main: '#ff9800', // Orange for secondary elements
      light: '#ffb74d',
      dark: '#f57c00',
      contrastText: '#000000',
    },
    error: {
      main: '#f44336', // Red for errors
      light: '#e57373',
      dark: '#d32f2f',
      contrastText: '#ffffff',
    },
    warning: {
      main: '#ff9800', // Orange for warnings
      light: '#ffb74d',
      dark: '#f57c00',
      contrastText: '#000000',
    },
    info: {
      main: '#2196f3', // Blue for info
      light: '#64b5f6',
      dark: '#1976d2',
      contrastText: '#ffffff',
    },
    success: {
      main: '#4caf50', // Green for success
      light: '#81c784',
      dark: '#388e3c',
      contrastText: '#ffffff',
    },
    background: {
      default: '#0a0a0a', // Very dark background
      paper: '#1a1a1a', // Slightly lighter for panels
    },
    text: {
      primary: '#00ff00', // Bright green for primary text
      secondary: '#4caf50', // Softer green for secondary text
      disabled: '#666666', // Gray for disabled text
    },
    divider: '#333333', // Dark gray for dividers
    action: {
      active: '#00ff00',
      hover: 'rgba(0, 255, 0, 0.08)',
      selected: 'rgba(0, 255, 0, 0.16)',
      disabled: 'rgba(255, 255, 255, 0.3)',
      disabledBackground: 'rgba(255, 255, 255, 0.12)',
    },
  },
  typography: {
    fontFamily: '"Courier New", monospace',
    fontSize: 14,
    h1: {
      fontSize: '2rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    h2: {
      fontSize: '1.75rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    h3: {
      fontSize: '1.5rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    h4: {
      fontSize: '1.25rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    h5: {
      fontSize: '1.125rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    h6: {
      fontSize: '1rem',
      fontWeight: 600,
      color: '#00ff00',
    },
    body1: {
      fontSize: '0.875rem',
      lineHeight: 1.4,
      color: '#00ff00',
    },
    body2: {
      fontSize: '0.75rem',
      lineHeight: 1.4,
      color: '#4caf50',
    },
  },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundColor: '#1a1a1a',
          color: '#00ff00',
          border: '1px solid #333333',
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          fontFamily: '"Courier New", monospace',
          textTransform: 'none',
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiInputBase-root': {
            fontFamily: '"Courier New", monospace',
          },
        },
      },
    },
    MuiChip: {
      styleOverrides: {
        root: {
          fontFamily: '"Courier New", monospace',
        },
      },
    },
    // Preserve MOTD styling while allowing theme for panels
    MuiCssBaseline: {
      styleOverrides: {
        // MOTD - preserve original styling completely
        '.motd-display': {
          display: 'flex !important',
          flexDirection: 'column !important',
          height: '100% !important',
          backgroundColor: '#0a0a0a !important',
          color: '#d4af37 !important',
          fontFamily: '"Courier New", monospace !important',
          overflowY: 'auto !important',
          padding: '20px !important',
        },
        '.motd-content': {
          flex: '1 !important',
          display: 'flex !important',
          flexDirection: 'column !important',
          maxWidth: '800px !important',
          margin: '0 auto !important',
          width: '100% !important',
        },
        '.motd-content .container': {
          maxWidth: 'none !important',
          margin: '0 !important',
          padding: '0 !important',
        },
        '.motd-content .title': {
          marginBottom: '20px !important',
          textAlign: 'center !important',
        },
        '.motd-content .title-border': {
          border: '2px solid #d4af37 !important',
          borderRadius: '5px !important',
          padding: '20px !important',
          background: 'linear-gradient(45deg, rgba(212, 175, 55, 0.1), rgba(212, 175, 55, 0.05)) !important',
          boxShadow: '0 0 20px rgba(212, 175, 55, 0.3) !important',
          position: 'relative !important',
        },
        '.motd-content .title-border::before': {
          position: 'absolute !important',
          top: '0 !important',
          left: '0 !important',
          right: '0 !important',
          bottom: '0 !important',
          background:
            'linear-gradient(45deg, transparent 30%, rgba(212, 175, 55, 0.1) 50%, transparent 70%) !important',
          pointerEvents: 'none !important',
          animation: 'shimmer 3s ease-in-out infinite !important',
        },
        '.motd-content .title-text': {
          fontSize: '2.2em !important',
          color: '#d4af37 !important',
          textShadow: '0 0 15px #d4af37 !important',
          fontWeight: 'bold !important',
          fontFamily: '"Courier New", monospace !important',
          marginBottom: '10px !important',
          letterSpacing: '2px !important',
        },
        '.motd-content .title-subtitle': {
          fontSize: '1.2em !important',
          color: '#d4af37 !important',
          textShadow: '0 0 10px #d4af37 !important',
          fontFamily: '"Courier New", monospace !important',
          fontStyle: 'italic !important',
          letterSpacing: '1px !important',
        },
        '.motd-content .yellow-sign': {
          fontSize: '1em !important',
          margin: '20px 0 !important',
          textAlign: 'center !important',
          color: '#ffd700 !important',
          textShadow: '0 0 5px #ffd700 !important',
          fontWeight: 'bold !important',
          lineHeight: '1 !important',
          whiteSpace: 'pre !important',
          fontFamily: '"Courier New", monospace !important',
        },
        '.motd-content .welcome-text': {
          fontSize: '0.95em !important',
          margin: '20px 0 !important',
          textAlign: 'left !important',
          color: '#d4af37 !important',
          lineHeight: '1.4 !important',
        },
        '.motd-content .warning': {
          color: '#8b0000 !important',
          fontWeight: 'bold !important',
          margin: '15px 0 !important',
          textAlign: 'center !important',
          fontSize: '0.9em !important',
          textShadow: '0 0 5px #8b0000 !important',
        },
        '.motd-content .stats': {
          backgroundColor: '#1a1a1a !important',
          border: '1px solid #333 !important',
          padding: '15px !important',
          margin: '15px 0 !important',
          borderRadius: '5px !important',
        },
        '.motd-content .stats h3': {
          marginTop: '0 !important',
          color: '#d4af37 !important',
          fontSize: '1.1em !important',
        },
        '.motd-content .stats p': {
          margin: '5px 0 !important',
          color: '#ccc !important',
          fontSize: '0.9em !important',
        },
        '.motd-content .footer': {
          marginTop: '20px !important',
          fontSize: '0.8em !important',
          color: '#666 !important',
          borderTop: '1px solid #333 !important',
          paddingTop: '15px !important',
          textAlign: 'center !important',
        },
        '.motd-actions': {
          textAlign: 'center !important',
          marginTop: '20px !important',
          paddingTop: '20px !important',
          borderTop: '1px solid #333 !important',
        },
        '.continue-button': {
          background: 'linear-gradient(45deg, #d4af37, #b8941f) !important',
          color: '#0a0a0a !important',
          border: 'none !important',
          padding: '12px 30px !important',
          fontSize: '1.1em !important',
          fontWeight: 'bold !important',
          fontFamily: '"Courier New", monospace !important',
          borderRadius: '5px !important',
          cursor: 'pointer !important',
          transition: 'all 0.3s ease !important',
          textTransform: 'uppercase !important',
          letterSpacing: '1px !important',
          boxShadow: '0 4px 8px rgba(212, 175, 55, 0.3) !important',
        },
        '.continue-button:hover': {
          background: 'linear-gradient(45deg, #b8941f, #d4af37) !important',
          transform: 'translateY(-2px) !important',
          boxShadow: '0 6px 12px rgba(212, 175, 55, 0.4) !important',
        },
        // Add shimmer animation
        '@keyframes shimmer': {
          '0%': {
            opacity: '0.3',
          },
          '50%': {
            opacity: '0.7',
          },
          '100%': {
            opacity: '0.3',
          },
        },
      },
    },
  },
});

// Export the theme for use in the app
export default mythosTheme;
