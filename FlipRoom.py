from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName, Direction
import Character
import Mansion
from typing import Tuple


class FlipRoom(Room):
    def __init__(self, name: RoomName, mansion: Mansion.Mansion) -> FlipRoom:
        super().__init__(name, RoomType.Flip, mansion)

    def enter(self, character: Character.Character, room: Room, direction: Tuple[int]) -> None:
        super().enter(character,room,direction)

        forward_pos = self.pos+direction
        room_ahead = self.mansion.layout.loc[self.mansion.layout.Position==forward_pos,'Room']
        # fliping of the previous room needs to happen after room_ahead is defined
        # else the position search will return both rooms
        room.flip(self.pos)

        if not room_ahead.empty:
            room_ahead = room_ahead.iloc[0]
            room_ahead.flip(self.pos)

