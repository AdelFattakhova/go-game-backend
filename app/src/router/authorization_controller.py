from fastapi import Query, Request, status, HTTPException
from requests import HTTPError

from app.src.service.authorization.authorization import signup, login, restore_password
from router.base_controller import app


@app.post("/signup", tags=['auth'])
async def post_signup(email: str, password: str):
    try:
        return signup(email=email, password=password)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)


@app.post("/login", tags=['auth'])
async def post_login(email: str, password: str):
    try:
        return login(email=email, password=password)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)


@app.post("/restore_password", tags=['auth'])
async def post_restore_password(email: str):
    try:
        return restore_password(email=email)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)
