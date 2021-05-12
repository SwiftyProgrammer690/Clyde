from random import *
import turtle

inspirational_quotes = ['Never give up', 'Belive in yourself', 'Focus on good', 'Without fear, there is no hope', 'Be you', 'Where ever you go, go with your hearth']

#Choose random message from inspirational_quotes array
def choose_inspire_quote():
  print(random.choice(inspirational_quotes))
  
#Init turtle
t = turtle.Turtle()

#Defining shapes
def circle(user_radius):
  t.circle(user_radius)

def square(user_side):
  for i in range(4):
    t.forward(user_side)
    t.right(90)

def triangle(user_side):
  for i in range(3):
    t.forward(user_side)
    t.right(120)

def rectangle(user_side_1, user_side_2):
  for i in range(2):
    t.forward(user_side_1)
    t.right(90)
    t.forward(user_side_2)
    t.right(90)

def hex_spiral(user_count):
  for i in range(user_count):
    t.forward(x)
    t.right(y)
    x += 5
    y += 5

def tri_spiral():
  dist = 1
  flag = 300
  
  
  t.speed(50)

  while flag:
    t.forward(dist)
    t.left(121)
    
    dist += 1
    flag -= 1

  turtle.done()


  
def spiral():
  for i in range(100):
    t.forward(5+i)
    t.right(15)

  turtle.done()

spiral()

#Where the magic begins
main_input = input('What would you like to do for now? 1. Get Inspired, 2. Make Clyde Draw ')

if main_input == '1':
  choose_inspire_quote()

elif main_input == '2':
  shape_select = input("What would Clyde like to draw? 1. Square, 2. Circle, 3. Triangle, 4. Hexagonical Spiral, 5. Triangular Spiral, 6 Regular Spiral ")

  if shape_select == "1":
    user_sq_side = input("What should be the sides of the square? ")
    square(user_sq_side)
 
  elif shape_select == "2":
    user_rad = input("What should be the radius of the circle? ")
    circle(user_rad)

  elif shape_select == "3":
    user_tri_side = input("What should be the sides of the triangle? ")
    triange(user_tri_side)

  elif shape_select == "4":
    hex_spiral()

  elif shape_select == "5":
    tri_spiral()

  elif shape_select == "6":
    spiral()

  else:
    print("Invalid response!")

else:
  print("Not valid option. Try again")

