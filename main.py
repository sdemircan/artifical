#from artificallib.network import Network
import sys
from PyQt4 import QtGui
from gui.gui import Gui

#network = Network(0.5, 0.8, [2, 2, 1])
#network.setWeights([0.129952, -0.923123, 0.570345, -0.328932, 0.164732, 0.752621])
#network.setBiasValues(0, [0.341232, -0.115223])
#network.setBiasValues(1, [-0.993423])
#network.train([[0,0], [1,1], [1,0], [0,1]], [0, 0, 1, 1])
#print network.process([1, 1])
#print network.process([0, 1])

app = QtGui.QApplication(sys.argv)
ex = Gui()
sys.exit(app.exec_())


