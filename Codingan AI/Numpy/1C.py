#Nama= Riska Octavia Arianto
#NIM= 21091397059
#Multi Neuron Batch Input

#inisialisasi numpy
import numpy as np

#inisialisasi variabel
#Input layer feature 10 
#per batch nya 6 input
inputs = [[3.0, 2.0, 1.0, 7.0, 5.0, 10.0],
[4.0, 7.0, 1.5, 2.0, 0.5, 9.0],
[3.0, 0.5, 1.0, 0.32, -1.0, 0.27],
[-2.0, 6.0, 1.0, 7.0, 5.0, 0.2],
[0.7, 2.0, 1.0, 0.3, -5.0, 0.22],
[0.25, -2.0, 0.33, 9.0, 0.8, 0.1],
[-0.2, -0.4, 1.25, 0.7, 3.0, 1.0],
[-3.0, 1.0, 0.3, 0.9, 6.0, 4.0],
[0.5, -2.0, 1.0, -0.25, 0.73, 6.0],
[3.0, 6.0, 1.0, 2.0, 3.0, -1.0]]

#Neuron 5
weights = [[ 0.4, 0.6, 0.2, 2.3, 0.5, -0.4],
[-0.4, 2.0, 0.89, 3.0, -0.5, 1.4],
[6.0, -0.6, 8.0, 0.3, 0.25, -0.7],
[8.0, 0.45, -4.0, 7.0, 5.0, 0.4],
[9.0, 4.0, -0.2, 0.89, -2.0, -0.4]]

#banyak bias tergantung dari berapa banyak neuron yang ada
biases = [8.0, 3.0, 4.0, 9.0, 1.0]

#output dari rumus numpy
output = np.dot(inputs, np.array(weights).T) + biases

#print out
print(output)
