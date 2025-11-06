from fastapi.testclient import TestClient

from server.main import app


def test_sse_events_readiness_gate_returns_503_when_persistence_missing():
    # AI Agent: Access connection_manager via app.state.container (no longer a global)
    connection_manager = app.state.container.connection_manager

    # Ensure persistence is None to trigger gate
    original = connection_manager.persistence
    connection_manager.persistence = None
    try:
        client = TestClient(app)
        resp = client.get("/api/events/test_player")
        assert resp.status_code == 503
    finally:
        connection_manager.persistence = original
