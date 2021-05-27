from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName
import Mansion


class NormalRoom(Room):
    def __init__(self, name: RoomName, mansion: Mansion.Mansion) -> NormalRoom:
        super().__init__(name, RoomType.Normal, mansion)
