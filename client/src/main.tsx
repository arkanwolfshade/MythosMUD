import { createRoot } from 'react-dom/client';
import App from './App.tsx';
import './index.css';

// Initialize XState Inspector in development mode for visual FSM debugging
// AI: XState Inspector provides real-time visualization of state machines
if (import.meta.env.DEV) {
  import('./utils/xstateInspector').then(({ initializeXStateInspector }) => {
    initializeXStateInspector();
  });
}

createRoot(document.getElementById('root')!).render(<App />);
