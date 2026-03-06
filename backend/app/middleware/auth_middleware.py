from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt, JWTError
from app.core.config import settings


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        public_routes = [
            "/",
            "/docs",
            "/openapi.json",
            "/auth/login",
            "/auth/register"
        ]

        if request.url.path in public_routes:
            return await call_next(request)


        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        try:

            scheme, token = auth_header.split()

            if scheme.lower() != "bearer":
                raise HTTPException(status_code=401, detail="Invalid auth scheme")

    
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.ALGORITHM]
            )

        
            request.state.user = payload

        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        response = await call_next(request)

        return response