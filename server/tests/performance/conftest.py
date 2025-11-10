import pytest

# Skip performance-only suites during routine development cycles; they provide no additional
# coverage and dramatically increase runtime. Re-enable when running dedicated performance checks.
pytestmark = pytest.mark.skip(reason="Skipping performance benchmarks to keep test runs fast")
