from default_config import *
from constants import *
import pandas as pd

def test_quantum_rooms()->None:
    # BallRoom and DinningRoom are the 2 quantum rooms
    room1 = default_mansion.rooms[RoomName.BallRoom]
    room2 = default_mansion.rooms[RoomName.DinningRoom]

    room1.enter(default_character,Direction)