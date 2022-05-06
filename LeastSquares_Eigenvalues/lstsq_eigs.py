# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
Peter J. Bloch
MTH 420
6 May 2022
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

from cProfile import label
from re import X
import numpy as np
from matplotlib import pyplot as plt
import sys
sys.path.append("../")
from MatplotlibIntro.matplotlib_intro import prob1
from scipy import linalg as la


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    # Ax = b
    Q, R = la.qr(A, mode='economic')    # QRx = b
    # print(Q.shape)
    # print(R.shape)
    b1 = Q.T @ b                         # Rx = b1
    x = la.solve_triangular(R, b1)      # x = R^-1 * b1

    return x
    # raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    # raise NotImplementedError("Problem 2 Incomplete")
    housing_data = np.load('housing.npy') #Columns: year, price index
    rows, columns = housing_data.shape
    years = housing_data[:,0]
    ones = np.ones((rows,))
    # print(years.shape, ones.shape)
    A = np.vstack((years, ones))
    price_index = housing_data[:,1]
    # print(A.shape, price_index.shape)
    x = least_squares(A.T,price_index)

    X = np.linspace(0, 20, 50)
    Y = x[0]*X + x[1]
    plt.plot(X,Y,'r')
    plt.scatter(years, price_index)
    print("Plotting y = {}x + {}".format(round(x[0], 3),round(x[1],3)))
    plt.show()

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    raise NotImplementedError("Problem 3 Incomplete")


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")


def main():
    return

if __name__ == "__main__":
    #Test prob1:
    # A = np.array([[1,1],[2,1],[3,1]])
    # b = np.array([2,4,6]) #x should return 2,0?
    # print(least_squares(A,b))
    line_fit()
    main()