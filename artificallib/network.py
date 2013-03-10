#!/usr/bin/python

from artificallib.layer import Layer

class Network:

    def __init__(self, learningRate, momentum, layers):
        self.learningRate = learningRate
        self.momentum = momentum

        self.layers = []

        for i in layers:
            self.addLayer(i)
        self.layers.pop(0)

    def addLayer(self, numberOfNeurons):
        if len(self.layers) == 0:
            self.layers.append(Layer(numberOfNeurons)) #input layer
        else:
            self.layers.append(Layer(numberOfNeurons, len(self.layers[len(self.layers)-1].neurons)))

    def getWeightCount(self):
        counter = 0

        for layer in self.layers:
            for neuron in layer.neurons:
                for dentrite in neuron.dentrites:
                    counter += 1

        return counter

    def setWeights(self, weigths):
        if self.getWeightCount() == len(weigths):
        
             counter = 0
             for layer in self.layers:
                 for neuron in layer.neurons:
                     for dentrite in neuron.dentrites:
                         dentrite.weight = weigths[counter]
                         counter += 1
        else:
            print "Number of given weigths not equal to total weight number in network !"
    
    def process(self, inputValues):
        layer_output = []

        layer_output = inputValues
        for layer in self.layers:
            layer_output = layer.process(layer_output)

        return layer_output
    
    def setBiasValues(self, layer, biasValues):
        neurons = self.layers[layer].neurons
        for i in range(len(biasValues)):
            neurons[i].bias = biasValues[i]
            


