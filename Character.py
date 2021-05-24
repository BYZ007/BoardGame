from __future__ import annotations
from constants import Direction, CharacterName
import Room
import Mansion
import logging
logging.basicConfig(level=logging.INFO)

class Character:
    def __init__(self, name: CharacterName, mansion: Mansion.Mansion) -> Character:
        self.name = name
        self.pos = None
        self.room = None
        self.mansion = mansion

    def intialize_character(self, starting_room: Room.Room) -> None:
        self.room = starting_room
        self.pos = (0, 0)
        starting_room.characters.append(self.name)

    def move(self, direction: Direction) -> None:
        next_room = self.room.connections[direction.value]
        if next_room == None:
            next_room = self.mansion.get_next_room()
            if next_room != None:
                logging.info(f'{self.name.name} exiting from {self.room.name.name} and entering {next_room.name.name}')
                self.room.exit(self)
                next_room.enter(self, self.room, direction.value)
            else:
                print('This path is blocked.')
