# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from __future__ import annotations
from QuantumRoom import QuantumRoom
from FlipRoom import FlipRoom
from constants import *
import random


class Mansion():
    def __init__(self)->Mansion:        
        self.unassigned_rooms = list(RoomName).copy()
        self.unstable_rooms = list(RoomName).copy()
        self.rooms = {}
        
    def _set_quantum_pair(self)->None:
        pair = random.sample(self.unassigned_rooms,2)
        room1,room2 = QuantumRoom(pair[0]),QuantumRoom(pair[1])
        self.unassigned_rooms.remove(pair[0])
        self.unassigned_rooms.remove(pair[1])
        self.rooms[pair[0]]=room1
        self.rooms[pair[1]]=room2
        
    def _set_flip_room(self)->None:
        room_name = random.sample(self.unassigned_rooms,1)
        room = FlipRoom(room_name)
        self.unassigned_rooms.remove(room_name)
        self.rooms[room_name]=room
    

    def _set_normal_rooms(self)->None:
        for room_name in self.unassigned_rooms:
            self.rooms[room_name]=



