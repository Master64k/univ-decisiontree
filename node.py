
__author__ = "Nícolas Costa"
__credits__ = ["Nícolas Costa"]
__license__ = "WTFPL"
__version__ = "0.3"
__maintainer__ = "Nícolas Costa"


class Node():

    state = None
    fatherNode = None
    action = None
    cost = 0
    depth = 0

    def __init__(self, state, fatherNode, action, cost, depth):
        self.state = state
        self.fatherNode = fatherNode
        self.action = action
        self.cost = cost
        self.depth = depth

    def show(self):
        print('[ state: ' + str(self.state) + ' -  father node: ' + str(self.fatherNode) + ' - action: ' + str(
            self.action) + ' - cost: ' + str(self.cost) + ' - depth: ' + str(self.depth) + ' ]')

# class Node