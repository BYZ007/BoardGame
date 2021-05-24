from __future__ import annotations
from abc import ABC, abstractmethod
from constants import RoomType, RoomName


class Room(ABC):
    def __init__(self, name: RoomName, room_type: RoomType) -> Room:
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

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def break_connection_actions(self):
        pass

    @abstractmethod
    def make_connection_actions(self):
        pass

    @classmethod
    def break_connection(self, direction: tuple) -> None:
        """Break connection in the direction specified

        Will break connection in the direction with respect to this room instance if any exists.
        The connecting room will break_connection in the negative direction. 
        """
        connected_room = self.connections[direction]
        if connected_room != None:
            self.connections[direction] = None
            connected_room.break_connection(-direction)
            self.break_connection_actions()

    @classmethod
    def make_connection(self, connecting_room: Room, direction: tuple) -> None:
        current_connected_room = self.connections[direction]
        if (current_connected_room != None) and (current_connected_room.name != connecting_room.name):
            current_connected_room.break_connection(-direction)
            self.connections[direction] = connecting_room
            connecting_room.make_connection(self, -direction)

        self.make_connection_actions()

    @classmethod
    def break_all_connections(self) -> None:
        for direction in self.connections.keys():
            self.break_connection(direction)
