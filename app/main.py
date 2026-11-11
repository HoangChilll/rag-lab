from fastapi import FastAPI

from app.config import Settings


def create_app() -> FastAPI:
    settings = Settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
    )

    @app.get("/health/live")
    async def liveness() -> dict[str, str]:
        return {"status": "ok"}

    return app
