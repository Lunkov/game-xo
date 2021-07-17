#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint


class Robot:
  def __init__(self, name):
    self.robotName = name
    self.rx = 1
    self.ry = 1
    self.prx = 1
    self.pry = 1
    self.mvr = -1
    self.mb = None
    self.board = None
  
  def addBoard(self, board):
    h = board.getHeight() + 1
    w = board.getWidth() + 1
    self.mb = [[' ' for j in range(h)] for i in range(w)]
    self.board = board

  def name(self):
    return self.robotName

  def x(self):
    return self.rx

  def y(self):
    return self.ry

  def clearSteps(self):
    for y in range(1, self.board.getHeight() + 1):
      for x in range(1, self.board.getWidth() + 1):
        if self.mb[x][y] == '.':
          self.mb[x][y] = ' '
  
  def iAm(self, x, y):
    return (self.rx == x) and (self.ry == y)
