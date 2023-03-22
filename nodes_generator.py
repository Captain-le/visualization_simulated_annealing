import numpy as np

class NodeGenerator:
    def __init__(self, width, height, weight, nodesNumber):
        self.width = width
        self.height = height
        self.weight = weight
        self.nodesNumber = nodesNumber
    
    def generate(self):
        x = np.random.randint(-self.width, self.width, size=self.nodesNumber)
        y = np.random.randint(-self.height, self.height, size=self.nodesNumber)
        z = np.random.randint(self.weight, size=self.nodesNumber)

        return np.column_stack((x,y,z))