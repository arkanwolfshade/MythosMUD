import { AppRootViews } from './mythosApp/AppRootViews.js';
import { useMythosApp } from './mythosApp/useMythosApp.js';

function App() {
  const vm = useMythosApp();
  return AppRootViews(vm);
}

export { App };
