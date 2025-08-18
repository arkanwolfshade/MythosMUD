/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
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
            primary: '#d4af37',
            secondary: '#ffd700',
            background: '#000000',
            text: '#ffffff',
          },
        },
      },
      fontFamily: {
        mono: ['Courier New', 'Courier', 'monospace'],
      },
      animation: {
        shimmer: 'shimmer 2s linear infinite',
        // Phase 4.1: Advanced Mythos Animations
        'eldritch-glow': 'eldritch-glow 1.5s ease-in-out infinite alternate',
        'eldritch-pulse': 'eldritch-pulse 1s ease-in-out infinite',
        'eldritch-shimmer': 'eldritch-shimmer 2s linear infinite',
        'eldritch-fade': 'eldritch-fade 1.5s ease-in-out infinite alternate',
        'eldritch-slide': 'eldritch-slide 1s ease-in-out infinite',
        'eldritch-scale': 'eldritch-scale 1s ease-in-out infinite alternate',
        'eldritch-rotate': 'eldritch-rotate 3s linear infinite',
        'eldritch-blur': 'eldritch-blur 1.5s ease-in-out infinite alternate',
        'eldritch-shadow': 'eldritch-shadow 2s ease-in-out infinite',
        'eldritch-border': 'eldritch-border 2s linear infinite',
      },
      keyframes: {
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
        // Phase 4.1: Advanced Mythos Keyframes
        'eldritch-glow': {
          '0%': {
            boxShadow: '0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00',
            textShadow: '0 0 10px #00ff00, 0 0 20px #00ff00',
          },
          '50%': {
            boxShadow: '0 0 20px #00ff00, 0 0 40px #00ff00, 0 0 60px #00ff00',
            textShadow: '0 0 20px #00ff00, 0 0 40px #00ff00',
          },
          '100%': {
            boxShadow: '0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00',
            textShadow: '0 0 10px #00ff00, 0 0 20px #00ff00',
          },
        },
        'eldritch-pulse': {
          '0%': {
            opacity: '1',
            transform: 'scale(1)',
          },
          '50%': {
            opacity: '0.5',
            transform: 'scale(1.1)',
          },
          '100%': {
            opacity: '1',
            transform: 'scale(1)',
          },
        },
        'eldritch-shimmer': {
          '0%': {
            backgroundPosition: '-200% 0',
            backgroundImage: 'linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.3), transparent)',
          },
          '50%': {
            backgroundPosition: '0% 0',
            backgroundImage: 'linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.5), transparent)',
          },
          '100%': {
            backgroundPosition: '200% 0',
            backgroundImage: 'linear-gradient(90deg, transparent, rgba(0, 255, 0, 0.3), transparent)',
          },
        },
        'eldritch-fade': {
          '0%': { opacity: '0.3' },
          '50%': { opacity: '1' },
          '100%': { opacity: '0.3' },
        },
        'eldritch-slide': {
          '0%': { transform: 'translateX(-5px)' },
          '50%': { transform: 'translateX(5px)' },
          '100%': { transform: 'translateX(-5px)' },
        },
        'eldritch-scale': {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.15)' },
          '100%': { transform: 'scale(1)' },
        },
        'eldritch-rotate': {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
        'eldritch-blur': {
          '0%': { filter: 'blur(0px)' },
          '50%': { filter: 'blur(3px)' },
          '100%': { filter: 'blur(0px)' },
        },
        'eldritch-shadow': {
          '0%': {
            boxShadow: '0 0 10px rgba(0, 255, 0, 0.5), 0 0 20px rgba(0, 255, 0, 0.3)',
            textShadow: '0 0 10px rgba(0, 255, 0, 0.5)',
          },
          '50%': {
            boxShadow: '0 0 25px rgba(0, 255, 0, 0.8), 0 0 50px rgba(0, 255, 0, 0.5)',
            textShadow: '0 0 25px rgba(0, 255, 0, 0.8)',
          },
          '100%': {
            boxShadow: '0 0 10px rgba(0, 255, 0, 0.5), 0 0 20px rgba(0, 255, 0, 0.3)',
            textShadow: '0 0 10px rgba(0, 255, 0, 0.5)',
          },
        },
        'eldritch-border': {
          '0%': {
            borderColor: 'rgba(0, 255, 0, 0.5)',
            borderWidth: '2px',
            boxShadow: 'inset 0 0 10px rgba(0, 255, 0, 0.3)',
          },
          '50%': {
            borderColor: 'rgba(0, 255, 0, 1)',
            borderWidth: '3px',
            boxShadow: 'inset 0 0 20px rgba(0, 255, 0, 0.6)',
          },
          '100%': {
            borderColor: 'rgba(0, 255, 0, 0.5)',
            borderWidth: '2px',
            boxShadow: 'inset 0 0 10px rgba(0, 255, 0, 0.3)',
          },
        },
      },
      // Phase 4.1: Custom utilities for eldritch effects
      backgroundImage: {
        'eldritch-gradient':
          'linear-gradient(45deg, rgba(0, 255, 0, 0.1), rgba(255, 152, 0, 0.1), rgba(0, 255, 0, 0.1))',
        'eldritch-radial': 'radial-gradient(circle, rgba(0, 255, 0, 0.1) 0%, transparent 70%)',
        'eldritch-noise':
          "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.1'/%3E%3C/svg%3E\")",
      },
      backdropBlur: {
        eldritch: '2px',
      },
      transitionProperty: {
        eldritch: 'all',
      },
      transitionDuration: {
        eldritch: '300ms',
      },
      transitionTimingFunction: {
        eldritch: 'cubic-bezier(0.4, 0, 0.2, 1)',
      },
    },
  },
  plugins: [],
};
