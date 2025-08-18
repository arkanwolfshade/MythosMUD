// import { createTheme } from '@mui/material/styles';

// Custom MythosMUD theme with proper contrast for terminal-style interface
// export const mythosTheme = createTheme({
//   palette: {
//     mode: 'dark',
//     primary: {
//       main: '#00ff00',
//       light: '#33ff33',
//       dark: '#00cc00',
//       contrastText: '#000000',
//     },
//     secondary: {
//       main: '#ff6600',
//       light: '#ff8533',
//       dark: '#cc5200',
//       contrastText: '#000000',
//     },
//     background: {
//       default: '#0a0a0a',
//       paper: '#1a1a1a',
//     },
//     text: {
//       primary: '#00ff00',
//       secondary: '#888888',
//     },
//     error: {
//       main: '#ff0000',
//       light: '#ff3333',
//       dark: '#cc0000',
//       contrastText: '#ffffff',
//     },
//     warning: {
//       main: '#ffaa00',
//       light: '#ffbb33',
//       dark: '#cc8800',
//       contrastText: '#000000',
//     },
//     success: {
//       main: '#00ff00',
//       light: '#33ff33',
//       dark: '#00cc00',
//       contrastText: '#000000',
//     },
//   },
//   typography: {
//     fontFamily: '"Courier New", monospace',
//     h1: {
//       fontSize: '2rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 10px #00ff00',
//     },
//     h2: {
//       fontSize: '1.5rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 8px #00ff00',
//     },
//     h3: {
//       fontSize: '1.25rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 6px #00ff00',
//     },
//     h4: {
//       fontSize: '1.125rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 4px #00ff00',
//     },
//     h5: {
//       fontSize: '1rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 3px #00ff00',
//     },
//     h6: {
//       fontSize: '0.875rem',
//       fontWeight: 'bold',
//       textShadow: '0 0 2px #00ff00',
//     },
//     body1: {
//       fontSize: '0.875rem',
//       lineHeight: 1.6,
//     },
//     body2: {
//       fontSize: '0.75rem',
//       lineHeight: 1.5,
//     },
//     caption: {
//       fontSize: '0.625rem',
//       lineHeight: 1.4,
//     },
//   },
//   components: {
//     MuiCssBaseline: {
//       styleOverrides: {
//         body: {
//           backgroundColor: '#0a0a0a',
//           color: '#00ff00',
//           fontFamily: '"Courier New", monospace',
//           lineHeight: 1.6,
//         },
//         '.motd-display': {
//           position: 'fixed !important',
//           top: '0 !important',
//           left: '0 !important',
//           width: '100vw !important',
//           height: '100vh !important',
//           backgroundColor: '#0a0a0a !important',
//           color: '#d4af37 !important',
//           display: 'flex !important',
//           flexDirection: 'column !important',
//           justifyContent: 'center !important',
//           alignItems: 'center !important',
//           zIndex: 9999 !important,
//           fontFamily: '"Courier New", monospace !important',
//           fontSize: '14px !important',
//           lineHeight: 1.6 !important',
//           padding: '20px !important',
//           textAlign: 'center !important',
//           overflow: 'auto !important',
//         },
//         '.motd-content': {
//           flex: '1 !important',
//           display: 'flex !important',
//           flexDirection: 'column !important',
//           justifyContent: 'center !important',
//           alignItems: 'center !important',
//           maxWidth: '800px !important',
//           width: '100% !important',
//         },
//         '.motd-title': {
//           fontSize: '2rem !important',
//           fontWeight: 'bold !important',
//           marginBottom: '1rem !important',
//           textShadow: '0 0 10px #d4af37 !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-subtitle': {
//           fontSize: '1.2rem !important',
//           marginBottom: '2rem !important',
//           color: '#d4af37 !important',
//           fontStyle: 'italic !important',
//         },
//         '.motd-yellow-sign': {
//           fontFamily: 'monospace !important',
//           fontSize: '1.5rem !important',
//           lineHeight: 1.2 !important',
//           marginBottom: '2rem !important',
//           color: '#d4af37 !important',
//           whiteSpace: 'pre !important',
//         },
//         '.motd-welcome': {
//           marginBottom: '1.5rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-description': {
//           marginBottom: '1.5rem !important',
//           color: '#d4af37 !important',
//           textAlign: 'justify !important',
//         },
//         '.motd-warning': {
//           marginBottom: '1.5rem !important',
//           color: '#ff6600 !important',
//           fontWeight: 'bold !important',
//           border: '1px solid #ff6600 !important',
//           padding: '1rem !important',
//           borderRadius: '4px !important',
//           backgroundColor: 'rgba(255, 102, 0, 0.1) !important',
//         },
//         '.motd-stats': {
//           marginBottom: '1.5rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-stats h3': {
//           fontSize: '1.1rem !important',
//           fontWeight: 'bold !important',
//           marginBottom: '0.5rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-stats p': {
//           marginBottom: '0.25rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-stats strong': {
//           color: '#ff6600 !important',
//         },
//         '.motd-commands': {
//           marginBottom: '1.5rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-commands p': {
//           marginBottom: '0.25rem !important',
//           color: '#d4af37 !important',
//         },
//         '.motd-commands code': {
//           backgroundColor: 'rgba(255, 102, 0, 0.2) !important',
//           padding: '0.125rem 0.25rem !important',
//           borderRadius: '2px !important',
//           color: '#ff6600 !important',
//           fontFamily: 'monospace !important',
//         },
//         '.motd-footer': {
//           marginTop: 'auto !important',
//           color: '#888888 !important',
//           fontSize: '0.8rem !important',
//           fontStyle: 'italic !important',
//         },
//         '.motd-footer p': {
//           marginBottom: '0.25rem !important',
//           color: '#888888 !important',
//         },
//         '.motd-actions': {
//           marginTop: '2rem !important',
//         },
//         '.continue-button': {
//           backgroundColor: '#d4af37 !important',
//           color: '#000000 !important',
//           border: 'none !important',
//           padding: '0.75rem 2rem !important',
//           fontSize: '1rem !important',
//           fontWeight: 'bold !important',
//           borderRadius: '4px !important',
//           cursor: 'pointer !important',
//           fontFamily: '"Courier New", monospace !important',
//           textTransform: 'none !important',
//           boxShadow: '0 0 10px rgba(212, 175, 55, 0.5) !important',
//           transition: 'all 0.3s ease !important',
//         },
//         '.continue-button:hover': {
//           backgroundColor: '#ffd700 !important',
//           boxShadow: '0 0 15px rgba(212, 175, 55, 0.8) !important',
//           transform: 'translateY(-2px) !important',
//         },
//         '.continue-button:active': {
//           transform: 'translateY(0) !important',
//         },
//       },
//     },
//   },
// });

export const mythosTheme = {}; // Placeholder for now
