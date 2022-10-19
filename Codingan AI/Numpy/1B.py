#Nama= Riska Octavia Arianto
#NIM= 21091397059
#Multi Neuron

#inisialisasi numpy
import numpy as np

#inisialisasi variabel
#Input layer feature 10 
inputs = [3.0, 0.5, 1.0, 0.32, -1.0, 0.27, 7.0, 5.0, 6.0, 10.0]

#Neuron 5
weights = [[1.0, 7.0, 5.0, 0.2, 0.8, 0.2, 0.1, 0.3, 0.5, -0.4],
[0.22, 0.24, 0.29, 0.2, 0.8, 0.25, -2.0, 0.33, 0.89, 0.49],
[0.34, 0.6, 0.7, 0.23, 0.24, -0.29, -0.46, 0.78, 0.99, -0.1],
[3.0, 0.29, 0.9, 6.0, 4.0, 4, 8, 0.75, 0.35, 0.22],
[1.0, 0.3, -2.0, 1.0, -0.25, -0.44, 7.0, -0.1, 0.34, -0.56]]

#banyak bias tergantung dari berapa banyak neuron yang ada
biases = [9.0, 4.0, 2.0, 8.0, 3.0]

#output dari rumus numpy
output = np.dot(weights, inputs) + biases

#print out
print(output)