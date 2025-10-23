import os
from config import Config
from fastapi import FastAPI

from app.http.server import HttpServer


def get_config() -> Config:
    """
    Fetches config. If no value found at key=>value position
    then returns default
    """
    return Config(http_port=os.getenv("HTTP_PORT", "8010"))


def build_app() -> FastAPI:
    cfg = get_config()
    http = HttpServer(cfg)
    app = http.app
    print("\n=== ROUTES REGISTERED ===")

    for r in app.router.routes:
        print(f"{r}")
    print("==========================\n")

    return app


app = build_app()

if __name__ == "__main__":
    from config import Config
    import uvicorn

    cfg = get_config()

    uvicorn.run("app.main:app", host="0.0.0.0", port=int(cfg.http_port))
