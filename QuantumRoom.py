from __future__ import annotations
from Room import Room
from constants import RoomType, RoomName
import Character


class QuantumRoom(Room):
    def __init__(self, name: RoomName) -> QuantumRoom:
        super().__init__(name, RoomType.QuantumPair)
        self.pair = None

    def pair_room(self, room_to_pair: QuantumRoom) -> None:
        self.pair = room_to_pair

    def enter(self,character:Character.Character,room:Room,direction:tuple) -> None:
        super().enter(character,room,direction)
        if not self.pair.occupied:
            self.pair.stable = False

    def exit(self,character:Character.Character) -> None:
        if self.pair.stable:
            self.stable = False
        self.characters.remove(character)

    def break_connection_actions(self) -> None:
        pass

    def make_connection_actions(self) -> None:
        pass
