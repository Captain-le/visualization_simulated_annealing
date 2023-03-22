import random

# generate a random solution
def randomSolution(curr_solution, temp):
    RAND_MAX = 2147483647
    
    random_x = curr_solution[0] + (random.random()*RAND_MAX*2-RAND_MAX)*temp
    random_y = curr_solution[1] + (random.random()*RAND_MAX*2-RAND_MAX)*temp

    randSolution = [random_x, random_y]

    return randSolution