from fastapi import Query, Request, status, HTTPException
from requests import HTTPError

from router.base_controller import app
from service.game.game import create_game, RulesEnum, BoardSizeEnum, find_game_by_code, send_move, end_game


@app.post("/create_game", tags=['game'])
async def post_create_game(user_email: str, rules_type: RulesEnum, board_size: BoardSizeEnum):
    try:
        return create_game(user_email=user_email, rules_type=rules_type, board_size=board_size)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)


@app.get("/find_game", tags=['game'])
async def get_find_game(user_email: str, game_code: str):
    try:
        return find_game_by_code(user_email=user_email, game_code=game_code)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)


@app.post("/send_move", tags=['game'])
async def post_send_move(user_email: str, game_token: str, x_axis: int, y_axis: int):
    try:
        return send_move(user_email=user_email, game_token=game_token, x_axis=x_axis, y_axis=y_axis)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)


@app.post("/end_game", tags=['game'])
async def post_end_game(game_token: str, winner_email: str):
    try:
        return end_game(game_token=game_token, winner_email=winner_email)
    except HTTPError as e:
        raise HTTPException(e.errno, e.strerror)