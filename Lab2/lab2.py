#Standard Library Lab

from doctest import Example
import calculator
from itertools import chain, combinations


def prob1(L):
    return "Min: {}, Max: {}, Average: {}".format(min(L), max(L), sum(L)/len(L))

def prob2():
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
    return

def prob3():
    #Using calculator file, compute hypotenuse
    side1 = 3
    side2 = 4
    print("Side A: {}".format(side1))
    print("Side B: {}".format(side2))
    #a^2
    a2 = calculator.product(side1,side1)
    #b^2
    b2 = calculator.product(side2,side2)
    hypotenuse = calculator.sqrt(calculator.sum(a2,b2))
    print("Hypotenuse: {}".format(hypotenuse))
    return

def prob4():
    #power of set A
    example = [1,2,3]
    powerset = power_set(example)
    print(list(powerset))
    return

def power_set(some_list):
    return chain.from_iterable(combinations(some_list, index) for index in range(len(some_list)+1))    

def main():
    #Problem 1
    print("\nProblem 1:")
    new_list = [1,2,3,4,5,6,7]
    answers = prob1(new_list)
    print(answers)
    
    #Problem 2
    print("\nProblem 2:")
    prob2()

    #Problem 3
    print("\nProblem 3:")
    prob3()

    print("\nProblem 4")
    prob4()


if __name__ == "__main__":
    main()