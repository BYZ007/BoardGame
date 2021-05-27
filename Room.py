from __future__ import annotations
from abc import ABC, abstractmethod
from constants import CharacterName, RoomType, RoomName, Flag, Position
import Character
import Mansion
import logging
from typing import Tuple, List
import numpy as np
logging.basicConfig(level=logging.INFO)


class Room(ABC):
    def __init__(self, name: RoomName, room_type: RoomType, mansion: Mansion.Mansion) -> Room:
        self.name: RoomName = name
        self.room_type: RoomType = room_type
        self.pos: Position = Position()
        self.occupied: Flag = Flag('occupied')
        self.stable: Flag = Flag('stable')
        self.characters: List[CharacterName] = []
        self.mansion = mansion

    def __str__(self) -> str:
        return self.name.name

    def __repr__(self) -> str:
        return self.name.name

    def enter(self, character: Character.Character, room: Room, direction: Tuple[int]) -> None:
        """Connect to the room you're entering from.

        Direction is with respect to the other room from which the player is entering this room.         
        """
        self.stable.set(True)
        self.characters.append(character)
        self.occupied.set(True)
        character.room = self        
        self.pos.set(room.pos+direction)
        character.pos.set(self.pos)

    def exit(self, character: Character.Character) -> None:
        self.characters.remove(character)
        if len(self.characters) == 0:
            self.occupied.set(False)

    def rotate_cw(self, center_pos: tuple[int]) -> None:
        vector = np.array(self.pos.value)-np.array(center_pos.value)
        self.pos.set(tuple(np.matmul(vector, np.array([[0, 1], [-1, 0]]))))
        for character in self.characters:
            character.pos.set(self.pos)
        logging.info(
            f'room {self.name.name} rotated cw to {self.pos}')

    def rotate_ccw(self, center_pos: tuple[int]) -> None:
        vector = np.array(self.pos.value)-np.array(center_pos.value)
        self.pos.set(tuple(np.matmul(vector, np.array([[0, -1], [1, 0]]))))
        for character in self.characters:
            character.pos.set(self.pos)
        logging.info(
            f'room {self.name.name} rotated ccw to {self.pos}')

    def flip(self, center_pos: Tuple[int]) -> None:
        direction = np.array(center_pos.value)-np.array(self.pos.value)
        new_pos = np.array(self.pos.value)+direction*2
        self.pos.set(tuple(new_pos))
        for character in self.characters:
            character.pos.set(self.pos)
        logging.info(
            f'room {self.name.name} flipped to {self.pos}')
