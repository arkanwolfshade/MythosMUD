from __future__ import annotations

from datetime import UTC, datetime
from types import SimpleNamespace
from unittest.mock import Mock

from fastapi.testclient import TestClient

from server.api import game
from server.main import app


class TestGameTimeApi:
    """Integration coverage for the /game/time endpoint."""

    def setup_method(self) -> None:
        self.client = TestClient(app)

    def teardown_method(self) -> None:
        if hasattr(app.state, "container"):
            delattr(app.state, "container")

    def test_game_time_endpoint_returns_calendar_payload(self, monkeypatch) -> None:
        """Ensure the endpoint surfaces formatted Mythos time metadata."""

        chronicle = Mock()
        mythos_dt = datetime(1930, 1, 5, 14, 0, tzinfo=UTC)
        components = SimpleNamespace(
            mythos_datetime=mythos_dt,
            month_name="January",
            day_of_month=5,
            week_of_month=1,
            day_of_week=2,
            day_name="Tertius",
            season="winter",
            is_daytime=True,
            is_witching_hour=False,
            daypart="afternoon",
        )
        chronicle.get_current_mythos_datetime.return_value = mythos_dt
        chronicle.get_calendar_components.return_value = components
        chronicle.format_clock.return_value = "14:00 Mythos"
        monkeypatch.setattr(game, "get_mythos_chronicle", lambda: chronicle)

        holiday_entry = SimpleNamespace(
            id="feast_of_yig",
            name="Feast of Yig",
            tradition="mythos",
            season="winter",
            duration_hours=24,
            bonus_tags=["serpent"],
            notes="Serpentine reverence",
        )

        app.state.container = SimpleNamespace(
            holiday_service=SimpleNamespace(
                refresh_active=lambda _dt: [holiday_entry],
                get_upcoming_holidays=lambda count=3: [holiday_entry],
                get_active_holiday_names=lambda: [holiday_entry.name],
                get_upcoming_summary=lambda count=3: ["01/06 - Feast of Yig"],
            )
        )

        response = self.client.get("/game/time")
        assert response.status_code == 200
        payload = response.json()

        assert payload["mythos_clock"] == "14:00 Mythos"
        assert payload["daypart"] == "afternoon"
        assert payload["active_holidays"][0]["id"] == "feast_of_yig"
        assert payload["upcoming_holidays"][0]["name"] == "Feast of Yig"
