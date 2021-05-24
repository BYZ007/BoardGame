from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName


class NormalRoom(Room):
    def __init__(self, name: RoomName) -> NormalRoom:
        super().__init__(name, RoomType.Normal)

    def enter(self, room: Room, direction: tuple) -> None:
        """Connect to the room you're entering from.

        Direction is with respect to the other room from which the player is entering this room.         
        """
        self.stable = True
        self.make_connection(room, -direction)

    def exit(self) -> None:
        pass

    def break_connection_actions(self) -> None:
        pass

    def make_connection_actions(self) -> None:
        pass
