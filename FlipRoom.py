from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName, Direction
import Character
import Mansion
from typing import Tuple


class FlipRoom(Room):
    def __init__(self, name: RoomName, mansion: Mansion.Mansion) -> FlipRoom:
        super().__init__(name, RoomType.Flip, mansion)

    def enter(self, character: Character.Character, room: Room, direction: Tuple[str]) -> None:
        self.stable = True
        self.occupied = True
        self.characters.append(character.name)
        connected_room = self.connections[direction]

        if connected_room != None:
            self.make_connection(connected_room, Direction.invert(direction))
            connected_room.break_connection(Direction.invert(direction))

        self.mansion.update_room(self)

        self.make_connection(room, direction)

    def break_connection_actions(self) -> None:
        pass

    def make_connection_actions(self) -> None:
        pass
