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
    t.forward(100)
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

def spiral():
  # import turtle

  # initialising variables
  dist = 1
  flag = 300

  # initialising turtle
  spiral = turtle.Turtle()

  # changing speed of turtle
  spiral.speed(50)
  spiral.shape('classic')

  # making patten
  while flag:
  
    # makes the turtle to move forward
    spiral.forward(dist)
  
    # makes the turtle to move left
    spiral.left(121)
    dist += 1
    flag -= 1

  turtle.done()

spiral()

#Where the magic begins
main_input = input('What would you like to do for now? 1. Get Inspired, 2. Make Clyde Draw ')

if main_input == '1':
  choose_inspire_quote()
elif main_input == '2':
  shape_select = input("What ")
else:
  print("Not valid option. Try again")

