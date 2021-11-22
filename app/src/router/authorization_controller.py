from fastapi import Query, Request, status, HTTPException
from requests import HTTPError
from starlette.responses import RedirectResponse
from starlette.requests import Request

from app.src.service.authorization.authorization import signup, login, restore_password
from router.base_controller import app

from util.firebase import oauth


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


@app.get('/login_by_google', tags=['auth'])
async def get_login_by_google(request: Request):
    redirect_uri = request.url_for('auth_by_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth_response", status_code=200)
async def auth_response(token: str, email: str):
    return {'token': token, 'email': email}


@app.get('/logout_by_google', tags=['auth'])  # Tag it as "authentication" for our docs
async def get_logout_by_google(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


@app.route('/auth_by_google')
async def auth_by_google(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    token_dict = dict(token)
    user_dict = dict(user)

    # Save the user
    request.session['user'] = user_dict

    resp_token = token_dict["access_token"]
    email = user_dict["email"]

    return RedirectResponse(url=f'/auth_response?token={resp_token}&email={email}')

