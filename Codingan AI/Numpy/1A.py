#Nama= Riska Octavia Arianto
#NIM= 21091397059
#Single Neuron

#inisialisasi numpy
import numpy as np

#inisialisasi variabel
#Input layer feature 10 
inputs = [5, 3, 2, 6, 4, 8, 7, 1, 10, 9]
#Neuron 1
weights = [0.1, 0.3, -0.6, 0.8, 0.4, 0.2, 0.1, 0.9, 0.5, -0.3]
#banyak bias tergantung dari berapa banyak neuron yang ada
bias = 6

#output dari rumus numpy
output = np.dot(weights, inputs) + bias

#print out
print(output)