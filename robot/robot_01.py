#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint

from robot import Robot


class Robot01(Robot):
  pass
  
  #def __init__(self, name):
  #  super(Robot01, self).__init__(name)

  def move(self):
    ct = 0
    while True:
      x = self.rx
      y = self.ry
      ct = ct + 1
      mt = int(random.random()*6)
      if ct > 10:
        self.clearSteps()
        self.mvr = -1

      if mt == 0 and self.mvr == 1:
        continue
      if mt == 4 and self.mvr == 1:
        continue
      if mt == 1 and self.mvr == 0:
        continue
      if mt == 2 and self.mvr == 3:
        continue
      if mt == 3 and self.mvr == 2:
        continue

      if mt == 0:
        x = x + 1
      if mt == 4:
        x = x + 1
      if mt == 5:
        x = x + 1
      if mt == 1:
        x = x - 1
      if mt == 2:
        y = y - 1
      if mt == 3:
        y = y + 1

      if self.board.canMove(x, y):
        if self.board.isWall(x, y):
          self.mb[x][y] = '#'
          continue
          
        if self.mb[x][y] == '.':
            continue
      
      if self.board.canMove(x, y):
        break
    self.mb[self.rx][self.ry] = '.'
    self.prx = self.rx
    self.pry = self.ry
    self.rx = x
    self.ry = y
    self.mvr = mt

