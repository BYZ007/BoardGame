from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName, Direction,Rotation
import Character
import Mansion
from typing import Tuple


class RotateRoom(Room):
    def __init__(self, name: RoomName, mansion: Mansion.Mansion, rotation:Rotation) -> FlipRoom:
        super().__init__(name, RoomType.Flip, mansion)
        self.rotation = rotation

    def enter(self, character: Character.Character, room: Room, direction: Tuple[int]) -> None:
        super().enter(character,room,direction)

        forward_pos = self.pos+direction
        backward_pos = room.pos.value
        left_pos = self.pos+Direction.Left.value
        right_pos = self.pos +Direction.Right.value

        neighbouring_rooms = [self.mansion.layout.loc[self.mansion.layout.Position==pos,'Room'] for pos in [forward_pos,backward_pos,left_pos,right_pos]]
        # fliping of the previous room needs to happen after room_ahead is defined
        # else the position search will return both rooms
        for room in neighbouring_rooms:
            if not room.empty:
                room = room.iloc[0]
                if self.rotation == Rotation.CW:
                    room.rotate_cw(self.pos)
                else:
                    room.rotate_ccw(self.pos)

