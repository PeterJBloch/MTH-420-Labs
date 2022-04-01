#!/Users/peterbloch/opt/anaconda3/bin python3
#Lab1
import numpy as np

def prob3():
    """Problems 1 + 3 added together
    """
    print("\nProblem 3:")
    r = 10
    print("The volume of a sphere with radius {} is {}.".format(r, sphere_volume(r)))
    return

def prob2():
    print("\nProblem 2:")
    print("Hello World!")

def sphere_volume(radius):
    """This funciton computes the volume of a sphere

    Args:
        radius (int or float): The radius of the sphere

    Returns:
        float: The computed volume
    """
    pi = 3.14159
    volume = 4/3* pi * radius**3
    return volume

def prob4():
    print("\nProblem 4:")
    A = np.array([[3,-1,4],[1,5,-9]])
    B = np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    product = np.dot(A,B)
    print(product)
    return

def prob5():
    print("\nProblem 5:")
    income1 = 100
    income2 = 100000
    print("A person with income ${} owes ${} in taxes".format(income1, tax_liability(income1)))
    print("A person with income ${} owes ${} in taxes".format(income2, tax_liability(income2)))
    return

def tax_liability(income):
    """Computes the tax an individual pays based upon income

    Args:
        income (integer or float): amount of dollar income

    Returns:
        float: The tax liability computed
    """
    liability = 0
    rates = [.10,.12,.22]
    cutoffs = [9875, 40125, 85525]
    #check first bracket
    if income < cutoffs[0]:
        liability += rates[0]*income
        return liability

    else:
        #if there's another bracket, tax the all of this section, then move on
        liability+=rates[0]*cutoffs[0]

    #check second bracket
    if income < cutoffs[1]:
        liability+= (income-cutoffs[0])*rates[1]
        return liability
    else:
        #if there's another bracket, tax the all of this section, then move on
        liability+=rates[1]*cutoffs[1]

    #third bracket is only thing left at this point
    liability+= (income-cutoffs[1])*rates[2]
    return liability

def prob6a():
    return

if __name__ == "__main__":
    prob2()
    prob3()
    prob4()
    prob5()