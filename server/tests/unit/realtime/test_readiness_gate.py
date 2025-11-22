def test_sse_events_readiness_gate_returns_503_when_persistence_missing():
    import uuid

    from fastapi.testclient import TestClient

    from server.main import app

    with TestClient(app) as client:
        connection_manager = client.app.state.container.connection_manager

        # Ensure persistence is None to trigger gate
        original = getattr(connection_manager, "persistence", None)
        connection_manager.persistence = None
        try:
            # Use valid UUID string for player_id (endpoint expects UUID)
            test_player_id = str(uuid.uuid4())
            resp = client.get(f"/api/events/{test_player_id}")
            assert resp.status_code == 503
        finally:
            connection_manager.persistence = original
