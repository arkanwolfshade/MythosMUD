/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  // Exclude MOTD classes from purging
  safelist: [
    'motd-display',
    'motd-content',
    'motd-content .container',
    'motd-content .title',
    'motd-content .title-border',
    'motd-content .title-text',
    'motd-content .title-subtitle',
    'motd-content .yellow-sign',
    'motd-content .welcome-text',
    'motd-content .warning',
    'motd-content .stats',
    'motd-content .footer',
    'motd-actions',
    'continue-button',
  ],
  theme: {
    extend: {
      colors: {
        mythos: {
          // Terminal colors for new interface
          terminal: {
            primary: '#00ff00',
            secondary: '#ff9800',
            background: '#0a0a0a',
            surface: '#1a1a1a',
            text: '#00ff00',
            'text-secondary': '#4caf50',
            error: '#f44336',
            warning: '#ff9800',
            success: '#4caf50',
          },
          // MOTD colors (preserved)
          motd: {
            gold: '#d4af37',
            'gold-bright': '#ffd700',
            background: '#0a0a0a',
          },
        },
      },
      fontFamily: {
        mono: ['Courier New', 'monospace'],
      },
      animation: {
        shimmer: 'shimmer 3s ease-in-out infinite',
      },
      keyframes: {
        shimmer: {
          '0%': { opacity: '0.3' },
          '50%': { opacity: '0.7' },
          '100%': { opacity: '0.3' },
        },
      },
    },
  },
};
