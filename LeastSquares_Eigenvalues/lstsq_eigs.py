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
from cv2 import ellipse
import numpy as np
# from numpy import linalg as la
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
    # print("Plotting y = {}x + {}".format(round(x[0], 3),round(x[1],3)))
    plt.show()

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    housing_data = np.load('housing.npy')
    rows, columns = housing_data.shape
    years = housing_data[:,0]
    price_index = housing_data[:,1]
    X = np.linspace(0, 16, 50)

    #======LEAST SQUARES======
    plt.subplot(121)
    #degree 3
    A1 = np.vander(years, 4)
    x = least_squares(A1, price_index)
    Y = np.vander(X,4)@x
    plt.plot(X, Y,'r', label="Degree 3")
    plt.scatter(years, price_index)

    #degree 6
    A2 = np.vander(years, 7)
    x = least_squares(A2, price_index)
    Y = np.vander(X,7)@x
    plt.plot(X, Y,'k', label="Degree 6")
    plt.scatter(years, price_index)

    #degree 9
    A3 = np.vander(years, 10)
    x = least_squares(A3, price_index)
    Y = np.vander(X,10)@x
    plt.plot(X, Y,'blue', label="Degree 9")
    plt.scatter(years, price_index)

    #degree 12
    A4 = np.vander(years, 13)
    x = least_squares(A4, price_index)
    Y = np.vander(X,13)@x
    plt.plot(X, Y,'cyan', label="Degree 12")
    plt.scatter(years, price_index)
    plt.title("My Least Squares Function")
    plt.legend(loc="lower right")

    #======POLYFIT======
    plt.subplot(122)

    #degree 3
    A1 = np.vander(years, 4)
    x = np.polyfit(years,price_index,3)
    Y = np.vander(X,4)@x
    plt.plot(X, Y,'r', label="Degree 3")
    plt.scatter(years, price_index)
    plt.title("Numpy Polyfit")

    #degree 6
    A2 = np.vander(years, 7)
    x = np.polyfit(years,price_index,6)
    Y = np.vander(X,7)@x
    plt.plot(X, Y,'k', label="Degree 6")
    plt.scatter(years, price_index)

    # #degree 9
    A3 = np.vander(years, 10)
    x = np.polyfit(years,price_index,9)
    Y = np.vander(X,10)@x
    plt.plot(X, Y,'blue', label="Degree 9")
    plt.scatter(years, price_index)

    #degree 12
    A4 = np.vander(years, 13)
    x = np.polyfit(years,price_index,12)
    Y = np.vander(X,13)@x
    plt.plot(X, Y,'cyan', label="Degree 12")
    plt.scatter(years, price_index)


    plt.legend(loc="lower right")

    plt.show()
    # raise NotImplementedError("Problem 3 Incomplete")


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
    ellipse_coords = np.load('ellipse.npy')
    rows, columns = ellipse_coords.shape #100 rows x 2 columns
    ellipse_x = ellipse_coords[:,0]
    ellipse_y = ellipse_coords[:,1]

    A = np.column_stack((ellipse_x**2, ellipse_x, ellipse_x*ellipse_y, ellipse_y, ellipse_y**2))
    b = np.ones((rows,))
    C_a, C_b, C_c, C_d, C_e = la.lstsq(A, b)[0] # a 5x1 array of coefficients to ellipse fit
    plot_ellipse(C_a, C_b, C_c, C_d, C_e)
    # print(ellipse_x.shape())
    # print(rows,columns)

    plt.scatter(ellipse_x, ellipse_y, c='r')
    plt.show()
    
    # raise NotImplementedError("Problem 4 Incomplete")
    return


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
    m, n = A.shape
    x_0 = np.random.rand(n, 1)
    x_0 = x_0 / np.linalg.norm(x_0)
    for k in range(0,N):
        x_0 = A@x_0
        x_0 = x_0 / np.linalg.norm(x_0)
    
    return x_0.T@A@x_0, x_0
    # raise NotImplementedError("Problem 5 Incomplete")


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
    m, n = A.shape
    S = la.hessenberg(A)
    for k in range(0,N):
        Q, R = la.qr(S)
        S = R@Q
        print(S.shape)
    eigs = []
    i = 0
    while i<n:
        print(S)
        exit()
    # raise NotImplementedError("Problem 6 Incomplete")
    return eigs


def main():
    #Test prob1:
    # A = np.array([[1,1],[2,1],[3,1]])
    # b = np.array([2,4,6]) #x should return 2,0?
    # print(least_squares(A,b))
    # line_fit()
    # polynomial_fit()
    # ellipse_fit()
    # A = np.random.random((10,10))
    # print("A = {}".format(A))
    # eigs, vecs = la.eig(A)
    # loc = np.argmax(eigs)
    # lamb, x = eigs[loc], vecs[:,loc]
    # L, x_0 = power_method(A)
    # print("\n== Eigenvalues ==\n",L,"?=", lamb)
    # print("\n== Eigen Vectors ==\n",x_0.T,"\n?=\n",x)
    A = np.random.random((2,2))
    qr_algorithm(A+ A.T)
    return

if __name__ == "__main__":
    main()