import matplotlib.pyplot as plt
from random_walk import RandomWalk

# keep creating random walks while active
while True:
    # make a random walk and plot the points
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Generate another walk? (y/n):")
    if keep_running == 'n':
        break
