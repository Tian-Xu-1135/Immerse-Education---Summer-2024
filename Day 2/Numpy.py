import numpy as np #import libary as np (most connon convention)
import matplotlib.pyplot as plt #import the plotting function for matplotlib libary

#print(np.pi) #prints all pi

array1 = np.linspace(0, 2*np.pi, 100) #create a linea space array form 0 to 2pi with 100 elements 
array1_sine = np.sin(array1) #take sin of array1, sin function of the umpy class 
array1_cos = np.cos(array1)

print(array1_sine)

plt.plot(array1, array1_sine) #plots a graph using array1 as x and the sine array as y 
plt.show()# command to run and display the graph 

plt.plot(array1, array1_cos) #plots on the same graph but with cosine 
plt.show()# command to run and display the graph 