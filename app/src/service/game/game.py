from enum import Enum


class RulesEnum(str, Enum):
    chinese = "chinese"
    japanese = "japanese"


class BoardSizeEnum(str, Enum):
    nine = 9
    thirteen = 13
    nineteen = 19


def create_game(user_email: str, rules_type: RulesEnum, board_size: BoardSizeEnum):
    #TODO call database create game
    #TODO create and bind socket
    return "123123"


def find_game_by_code(user_email: str, game_code: str):
    #TODO find game in db
    #TODO create and bind socket
    return "game_token_navernoe"


def send_move(user_email: str, game_token: str, x_axis: int, y_axis: int):
    #TODO find socket by game token and user (choose second one)
    #TODO send message to 2nd player's socket
    return "OK"


def end_game(game_token: str, winner_email: str):
    #TODO save results for statistics
    return "OK"

