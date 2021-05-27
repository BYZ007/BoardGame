from __future__ import annotations

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
    def invert(direction: Tuple[int]) -> Tuple[int]:
        return tuple([-i for i in direction])


class CharacterName(Enum):
    Bohiem = 0
    Jessie = 1
    Huxley = 2
    Cirilla = 3


class Rotation(Enum):
    CW = 0
    CCW = 1
    

class Flag:
    def __init__(self, name) -> Flag:
        self.name: str = name
        self.value: bool = False

    def __repr__(self) -> str:
        return str(self.value)

    def __call__(self) -> bool:
        return self.value

    def set(self, value: bool) -> None:
        self.value = value

    def __eq__(self, other: bool) -> bool:
        return self.value == other

    def __ne__(self, other: bool) -> bool:
        return self.value != other


class Position:
    def __init__(self) -> Position:
        self.value: Tuple[int] = None

    def __repr__(self) -> str:
        return str(self.value)

    def __call__(self) -> bool:
        return self.value

    def set(self, value: Tuple[int]) -> None:
        if isinstance(value,Position):
            self.value = value.value
        else:
            self.value = value

    def __add__(self, other: Tuple[int]) -> Tuple[int]:
        return tuple([i+j for i, j in (self.value, other)])

    def __eq__(self, other: Tuple[int]) -> bool:
        return self.value == other

    def __ne__(self, other: Tuple[int]) -> bool:
        return self.value != other

    def __sub__(self,other: Tuple[int])->Tuple[int]:
        return tuple([i-j for i, j in (self.value, other)])
