import React from 'react';

interface MythosPanelProps {
  children: React.ReactNode;
  title?: string;
  subtitle?: string;
  className?: string;
  variant?: 'default' | 'elevated' | 'outlined' | 'eldritch';
  size?: 'sm' | 'md' | 'lg';
  showEldritchBorder?: boolean;
  interactive?: boolean;
}

const VARIANT_CLASSES = {
  default: 'bg-mythos-terminal-surface border-gray-700 text-mythos-terminal-text',
  elevated:
    'bg-mythos-terminal-surface border-mythos-terminal-primary shadow-lg shadow-green-900/20 text-mythos-terminal-text hover:shadow-xl hover:shadow-green-900/30 hover:animate-eldritch-shadow',
  outlined:
    'bg-transparent border-mythos-terminal-primary text-mythos-terminal-text hover:bg-mythos-terminal-surface/10 hover:animate-eldritch-border',
  eldritch:
    'bg-mythos-terminal-surface border-mythos-terminal-primary text-mythos-terminal-text shadow-lg shadow-green-900/30 hover:shadow-2xl hover:shadow-green-900/50 hover:animate-eldritch-glow',
} as const;

const SIZE_CLASSES = {
  sm: 'p-3',
  md: 'p-4',
  lg: 'p-6',
} as const;

const CONTENT_PADDING = {
  sm: 'p-2',
  md: 'p-3',
  lg: 'p-4',
} as const;

const HEADER_PADDING = {
  sm: 'px-2 py-1',
  md: 'px-3 py-2',
  lg: 'px-4 py-3',
} as const;

function EldritchCorners() {
  return (
    <>
      <div className="absolute top-0 left-0 w-2 h-2 border-l-2 border-t-2 border-mythos-terminal-primary/50 animate-eldritch-glow"></div>
      <div className="absolute top-0 right-0 w-2 h-2 border-r-2 border-t-2 border-mythos-terminal-primary/50 animate-eldritch-glow"></div>
      <div className="absolute bottom-0 left-0 w-2 h-2 border-l-2 border-b-2 border-mythos-terminal-primary/50 animate-eldritch-glow"></div>
      <div className="absolute bottom-0 right-0 w-2 h-2 border-r-2 border-b-2 border-mythos-terminal-primary/50 animate-eldritch-glow"></div>
    </>
  );
}

function PanelHeader({ title, subtitle, size }: { title: string; subtitle?: string; size: 'sm' | 'md' | 'lg' }) {
  return (
    <div className={`border-b border-gray-700 bg-mythos-terminal-background ${HEADER_PADDING[size]}`}>
      <h3 className="text-mythos-terminal-primary font-bold text-sm">{title}</h3>
      {subtitle && <p className="text-mythos-terminal-text-secondary text-xs mt-1">{subtitle}</p>}
    </div>
  );
}

function buildPanelClasses(props: MythosPanelProps): string {
  const { className = '', variant = 'default', size = 'md', showEldritchBorder = false, interactive = false } = props;
  const eldritchBorderClasses = showEldritchBorder
    ? [
        'before:absolute before:inset-0 before:border',
        'before:border-mythos-terminal-primary/30 before:rounded',
        'before:pointer-events-none before:animate-pulse',
      ].join(' ')
    : '';
  const interactiveClasses = interactive ? 'cursor-pointer hover:scale-[1.02] hover:animate-eldritch-pulse' : '';
  return [
    'font-mono border rounded relative overflow-hidden transition-eldritch duration-eldritch ease-eldritch',
    VARIANT_CLASSES[variant],
    SIZE_CLASSES[size],
    eldritchBorderClasses,
    interactiveClasses,
    className,
  ].join(' ');
}

export const MythosPanel: React.FC<MythosPanelProps> = props => {
  const { children, title, subtitle, variant = 'default', size = 'md' } = props;

  return (
    <div className={buildPanelClasses(props)}>
      {variant === 'eldritch' && <EldritchCorners />}
      {title && <PanelHeader title={title} subtitle={subtitle} size={size} />}
      <div className={CONTENT_PADDING[size]}>{children}</div>
    </div>
  );
};
