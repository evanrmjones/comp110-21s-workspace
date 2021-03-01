""" An Oregon trail type game"""

#named constant 
__author__ = "730389248"

import random

def greet() -> None:
    print(f"Welcome {player}! This is an Oregon Trail game where you attempt to travel from New York to Oregon, along the Oregon trail. After you enter your player, use the status command to see the other commands you can take. Every time you travel, you randomly travel for 3-7 days, the miles you travelled randomly decreases by 35-60. When you rest, you gain 1 health and rest for 2-5 days. When you hunt, your food increases by 100. Your health begins at 5 and decreases once per month if you never rest. Good luck and make it to oregon before you run out of health or food!")
    return None
def main() -> None: 
    greet()
    points: int = 0 
    func()
    return None 


HEALTH_SUBTRACTION: int = 1 
RANDOM_DAY_TRAVEL: int = random.randint(3,7)
RANDOM_DAY_OTHER: int = random.randint(2,5)
player: str = input("what is your name? ")
points: int = 0 
months_with_31_days: list[int]
months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
month: int = 3 

# We start our journey in March, per starting in month 3 

day: int = 1 

# We start on the first of March, per declaring it day 1 

food: int = 500

# We start with 500 units of food

health: int = 5
#health starts at 5 and decreases once per month 
a: int = random.randint(1,30)
b: int = random.randint(1,30)
miles_to_go: int = 2000

# available functions: travel, rest, hunt, status, help, quit

game_over= False 
def add_day():
  global month 
  global day
  global food
  global health
  global a 
  global b 
  global game_over
  if day == 32 and month in months_with_31_days: 
    month = month + 1
    day = 1
    a = random.randint(1,30)
    b = random.randint(1,30)
  elif day == 31 and month not in months_with_31_days: 
    month = month + 1 
    day = 1
    a = random.randint(1,30)
    b = random.randint(1,30)
  else: 
    day += 1
    food -= 5 
    if day == a: 
      if health == 1: 
        print(f"Sorry {player} you lost \U0001F614") 
        print(status_function())
        game_over= True
      else: 
        health -= HEALTH_SUBTRACTION
    if day == b: 
      if health == 1: 
        print(f"Sorry {player} you lost \U0001F614") 
        print(status_function())
        game_over= True
      else: 
        health -= HEALTH_SUBTRACTION
    return day
    return food
    return health
    return month 
def travel_func():
    global action
    global miles_to_go
    #global points 
    for i in range(0, random.randint(3,7)):
        add_day()
    rand_dist: int = random.randint(35,60)
    miles_to_go -= rand_dist
    #points += rand_dist
    
def rest_function():
    global health
    global month
    for i in range(0, random.randint(2,5)):
        add_day()
    health = health + 1 
def hunt_function():
    global food 
    global month
    for i in range(0, random.randint(2,5)):
        add_day()
    food = food + 100
def help_function():
    a= "the actions you can take are: travel, rest, hunt, status, help, quit "
    return a
def status_function(): 
  global food 
  global health
  global miles_to_go
  global day
  global month
  #global points
  foodstat: str = f"food is {food}" 
  healthstat: str = f"health is {health}"
  distanceleft: str = f"Miles to go is {miles_to_go}"
  #points_current: str = f"Points is {points}"
  date: str = f"Date is {month}/{day}"
  totstat: str = f"{foodstat}, {healthstat}, {distanceleft}, {date}"
  return totstat

 
def func() -> None: 
  global month 
  global day
  global food
  global health
  global a 
  global b 
  global game_over
  while game_over == False:
      action = input("What would you like to do? ")
      if health > 1 and food >= 1 and month <= 12 and miles_to_go >= 1 :
          if day <= 30 or day <= 31 and month in months_with_31_days:
              if action == "travel":
                  travel_func()
              elif action == "rest":
                  rest_function()
              elif action == "hunt":
                  hunt_function()
              elif action == "help":
                  print(help_function())
              elif action == "status":
                  print(status_function())
              elif action == "quit":
                  game_over= True 
                  print(f"Sorry { player } you lost \U0001F614") 
          else: 
              print(status_function())
              game_over = True
              if miles_to_go <= 0:
                  print(f"congratulations{player} you won! \U0001F973")
              else: 
                  print(f"Sorry {player} you lost \U0001F614") 
      else: 
              print(status_function())
              game_over= True
              if miles_to_go <= 0:
                  print(f"congratulations{player} you won! \U0001F973")
              else: 
                  print(f"Sorry {player} you lost \U0001F614") 


if __name__ == "__main__":
    main()
