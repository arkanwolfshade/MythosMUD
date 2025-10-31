from fastapi.testclient import TestClient

from server.main import app
from server.realtime.connection_manager import connection_manager


def test_sse_events_readiness_gate_returns_503_when_persistence_missing():
    # Ensure persistence is None to trigger gate
    original = connection_manager.persistence
    connection_manager.persistence = None
    try:
        client = TestClient(app)
        resp = client.get("/api/events/test_player")
        assert resp.status_code == 503
    finally:
        connection_manager.persistence = original
