/**
 * Design Tokens for MythosMUD UI Components
 *
 * This file defines consistent design tokens used across all UI components.
 * It provides a single source of truth for colors, spacing, typography, and other design elements.
 */

// Color Palette
export const colors = {
  // Terminal Theme Colors
  terminal: {
    background: 'bg-mythos-terminal-background',
    surface: 'bg-mythos-terminal-surface',
    text: 'text-mythos-terminal-text',
    'text-secondary': 'text-mythos-terminal-text-secondary',
    primary: 'text-mythos-terminal-primary',
    success: 'text-mythos-terminal-success',
    error: 'text-mythos-terminal-error',
    warning: 'text-mythos-terminal-warning',
    border: 'border-mythos-terminal-border',
  },

  // Standard Colors
  gray: {
    50: 'bg-gray-50',
    100: 'bg-gray-100',
    200: 'bg-gray-200',
    300: 'bg-gray-300',
    400: 'bg-gray-400',
    500: 'bg-gray-500',
    600: 'bg-gray-600',
    700: 'bg-gray-700',
    800: 'bg-gray-800',
    900: 'bg-gray-900',
  },

  // Status Colors
  status: {
    success: 'bg-green-500',
    error: 'bg-red-500',
    warning: 'bg-yellow-500',
    info: 'bg-blue-500',
  },
} as const;

// Spacing Scale
export const spacing = {
  xs: 'p-1',
  sm: 'p-2',
  md: 'p-3',
  lg: 'p-4',
  xl: 'p-6',
  '2xl': 'p-8',

  // Padding variants
  padding: {
    xs: 'px-1 py-1',
    sm: 'px-2 py-1',
    md: 'px-3 py-2',
    lg: 'px-4 py-3',
    xl: 'px-6 py-4',
  },

  // Margin variants
  margin: {
    xs: 'm-1',
    sm: 'm-2',
    md: 'm-3',
    lg: 'm-4',
    xl: 'm-6',
  },
} as const;

// Typography Scale
export const typography = {
  // Font sizes
  sizes: {
    xs: 'text-xs',
    sm: 'text-sm',
    base: 'text-base',
    lg: 'text-lg',
    xl: 'text-xl',
    '2xl': 'text-2xl',
    '3xl': 'text-3xl',
  },

  // Font weights
  weights: {
    normal: 'font-normal',
    medium: 'font-medium',
    semibold: 'font-semibold',
    bold: 'font-bold',
  },

  // Line heights
  lineHeights: {
    tight: 'leading-tight',
    normal: 'leading-normal',
    relaxed: 'leading-relaxed',
  },
} as const;

// Border Radius
export const borderRadius = {
  none: 'rounded-none',
  sm: 'rounded-sm',
  base: 'rounded',
  md: 'rounded-md',
  lg: 'rounded-lg',
  xl: 'rounded-xl',
  '2xl': 'rounded-2xl',
  full: 'rounded-full',
} as const;

// Shadows
export const shadows = {
  none: 'shadow-none',
  sm: 'shadow-sm',
  base: 'shadow',
  md: 'shadow-md',
  lg: 'shadow-lg',
  xl: 'shadow-xl',
  '2xl': 'shadow-2xl',
} as const;

// Component Variants
export const variants = {
  button: {
    primary: 'bg-mythos-terminal-primary text-black hover:bg-mythos-terminal-primary/90',
    secondary:
      'bg-mythos-terminal-surface border border-gray-700 text-mythos-terminal-text hover:bg-mythos-terminal-background',
    error: 'bg-mythos-terminal-error text-white hover:bg-red-600',
    success: 'bg-mythos-terminal-success text-black hover:bg-green-600',
    warning: 'bg-mythos-terminal-warning text-black hover:bg-yellow-600',
  },

  input: {
    default:
      'bg-mythos-terminal-surface border border-gray-700 text-mythos-terminal-text focus:border-mythos-terminal-primary focus:ring-1 focus:ring-mythos-terminal-primary',
    error:
      'bg-mythos-terminal-surface border border-red-500 text-mythos-terminal-text focus:border-red-500 focus:ring-1 focus:ring-red-500',
  },

  panel: {
    default: 'bg-mythos-terminal-surface border border-gray-700',
    elevated: 'bg-mythos-terminal-surface border border-gray-700 shadow-lg',
    eldritch:
      'bg-mythos-terminal-surface border border-mythos-terminal-primary/50 shadow-lg shadow-mythos-terminal-primary/20',
  },
} as const;

// Component Sizes
export const sizes = {
  button: {
    sm: 'px-2 py-1 text-xs',
    md: 'px-3 py-2 text-sm',
    lg: 'px-4 py-3 text-base',
  },

  input: {
    sm: 'px-2 py-1 text-xs',
    md: 'px-3 py-2 text-sm',
    lg: 'px-4 py-3 text-base',
  },

  panel: {
    sm: 'p-2',
    md: 'p-3',
    lg: 'p-4',
  },
} as const;

// Animation Classes
export const animations = {
  // Transitions
  transition: 'transition-all duration-200',
  transitionSlow: 'transition-all duration-300',
  transitionFast: 'transition-all duration-150',

  // Hover effects
  hover: 'hover:scale-105 hover:shadow-md',
  hoverSubtle: 'hover:bg-opacity-80',

  // Focus effects
  focus: 'focus:outline-none focus:ring-2 focus:ring-mythos-terminal-primary focus:ring-opacity-50',

  // Loading states
  loading: 'animate-pulse',
  spinning: 'animate-spin',

  // Entrance animations
  fadeIn: 'animate-fade-in',
  slideIn: 'animate-slide-in',
} as const;

// Layout Utilities
export const layout = {
  // Flexbox
  flex: {
    center: 'flex items-center justify-center',
    between: 'flex items-center justify-between',
    start: 'flex items-center justify-start',
    end: 'flex items-center justify-end',
  },

  // Grid
  grid: {
    '2': 'grid grid-cols-2 gap-2',
    '3': 'grid grid-cols-3 gap-3',
    '4': 'grid grid-cols-4 gap-4',
    auto: 'grid grid-cols-auto gap-2',
  },

  // Spacing
  space: {
    '2': 'space-y-2',
    '3': 'space-y-3',
    '4': 'space-y-4',
    '6': 'space-y-6',
  },
} as const;

// Responsive Breakpoints
export const breakpoints = {
  sm: 'sm:',
  md: 'md:',
  lg: 'lg:',
  xl: 'xl:',
  '2xl': '2xl:',
} as const;

// Z-Index Scale
export const zIndex = {
  dropdown: 'z-10',
  sticky: 'z-20',
  fixed: 'z-30',
  modal: 'z-40',
  popover: 'z-50',
  tooltip: 'z-60',
  toast: 'z-70',
  overlay: 'z-100000',
} as const;

// Component Class Builders
export const buildClasses = {
  /**
   * Build button classes based on variant and size
   */
  button: (variant: keyof typeof variants.button, size: keyof typeof sizes.button, disabled = false) => {
    const baseClasses =
      'inline-flex items-center justify-center font-medium border rounded transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2';
    const variantClasses = variants.button[variant];
    const sizeClasses = sizes.button[size];
    const disabledClasses = disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer';

    return `${baseClasses} ${variantClasses} ${sizeClasses} ${disabledClasses}`;
  },

  /**
   * Build input classes based on variant and size
   */
  input: (variant: keyof typeof variants.input, size: keyof typeof sizes.input, disabled = false) => {
    const baseClasses = 'block w-full rounded transition-colors duration-200 focus:outline-none';
    const variantClasses = variants.input[variant];
    const sizeClasses = sizes.input[size];
    const disabledClasses = disabled ? 'opacity-50 cursor-not-allowed' : '';

    return `${baseClasses} ${variantClasses} ${sizeClasses} ${disabledClasses}`;
  },

  /**
   * Build panel classes based on variant and size
   */
  panel: (variant: keyof typeof variants.panel, size: keyof typeof sizes.panel) => {
    const baseClasses = 'rounded';
    const variantClasses = variants.panel[variant];
    const sizeClasses = sizes.panel[size];

    return `${baseClasses} ${variantClasses} ${sizeClasses}`;
  },
};

// Type Definitions
export type ColorVariant = keyof typeof colors.terminal;
export type ButtonVariant = keyof typeof variants.button;
export type InputVariant = keyof typeof variants.input;
export type PanelVariant = keyof typeof variants.panel;
export type ComponentSize = keyof typeof sizes.button;
export type SpacingSize = keyof typeof spacing;
export type TypographySize = keyof typeof typography.sizes;
