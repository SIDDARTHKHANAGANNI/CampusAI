from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from backend.app.core.logger import logger


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    logger.warning(
        f"HTTP Exception | {request.method} {request.url.path} | "
        f"Status: {exc.status_code} | Detail: {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    logger.warning(
        f"Validation Error | {request.method} {request.url.path} | "
        f"Errors: {exc.errors()}"
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": exc.errors()
        }
    )


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    logger.exception(
        f"Unhandled Exception | {request.method} {request.url.path}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )