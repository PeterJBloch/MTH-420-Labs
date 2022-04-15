# standard_library.py
"""Python Essentials: The Standard Library.
Peter J. Bloch
MTH 420
15 April 2022
"""
import calculator
from itertools import chain, combinations

# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return "Min: {}, Max: {}, Average: {}".format(min(L), max(L), sum(L)/len(L))


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
    set1 = set([1,2,3,1])
    set2 = set1
    set1.add(4)
    print("Set mutable:",s2==s1)
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
        eturn chain.from_iterable(combinations(some_list, index) for index in range(len(some_list)+1))    



# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""