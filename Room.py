from __future__ import annotations
from abc import ABC, abstractmethod
from constants import RoomType, RoomName, Direction
import Character
import Mansion
import logging
from typing import Tuple
logging.basicConfig(level=logging.INFO)



class Room(ABC):
    def __init__(self, name: RoomName, room_type: RoomType, mansion: Mansion.Mansion) -> Room:
        self.name = name
        self.room_type = room_type
        self.connections = {
            (0, 1): None,
            (1, 0): None,
            (0, -1): None,
            (-1, 0): None
        }
        self.occupied = False
        self.stable = False
        self.characters = []
        self.mansion = mansion

    def enter(self, character: Character.Character, room: Room, direction: Tuple[int]) -> None:
        """Connect to the room you're entering from.

        Direction is with respect to the other room from which the player is entering this room.         
        """
        self.stable = True
        self.make_connection(room, Direction.invert(direction))
        self.characters.append(character.name)
        self.occupied = True
        self.mansion.update_room(self)
        character.room = self

    def exit(self, character: Character.Character) -> None:
        self.characters.remove(character.name)
        if len(self.characters) == 0:
            self.occupied = False
        self.mansion.update_room(self)

    @abstractmethod
    def break_connection_actions(self):
        pass

    @abstractmethod
    def make_connection_actions(self):
        pass

    def break_connection(self, direction: tuple) -> None:
        """Break connection in the direction specified

        Will break connection in the direction with respect to this room instance if any exists.
        The connecting room will break_connection in the negative direction. 
        """
        connected_room = self.connections[direction]
        if connected_room != None:            
            logging.info(f'Breaking connections between {self.name.name} and {connected_room.name.name}')
            self.connections[direction] = None
            connected_room.connections[Direction.invert(direction)] = None
            self.break_connection_actions()
            connected_room.break_connection_actions()

    def make_connection(self, connecting_room: Room, direction: tuple) -> None:
        current_connected_room = self.connections[direction]
        if (current_connected_room != None) and (current_connected_room.name != connecting_room.name):
            current_connected_room.break_connection(
                Direction.invert(direction))

        self.connections[direction] = connecting_room
        connecting_room.make_connection(self, Direction.invert(direction))

        self.make_connection_actions()

    def break_all_connections(self) -> None:
        for direction in self.connections.keys():
            self.break_connection(direction)
