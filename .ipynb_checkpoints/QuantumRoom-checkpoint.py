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
from Room import Room
from constants import RoomType,RoomName


class QuantumRoom(Room):
    def __init__(self,name:RoomName)->QuantumRoom:
        super().__init__(name,RoomType.QuantumPair)
        self.pair = None
    
    def pair_room(self,room_to_pair:QuantumRoom)->None:
        self.pair = room_to_pair
    
    def enter(self)->None:
        self.stable = True
        if not self.pair.occupied:
            self.pair.stable = False
        
    def exit(self)->None:
        if self.pair.stable:
            self.stable = False
            
    def break_connection_actions(self)->None:
        pass
    
    def make_connection_actions(self)->None:
        pass    
