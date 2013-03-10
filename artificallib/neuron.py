#!/usr/bin/python

from artificallib.dentrite import Dentrite
from artificallib.utils import sigmoid

class Neuron:
     
    def __init__(self, numberOfDentrites=0, weigths=None):
        self.bias = 0.5
        self.activation = 1
        self.dentrites = []
        self.currentDentrite = 0

        self.output = 0
        self.delta = 0
        self.error = 0

        if (weigths != None) and (numberOfDentrites == len(weigths)):
            for i in range(len(weigths)):
                self.dentrites.append(Dentrite(weigths[i]))
        else:
            for i in range(numberOfDentrites):
                self.dentrites.append(Dentrite())
    
    def process(self, inputValue):
        if len(self.dentrites) > 0:
            self.output += inputValue * self.dentrites[self.currentDentrite].weight
            self.currentDentrite += 1
            
            if self.currentDentrite == len(self.dentrites):
                self.currentDentrite = 0
        else:
            self.output += inputValue
    
    def activate(self):
        if len(self.dentrites) > 0:
            self.output += self.bias * self.activation
            self.output = sigmoid(self.output)

    def reset(self):
        self.output = 0
        self.error = 0

    def calculateError(expected):
        self.error = expected - self.output
        return self.error

