from __future__ import annotations
from constants import Direction, CharacterName, Position
import Room
import Mansion
import logging
from typing import Tuple
logging.basicConfig(level=logging.INFO)


class Character:
    def __init__(self, name: CharacterName, mansion: Mansion.Mansion) -> Character:
        self.name: CharacterName = name
        self.pos: Position = Position()
        self.room: Room = None
        self.mansion: Mansion.Mansion = mansion

    def __str__(self) -> str:
        return self.name.name

    def __repr__(self) -> str:
        return self.name.name

    def intialize_character(self, starting_room: Room.Room) -> None:
        self.room = starting_room
        self.pos.set((0, 0))
        starting_room.characters.append(self)

    def move(self, direction: Tuple[int]) -> None:
        next_room = self.mansion.layout.loc[self.mansion.layout.Position ==
                                            self.pos+direction, 'Room']
        if next_room.empty:
            next_room = self.mansion.get_next_room()
        else:
            next_room = next_room.iloc[0]

        if next_room != None:
            logging.info(
                f'{self.name.name} exiting from {self.room.name.name} and entering {next_room.name.name}')
            self.room.exit(self)
            next_room.enter(self, self.room, direction)
        else:
            logging.info('This path is blocked.')

        
