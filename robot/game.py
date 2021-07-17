#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint


class Game:
  def __init__(self, name, max_steps, timeout):
    self.name = name
    self.step = 0
    self.max_steps = max_steps
    self.timeout = timeout
    self.running = True
    self.board = None
    self.robots = {}

  def addBoard(self, board):
    self.board = board

  def addRobot(self, robot):
    self.robots[robot.name()] = robot
    robot.addBoard(self.board)
    self.board.addRobot(robot)

  def run(self):
    self.board.new()
    self.board.print()
    while self.running:
      self.step = self.step + 1
      for r in self.robots.values():
        r.move()
        if r.iAm(self.board.finishX(), self.board.finishY()):
          self.running = False
      self.print()
      if self.step > self.max_steps or (not self.running):
        self.running = False
        break
      time.sleep(self.timeout)

    print("Game Over")
    print("Winners:")
    
    for r in self.robots.values():
      if r.iAm(self.board.finishX(), self.board.finishY()):
        print("Robot '%s' Win!!!" % (r.name()))

  def print(self):
    print("Game: %s" % (self.name))
    self.board.print()
    print("Step: %d / %d" % (self.step, self.max_steps))
    print("Finish: (%d, %d)" % (self.board.finishX(), self.board.finishY()))
    for r in self.robots.values():
      print("Robot '%s' (%d, %d)" % (r.name(), r.x(), r.y()))
