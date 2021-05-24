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

# +
from enum import Enum
class RoomType(Enum):
    Normal = 0
    Flip = 1
    QuantumPair = 2
    Rotate = 3
    
class RoomName(Enum):
    BallRoom = 0
    DinningRoom = 1
    BedRoom = 2
    BathRoom = 3
    GameRoom = 4 
    LivingRoom = 5

