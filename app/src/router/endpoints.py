import datetime
from typing import List

from fastapi import Query, Request, status, HTTPException
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.src.service.authorization.authorization import signup, login

app = APIRouter()
FROM_DATE = 'from'
TO_DATE = 'to'

def validation_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": str(exc)})
    )


@app.get("/authorize", tags=['auth'])
async def get_authorized(cnums: List[str] = Query(['412740', '427913']),
                                       from_date: datetime.datetime = Query('2021-02-15T00:15:40Z',
                                                                            alias=FROM_DATE),
                                       to_date: datetime.datetime = Query('2021-04-29T13:05:34Z',
                                                                          alias=TO_DATE)):
    return None #authorize()


@app.post("/signup", tags=['auth'])
async def post_signup(email: str, password: str):
    return signup(email=email, password=password)


@app.post("/login", tags=['auth'])
async def post_login(email: str, password: str):
    try:
        return login(email=email, password=password)
    except:
        raise HTTPException(status_code=401, detail="Invalid password!")


