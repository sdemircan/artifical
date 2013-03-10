#1/usr/bin/python

import random

class Dentrite:

    def __init__(self, weight=None):
        if weight == None:
            self.weight = random.random()
        else:
            self.weight = weight
