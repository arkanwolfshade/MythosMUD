"""Unit tests for the shared hallucination RNG (#714)."""

from unittest.mock import MagicMock, patch

from server.services.hallucination_rng import HallucinationRng


def test_get_returns_same_instance_across_calls() -> None:
    rng = HallucinationRng()
    with patch("server.config.get_config") as get_config:
        get_config.return_value = MagicMock(game=MagicMock(hallucination_rng_seed=None))
        first = rng.get()
        second = rng.get()
    assert first is second
    get_config.assert_called_once()  # config re-read only on first access


def test_seeded_rng_is_deterministic() -> None:
    rng_a = HallucinationRng()
    rng_b = HallucinationRng()
    with patch("server.config.get_config") as get_config:
        get_config.return_value = MagicMock(game=MagicMock(hallucination_rng_seed=42))
        sequence_a = [rng_a.get().random() for _ in range(5)]
    with patch("server.config.get_config") as get_config:
        get_config.return_value = MagicMock(game=MagicMock(hallucination_rng_seed=42))
        sequence_b = [rng_b.get().random() for _ in range(5)]
    assert sequence_a == sequence_b


def test_reset_forces_reread_of_config() -> None:
    rng = HallucinationRng()
    with patch("server.config.get_config") as get_config:
        get_config.return_value = MagicMock(game=MagicMock(hallucination_rng_seed=1))
        _ = rng.get()
    rng.reset()
    with patch("server.config.get_config") as get_config:
        get_config.return_value = MagicMock(game=MagicMock(hallucination_rng_seed=2))
        _ = rng.get()
    assert get_config.call_count == 1  # this `with` block's own mock, confirms reset caused a re-read
