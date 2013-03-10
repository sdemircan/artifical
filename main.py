from artificallib.network import Network

network = Network(0.5, 0.8, [2, 2, 1])
network.setWeights([0.129952, -0.923123, 0.570345, -0.328932, 0.164732, 0.752621])
network.setBiasValues(0, [0.341332, -0.115223])
network.setBiasValues(1, [-0.993423])
print ""
network.train([[0,0]], [0])

