import os, sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def log_data_path():
    return 'tests/data/unit-test.logs'
