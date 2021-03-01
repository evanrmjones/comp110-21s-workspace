""" An Oregon trail type game"""


__author__ = "730389248"

import random


def main() -> None: 
    print(greet())
    
    return None 
def greet() -> None:
    print(f"Welcome {player}! This is an Oregon Trail game where you attempt to travel from New York to Oregon, along the Oregon trail. After you enter your player, use the status command to see the other commands you can take. Every time you travel, you randomly travel for 3-7 days, the miles you travelled randomly decreases by 35-60. When you rest, you gain 1 health and rest for 2-5 days. When you hunt, your food increases by 100. Your health begins at 5 and decreases once per month if you never rest. Good luck and make it to oregon before you run out of health or food!")
    return None

points: int = 0 
HEALTH_CONSTANT: int = 1 
RANDOM_DAY_TRAVEL: int = random.randint(3,7)
RANDOM_DAY_OTHER: int = random.randint(2,5)
player: str = input("what is your name? ")
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

game_over: bool = False 


def add_day() -> int:
  global month 
  global day
  global food
  global health
  global a 
  global b 
  global game_over
  if day == 32 and month in months_with_31_days: 
    month +=1
    day: int = 1
    a = random.randint(1,30)
    b = random.randint(1,30)
  elif day == 31 and month not in months_with_31_days: 
    month += 1  
    day: int = 1
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
        health -= HEALTH_CONSTANT
    if day == b: 
      if health == 1: 
        print(f"Sorry {player} you lost \U0001F614") 
        print(status_function())
        game_over= True
      else: 
        health -= HEALTH_CONSTANT
    return day
    return food
    return health
    return month 
def travel_func() -> int:
    global action
    global miles_to_go
    i: int = 0 
    while i < RANDOM_DAY_TRAVEL:
        add_day()
        i += 1                                                                                                                  
    miles_to_go =  miles_to_go - random.randint(35,60)
def rest_function(): #what we returning?
    global health
    global month
    i = 0 
    while i < RANDOM_DAY_OTHER: 
        add_day()
        i += 1 
    health += HEALTH_CONSTANT
def hunt_function(): #what we returning?
    global food 
    global month
    i = 0 
    while i < RANDOM_DAY_OTHER:
        add_day()
        i += 1 
    food += 100 
def help_function() -> str:
    a= "the actions you can take are: travel, rest, hunt, status, help, quit "
    return a
def status_function() -> str: 
  global food 
  global health
  global miles_to_go
  global day
  global month
  foodstat: str = f"food is {food}" 
  healthstat: str = f"health is {health}"
  distanceleft: str = f"Miles to go is {miles_to_go}"
  date: str = f"Date is {month}/{day}"
  totstat: str = f"{foodstat}, {healthstat}, {distanceleft}, {date}"
  return totstat

# def action_func(action: str) -> str: 

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


__name__ == "__main__":
    main()
