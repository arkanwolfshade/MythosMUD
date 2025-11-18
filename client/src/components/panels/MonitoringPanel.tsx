import React, { useCallback, useEffect, useState } from 'react';
import { EldritchIcon } from '../ui/EldritchIcon';
import { getApiBaseUrl } from '../../utils/config';
import './MonitoringPanel.css';

interface MonitoringData {
  dualConnections?: {
    connection_distribution: {
      total_players: number;
      websocket_only_players: number;
      sse_only_players: number;
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
      total_sse_connections: number;
      avg_connections_per_player: number;
    };
  };
  performance?: {
    connection_establishment: {
      total_connections: number;
      websocket_connections: number;
      sse_connections: number;
      avg_websocket_establishment_ms: number;
      avg_sse_establishment_ms: number;
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

export const MonitoringPanel: React.FC<MonitoringPanelProps> = ({
  baseUrl = getApiBaseUrl(),
  refreshInterval = 5000,
}) => {
  const [monitoringData, setMonitoringData] = useState<MonitoringData>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);

  const fetchMonitoringData = useCallback(async () => {
    try {
      setError(null);

      // Fetch dual connection stats
      const dualConnectionsResponse = await fetch(`${baseUrl}/api/monitoring/dual-connections`);
      const dualConnections = dualConnectionsResponse.ok ? await dualConnectionsResponse.json() : null;

      // Fetch performance stats
      const performanceResponse = await fetch(`${baseUrl}/api/monitoring/performance`);
      const performance = performanceResponse.ok ? await performanceResponse.json() : null;

      // Fetch connection health stats
      const healthResponse = await fetch(`${baseUrl}/api/monitoring/connection-health`);
      const connectionHealth = healthResponse.ok ? await healthResponse.json() : null;

      setMonitoringData({
        dualConnections,
        performance,
        connectionHealth,
      });

      setLastUpdated(new Date());
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch monitoring data');
    } finally {
      setLoading(false);
    }
  }, [baseUrl]);

  useEffect(() => {
    fetchMonitoringData();

    if (refreshInterval > 0) {
      const interval = setInterval(fetchMonitoringData, refreshInterval);
      return () => clearInterval(interval);
    }
  }, [baseUrl, refreshInterval, fetchMonitoringData]);

  const formatNumber = (num: number) => {
    return typeof num === 'number' ? num.toFixed(1) : '0';
  };

  const formatPercentage = (num: number) => {
    return typeof num === 'number' ? `${num.toFixed(1)}%` : '0%';
  };

  const formatTime = (seconds: number) => {
    if (seconds < 60) return `${seconds.toFixed(0)}s`;
    if (seconds < 3600) return `${(seconds / 60).toFixed(1)}m`;
    return `${(seconds / 3600).toFixed(1)}h`;
  };

  if (loading) {
    return (
      <div className="monitoring-panel">
        <div className="panel-header">
          <EldritchIcon name="stats" className="panel-icon" />
          <h3>Connection Monitoring</h3>
        </div>
        <div className="panel-content">
          <div className="loading">Loading monitoring data...</div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="monitoring-panel">
        <div className="panel-header">
          <EldritchIcon name="stats" className="panel-icon" />
          <h3>Connection Monitoring</h3>
        </div>
        <div className="panel-content">
          <div className="error">Error: {error}</div>
          <button onClick={fetchMonitoringData} className="retry-button">
            Retry
          </button>
        </div>
      </div>
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
        {/* Dual Connection Statistics */}
        {monitoringData.dualConnections && (
          <div className="monitoring-section">
            <h4>Dual Connection Distribution</h4>
            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-label">Total Players</div>
                <div className="stat-value">{monitoringData.dualConnections.connection_distribution.total_players}</div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Dual Connections</div>
                <div className="stat-value">
                  {monitoringData.dualConnections.connection_distribution.dual_connection_players}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Dual Connection Rate</div>
                <div className="stat-value">
                  {formatPercentage(monitoringData.dualConnections.connection_distribution.dual_connection_percentage)}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">WebSocket Only</div>
                <div className="stat-value">
                  {monitoringData.dualConnections.connection_distribution.websocket_only_players}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">SSE Only</div>
                <div className="stat-value">
                  {monitoringData.dualConnections.connection_distribution.sse_only_players}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Connection Health */}
        {monitoringData.connectionHealth && (
          <div className="monitoring-section">
            <h4>Connection Health</h4>
            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-label">Total Connections</div>
                <div className="stat-value">{monitoringData.connectionHealth.overall_health.total_connections}</div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Healthy</div>
                <div className="stat-value healthy">
                  {monitoringData.connectionHealth.overall_health.healthy_connections}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Unhealthy</div>
                <div className="stat-value unhealthy">
                  {monitoringData.connectionHealth.overall_health.unhealthy_connections}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Health Rate</div>
                <div className="stat-value">
                  {formatPercentage(monitoringData.connectionHealth.overall_health.health_percentage)}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Avg Connection Age</div>
                <div className="stat-value">
                  {formatTime(monitoringData.connectionHealth.connection_lifecycle.avg_connection_age_seconds)}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Stale Connections</div>
                <div className="stat-value">
                  {monitoringData.connectionHealth.connection_lifecycle.stale_connections}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Performance Metrics */}
        {monitoringData.performance && (
          <div className="monitoring-section">
            <h4>Performance Metrics</h4>
            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-label">Total Connections</div>
                <div className="stat-value">
                  {monitoringData.performance.connection_establishment.total_connections}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">WebSocket Avg</div>
                <div className="stat-value">
                  {formatNumber(monitoringData.performance.connection_establishment.avg_websocket_establishment_ms)}ms
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">SSE Avg</div>
                <div className="stat-value">
                  {formatNumber(monitoringData.performance.connection_establishment.avg_sse_establishment_ms)}ms
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Total Messages</div>
                <div className="stat-value">{monitoringData.performance.message_delivery.total_messages}</div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Avg Delivery Time</div>
                <div className="stat-value">
                  {formatNumber(monitoringData.performance.message_delivery.avg_delivery_time_ms)}ms
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Session Metrics */}
        {monitoringData.dualConnections?.session_metrics && (
          <div className="monitoring-section">
            <h4>Session Management</h4>
            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-label">Total Sessions</div>
                <div className="stat-value">{monitoringData.dualConnections.session_metrics.total_sessions}</div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Session Connections</div>
                <div className="stat-value">
                  {monitoringData.dualConnections.session_metrics.total_session_connections}
                </div>
              </div>
              <div className="stat-item">
                <div className="stat-label">Avg per Session</div>
                <div className="stat-value">
                  {formatNumber(monitoringData.dualConnections.session_metrics.avg_connections_per_session)}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
