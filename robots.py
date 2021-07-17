#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import time
from array import *
from pprint import pprint

count_walls = 100
height = 15
width = 30
board = [[' ' for j in range(height + 1)] for i in range(width + 1)]

rx = 1
ry = 1
prx = 1
pry = 1
mvr = -1
step = False
max_steps = 300
running = True

def print_board():
  clear = lambda: os.system('clear') 
  clear()
  for y in range(1, height + 1):
    for x in range(1, width + 1):
      print('+-', end='')
    print('+')
    for x in range(1, width + 1):
      print('|', end='')
      if rx == x and ry == y:
        print('k', end='')
      else:
        print(board[x][y], end='')
    print('|')

  for x in range(1, width + 1):
    print('+-', end='')
  print('+')
  print("Step: %d" % (step))

def make_walls():
  for wall in range(1, count_walls + 1):
    x = int(random.random()*width)
    y = int(random.random()*height)
    board[x][y] = '#'

def make_finish():
  x = width
  y = int(random.random()*height - 1)
  board[x][y] = '0'

def move_robot_v1():
  global rx, ry
  while True:
    x = rx
    y = ry
    mt = int(random.random()*4)
    if mt == 0:
      x = x + 1
    if mt == 1:
      x = x - 1
    if mt == 2:
      y = y - 1
    if mt == 3:
      y = y + 1
    if x < 1:
      continue
    if x > width:
      continue
    if y < 1:
      continue
    if y > height:
      continue
    if board[x][y] == '#':
      continue
    break
  rx = x
  ry = y

def clear_steps_robot():
  for y in range(1, height + 1):
    for x in range(1, width + 1):
      if board[x][y] == '.':
        board[x][y] = ' '
 
def move_robot_v2():
  global rx, ry, mvr, prx, pry
  ct = 0
  while True:
    x = rx
    y = ry
    ct = ct + 1
    mt = int(random.random()*6)
    if ct > 10:
      clear_steps_robot()
      mvr = -1

    if mt == 0 and mvr == 1:
      continue
    if mt == 4 and mvr == 1:
      continue
    if mt == 1 and mvr == 0:
      continue
    if mt == 2 and mvr == 3:
      continue
    if mt == 3 and mvr == 2:
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
    if x < 1:
      continue
    if x > width:
      clear_steps_robot()
      continue
    if y < 1:
      continue
    if y > height:
      continue
    if board[x][y] == '.':
      continue
    if board[x][y] == '#':
      continue

    break
  board[rx][ry] = '.'
  prx = rx
  pry = ry
  rx = x
  ry = y
  mvr = mt

def move_robot():
  global rx, ry, mvr, prx, pry
  ct = 0
  mt = 0
  while True:
    x = rx
    y = ry
    if ct > 10:
      clear_steps_robot()
      mvr = -1

    if mt == 0 and mvr == 1:
      mt = 2
      continue
    if mt == 4 and mvr == 1:
      mt = 2
      continue
    if mt == 1 and mvr == 0:
      continue
    if mt == 2 and mvr == 3:
      continue
    if mt == 3 and mvr == 2:
      continue

    if mt == 0:
      x = x + 1
    if mt == 1:
      x = x - 1
    if mt == 2:
      y = y - 1
    if mt == 3:
      y = y + 1
    if x < 1:
      continue
    if x > width:
      continue
    if y < 1:
      continue
    if y > height:
      continue
    if board[x][y] == '.':
      continue
    if board[x][y] == '#':
      continue

    break
  board[rx][ry] = '.'
  prx = rx
  pry = ry
  rx = x
  ry = y
  mvr = mt

make_walls()
make_finish()

while running:
  print_board()
  step = step + 1
  move_robot_v2()
  time.sleep(0.5)
  if step > max_steps:
    running = False
  if board[rx][ry] == '0':
    running = False

print("Game Over")

if board[rx][ry] == '0':
  print("Robot Win!!!")
