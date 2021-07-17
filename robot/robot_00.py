#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint

from robot import Robot


class Robot00(Robot):
  pass
  
  def move(self):
    while True:
      x = self.rx
      y = self.ry
      mt = int(random.random()*4)
      if mt == 0:
        x = x + 1
      if mt == 1:
        x = x - 1
      if mt == 2:
        y = y - 1
      if mt == 3:
        y = y + 1
      if self.board.canMove(x, y):
        if self.board.isWall(x, y):
          continue
      if self.board.canMove(x, y):
        break
    self.rx = x
    self.ry = y
    
