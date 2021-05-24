from __future__ import annotations
from QuantumRoom import QuantumRoom
from FlipRoom import FlipRoom
from NormalRoom import NormalRoom
from constants import *
import random


class Mansion():
    def __init__(self) -> Mansion:
        self.unassigned_rooms = list(RoomName).copy()
        self.unstable_rooms = list(RoomName).copy()
        self.rooms = {}

    def _set_quantum_pair(self) -> None:
        pair = random.sample(self.unassigned_rooms, 2)
        room1, room2 = QuantumRoom(pair[0]), QuantumRoom(pair[1])
        self.unassigned_rooms.remove(pair[0])
        self.unassigned_rooms.remove(pair[1])
        self.rooms[pair[0]] = room1
        self.rooms[pair[1]] = room2

    def _set_flip_room(self) -> None:
        room_name = random.sample(self.unassigned_rooms, 1)
        room = FlipRoom(room_name)
        self.unassigned_rooms.remove(room_name)
        self.rooms[room_name] = room

    def _set_normal_rooms(self) -> None:
        """Set the remaining rooms as normal

        Should be done as the last step of room initialization. All remaining rooms in
        `self.unassigned_rooms` will be set to normal and `self.unassigned_rooms` will be set to empty.
        """

        for room_name in self.unassigned_rooms:
            self.rooms[room_name] = NormalRoom(room_name)

        self.unassigned_rooms = []

    def initialize_rooms(self) -> None:
        self._set_quantum_pair()
        self._set_flip_room()
        self._set_normal_rooms()
