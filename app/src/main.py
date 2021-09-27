import uvicorn
from logging.config import dictConfig

from fastapi import FastAPI



from app.src.router.endpoints import validation_exception_handler

tags_metadata = [
    {
        "name": "auth",
        "description": "Authorization"
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

    from router.endpoints import app as routers

    app.include_router(routers)

    app.add_exception_handler(ValueError, validation_exception_handler)

    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app)


