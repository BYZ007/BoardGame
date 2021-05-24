from enum import Enum
from typing import Tuple

class RoomType(Enum):
    Normal = 0
    Flip = 1
    QuantumPair = 2


class RoomName(Enum):
    BallRoom = 0
    DinningRoom = 1
    BedRoom = 2
    BathRoom = 3
    GameRoom = 4
    LivingRoom = 5


class Direction(Enum):
    Left = (0, -1)
    Right = (0, 1)
    Up = (-1, 0)
    Down = (1, 0)

    @staticmethod
    def invert(direction:Tuple[int])->Tuple[int]:
        return tuple([-i for i in direction])


class CharacterName(Enum):
    Bohiem = 0
    Jessie = 1
    Huxley = 2
    Cirilla = 3
