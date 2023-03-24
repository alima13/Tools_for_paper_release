import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Fixing random state for reproducibility
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

df = pd.read_csv('Book1.csv', sep=",")
target_column = ['1'] 
target4_column = ['2'] 
target2_column = ['3'] 
target3_column = ['4'] 


df.describe()
x = df[target_column].values
y = df[target2_column].values
z = df[target3_column].values
d = df[target4_column].values

n = 100

# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = z
    ys = y
    zs = x
    zd = d
    ax.scatter(xs, ys, zs)
    ax.scatter(xs, ys, zd)

#Change the below if you want to use another degree
ax.set_xlabel('1')
ax.set_ylabel('2')
ax.set_zlabel('3')



for angle in range(0, 220):
   ax.view_init(30, angle)

plt.show()
