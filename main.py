from typing import Any, Dict

import dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, Request, Response, status, HTTPException
from contextlib import asynccontextmanager
# from prometheus_fastapi_instrumentator import Instrumentator

from app.routes.api import router as api_router

# from app.database.indexes import create_db_indexes
from app.settings import settings

app = FastAPI(title="Astrologer App")
app.include_router(api_router)

@app.get("/health", status_code=status.HTTP_200_OK)
async def root(request: Request, response: Response) -> Dict[str, Any]:
    response.status_code = status.HTTP_200_OK
    return {"message": f"Your Horoscope APP is created and is running on port: {settings.PORT}"}

if __name__ == "__main__":
    dotenv.load_dotenv()

    uvicorn.run("main:app", host="0.0.0.0", port=4000, reload=True, log_level='info', loop="asyncio")


