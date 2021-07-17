#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint

from game import Game
from board import Board
from robot_00 import Robot00
from robot_01 import Robot01
from robot_02 import Robot02


game = Game("Robot 01", 300, 0.3)
board = Board(30, 15, 100)

r01 = Robot00("1")
r02 = Robot01("2")
r03 = Robot01("3")
r04 = Robot02("4")

game.addBoard(board)
game.addRobot(r01)
game.addRobot(r02)
game.addRobot(r03)
game.addRobot(r04)
game.run()
