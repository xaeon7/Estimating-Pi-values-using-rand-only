import random 
import numpy as np
import matplotlib.pyplot as plt

def estimated_pi(n):

  X = np.random.random(n)
  Y = np.random.random(n)

  in_cercle_x = []
  in_cercle_y = []

  points_in_circle = 0
  points_in_square = 0

  for _ in range(n) :
    x = X[_]
    y = Y[_]
    if x**2 + y **2 < 1 :
      points_in_circle += 1
      # Create data for ploting
      in_cercle_x.append(x)
      in_cercle_y.append(y)

    points_in_square += 1

  # Assigning estimated pi to a variable
  estime_pi = points_in_circle * 4 /points_in_square 

  # Ploting parameters
  fig, ax = plt.subplots(figsize=(15,15))
  draw_circle = plt.Circle((0, 0), 1,fill=False)
  ax.set_aspect(1)
  ax.add_artist(draw_circle)
  ax.set_xlim([-1, 1])
  ax.set_ylim([-1, 1])
  ax.scatter(X, Y, s = 1);
  ax.scatter(in_cercle_x, in_cercle_y, color='r', s = 1);
  ax.axhline(0, linewidth=0.5, color='black');
  ax.axvline(0, linewidth=0.5, color='black');
  fig.suptitle(f'Estimated Pi :{estime_pi}',fontsize=16, fontweight="bold")
  fig.savefig('graph.png')

  return estime_pi