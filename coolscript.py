from random import *
from kandinsky import *
from ion import *
state=True
halfLenght=int(320/2)
fill_rect(0,0,320,222,(255,255,255))
while state==True:
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  if keydown(KEY_HOME):
    state=False
  if keydown(KEY_ZERO):
    for i in range(320):
      draw_line(0,0,319-i,222,(r,g,b))
      draw_line(320,222,0+i,0,(r,g,b))
  if keydown(KEY_DOT):
    for i in range(320):
      draw_line(0,222,i,-1,(r,g,b))
      draw_line(320,-1,320-i,222,(r,g,b))
  if keydown(KEY_EE):
    for i in range(halfLenght):
      draw_line(halfLenght-i,0,halfLenght-i,222,(r,g,b))
      draw_line(halfLenght+i,0,halfLenght+i,222,(r,g,b))
  if keydown(KEY_ANS):
    for i in range(halfLenght):
      draw_line(i+1,0,i+1,222,(r,g,b))
      draw_line(320-i,0,320-i,222,(r,g,b))
  if keydown(KEY_ONE):
    for i in range(320):
      draw_line(0,0,319-i,222,(r,g,b))
  if keydown(KEY_TWO):
    for i in range(320):
      draw_line(320,222,0+i,0,(r,g,b))
  if keydown(KEY_THREE):
    for i in range(320):
      draw_line(0,222,i,-1,(r,g,b))
  if keydown(KEY_FOUR):
    for i in range(320):
      draw_line(320,-1,320-i,222,(r,g,b))    
  if keydown(KEY_FIVE):
    for i in range(320):
      draw_line(halfLenght-i,0,halfLenght-i,222,(r,g,b))
  if keydown(KEY_SIX):
    for i in range(320):
      draw_line(halfLenght+i,0,halfLenght+i,222,(r,g,b))
  if keydown(KEY_SEVEN):
    for i in range(halfLenght):
      draw_line(i+1,0,i+1,222,(r,g,b))
  if keydown(KEY_EIGHT):
    for i in range(halfLenght):
      draw_line(320-i,0,320-i,222,(r,g,b))
