from artificallib.network import Network

network = Network(0.5, 0.8, [2, 2, 1])
print network.process([0, 0])
print network.process([0, 1])
print network.process([1, 0])
print network.process([1, 1])

