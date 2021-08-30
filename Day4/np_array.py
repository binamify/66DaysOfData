
#2D Numpy Arrays
import numpy as np 
data = [[1,11],[2,22],[3,33],[4,44]] #python list inside list

np_data = np.array(data)  #python 2d numpy array
print(np_data)            #(4,2)-4 rows,2 columns
print(np_data.shape)      #number of rows and columns
#Accessing 2d array items
print(np_data[3][1])     # [index_of_row,index_of_column]
print(np_data[2,0])      # first colum of 3rd row

#Basic Statistics in Numpy
weight = [50,43,56,76,59,76,87,45] #weight in kg
height = [1.3,1.1,1.4,1.2,1.3,1.3,1.4,1.5] #height in kg
np_weight = np.array(weight) #conversion into numpy array
np_height = np.array(height) #conversion into numpy array
print("Mean is: " + str(np.mean(np_weight)))
print("Median is :" + str(np.median(np_height)))
print("Correlation between them is: "+ str(np.corrcoef(np_weight,np_height)))
