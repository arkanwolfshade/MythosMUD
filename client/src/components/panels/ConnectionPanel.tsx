import React, { useEffect, useState } from 'react';

interface ConnectionPanelProps {
  placeholderText?: string;
}

export const ConnectionPanel: React.FC<ConnectionPanelProps> = ({ placeholderText = 'Connection Panel' }) => {
  const [showTickVerbosity, setShowTickVerbosity] = useState(false);

  useEffect(() => {
    // Load setting from localStorage
    const saved = localStorage.getItem('showTickVerbosity');
    setShowTickVerbosity(saved === 'true');
  }, []);

  const handleTickVerbosityToggle = () => {
    const newValue = !showTickVerbosity;
    setShowTickVerbosity(newValue);
    localStorage.setItem('showTickVerbosity', newValue.toString());
  };

  return (
    <div className="p-4">
      <h3 className="text-lg font-semibold mb-4">{placeholderText}</h3>

      <div className="space-y-4">
        <div className="flex items-center space-x-2">
          <input
            type="checkbox"
            id="tickVerbosity"
            checked={showTickVerbosity}
            onChange={handleTickVerbosityToggle}
            className="rounded"
          />
          <label htmlFor="tickVerbosity" className="text-sm">
            Show Game Tick Verbosity (every 10th tick)
          </label>
        </div>

        {showTickVerbosity && (
          <div className="text-xs text-gray-600">Game ticks will be displayed in the terminal every 10 ticks.</div>
        )}
      </div>
    </div>
  );
};
