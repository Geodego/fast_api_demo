"""
Includes unitary tests for API defined in main.py. These tests can be run automatically in a
 Continuous Integration framework.
"""

from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)


def test_get_path():
    r = client.get("/items/42")
    # tests the status code
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 42"}


def test_get_path_query():
    r = client.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}


def test_get_wrong():
    """
    Test a query not properly specified
    """
    r = client.get("/items/")
    assert r.status_code != 200

