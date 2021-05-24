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


class FlipRoom(Room):
    def __init__(self,name:RoomName)->FlipRoom:
        super().__init__(name,RoomType.Flip)
    
    def enter(self,room:Room,direction:tuple)->None:
        self.stable = True
        connected_room = self.connections[direction]        

        if connected_room!=None:
            self.make_connection(connected_room,-direction)
            connected_room.break_connection(-direction)
            
        self.make_connection(room,direction)
        
    def exit(self)->None:
        pass
            
    def break_connection_actions(self)->None:
        pass
    
    def make_connection_actions(self)->None:
        pass    
