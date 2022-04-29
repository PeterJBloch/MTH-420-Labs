# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Peter J. Bloch
28 April 2022
MTH 420
"""

import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    random_array = np.random.normal(size=(n,n))
    means = np.mean(random_array,axis=0)
    variance = np.var(means)
    # raise NotImplementedError("Problem 1 Incomplete")
    return variance

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    x_values = [i for i in range(100,1001, 100)]
    y_values = []
    for i in range(100,1001, 100):
        y_values.append(var_of_means(i))

    plt.plot(x_values,y_values)
    plt.title("Problem 1: Variation of Means")
    plt.show()
    # raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    # x = [i for i in range(-np.pi, np.pi+0.1, np.pi/8)]
    x = np.linspace(-np.pi,np.pi,30)
    plt.plot(x, np.sin(x),label="Sin(x)")
    plt.plot(x, np.cos(x), label = "Cos(x)")
    plt.plot(x, np.arctan(x), label="Arctan(x)")
    plt.title("Problem 2: Sin, Cos, Arctan of x")
    plt.legend()
    plt.show()
    
    # raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2,1-.00001,60)
    x2 = np.linspace(1.0001,6,60)
    y1 = 1/(x1-1)
    y2 = 1/(x2-1)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.plot(x1,y1,'m--')
    plt.plot(x2,y2,'m--')
    plt.title("Problem3: f(x) = 1/(x-1)")
    plt.show()
    # raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    bounds = [0, 2*np.pi, -2, 2]
    x = np.linspace(0, 2*np.pi, 50)
    fig, axs = plt.subplots(2, 2)

    axs[0,0].plot(x, np.sin(x), "g")
    axs[0,0].axis(bounds) 
    axs[0,0].set_title("sin(x)")

    axs[0,1].plot(x, np.sin(2*x), "r--")
    axs[0,1].axis(bounds)
    axs[0,1].set_title("sin(2x)")

    axs[1,0].plot(x, 2*np.sin(x), "b--")
    axs[1,0].axis(bounds) 
    axs[1,0].set_title("2sin(x)")

    axs[1,1].plot(x, 2*np.sin(2*x), "m.")
    axs[1,1].axis(bounds) 
    axs[1,1].set_title("2sin(2x)")

    plt.suptitle("Problem 4: Coefficients of sin(x)")
    plt.show()
    # raise NotImplementedError("Problem 4 Incomplete")
    return


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    # PART 1:
    fars_data = np.load("FARS.npy")
    #columns are: times (integer), longitude (float), latitude (float)
    times = fars_data[:,0]
    longitudes = fars_data[:,1]
    latitudes = fars_data[:,2]
    plt.scatter(longitudes,latitudes, 1, "k")
    plt.axis("equal")
    plt.title("Problem 5: Scatter Plot of Car Accidents")
    plt.show()

    # PART 2
    plt.hist(times, bins = np.arange(0, 25))
    plt.xlim(0,24)
    plt.title("Problem 5: Histogram of Car Crash Times")
    plt.show()


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    raise NotImplementedError("Problem 6 Incomplete")

def main():
    # print(var_of_means(100))
    # prob1()
    # prob2()
    # prob3()
    # prob4()
    prob5()

if __name__ == "__main__":
    main()