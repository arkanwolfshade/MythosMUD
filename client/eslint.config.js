import js from '@eslint/js';
import jsxA11y from 'eslint-plugin-jsx-a11y';
import playwright from 'eslint-plugin-playwright';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import { globalIgnores } from 'eslint/config';
import globals from 'globals';
import tseslint from 'typescript-eslint';

/** jsx-a11y recommended rules, downgraded to warnings (plan: warn-first). */
const jsxA11yRecommendedWarnRules = Object.fromEntries(
  Object.entries(jsxA11y.flatConfigs.recommended.rules).map(([key, value]) => {
    if (value === 'error') {
      return [key, 'warn'];
    }
    if (Array.isArray(value) && value[0] === 'error') {
      return [key, ['warn', ...value.slice(1)]];
    }
    return [key, value];
  })
);

/** Vitest / RTL files: a11y rules are noise; focus fixes in production components. */
const jsxA11yRulesOff = Object.fromEntries(Object.keys(jsxA11y.rules).map(name => [`jsx-a11y/${name}`, 'off']));

export default tseslint.config([
  globalIgnores(['dist', 'playwright.config.ts', 'playwright-report/**']),
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    files: ['**/*.{ts,tsx}'],
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
      // Line-length checks disabled project-wide; file length / TLOC checks remain
      'max-len': 'off',
      'prefer-const': 'error',
      'no-var': 'error',
      'no-unused-vars': 'off',
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    },
  },
  {
    files: ['src/**/*.{ts,tsx}'],
    ...jsxA11y.flatConfigs.recommended,
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaFeatures: { jsx: true },
      },
    },
    rules: jsxA11yRecommendedWarnRules,
  },
  {
    files: ['src/**/*.test.{ts,tsx}', 'src/**/__tests__/**/*.{ts,tsx}', 'src/**/*Test.tsx'],
    rules: jsxA11yRulesOff,
  },
  {
    files: ['scripts/**/*.js'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.node,
    },
  },
  {
    // Vite / Vitest config runs in Node; eslint-env comments are unsupported in flat config.
    files: ['vite*.ts', 'vitest.config.ts'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.node,
    },
  },
  {
    files: ['src/test/**/*.js'],
    languageOptions: {
      ecmaVersion: 2020,
      globals: {
        ...globals.node,
        ...globals.browser,
        window: 'readonly',
        Element: 'readonly',
      },
    },
  },
  {
    files: ['tests/e2e/**/*.ts', 'tests/e2e/**/*.tsx'],
    extends: [playwright.configs['flat/recommended']],
    languageOptions: {
      ecmaVersion: 2020,
      globals: { ...globals.node, ...globals.browser },
    },
  },
  {
    files: ['playwright.config.ts'],
    rules: {
      // Suppress Playwright connection errors during linting - these are false positives
      // that occur when Playwright tries to validate the config by connecting to browser ports
      // on Windows/IPv6. The error "connect EACCES ::1:XXXXX" is a known issue and does not
      // indicate a configuration problem.
      '@typescript-eslint/ban-ts-comment': 'off',
    },
  },
]);
