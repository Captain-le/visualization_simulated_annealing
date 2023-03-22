from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing

def main():
    # set simulated annealing parameters
    temp = 1926
    stopping_temp = 0.00000000000001
    alpha = 0.993

    # set parameters for nodes
    size_width = 1000
    size_height = 1000
    size_weight = 1000
    size_nodesNumber = 1000

    # generate random list of nodes
    nodes = NodeGenerator(size_width, size_height, size_weight, size_nodesNumber).generate()
    
    # run simulated annealing
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp)
    sa.anneal()

    # animate solutions during simulated annealing
    sa.animateSolutions()

    # show improvement of weight during simulated annealing
    sa.drawWeight()

if __name__ == "__main__":
    main()