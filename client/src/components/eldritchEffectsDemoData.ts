import { MythosIcons } from './ui/EldritchIcon';

export type EffectOption = {
  name: string;
  title: string;
  description: string;
  icon: keyof typeof MythosIcons;
};

export const ELDRITCH_EFFECT_OPTIONS: EffectOption[] = [
  {
    name: 'eldritch-glow',
    title: 'Eldritch Glow',
    description: 'Pulsing green glow effect',
    icon: MythosIcons.lightbulb,
  },
  { name: 'eldritch-pulse', title: 'Eldritch Pulse', description: 'Subtle opacity pulse', icon: MythosIcons.heart },
  {
    name: 'eldritch-shimmer',
    title: 'Eldritch Shimmer',
    description: 'Horizontal light shimmer',
    icon: MythosIcons.sparkles,
  },
  { name: 'eldritch-fade', title: 'Eldritch Fade', description: 'Fading in and out', icon: MythosIcons.eye },
  {
    name: 'eldritch-slide',
    title: 'Eldritch Slide',
    description: 'Subtle horizontal movement',
    icon: MythosIcons.move,
  },
  { name: 'eldritch-scale', title: 'Eldritch Scale', description: 'Slight scaling effect', icon: MythosIcons.maximize },
  {
    name: 'eldritch-rotate',
    title: 'Eldritch Rotate',
    description: 'Slow, continuous rotation',
    icon: MythosIcons.rotate,
  },
  { name: 'eldritch-blur', title: 'Eldritch Blur', description: 'Blurring and unblurring', icon: MythosIcons.eyeOff },
  { name: 'eldritch-shadow', title: 'Eldritch Shadow', description: 'Pulsing shadow effect', icon: MythosIcons.shadow },
  { name: 'eldritch-border', title: 'Eldritch Border', description: 'Pulsing border color', icon: MythosIcons.square },
];

export const ALWAYS_ACTIVE_EFFECTS = [
  { className: 'animate-eldritch-glow', label: 'Glow Effect' },
  { className: 'animate-eldritch-pulse', label: 'Pulse Effect' },
  { className: 'animate-eldritch-rotate', label: 'Rotate Effect' },
  { className: 'animate-eldritch-scale', label: 'Scale Effect' },
  { className: 'animate-eldritch-border', label: 'Border Effect' },
];

export function hasEffect(active: string[], name: string): boolean {
  return active.includes(name);
}

export function effectClass(active: string[], name: string, animation: string): string {
  return hasEffect(active, name) ? animation : '';
}

export function pairClass(active: string[], a: string, b: string): string {
  return `${effectClass(active, a, `animate-${a}`)} ${effectClass(active, b, `animate-${b}`)}`;
}
