#!/usr/bin/python

from artificallib.layer import Layer

class Network:

    def __init__(self, learningRate, momentum, layers, trainingCycles=100, errorTolerance=0.0):
        self.learningRate = learningRate
        self.momentum = momentum

        self.layers = []

        for i in layers:
            self.addLayer(i)
        self.layers.pop(0)

        self.TRAINING_CYCLES = trainingCycles
        self.ERROR_TOLERANCE = errorTolerance

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
            
    
    def train(self, listOfInputValues, expectedOutputs):
        if len(listOfInputValues) != len(expectedOutputs):
            print "expectedOutputs length not equal listOfInputValues length !"
            return

        for i in range(1):
            #For every input
            for j in range(len(listOfInputValues)):
                output = self.process(listOfInputValues[j])

                #Calculate output error
                error = 0
                for neuron in self.layers[-1].neurons:
                    error += neuron.calculateErrorOutput(expectedOutputs[j])
                if abs(error) <= self.ERROR_TOLERANCE:
                    print "Network trained."
                    return
               
                sigmaValues = []
                for value in output:
                    sigmaValues.append((1-value)*value*error)

                for layerIndex in range(len(self.layers)-1, -1, -1):
                    for neuronIndex in range(0, len(self.layers[layerIndex].neurons)):
                        if len(self.layers) -1 == layerIndex: #output layer
                            self.layers[layerIndex].neurons[neuronIndex].reCalculateOutputNeuronWeights(self.learningRate, 
                                            self.momentum, self.layers[layerIndex-1].getOutputs())
                    
                        break
                    break







