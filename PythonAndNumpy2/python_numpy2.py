# python_intro.py
"""Python Essentials: Introduction to Python.
Peter Bloch
MTH 420
22 April, 2022
"""
from unittest import result
import numpy as np

#Problem 1
def isolate(a, b, c, d, e):
    # print("{}     {}     {} {} {}".format(a,b,c,d,e))
    print(a,b,c, sep="     ",end=" ")
    print(d,e, sep=" ",end="\n")
    return
    # raise NotImplementedError("Problem 1 Incomplete")

#Problem 2
def first_half(string):
    middle_char = len(string) // 2 #Floor division
    return string[0:middle_char]
    # raise NotImplementedError("Problem 2 Incomplete")

def backward(first_string):
    return first_string[::-1] #is this a cheat way of using slicing?
    # raise NotImplementedError("Problem 2 Incomplete")

#Problem 3
def list_ops():
    """Does operations 1-6 of prompt

    I predict this will return: ["fox", "hawk", "dog", "ant", "hunter"]

    Returns:
        list: the list that has been operated on
    """
    animals = ["bear","ant","cat","dog"]
    animals.append("eagle")
    animals[2] = "fox"
    animals.pop(1)
    animals = sorted(animals, reverse=True)
    eagle_index = animals.index("eagle")
    animals[eagle_index] = "hawk"
    animals.append("hunter")
    return animals
    # raise NotImplementedError("Problem 3 Incomplete")

#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """

    series = [((-1)**(i+1))/i for i in range(1,n+1)]
    return sum(series)
    # raise NotImplementedError("Problem 4 Incomplete")



def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    mask = A < 0
    A[mask] = 0
    return(A)
    # raise NotImplementedError("Problem 5 Incomplete")


def prob6():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0,2,4],[1,3,5]])
    B = np.array([[3,0,0],[3,3,0],[3,3,3]])
    C = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
    I = np.identity(3)

    row1 = np.hstack((np.zeros((3,2)), np.hstack((A.T, I))))
    row2 = np.hstack((A, np.zeros((2,4))))
    row3 = np.hstack((np.hstack((B, np.zeros((3,1)))), C))

    full_matrix = np.vstack((np.vstack((row1,row2)),row3))
    # raise NotImplementedError("Problem 6 Incomplete")
    # print(full_matrix.shape)
    # print(full_matrix)
    return full_matrix

def prob7(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    result = (A.T*(1/A.sum(axis=1))).T
    return result
    # raise NotImplementedError("Problem 7 Incomplete")


def prob8():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """

    grid = np.load("grid.npy")
    # raise NotImplementedError("Problem 8 Incomplete")


def main():
    isolate(1,2,3,4,5)
    print(alt_harmonic(500000))
    A = np.array([-3,-1,3])
    print(prob5(A))
    prob6()
    prob7(A=0)

if __name__ == "__main__":
    main()