# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt 
# Simulated random walk for  2000 times
all_walks = []
for i in range(2000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
#last row of np_aw_t
ends = np_aw_t[-1]
#histogram for analysis
plt.hist(ends)
plt.show()