from fastapi import FastAPI, HTTPException

from app.db import get_connection

app = FastAPI(title="Travel Planner API", version="0.1.0")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/db-check")
def db_check() -> dict[str, str]:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
                cur.execute("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
                row = cur.fetchone()
                vector_version = row[0] if row else None
        return {
            "db": "ok",
            "pgvector": vector_version or "not installed",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"db error: {type(e).__name__}: {e}")
