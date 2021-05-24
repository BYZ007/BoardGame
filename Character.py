from __future__ import annotations
from constants import Direction
import Room
import Mansion


class Character:
    def __init__(self, name, mansion: Mansion.Mansion) -> Character:
        self.name = name
        self.pos = None
        self.room = None
        self.mansion = mansion

    def intialize_character(self, starting_room: Room.Room) -> None:
        self.room = starting_room
        self.pos = (0, 0)

    def move(self, direction: Direction) -> None:
        next_room = self.room.connections[direction.value]
        if next_room == None:
            next_room = self.mansion.get_next_room()
            if next_room != None:
                next_room.enter(self, self.room, direction.value)
            else:
                print('This path is blocked.')
