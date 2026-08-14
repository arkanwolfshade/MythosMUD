import React, { useCallback, useEffect, useState } from 'react';
import { getVersionedApiBaseUrl } from '../../utils/config';
import { EldritchIcon } from '../ui/EldritchIcon';
import './MonitoringPanel.css';

interface MonitoringData {
  dualConnections?: {
    connection_distribution: {
      total_players: number;
      websocket_only_players: number;
      dual_connection_players: number;
      dual_connection_percentage: number;
    };
    connection_health: {
      total_connections: number;
      healthy_connections: number;
      unhealthy_connections: number;
      health_percentage: number;
    };
    session_metrics: {
      total_sessions: number;
      total_session_connections: number;
      avg_connections_per_session: number;
    };
    performance_metrics: {
      total_websocket_connections: number;
      avg_connections_per_player: number;
    };
  };
  performance?: {
    connection_establishment: {
      total_connections: number;
      websocket_connections: number;
      avg_websocket_establishment_ms: number;
    };
    message_delivery: {
      total_messages: number;
      avg_delivery_time_ms: number;
    };
  };
  connectionHealth?: {
    overall_health: {
      total_connections: number;
      healthy_connections: number;
      unhealthy_connections: number;
      health_percentage: number;
    };
    connection_lifecycle: {
      avg_connection_age_seconds: number;
      stale_connections: number;
      stale_connection_percentage: number;
    };
  };
}

interface MonitoringPanelProps {
  baseUrl?: string;
  refreshInterval?: number;
}

async function loadMonitoringSnapshot(baseUrl: string): Promise<MonitoringData> {
  const dualConnectionsResponse = await fetch(`${baseUrl}/api/monitoring/dual-connections`);
  const rawDual: unknown = dualConnectionsResponse.ok ? await dualConnectionsResponse.json() : null;
  const performanceResponse = await fetch(`${baseUrl}/api/monitoring/performance`);
  const rawPerformance: unknown = performanceResponse.ok ? await performanceResponse.json() : null;
  const healthResponse = await fetch(`${baseUrl}/api/monitoring/connection-health`);
  const rawHealth: unknown = healthResponse.ok ? await healthResponse.json() : null;
  return {
    dualConnections: rawDual as MonitoringData['dualConnections'],
    performance: rawPerformance as MonitoringData['performance'],
    connectionHealth: rawHealth as MonitoringData['connectionHealth'],
  };
}

const formatNumber = (num: number) => (typeof num === 'number' ? num.toFixed(1) : '0');
const formatPercentage = (num: number) => (typeof num === 'number' ? `${num.toFixed(1)}%` : '0%');
const formatTime = (seconds: number) => {
  if (seconds < 60) return `${seconds.toFixed(0)}s`;
  if (seconds < 3600) return `${(seconds / 60).toFixed(1)}m`;
  return `${(seconds / 3600).toFixed(1)}h`;
};

function MonitoringPanelShell({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="monitoring-panel">
      <div className="panel-header">
        <EldritchIcon name="stats" className="panel-icon" />
        <h3>{title}</h3>
      </div>
      <div className="panel-content">{children}</div>
    </div>
  );
}

function DualConnectionStats({ data }: { data: NonNullable<MonitoringData['dualConnections']> }) {
  return (
    <div className="monitoring-section">
      <h4>Dual Connection Distribution</h4>
      <div className="stats-grid">
        <div className="stat-item">
          <div className="stat-label">Total Players</div>
          <div className="stat-value">{data.connection_distribution.total_players}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Dual Connections</div>
          <div className="stat-value">{data.connection_distribution.dual_connection_players}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Dual Connection Rate</div>
          <div className="stat-value">{formatPercentage(data.connection_distribution.dual_connection_percentage)}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">WebSocket Only</div>
          <div className="stat-value">{data.connection_distribution.websocket_only_players}</div>
        </div>
      </div>
    </div>
  );
}

function ConnectionHealthStats({ data }: { data: NonNullable<MonitoringData['connectionHealth']> }) {
  return (
    <div className="monitoring-section">
      <h4>Connection Health</h4>
      <div className="stats-grid">
        <div className="stat-item">
          <div className="stat-label">Total Connections</div>
          <div className="stat-value">{data.overall_health.total_connections}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Healthy</div>
          <div className="stat-value healthy">{data.overall_health.healthy_connections}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Unhealthy</div>
          <div className="stat-value unhealthy">{data.overall_health.unhealthy_connections}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Health Rate</div>
          <div className="stat-value">{formatPercentage(data.overall_health.health_percentage)}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Avg Connection Age</div>
          <div className="stat-value">{formatTime(data.connection_lifecycle.avg_connection_age_seconds)}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Stale Connections</div>
          <div className="stat-value">{data.connection_lifecycle.stale_connections}</div>
        </div>
      </div>
    </div>
  );
}

function PerformanceStats({ data }: { data: NonNullable<MonitoringData['performance']> }) {
  return (
    <div className="monitoring-section">
      <h4>Performance Metrics</h4>
      <div className="stats-grid">
        <div className="stat-item">
          <div className="stat-label">Total Connections</div>
          <div className="stat-value">{data.connection_establishment.total_connections}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">WebSocket Avg</div>
          <div className="stat-value">
            {formatNumber(data.connection_establishment.avg_websocket_establishment_ms)}ms
          </div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Total Messages</div>
          <div className="stat-value">{data.message_delivery.total_messages}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Avg Delivery Time</div>
          <div className="stat-value">{formatNumber(data.message_delivery.avg_delivery_time_ms)}ms</div>
        </div>
      </div>
    </div>
  );
}

function SessionStats({ data }: { data: NonNullable<MonitoringData['dualConnections']>['session_metrics'] }) {
  return (
    <div className="monitoring-section">
      <h4>Session Management</h4>
      <div className="stats-grid">
        <div className="stat-item">
          <div className="stat-label">Total Sessions</div>
          <div className="stat-value">{data.total_sessions}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Session Connections</div>
          <div className="stat-value">{data.total_session_connections}</div>
        </div>
        <div className="stat-item">
          <div className="stat-label">Avg per Session</div>
          <div className="stat-value">{formatNumber(data.avg_connections_per_session)}</div>
        </div>
      </div>
    </div>
  );
}

function MonitoringStatsBody({ monitoringData }: { monitoringData: MonitoringData }) {
  return (
    <>
      {monitoringData.dualConnections && <DualConnectionStats data={monitoringData.dualConnections} />}
      {monitoringData.connectionHealth && <ConnectionHealthStats data={monitoringData.connectionHealth} />}
      {monitoringData.performance && <PerformanceStats data={monitoringData.performance} />}
      {monitoringData.dualConnections?.session_metrics && (
        <SessionStats data={monitoringData.dualConnections.session_metrics} />
      )}
    </>
  );
}

function useMonitoringPanel(baseUrl: string, refreshInterval: number) {
  const [monitoringData, setMonitoringData] = useState<MonitoringData>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);

  const fetchMonitoringData = useCallback(async () => {
    try {
      setError(null);
      setMonitoringData(await loadMonitoringSnapshot(baseUrl));
      setLastUpdated(new Date());
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch monitoring data');
    } finally {
      setLoading(false);
    }
  }, [baseUrl]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect -- load monitoring + interval
    void fetchMonitoringData();

    if (refreshInterval <= 0) {
      return undefined;
    }

    const interval = setInterval(fetchMonitoringData, refreshInterval);
    return () => {
      clearInterval(interval);
    };
  }, [baseUrl, refreshInterval, fetchMonitoringData]);

  return { monitoringData, loading, error, lastUpdated, fetchMonitoringData };
}

export const MonitoringPanel: React.FC<MonitoringPanelProps> = props => {
  const { baseUrl = getVersionedApiBaseUrl(), refreshInterval = 5000 } = props;
  const { monitoringData, loading, error, lastUpdated, fetchMonitoringData } = useMonitoringPanel(
    baseUrl,
    refreshInterval
  );

  if (loading) {
    return (
      <MonitoringPanelShell title="Connection Monitoring">
        <div className="loading">Loading monitoring data...</div>
      </MonitoringPanelShell>
    );
  }

  if (error) {
    return (
      <MonitoringPanelShell title="Connection Monitoring">
        <div className="error">Error: {error}</div>
        <button onClick={fetchMonitoringData} className="retry-button">
          Retry
        </button>
      </MonitoringPanelShell>
    );
  }

  return (
    <div className="monitoring-panel">
      <div className="panel-header">
        <EldritchIcon name="stats" className="panel-icon" />
        <h3>Connection Monitoring</h3>
        {lastUpdated && <div className="last-updated">Last updated: {lastUpdated.toLocaleTimeString()}</div>}
      </div>
      <div className="panel-content">
        <MonitoringStatsBody monitoringData={monitoringData} />
      </div>
    </div>
  );
};
