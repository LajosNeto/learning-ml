#%% [markdown]
## Operation

#%%
class Graph():

    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []
    
    def set_as_default(self):
        global _default_graph
        _default_graph = self


class Operation():
    
    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)
        
        _default_graph.operations.append(self)
    
    def compute(self):
        pass


class Add(Operation):
    
    def __init__(self, x, y):
        super.__init__([x,y])
    
    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var + y_var


class Multiply(Operation):
    
    def __init__(self, x, y):
        super.__init__([x,y])
    
    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var * y_var


class Matmul(Operation):
    
    def __init__(self, x, y):
        super.__init__([x,y])
    
    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)


class Placeholder():

    def __init__(self):
        self.output_nodes = []
        _default_graph.placeholders.append(self)


class Variable():

    def __init__(self, initial_value=None):
        self.value = initial_value
        self.output_nodes = []
        _default_graph.variables.append(self)


def traverse_postorder(operation):
    nodes_postorder = []
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
            nodes_postorder.append(node)
    recurse(operation)
    return nodes_postorder


#%%
g = Graph()
g.set_as_default()

A = Variable(10)
b = Variable(1)

x = Placeholder()

#%%
y = Multiply(A, x)
z = Add(y, b)

#%%
