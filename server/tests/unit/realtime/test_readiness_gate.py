def test_sse_events_readiness_gate_returns_503_when_persistence_missing():
    from fastapi.testclient import TestClient

    from server.main import app

    with TestClient(app) as client:
        connection_manager = client.app.state.container.connection_manager

        # Ensure persistence is None to trigger gate
        original = getattr(connection_manager, "persistence", None)
        connection_manager.persistence = None
        try:
            resp = client.get("/api/events/test_player")
            assert resp.status_code == 503
        finally:
            connection_manager.persistence = original
