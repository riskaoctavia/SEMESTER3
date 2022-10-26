#Nama= Riska Octavia Arianto
#NIM= 21091397059
#UTS part 2

#inisialisasi numpy
import numpy as num

#inisialisasi variabel
#Input layer feature 10 
#per batch nya 6 input
inputs = [[3.0, 2.0, 1.0, 7.0, 5.0, 10.0, 0.33, 9.0, 0.8, 0.1],
[4.0, 7.0, 1.5, 2.0, 0.5, 9.0, 1.25, 0.7, 3.0, 1.0],
[3.0, 0.5, 1.0, 0.32, -1.0, 0.27, 0.3, 0.9, 6.0, 4.0],
[-2.0, 6.0, 1.0, 7.0, 5.0, 0.2, 1.0, 2.0, 3.0, -1.0],
[0.7, 2.0, 1.0, 0.3, -5.0, 0.22,1.0, -0.25, 0.73, 6.0],
[0.25, -2.0, 0.33, 9.0, 0.8, 0.1, 0.5, -2.0, 1.0, -0.25]]

#Hidden layer 1, Neuron 5
weights1 = [[ 0.4, 0.6, 0.2, 2.3, 0.5, -0.4, 9.0, 0.8, 0.1, 0.5],
[-0.4, 2.0, 0.89, 3.0, -0.5, 1.4, 2.0, 1.0, 0.3, -5.0],
[6.0, -0.6, 8.0, 0.3, 0.25, -0.7, 1.0, 0.32, -1.0, 2.0],
[8.0, 0.45, -4.0, 7.0, 5.0, 0.4, 7.0, 5.0, 10.0, 0.33],
[9.0, 4.0, -0.2, 0.89, -2.0, -0.4, 0.5, -2.0, 1.0, -0.25]]

#banyak bias tergantung dari berapa banyak neuron layer1
biases1 = [8.0, 3.0, 4.0, 9.0, 1.0]

#Hidden layer2, neuron 3
weights2 = [[ -0.5, 1.4, 2.0, 2.3, 0.5],
[-0.4, 2.0, 0.89, 2.0, -5.0],
[0.45, -4.0, 7.0, -1.0, 2.0]]

#banyak bias tergantung dari berapa banyak neuron layer2
biases2 = [8.0, 3.0, 4.0]

#output layer1
layer1_output = num.dot(inputs, num.array(weights1).T) + biases1
#output layer2
#layer2_output = num.dot(layer1_output, num.array(weights2).T) + biases2

#print out
print(layer1_output)