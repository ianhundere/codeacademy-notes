"""
number-guess.py
roll a pair of dice, add the values of the roll, you guess a number, compare
yo guess with the total value, and boom! you may win or lose.
"""
from random import randint
from time import sleep
print "Welcome to the amazing guessing game!"
sleep(1)
def get_user_guess():
  guess = int(raw_input("What number will roll?: "))
  return guess
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print "The maximum value that can be rolled is %d" % max_val
    guess = get_user_guess()
    if guess > max_val:
        print "Your guess is invalid, higher than possible value."
    else:
          print "Rolling..."
          sleep(2)
          print "The first roll is %d!" % first_roll
          sleep(1)
          print "The second roll is %d!" % second_roll
          sleep(1)
          total_roll = first_roll + second_roll
          print "The total is %d!" % total_roll
          print "Result..."
          sleep(1)
          if guess == total_roll:
              print "Weeeee doggy, you done did it boy!!!"
          else:
              print "Whomp whomp, try again."    
roll_dice(6)