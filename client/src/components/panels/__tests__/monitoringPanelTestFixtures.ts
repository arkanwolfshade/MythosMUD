/**
 * Shared fetch mocks and helpers for MonitoringPanel tests.
 */

import type { MockInstance } from 'vitest';

export type MonitoringMocks = {
  dualConnections: {
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
  performance: {
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
  connectionHealth: {
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
};

export const SAMPLE_MONITORING_MOCKS: MonitoringMocks = {
  dualConnections: {
    connection_distribution: {
      total_players: 10,
      websocket_only_players: 5,
      dual_connection_players: 5,
      dual_connection_percentage: 50,
    },
    connection_health: {
      total_connections: 15,
      healthy_connections: 12,
      unhealthy_connections: 3,
      health_percentage: 80,
    },
    session_metrics: {
      total_sessions: 10,
      total_session_connections: 15,
      avg_connections_per_session: 1.5,
    },
    performance_metrics: {
      total_websocket_connections: 15,
      avg_connections_per_player: 1.5,
    },
  },
  performance: {
    connection_establishment: {
      total_connections: 15,
      websocket_connections: 15,
      avg_websocket_establishment_ms: 100,
    },
    message_delivery: {
      total_messages: 1000,
      avg_delivery_time_ms: 50,
    },
  },
  connectionHealth: {
    overall_health: {
      total_connections: 15,
      healthy_connections: 12,
      unhealthy_connections: 3,
      health_percentage: 80,
    },
    connection_lifecycle: {
      avg_connection_age_seconds: 3600,
      stale_connections: 2,
      stale_connection_percentage: 13.3,
    },
  },
};

export const EMPTY_MONITORING_MOCKS: MonitoringMocks = {
  dualConnections: {
    connection_distribution: {
      total_players: 0,
      websocket_only_players: 0,
      dual_connection_players: 0,
      dual_connection_percentage: 0,
    },
    connection_health: {
      total_connections: 0,
      healthy_connections: 0,
      unhealthy_connections: 0,
      health_percentage: 0,
    },
    session_metrics: {
      total_sessions: 0,
      total_session_connections: 0,
      avg_connections_per_session: 0,
    },
    performance_metrics: {
      total_websocket_connections: 0,
      avg_connections_per_player: 0,
    },
  },
  performance: {
    connection_establishment: {
      total_connections: 0,
      websocket_connections: 0,
      avg_websocket_establishment_ms: 0,
    },
    message_delivery: {
      total_messages: 0,
      avg_delivery_time_ms: 0,
    },
  },
  connectionHealth: {
    overall_health: {
      total_connections: 0,
      healthy_connections: 0,
      unhealthy_connections: 0,
      health_percentage: 0,
    },
    connection_lifecycle: {
      avg_connection_age_seconds: 0,
      stale_connections: 0,
      stale_connection_percentage: 0,
    },
  },
};

export const TIMESTAMP_DUAL_CONNECTIONS: MonitoringMocks['dualConnections'] = {
  connection_distribution: {
    total_players: 5,
    websocket_only_players: 3,
    dual_connection_players: 2,
    dual_connection_percentage: 40,
  },
  connection_health: {
    total_connections: 5,
    healthy_connections: 4,
    unhealthy_connections: 1,
    health_percentage: 80,
  },
  session_metrics: {
    total_sessions: 5,
    total_session_connections: 5,
    avg_connections_per_session: 1.0,
  },
  performance_metrics: {
    total_websocket_connections: 5,
    avg_connections_per_player: 1.0,
  },
};

export function mockOkJsonResponse<T>(body: T): Response {
  return {
    ok: true,
    json: async () => body,
  } as Response;
}

type FetchSpy = MockInstance<typeof fetch>;

export function setupSequentialMonitoringFetch(fetchSpy: FetchSpy, mocks: MonitoringMocks): void {
  fetchSpy
    .mockResolvedValueOnce(mockOkJsonResponse(mocks.dualConnections))
    .mockResolvedValueOnce(mockOkJsonResponse(mocks.performance))
    .mockResolvedValueOnce(mockOkJsonResponse(mocks.connectionHealth));
}

export function setupRoundRobinMonitoringFetch(
  fetchSpy: FetchSpy,
  mocks: MonitoringMocks
): { getCallCount: () => number } {
  let callCount = 0;
  const payloads = [mocks.dualConnections, mocks.performance, mocks.connectionHealth];
  fetchSpy.mockImplementation(() => {
    const body = payloads[callCount % 3];
    callCount += 1;
    return Promise.resolve(mockOkJsonResponse(body));
  });
  return { getCallCount: () => callCount };
}

export function setupDualConnectionsUrlFetch(
  fetchSpy: FetchSpy,
  dualConnections: MonitoringMocks['dualConnections']
): { fetchCalls: string[] } {
  const fetchCalls: string[] = [];
  fetchSpy.mockImplementation(url => {
    const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : String(url);
    fetchCalls.push(urlString);

    if (urlString.includes('dual-connections')) {
      return Promise.resolve(mockOkJsonResponse(dualConnections));
    }
    return Promise.resolve(mockOkJsonResponse(null));
  });
  return { fetchCalls };
}

export function setupTimestampMonitoringFetch(fetchSpy: FetchSpy): void {
  fetchSpy
    .mockResolvedValueOnce(mockOkJsonResponse(TIMESTAMP_DUAL_CONNECTIONS))
    .mockResolvedValueOnce(mockOkJsonResponse(null))
    .mockResolvedValueOnce(mockOkJsonResponse(null));
}
