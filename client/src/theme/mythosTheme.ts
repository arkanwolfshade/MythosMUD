// MythosMUD Theme Configuration
// This file contains the theme configuration for the MythosMUD client

export const mythosTheme = {
  typography: {
    fontFamily: '"Courier New", monospace',
    h1: {
      fontSize: '1.5rem', // 24px - reasonable size
      fontWeight: 'bold',
      textShadow: '0 0 10px #00ff00',
    },
    h2: {
      fontSize: '1.375rem', // 22px
      fontWeight: 'bold',
      textShadow: '0 0 8px #00ff00',
    },
    h3: {
      fontSize: '1.25rem', // 20px
      fontWeight: 'bold',
      textShadow: '0 0 6px #00ff00',
    },
    h4: {
      fontSize: '1.125rem', // 18px
      fontWeight: 'bold',
      textShadow: '0 0 4px #00ff00',
    },
    h5: {
      fontSize: '1rem', // 16px
      fontWeight: 'bold',
      textShadow: '0 0 3px #00ff00',
    },
    h6: {
      fontSize: '0.875rem', // 14px
      fontWeight: 'bold',
      textShadow: '0 0 2px #00ff00',
    },
    body1: {
      fontSize: '1.25rem', // 20px - base size
      lineHeight: 1.6,
    },
    body2: {
      fontSize: '1rem', // 16px
      lineHeight: 1.5,
    },
    caption: {
      fontSize: '0.875rem', // 14px
      lineHeight: 1.4,
    },
  },
  // Note: MUI components are commented out for now as they're not being used
  // components: {
  //   MuiCssBaseline: {
  //     styleOverrides: {
  //       body: {
  //         backgroundColor: '#0a0a0a',
  //         color: '#00ff00',
  //         fontFamily: '"Courier New", monospace',
  //         lineHeight: 1.6,
  //       },
  //       '.motd-display': {
  //         position: 'fixed !important',
  //         top: '0 !important',
  //         left: '0 !important',
  //         width: '100vw !important',
  //         height: '100vh !important',
  //         backgroundColor: '#0a0a0a !important',
  //         color: '#d4af37 !important',
  //         display: 'flex !important',
  //         flexDirection: 'column !important',
  //         justifyContent: 'center !important',
  //         alignItems: 'center !important',
  //         zIndex: 9999 !important',
  //         fontFamily: '"Courier New", monospace !important',
  //         fontSize: '16px !important',
  //         lineHeight: 1.6 !important',
  //         padding: '20px !important',
  //         textAlign: 'center !important',
  //         overflow: 'auto !important',
  //       },
  //       '.motd-content': {
  //         flex: '1 !important',
  //         display: 'flex !important',
  //         flexDirection: 'column !important',
  //         justifyContent: 'center !important',
  //         alignItems: 'center !important',
  //         maxWidth: '800px !important',
  //         width: '100% !important',
  //       },
  //       '.motd-title': {
  //         fontSize: '2.25rem !important',
  //         fontWeight: 'bold !important',
  //         marginBottom: '1rem !important',
  //         textShadow: '0 0 10px #d4af37 !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-subtitle': {
  //         fontSize: '1.4rem !important',
  //         marginBottom: '2rem !important',
  //         color: '#d4af37 !important',
  //         fontStyle: 'italic !important',
  //       },
  //       '.motd-yellow-sign': {
  //         fontFamily: 'monospace !important',
  //         fontSize: '1.75rem !important',
  //         lineHeight: 1.2 !important',
  //         marginBottom: '2rem !important',
  //         color: '#d4af37 !important',
  //         whiteSpace: 'pre !important',
  //       },
  //       '.motd-welcome': {
  //         marginBottom: '1.5rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-description': {
  //         marginBottom: '1.5rem !important',
  //         color: '#d4af37 !important',
  //         textAlign: 'justify !important',
  //       },
  //       '.motd-warning': {
  //         marginBottom: '1.5rem !important',
  //         color: '#ff6600 !important',
  //         fontWeight: 'bold !important',
  //         border: '1px solid #ff6600 !important',
  //         padding: '1rem !important',
  //         borderRadius: '4px !important',
  //         backgroundColor: 'rgba(255, 102, 0, 0.1) !important',
  //       },
  //       '.motd-stats': {
  //         marginBottom: '1.5rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-stats h3': {
  //         fontSize: '1.3rem !important',
  //         fontWeight: 'bold !important',
  //         marginBottom: '0.5rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-stats p': {
  //         marginBottom: '0.25rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-stats strong': {
  //         color: '#ff6600 !important',
  //       },
  //       '.motd-commands': {
  //         marginBottom: '1.5rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-commands p': {
  //         marginBottom: '0.25rem !important',
  //         color: '#d4af37 !important',
  //       },
  //       '.motd-commands code': {
  //         backgroundColor: 'rgba(255, 102, 0, 0.2) !important',
  //         padding: '0.125rem 0.25rem !important',
  //         borderRadius: '2px !important',
  //         color: '#ff6600 !important',
  //         fontFamily: 'monospace !important',
  //       },
  //       '.motd-footer': {
  //         marginTop: 'auto !important',
  //         color: '#888888 !important',
  //         fontSize: '1rem !important',
  //         fontStyle: 'italic !important',
  //       },
  //       '.motd-footer p': {
  //         marginBottom: '0.25rem !important',
  //         color: '#888888 !important',
  //       },
  //       '.motd-actions': {
  //         marginTop: '2rem !important',
  //       },
  //       '.continue-button': {
  //         backgroundColor: '#d4af37 !important',
  //         color: '#000000 !important',
  //         border: 'none !important',
  //         padding: '0.75rem 2rem !important',
  //         fontSize: '1.125rem !important',
  //         fontWeight: 'bold !important',
  //         borderRadius: '4px !important',
  //         cursor: 'pointer !important',
  //         fontFamily: '"Courier New", monospace !important',
  //         textTransform: 'none !important',
  //         boxShadow: '0 0 10px rgba(212, 175, 55, 0.5) !important',
  //         transition: 'all 0.3s ease !important',
  //       },
  //       '.continue-button:hover': {
  //         backgroundColor: '#ffd700 !important',
  //         boxShadow: '0 0 15px rgba(212, 175, 55, 0.8) !important',
  //         transform: 'translateY(-2px) !important',
  //       },
  //       '.continue-button:active': {
  //         transform: 'translateY(0) !important',
  //       },
  //     },
  //   },
  // },
};
