'''题目：画椭圆。'''

# 1
import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import Ellipse

NUM = 250

ells = [Ellipse(xy=rnd.rand(2) * 10, width=rnd.rand(), height=rnd.rand(), angle=rnd.rand() * 360)
        for i in range(NUM)]

fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(rnd.rand())
    e.set_facecolor(rnd.rand(3))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()

# 2
from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ell1 = Ellipse(xy=(0.0, 0.0), width=4, height=8,
               angle=30.0, facecolor='yellow', alpha=0.3)
# cir1 = Circle(xy=(0.0, 0.0), radius=2, alpha=0.5)
ax.add_patch(ell1)
# ax.add_patch(cir1)

x, y = 0, 0
ax.plot(x, y, 'ro')

plt.axis('scaled')

# changes limits of x or y axis so that equal increments of x and y have the same length
plt.axis('equal')

plt.show()
