import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

# Import matplotlib.pyplot as plt and set %matplotlib inline
# if you are using the jupyter notebook. What command do you 
# use if you aren't using the jupyter notebook?
plt.show()

# Follow along with these steps:
# - Create a figure object called fig using plt.figure()
# - Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
# - Plot (x,y) on that axes and set the labels and titles to match the plot below:
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.set_title('title')

# Create a figure object and put two axes on it, ax1 and ax2. 
# Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.
fig_2 = plt.figure()

ax1 = fig_2.add_axes([0 ,0, 1, 1])
ax2 = fig_2.add_axes([0.2, 0.5, .2, .2])

ax1.plot(x, y, color='red')
ax2.plot(x, y, color='red')

# Create the plot below by adding two axes 
# to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4].
fig_3 = plt.figure()

axes_1 = fig_3.add_axes([0, 0, 1, 1])
axes_2 = fig_3.add_axes([0.2, 0.5, .4, .4])

axes_2.plot(x, y)

axes_2.set_title('zoom')
axes_2.set_xlabel('x')
axes_2.set_ylabel('y')

axes_2.set_xlim(20, 22)
axes_2.set_ylim(30, 50)

axes_1.plot(x, z)

axes_1.set_xlabel('x')
axes_1.set_ylabel('z')

axes_1.set_xlim(0, 100)
axes_1.set_ylim(0, 10000)

# Use plt.subplots(nrows=1, ncols=2) to create the plot below.
fig_4,axes_3 = plt.subplots(nrows=1, ncols=2, figsize=(8,2))

# Now plot (x,y) and (x,z) on the axes. 
# Play around with the linewidth and style.

axes_3[0].plot(x, y, lw=2, linestyle='--')
axes_3[1].plot(x, z, lw=2, color='red')

axes_3[0].set_xlim(0, 100)
axes_3[0].set_ylim(0, 200)

axes_3[1].set_xlim(0, 100)
axes_3[1].set_ylim(0, 10000)

plt.tight_layout()
plt.show()
