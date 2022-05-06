# standard_library.py
"""Python Essentials: The Standard Library.
Peter J. Bloch
MTH 420
15 April 2022
"""
import calculator, time
from itertools import chain, combinations
from random import randint

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    my_list = list(L)
    return "Min: {0}, Max: {1}, Average: {2}".format(min(my_list), max(my_list), sum(my_list)/len(my_list))


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    #int
    a = 1
    b=a
    a+=1
    print("Int mutable:",b==a)

    #string
    s1 = "hello"
    s2 = s1
    s1 = "hi"
    print("String mutable:",s1==s2)

    #list
    l1 = ['hi','hello','goodbye']
    l2=l1
    l2[0]='hey'
    print("List mutable:", l2==l1)

    #tuple
    t1 = (1,2)
    t2=t1
    t1+=(1,)
    print("Tuple mutable:",t2==t1)

    #set
    set1 = {1,2,3}
    set2 = set1
    set1.add(4)
    print("Set mutable:",set1==set2)
    # raise NotImplementedError("Problem 2 Incomplete")
    return


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    a2 = calculator.product(a,a)
    b2 = calculator.product(b,b)
    hypotenuse = calculator.sqrt(calculator.sum(a2,b2))
    # print("Hypotenuse: {}".format(hypotenuse))
    # raise NotImplementedError("Problem 3 Incomplete")
    return hypotenuse


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    # raise NotImplementedError("Problem 4 Incomplete")
    return list(chain.from_iterable(combinations(A, index) for index in range(len(A)+1)))



# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    #Start the game
    print("\nWelcome {}, you have {} seconds to play the game!".format(player, timelimit))
    
    #Numbers in the game
    numbers = [1,2,3,4,5,6,7,8,9]
    time_remaining = timelimit
    while True:
        numbers, time_taken = play_round(numbers, time_remaining, player)
        time_remaining-=time_taken
        if time_remaining<0:
            print("\nSorry {}, the game time elapsed. Better luck next time!".format(player))
            return
        if numbers == []:
            print("\nCongratulations {}! You won with {} seconds remaining!".format(player, time_remaining))

def roll_dice(numbers):
    roll = 0
    #Roll first dice
    roll += randint(1,6)

    #If the sum of remaining numbers is less than six, proceed
    if sum(numbers)<6:
        return roll

    #Roll second dice
    else:
        roll+=randint(1,6)
    return roll

def play_round(numbers, seconds_remaining, name):
    print("The remaining numbers available are: {}".format(numbers))
    roll = roll_dice(numbers)

    #Check if there is a viable combination of leftover numbers for the roll
    found_combo = False
    #Use the power set from previous problem
    powerset = list(power_set(numbers))
    # print("Powerset left: {}".format(powerset))
    for combo in powerset:
        if sum(combo) == roll:
            found_combo = True
    if found_combo == False:
        print("\nSorry {}, you rolled a {} and there are no more combinations left. Better luck next time!".format(name, roll))
        exit(0)
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
    prob1([1,2,3,4])
    prob2()
    return

if __name__ == "__main__":
    main()