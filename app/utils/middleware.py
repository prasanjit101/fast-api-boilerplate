from app.utils.logger import logging
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import Request, Response

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ):
        # Log the request information
        logging.info(f"Request received: {request.method} {request.url}")
        response = await call_next(request)
        # Log the response information
        logging.info(f"Response returned: {response.status_code}")
        return response

