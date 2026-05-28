import os
from contextlib import contextmanager
from typing import Iterator

import psycopg
from psycopg import Connection

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://dev:dev@localhost:5432/travel",
)


@contextmanager
def get_connection() -> Iterator[Connection]:
    """Yield a Postgres connection. Closes automatically on exit."""
    conn = psycopg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()