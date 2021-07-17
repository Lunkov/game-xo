#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint


class Board:

  def __init__(self, width, height, walls):
    self.count_walls = walls
    self.height = height
    self.width = width
    self.xf = 0
    self.yf = 0
    self.board = [[' ' for j in range(height + 1)] for i in range(width + 1)]
    self.robots = {}

  def addRobot(self, robot):
    self.robots[robot.name()] = robot

  def print(self):
    clear = lambda: os.system('clear') 
    clear()
    for y in range(1, self.height + 1):
      for x in range(1, self.width + 1):
        print('+-', end='')
      print('+')
      for x in range(1, self.width + 1):
        print('|', end='')
        rbt = False
        for r in self.robots.values():
          if r.iAm(x, y):
            print(r.name(), end='')
            rbt = True
            break
        if not rbt:
          print(self.board[x][y], end='')

      print('|')

    for x in range(1, self.width + 1):
      print('+-', end='')
    print('+')

  def makeWalls(self):
    for wall in range(1, self.count_walls + 1):
      x = int(random.random()*self.width) + 1
      y = int(random.random()*self.height) + 1
      self.board[x][y] = '#'
    self.board[1][1] = ' '
    self.board[1][2] = ' '
    self.board[2][1] = ' '

  def makeFinish(self):
    self.xf = self.width
    self.yf = int(random.random()*self.height - 1) + 1
    self.board[self.xf][self.yf] = '0'

  def new(self):
    self.makeWalls()
    self.makeFinish()

  def getWidth(self):
    return self.width
    
  def getHeight(self):
    return self.height

  def isWall(self, x, y):
    if self.canMove(x, y):
      return self.board[x][y] == '#'
    return True

  def canMove(self, x, y):
    if x < 1:
      return False
    if x > self.width:
      return False
    if y < 1:
      return False
    if y > self.height:
      return False
      
    return self.board[x][y] != '#'

  def isFinish(self, x, y):
    return self.board[x][y] == '0'

  def finish(self):
    return self.xf, self.yf

  def finishX(self):
    return self.xf

  def finishY(self):
    return self.yf
