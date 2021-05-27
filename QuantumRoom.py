from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName
import Character
import Mansion
from typing import Tuple


class QuantumRoom(Room):
    def __init__(self, name: RoomName, mansion: Mansion) -> QuantumRoom:
        super().__init__(name, RoomType.QuantumPair, mansion)
        self.pair = None

    def pair_room(self, room_to_pair: QuantumRoom) -> None:
        self.pair = room_to_pair

    def enter(self, character: Character.Character, room: Room, direction: Tuple[int]) -> None:
        super().enter(character, room, direction)
        if not self.pair.occupied:
            self.pair.stable.set(False)

    def exit(self, character: Character.Character) -> None:
        super().exit(character)
        if self.pair.stable and len(self.characters) == 0:
            self.stable.set(False)
