#!/usr/bin/python

from artificallib.neuron import Neuron

class Layer:

    def __init__(self, numberOfNeurons, numberOfDentrits = 0):
        self.neurons = []

        for i in range(numberOfNeurons):
            self.neurons.append(Neuron(numberOfDentrits))
    
    def process(self, inputValues):
        outputs = []

        for i in range(len(self.neurons)):
            self.neurons[i].reset()

            for inputValue in inputValues:
                self.neurons[i].process(inputValue)

            self.neurons[i].activate()

            outputs.append(self.neurons[i].output)

        return outputs


    def getErrors(self):
        errors = []

        for i in neuron in self.neurons:
            errors.add(neuron.error)

        return errors

    def getOutputs(self):
        outputs = []

        for i in neuron in self.neurons:
            outputs.add(neuron.output)

        return outputs

    def getWeights(self, index):
        weights = []

        for i in neuron in self.neurons:
            weights.add(neuron.dentrites[index].weight)

        return weights
