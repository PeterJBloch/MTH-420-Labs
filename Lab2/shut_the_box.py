#Problem 5 - Shut the box

from sys import argv
from random import randint
import time
from itertools import chain, combinations
from numpy import number

def power_set(some_list):
    return chain.from_iterable(combinations(some_list, index) for index in range(len(some_list)+1))    


def roll_dice(numbers):
    roll = 0
    #Roll first dice
    roll += randint(1,6)

    #If the sum of remaining numbers is less than six, proceed
    if sum(numbers)<6:
        return

    #Roll second dice
    else:
        roll+=randint(1,6)
    return roll

def play_round(numbers, seconds_remaining):
    #Check if a viable combination exists
    #Find all combinations of numbers from previous problem
    print("The remaining numbers available are: {}".format(numbers))
    roll = roll_dice(numbers)
    print("Your roll was {}, and you have {} seconds left to play the game".format(roll, seconds_remaining))
    start = time.time() #Get current time
    #User can make decisions now
    making_selection = True
    selection = []
    while making_selection:
        selection = input("What number(s) would you like to remove next: ").split(" ")
        for i in range(len(selection)):
            try:
                selection[i] = int(selection[i])
            except:
                print("{} could not be made into a number.".format(i))
                continue
            if selection[i] not in numbers:
                print("This number is not available: {}".format(int(i)))
                continue
        # print(new_selection)
        if sum(selection) == roll:
            making_selection = False
        else:
            print("Those numbers add to {}, not your roll: {}".format(sum(selection), roll))
    for i in selection:
        numbers.remove(i)
    return numbers, time.time()-start #The remaining unchosen numbers and the time difference of user decision is returned

def main():
    #Get command line arguments
    name = ""
    time_limit = 0

    if len(argv) != 3:
        print("Incorrect number of command line arguments")
        return 1

    else:
        name = argv[1]
        time_limit = float(argv[2])

    #Start the game
    print("\nWelcome {}, you have {} seconds to play the game!".format(name, time_limit))
    numbers = [1,2,3,4,5,6,7,8,9]
    time_remaining = time_limit
    while True:
        numbers, time_taken = play_round(numbers, time_remaining)
        time_remaining-=time_taken
        if time_remaining<0:
            print("\nSorry, the game time elapsed. Better luck next time!")
            return
        if numbers == []:
            print("Congratulations! You won with {} seconds remaining!".format(time_remaining))

if __name__ == "__main__":
    main()