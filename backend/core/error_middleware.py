from utils.logging_helper import logger
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to help with handling exceptions and
    validation errors
    """
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except StarletteHTTPException as exc:
            logger.error(f"HTTP Exception: {exc.detail}")
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "success": False,
                    "message": exc.detail,
                },
            )
        
        except ValueError as exc:
            logger.error(f"Validation error: {exc}")
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "message": str(exc),
                },
            )
        
        except Exception as exc:
            logger.error(f"Unhandled error: {exc}")
            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "message": str(exc),
                },
            )
