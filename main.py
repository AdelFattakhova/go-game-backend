import uvicorn
from logging.config import dictConfig

from fastapi import FastAPI

from starlette.middleware.sessions import SessionMiddleware

tags_metadata = [
    {
        "name": "auth",
        "description": "Authorization"
    },
    {
        "name": "game",
        "description": "Game"
    }
]


def create_app():
    logger_conf = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(levelprefix)s %(asctime)s :: %(client_addr)s - "%(request_line)s" %(status_code)s',
                "use_colors": True
            },
        },
        "handlers": {
            "access": {
                "formatter": "access",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "uvicorn.access": {
                "handlers": ["access"],
                "level": "INFO",
                "propagate": False
            },
        },
    }

    dictConfig(logger_conf)

    app = FastAPI(
        title="Go game",
        description="The documentation of Mobile Go Game API",
        openapi_tags=tags_metadata)

    app.add_middleware(SessionMiddleware, secret_key='!secret')

    from app.src.router.authorization_controller import app as auth_routers
    from app.src.router.game_controller import app as game_routers

    app.include_router(auth_routers)
    app.include_router(game_routers)

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)


