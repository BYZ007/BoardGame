from __future__ import annotations

from Character import Character
from QuantumRoom import QuantumRoom
from FlipRoom import FlipRoom
from NormalRoom import NormalRoom
from Room import Room
from constants import *
import random
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)


class Mansion():
    def __init__(self) -> Mansion:
        self.unassigned_rooms = None
        self.unstable_rooms = None
        self.rooms = None
        self.layout = None
        self.n_rooms = len(RoomName)
        self.characters = None

    def _set_quantum_pair(self) -> None:
        pair = random.sample(self.unassigned_rooms, 2)
        room1, room2 = QuantumRoom(pair[0], self), QuantumRoom(pair[1], self)
        room1.pair_room(room2)
        room2.pair_room(room1)
        self.unassigned_rooms -= set(pair)
        self.rooms[pair[0]] = room1
        self.rooms[pair[1]] = room2

    def _set_flip_room(self) -> None:
        room_name = random.sample(self.unassigned_rooms, 1)[0]
        room = FlipRoom(room_name, self)
        self.unassigned_rooms -= set([room_name])
        self.rooms[room_name] = room

    def _set_normal_rooms(self) -> None:
        """Set the remaining rooms as normal

        Should be done as the last step of room initialization. All remaining rooms in
        `self.unassigned_rooms` will be set to normal and `self.unassigned_rooms` will be set to empty.
        """

        for room_name in self.unassigned_rooms:
            room = NormalRoom(room_name, self)
            self.rooms[room_name] = room

        self.unassigned_rooms = []

    def _initialize_rooms(self) -> None:
        self._set_quantum_pair()
        self._set_flip_room()
        self._set_normal_rooms()

    def _initialize_layout(self) -> None:
        self.layout = pd.DataFrame(
            {
                'Room Name': list(self.rooms.keys()),
                'Room Type': [room.room_type.name for room in self.rooms.values()],
                'Stable': [room.stable for room in self.rooms.values()],
                'Occupied': [room.occupied for room in self.rooms.values()],
                'Characters': [room.characters for room in self.rooms.values()],
                'Connections': [room.connections for room in self.rooms.values()]
            })

        self.layout.set_index('Room Name', inplace=True)

    def get_next_room(self) -> Room:
        if len(self.unstable_rooms) != 0:
            sampled_room_name = random.sample(self.unstable_rooms, 1)[0]
            self.unstable_rooms -= set([sampled_room_name])

            sampled_room = self.rooms[sampled_room_name]
            logging.info(f'{sampled_room.name.name} drawn as the next room')
            return sampled_room
        else:
            logging.info(f'No more rooms available')
            return None

    def _initailize_characters(self) -> None:
        starting_room = self.get_next_room()
        starting_room.stable = True
        starting_room.occupied = True
        self.update_room(starting_room)

        for name in list(CharacterName):
            character = Character(name, self)
            self.characters[name] = character
            character.intialize_character(starting_room)

    def setup_game(self) -> None:
        self.unassigned_rooms = set(list(RoomName))
        self.unstable_rooms = set(list(RoomName))
        self.rooms = {}
        self.layout = None
        self.characters = {}

        self._initialize_rooms()
        self._initialize_layout()
        self._initailize_characters()

    def update_room(self, room: Room) -> None:
        logging.info(f'Updating room {room.name.name}')
        self.layout.loc[room.name, 'Stable'] = room.stable
        self.layout.loc[room.name, 'Occupied'] = room.occupied
