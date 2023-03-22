import math
import random
import utils
import numpy as np
import animated_visualizer

class SimulatedAnnealing:
    def __init__(self, objects, temp, alpha, stopping_temp):
        ''' parameters
            ---------
            objects: array-like
                list of objects which contain coordinates and weight
            temp: float
                initial temperature
            alpha: float
                rate at which temp decreases
            stopping_temp: float
                temperature at which annealing process terminates 
        '''

        self.objects = objects
        self.sample_size = len(objects)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temp = stopping_temp

        self.curr_solution = utils.randomSolution([0,0], self.temp)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

    # weight for this problem is potential energy of the whole system
    def weight(self, solution):
        ans = np.sqrt(np.square(self.objects[:,0]-np.array(solution[0]).T) + np.square(self.objects[:,1]-np.array(solution[1]).T)) * self.objects[:,2]
        ret = np.sum(ans)
        return ret

    def acceptance_probability(self, new_weight):
        return math.exp(-abs(new_weight - self.curr_weight) / self.temp)

    def accept(self, new_solution):
        new_weight = self.weight(new_solution)
        if new_weight < self.curr_weight:
            self.curr_weight = new_weight
            self.curr_solution = new_solution
            if new_weight < self.min_weight:
                self.min_weight = new_weight
                self.best_solution = new_solution
        
        else:
            if random.random() < self.acceptance_probability(new_weight):
                self.curr_weight = new_weight
                self.curr_solution = new_solution

    def anneal(self):
        while self.temp >= self.stopping_temp:
            new_solution = utils.randomSolution(self.curr_solution, self.temp)

            self.accept(new_solution)
            self.temp *= self.alpha
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)
        
        print("The final location of the knot is: ")
        print(self.best_solution)
    
    def animateSolutions(self):
        animated_visualizer.animateSA(self.solution_history)
    
    def drawWeight(self):
        animated_visualizer.animateWeightSA(self.weight_list)
