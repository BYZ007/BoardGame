from QuantumRoom import QuantumRoom
from Character import Character
from QuantumRoom import QuantumRoom
from FlipRoom import FlipRoom
from NormalRoom import NormalRoom
from constants import *
from Mansion import Mansion

default_mansion = Mansion()
default_character = Character(CharacterName.Bohiem,default_mansion)

default_mansion.rooms = {
    RoomName.BallRoom : QuantumRoom(RoomName.BallRoom,default_mansion),
    RoomName.DinningRoom : QuantumRoom(RoomName.DinningRoom,default_mansion),
    RoomName.GameRoom : FlipRoom(RoomName.GameRoom,default_mansion),
    RoomName.BedRoom : NormalRoom(RoomName.BedRoom,default_mansion)
}

starting_room = default_mansion.rooms[RoomName.BedRoom]
default_character.intialize_character(starting_room)
starting_room.stable = True
starting_room.occupied = True
default_mansion.update_room(starting_room)
default_mansion.unstable_rooms = set(list(default_mansion.rooms.keys()))-set([starting_room.name])
default_mansion._initialize_layout()

