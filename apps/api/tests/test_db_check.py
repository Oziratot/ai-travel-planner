from unittest.mock import patch

import psycopg
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def _db_available() -> bool:
    try:
        with psycopg.connect(
            "postgresql://dev:dev@localhost:5432/travel",
            connect_timeout=2,
        ):
            return True
    except Exception:
        return False


@pytest.mark.skipif(not _db_available(), reason="Postgres not running")
def test_db_check_real_connection():
    response = client.get("/db-check")
    assert response.status_code == 200
    body = response.json()
    assert body["db"] == "ok"
    assert body["pgvector"] != "not installed"


def test_db_check_handles_failure():
    with patch("app.main.get_connection") as mock_get_conn:
        mock_get_conn.side_effect = psycopg.OperationalError("connection refused")
        response = client.get("/db-check")
        assert response.status_code == 500
        assert "OperationalError" in response.json()["detail"]