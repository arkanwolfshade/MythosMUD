import './App.css';
import { CommandPanelTest } from './components/CommandPanelTest';
import { logger } from './utils/logger';

function App() {
  const baseUrl = import.meta.env.VITE_API_URL || '/api';

  logger.info('App', 'Component initialized', { baseUrl });

  // Show CommandPanel test
  return <CommandPanelTest />;
}

export default App;
