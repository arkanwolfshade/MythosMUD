import { describe, expect, it } from 'vitest';
import {
  animations,
  borderRadius,
  breakpoints,
  buildClasses,
  colors,
  layout,
  shadows,
  sizes,
  spacing,
  typography,
  variants,
  zIndex,
} from '../designTokens';

describe('designTokens', () => {
  describe('colors', () => {
    it('should have terminal colors', () => {
      expect(colors.terminal.background).toBe('bg-mythos-terminal-background');
      expect(colors.terminal.primary).toBe('text-mythos-terminal-primary');
      expect(colors.terminal.success).toBe('text-mythos-terminal-success');
      expect(colors.terminal.error).toBe('text-mythos-terminal-error');
    });

    it('should have gray scale colors', () => {
      expect(colors.gray[50]).toBe('bg-gray-50');
      expect(colors.gray[500]).toBe('bg-gray-500');
      expect(colors.gray[900]).toBe('bg-gray-900');
    });

    it('should have status colors', () => {
      expect(colors.status.success).toBe('bg-green-500');
      expect(colors.status.error).toBe('bg-red-500');
      expect(colors.status.warning).toBe('bg-yellow-500');
      expect(colors.status.info).toBe('bg-blue-500');
    });
  });

  describe('spacing', () => {
    it('should have spacing scale', () => {
      expect(spacing.xs).toBe('p-1');
      expect(spacing.sm).toBe('p-2');
      expect(spacing.md).toBe('p-3');
      expect(spacing.lg).toBe('p-4');
      expect(spacing.xl).toBe('p-6');
    });

    it('should have padding variants', () => {
      expect(spacing.padding.xs).toBe('px-1 py-1');
      expect(spacing.padding.md).toBe('px-3 py-2');
      expect(spacing.padding.xl).toBe('px-6 py-4');
    });

    it('should have margin variants', () => {
      expect(spacing.margin.xs).toBe('m-1');
      expect(spacing.margin.md).toBe('m-3');
      expect(spacing.margin.xl).toBe('m-6');
    });
  });

  describe('typography', () => {
    it('should have font sizes', () => {
      expect(typography.sizes.xs).toBe('text-xs');
      expect(typography.sizes.base).toBe('text-base');
      expect(typography.sizes.lg).toBe('text-lg');
      expect(typography.sizes['3xl']).toBe('text-3xl');
    });

    it('should have font weights', () => {
      expect(typography.weights.normal).toBe('font-normal');
      expect(typography.weights.bold).toBe('font-bold');
    });

    it('should have line heights', () => {
      expect(typography.lineHeights.tight).toBe('leading-tight');
      expect(typography.lineHeights.normal).toBe('leading-normal');
      expect(typography.lineHeights.relaxed).toBe('leading-relaxed');
    });
  });

  describe('borderRadius', () => {
    it('should have border radius values', () => {
      expect(borderRadius.none).toBe('rounded-none');
      expect(borderRadius.sm).toBe('rounded-sm');
      expect(borderRadius.full).toBe('rounded-full');
    });
  });

  describe('shadows', () => {
    it('should have shadow values', () => {
      expect(shadows.none).toBe('shadow-none');
      expect(shadows.sm).toBe('shadow-sm');
      expect(shadows.lg).toBe('shadow-lg');
      expect(shadows['2xl']).toBe('shadow-2xl');
    });
  });

  describe('variants', () => {
    it('should have button variants', () => {
      expect(variants.button.primary).toContain('bg-mythos-terminal-primary');
      expect(variants.button.secondary).toContain('bg-mythos-terminal-surface');
      expect(variants.button.error).toContain('bg-mythos-terminal-error');
    });

    it('should have input variants', () => {
      expect(variants.input.default).toContain('bg-mythos-terminal-surface');
      expect(variants.input.error).toContain('border-red-500');
    });

    it('should have panel variants', () => {
      expect(variants.panel.default).toContain('bg-mythos-terminal-surface');
      expect(variants.panel.elevated).toContain('shadow-lg');
      expect(variants.panel.eldritch).toContain('border-mythos-terminal-primary');
    });
  });

  describe('sizes', () => {
    it('should have button sizes', () => {
      expect(sizes.button.sm).toContain('text-xs');
      expect(sizes.button.md).toContain('text-sm');
      expect(sizes.button.lg).toContain('text-base');
    });

    it('should have input sizes', () => {
      expect(sizes.input.sm).toContain('text-xs');
      expect(sizes.input.md).toContain('text-sm');
    });

    it('should have panel sizes', () => {
      expect(sizes.panel.sm).toBe('p-2');
      expect(sizes.panel.md).toBe('p-3');
      expect(sizes.panel.lg).toBe('p-4');
    });
  });

  describe('animations', () => {
    it('should have transition classes', () => {
      expect(animations.transition).toContain('transition-all');
      expect(animations.transitionSlow).toContain('duration-300');
      expect(animations.transitionFast).toContain('duration-150');
    });

    it('should have hover effects', () => {
      expect(animations.hover).toContain('hover:scale-105');
      expect(animations.hoverSubtle).toContain('hover:bg-opacity-80');
    });

    it('should have focus effects', () => {
      expect(animations.focus).toContain('focus:ring-2');
    });

    it('should have loading states', () => {
      expect(animations.loading).toBe('animate-pulse');
      expect(animations.spinning).toBe('animate-spin');
    });
  });

  describe('layout', () => {
    it('should have flex utilities', () => {
      expect(layout.flex.center).toContain('flex');
      expect(layout.flex.center).toContain('justify-center');
      expect(layout.flex.between).toContain('justify-between');
    });

    it('should have grid utilities', () => {
      expect(layout.grid['2']).toContain('grid-cols-2');
      expect(layout.grid['3']).toContain('grid-cols-3');
    });

    it('should have spacing utilities', () => {
      expect(layout.space['2']).toBe('space-y-2');
      expect(layout.space['4']).toBe('space-y-4');
    });
  });

  describe('breakpoints', () => {
    it('should have breakpoint prefixes', () => {
      expect(breakpoints.sm).toBe('sm:');
      expect(breakpoints.md).toBe('md:');
      expect(breakpoints.lg).toBe('lg:');
    });
  });

  describe('zIndex', () => {
    it('should have z-index values', () => {
      expect(zIndex.dropdown).toBe('z-10');
      expect(zIndex.modal).toBe('z-40');
      expect(zIndex.overlay).toBe('z-100000');
    });
  });

  describe('buildClasses', () => {
    describe('button', () => {
      it('should build button classes with variant and size', () => {
        const classes = buildClasses.button('primary', 'md');
        expect(classes).toContain('inline-flex');
        expect(classes).toContain('bg-mythos-terminal-primary');
        expect(classes).toContain('text-sm');
      });

      it('should include disabled classes when disabled', () => {
        const classes = buildClasses.button('primary', 'md', true);
        expect(classes).toContain('opacity-50');
        expect(classes).toContain('cursor-not-allowed');
      });

      it('should not include disabled classes when enabled', () => {
        const classes = buildClasses.button('primary', 'md', false);
        expect(classes).toContain('cursor-pointer');
        expect(classes).not.toContain('opacity-50');
      });

      it('should work with all button variants', () => {
        const variants: Array<keyof typeof variants.button> = ['primary', 'secondary', 'error', 'success', 'warning'];
        variants.forEach(variant => {
          const classes = buildClasses.button(variant, 'md');
          expect(classes).toBeTruthy();
          expect(classes.length).toBeGreaterThan(0);
        });
      });

      it('should work with all button sizes', () => {
        const sizes: Array<keyof typeof sizes.button> = ['sm', 'md', 'lg'];
        sizes.forEach(size => {
          const classes = buildClasses.button('primary', size);
          expect(classes).toBeTruthy();
          expect(classes.length).toBeGreaterThan(0);
        });
      });
    });

    describe('input', () => {
      it('should build input classes with variant and size', () => {
        const classes = buildClasses.input('default', 'md');
        expect(classes).toContain('block');
        expect(classes).toContain('w-full');
        expect(classes).toContain('bg-mythos-terminal-surface');
      });

      it('should include disabled classes when disabled', () => {
        const classes = buildClasses.input('default', 'md', true);
        expect(classes).toContain('opacity-50');
        expect(classes).toContain('cursor-not-allowed');
      });

      it('should work with error variant', () => {
        const classes = buildClasses.input('error', 'md');
        expect(classes).toContain('border-red-500');
      });
    });

    describe('panel', () => {
      it('should build panel classes with variant and size', () => {
        const classes = buildClasses.panel('default', 'md');
        expect(classes).toContain('rounded');
        expect(classes).toContain('bg-mythos-terminal-surface');
        expect(classes).toContain('p-3');
      });

      it('should work with all panel variants', () => {
        const variants: Array<keyof typeof variants.panel> = ['default', 'elevated', 'eldritch'];
        variants.forEach(variant => {
          const classes = buildClasses.panel(variant, 'md');
          expect(classes).toBeTruthy();
          expect(classes.length).toBeGreaterThan(0);
        });
      });

      it('should work with all panel sizes', () => {
        const sizes: Array<keyof typeof sizes.panel> = ['sm', 'md', 'lg'];
        sizes.forEach(size => {
          const classes = buildClasses.panel('default', size);
          expect(classes).toBeTruthy();
          expect(classes.length).toBeGreaterThan(0);
        });
      });
    });
  });
});
