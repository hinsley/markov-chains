import random

class MarkovChain(object):
    def __init__(self, initial_state=None):
        self._state_matrix = {}
        self._current_state = initial_state

    def delNode(self, a, b):
        del self._state_matrix[a][b]

        if len(self._state_matrix[a]) == 0:
            del self._state_matrix[a]

    def getNode(self, a=None, b=None):
        try:
            if a == None:
                return self._state_matrix
            elif b == None:
                return self._state_matrix[a]
            else:
                return self._state_matrix[a][b]
        except KeyError:
            return None

    def getState(self):
        return self._current_state

    def nextNode(self):
        option_vectors = self.getNode(self._current_state)

        options = [option for option in option_vectors]
        weights = [option_vectors[option] for option in options]

        self._current_state = random.choices(options, weights)[0]

    def setNode(self, a, b, weight):
        if not (a in self._state_matrix):
            self._state_matrix[a] = {}

        self._state_matrix[a][b] = weight

    def setState(self, state):
        self._current_state = state
