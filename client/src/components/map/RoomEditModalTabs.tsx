import React from 'react';

export function RoomEditModalTabs(props: {
  activeTab: 'basic' | 'location' | 'properties';
  onTabChange: (tab: 'basic' | 'location' | 'properties') => void;
}): React.ReactElement {
  const tabClass = (tab: 'basic' | 'location' | 'properties') =>
    `px-4 py-2 font-medium text-sm transition-colors rounded-t ${
      props.activeTab === tab
        ? 'text-mythos-terminal-primary border-b-2 border-mythos-terminal-primary bg-mythos-terminal-background'
        : 'text-mythos-terminal-text/70 hover:text-mythos-terminal-text hover:bg-mythos-terminal-background/50'
    }`;

  return (
    <div className="flex gap-1 px-6 pt-4 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
      <button
        onClick={() => props.onTabChange('basic')}
        type="button"
        className={tabClass('basic')}
        aria-selected={props.activeTab === 'basic'}
        role="tab"
      >
        Basic Info
      </button>
      <button
        onClick={() => props.onTabChange('location')}
        type="button"
        className={tabClass('location')}
        aria-selected={props.activeTab === 'location'}
        role="tab"
      >
        Location
      </button>
      <button
        onClick={() => props.onTabChange('properties')}
        type="button"
        className={tabClass('properties')}
        aria-selected={props.activeTab === 'properties'}
        role="tab"
      >
        Properties
      </button>
    </div>
  );
}
