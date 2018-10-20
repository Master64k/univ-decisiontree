from node import Node

__author__ = "Nícolas Costa"
__credits__ = ["Nícolas Costa"]
__license__ = "WTFPL"
__version__ = "0.3"
__maintainer__ = "Nícolas Costa"


problem = {'state_inicial': 3,
           'state_final': 8,
            'actions':
            [
                {'state': 2, 'action': 1, 'distance': 280},
                {'state': 2, 'action': 2, 'distance': 230},
                {'state': 4, 'action': 3, 'distance': 240},
                {'state': 5, 'action': 4, 'distance': 770},
                {'state': 6, 'action': 5, 'distance': 180},
                {'state': 8, 'action': 6, 'distance': 770},
                {'state': 7, 'action': 7, 'distance': 1330},
                {'state': 7, 'action': 8, 'distance': 1000},
                {'state': 9, 'action': 9, 'distance': 830},
                {'state': 8, 'action': 10, 'distance': 1400}
            ],
           'costs':
           [
               {'state': 1, 'action': 1, 'distance': 280},
               {'state': 2, 'action': 1, 'distance': 230},
               {'state': 3, 'action': 3, 'distance': 240},
               {'state': 3, 'action': 2, 'distance': 230},
               {'state': 3, 'action': 8, 'distance': 1000},
               {'state': 4, 'action': 4, 'distance': 120},
               {'state': 4, 'action': 6, 'distance': 770},
               {'state': 4, 'action': 7, 'distance': 1130},
               {'state': 5, 'action': 5, 'distance': 180},
               {'state': 7, 'action': 10, 'distance': 830},
               {'state': 7, 'action': 9, 'distance': 1400}
           ]}

class DecisionTree():

    problem = dict()
    border = None #Node()
    solution = list()

    def __init__(self):

        pass

    def search(self):

        self.border = Node(self.problem['initial_state'], None, None, 0,0)

        self.check_sublevel(self.border)

        print('solutions found:')

        for a in range(len(self.solution)):

            self.solution[a].show()

    def check_sublevel(self, level):

        if self.test_node(level):

            if len(self.solution) < 1:

                print('** one solution found **')

            else: print('** another solution found **')

            self.solution.append(level)

            return

        print('expanding...')

        sub_level = self.expand_node(level)

        if len(sub_level):

            print('sublevels:')

            for a in range(len(sub_level)):

                sub_level[a].show()

            print('-----------------')

            for a in range(len(sub_level)):

                print('checking sublevel...')

                sub_level[a].show()

                self.check_sublevel(sub_level[a])

        else: return False

    def expand_node(self, problem):

        actions = list()
        nodes = list()

        for a in range(len(self.problem['costs'])):

            if self.problem['costs'][a]['state'] == problem.state:

                actions.append(self.problem['costs'][a])

        for a in range(len(self.problem['actions'])):

            for b in range(len(actions)):

                if self.problem['actions'][a]['action'] == actions[b]['action']:

                    if actions[b]['action'] != problem.fatherNode and self.problem['actions'][a]['state'] != problem.state:

                        nodes.append(Node(self.problem['actions'][a]['state'], problem.state, None, actions[b]['distance'] + problem.cost, problem.depth+1))

        return nodes

    def test_node(self,  node) -> bool:

        if self.problem['final_state'] == node.state:

            return True

        else: return False

    def set_problem(self, init_state, end_state, actions: list, costs: list):

        self.problem['initial_state'] = init_state

        self.problem['final_state'] = end_state

        self.problem['actions'] = actions

        self.problem['costs'] = costs

# class DecisionTree

if __name__ == "__main__":

    dt = DecisionTree()

    dt.set_problem(3, 8, problem['actions'], problem['costs'])

    dt.search()

