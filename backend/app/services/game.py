import random

type Board = list[list[int]]
SIZE = 4
SPAWN = 2
DIRECTIONS = ("up", "down", "left", "right")


class GameError(Exception):
    """Base class for game-related errors."""

def slide_row(row: list[int]) -> list[int]:

    tiles = [value for value in row if value != 0]
    result : list[int] =[]
    i=0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            result.append(tiles[i] * 2)
            i += 2
        else:
            result.append(tiles[i])
            i += 1
    return result + [0] * (len(row) - len(result))

def transpose(board: Board) -> Board:
    return [list(column) for column in zip(*board)]

def move_board(board:Board, direction:str | None) -> Board:
     match direction:
         case "left":
             return [slide_row(row) for row in board]
         case "right":
             return [slide_row(row[::-1])[::-1] for row in board]
         case "up":
             return transpose(move_board(transpose(board), "left"))
         case "down":
             return transpose(move_board(transpose(board), "right"))
         case _:
             raise GameError(f"Invalid direction: {direction}")
         
class Game:
    def __init__(self):
        self._board: Board | None = None
        self._new_board()

    def _new_board(self) -> None:
        """Create a new game board."""
        self._board = [[0] * SIZE for _ in range(SIZE)]
        self._spawn_tile()
        self._spawn_tile()

    def board(self) -> Board:
        if self._board is None:
            raise GameError("Board has not been initialized.")
        return [row[:] for row in self._board]

    def _spawn_tile(self):
        assert self._board is not None, "Board must be initialized before spawning a tile."
        empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if self._board[r][c] == 0]
        if not empty:
            return
        r, c = random.choice(empty)
        self._board[r][c] = SPAWN

    def move(self, direction: str | None) -> tuple[Board, bool]:
        current = self.board()
        moved = move_board(current, direction)
        changed = moved != current
        if changed:
            self._board = moved
            self._spawn_tile()
        return self.board(), changed
    
    

    
    

game = Game()