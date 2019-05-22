import numpy as np
#%%
class Graph():
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
        self.constants = []
    
    def set_as_default(self):
        global _default_graph
        _default_graph = self


class Operation():
    def __init__(self, input_nodes=None):
        self.input_nodes = input_nodes
        self.output = None

        _default_graph.operations.append(self)
    
    def forward(self):
        pass
    
    def backward(self):
        pass


class BinaryOperation(Operation):
    def __init__(self, a, b):
        super().__init__([a,b])


class Add(BinaryOperation):
    def forward(self, a, b):
        return a + b


class Multiply(BinaryOperation):
    def forward(self, a, b):
        return a * b


class Divide(BinaryOperation):
    def forward(self, a, b):
        return np.true_divide(a, b)


class Matmul(BinaryOperation):
    def forward(self, a, b):
        return a.dot(b)