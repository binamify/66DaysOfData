# # Import numpy and set seed
# import numpy as np
# np.random.seed(123)

# # Use randint() to simulate a dice
# np.random.randint(1,7)

# # Use randint() again
# np.random.randint(1,7)

# #######################################################################################################

# # Numpy is imported, seed is set

# # Starting step
# step = 50

# # Roll the dice
# dice = np.random.randint(1,7)

# # Finish the control construct
# if dice <= 2 :
#     step = step - 1
# elif dice >=3 and dice <=5 :
#     step = step +1
# else :
#     step = step + np.random.randint(1,7)

# # Print out dice and step
# print(dice)
# print(step)


# #########################################################################################
# # Numpy is imported, seed is set

# # Initialize random_walk
# random_walk = [0]

# # Complete the for loo[]
# for x in range(100) :
#     # Set step: last element in random_walk
#     step = random_walk[-1]

#     # Roll the dice
#     dice = np.random.randint(1,7)

#     # Determine next step
#     if dice <= 2:
#         step = step - 1
#     elif dice <= 5:
#         step = step + 1
#     else:
#         step = step + np.random.randint(1,7)

#     # append next_step to random_walk
#     random_walk.append(step)

# # Print random_walk
# print(random_walk)


# #####################################################################################
# # Numpy is imported, seed is set

# # Initialization
# random_walk = [0]

# for x in range(100) :
#     step = random_walk[-1]
#     dice = np.random.randint(1,7)

#     if dice <= 2:
#         step = max(0, step - 1)
#     elif dice <= 5:
#         step = step + 1
#     else:
#         step = step + np.random.randint(1,7)

#     random_walk.append(step)

# # Import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt 

# # Plot random_walk
# plt.plot(random_walk)

# # Show the plot
# plt.show()


# ##########################################################################
# # Numpy is imported; seed is set

# # Initialize all_walks (don't change this line)
# all_walks = []

# # Simulate random walk 10 times
# for i in range(10) :

#     # Code from before
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)

#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#         random_walk.append(step)

#     # Append random_walk to all_walks
#     all_walks.append(random_walk)

# # Print all_walks
# print(all_walks)


# ###########################################################################################
# # numpy and matplotlib imported, seed set.

# # initialize and populate all_walks
# all_walks = []
# for i in range(10) :
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)
#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#         random_walk.append(step)
#     all_walks.append(random_walk)

# # Convert all_walks to Numpy array: np_aw
# np_aw = np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()


# ##############################################################################################
# # numpy and matplotlib imported, seed set.

# # initialize and populate all_walks
# all_walks = []
# for i in range(10) :
#     random_walk = [0]
#     for x in range(100) :
#         step = random_walk[-1]
#         dice = np.random.randint(1,7)
#         if dice <= 2:
#             step = max(0, step - 1)
#         elif dice <= 5:
#             step = step + 1
#         else:
#             step = step + np.random.randint(1,7)
#         random_walk.append(step)
#     all_walks.append(random_walk)

# # Convert all_walks to Numpy array: np_aw
# np_aw = np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()

# # Clear the figure
# plt.clf()

# # Transpose np_aw: np_aw_t
# np_aw_t = np.transpose(np_aw)

# # Plot np_aw_t and show
# plt.plot(np_aw_t)
# plt.show()


# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt 
# Simulate random walk 500 times
all_walks = []
for i in range(500) :
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

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()