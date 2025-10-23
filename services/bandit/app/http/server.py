from fastapi import FastAPI, APIRouter

from config import Config


class HttpServer:
    """
    FastApi based server
    """

    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.app = FastAPI(title="LOR", version="0.1.0")
        self._mount_health_router()

    def _mount_health_router(self):
        router = APIRouter(tags=["health"])

        @router.get("/health")
        def health():
            return {"Status": "OK"}

        self.app.include_router(router)
