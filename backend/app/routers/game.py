from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

from app.services.game import GameError, game

router = APIRouter(prefix="/api/game", tags=["game"])


class MoveRequest(BaseModel):
    direction: str

class BoardResponse(BaseModel):
    board:list[list[int]]

class MoveResponse(BaseModel):
    board: list[list[int]]
    changed: bool


@router.get("")
def get_board() -> BoardResponse:
    return BoardResponse(board=game.board())


@router.post("/move")
def move(payload: MoveRequest | None = None) -> MoveResponse:
    direction = payload.direction if payload else None
    try:
        board, changed = game.move(direction)
    except GameError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return MoveResponse(board=board, changed=changed)


@router.post("/new")
def new_game() -> BoardResponse:
    game._new_board()
    return BoardResponse(board=game.board())