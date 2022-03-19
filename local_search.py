from random import Random 
import numpy as np
import itertools
class LocalSearch():

    def __init__(self, seed, n, max_weight):
        self.seed = seed
        self.n = n
        self.myPRNG = Random(seed)
        self.values = []
        self.weights = []
        self.max_weight = max_weight

    def initialize_values(self):
        for i in range(0,self.n):
            self.values.append(round(self.myPRNG.triangular(150,2000,500),1))

    def initialize_weights(self):
        for i in range(0,self.n):
            self.weights.append(round(self.myPRNG.triangular(8,300,95),1))

    def get_1flip_neighborhood(self, solution):
        neighborhood = []
        
        for i in range(0,self.n):
            neighborhood.append(solution[:])
            if neighborhood[i][i] == 1:
                neighborhood[i][i] = 0
            else:
                neighborhood[i][i] = 1
        
        return neighborhood
    
    def initialize_randn_solution(self):
        return [self.myPRNG.randint(0,1) for _ in range(self.n)]
    
    def get_total_value(self,solution):
        a = np.array(solution)
        b = np.array(self.values)
        totalValue = np.dot(a,b)
        return totalValue

    def get_total_weight(self, solution):
        c = np.array(self.weights)
        a = np.array(solution)
        totalWeight = np.dot(a,c)
        return totalWeight
    
    def remove_infeasibility(self, solution):
        while self.get_total_weight(solution) > self.max_weight:
            ind = self.myPRNG.randint(0,self.n-1)
            solution[ind] = 0
        return solution


    def evaluate(self, solution):    
        a = np.array(solution)
        b = np.array(self.values)
        c = np.array(self.weights)
        
        totalValue = np.dot(a,b)     #compute the value of the knapsack selection
        totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
        if totalWeight > self.max_weight:
            totalValue = 0
        return [totalValue, totalWeight]   #returns a list of both total value and total weight
    
    #flips one item of the knapsack initial solution
    def gen_one_flip_neighbood(self,x):
        nbhood = []
        for _ in range(self.n):
            tempx = x[:]

            ind = self.myPRNG.randint(0,self.n-1)
            if tempx[ind] == 0:
                tempx[ind] = 1
            else:
                tempx[ind] = 0
            nbhood.append(tempx)
        
        return nbhood

    #flips 2 items of the knapsack initial solution
    def gen_two_flip_neighbood(self,x):
        nbhood = []
        
        for i, j in itertools.combinations(range(0, self.n), 2):
            tempx = x[:]
            if tempx[i] == 1:
                tempx[i] = 0
            else:
                tempx[i] = 1
            if tempx[j] == 1:
                tempx[j] = 0
            else:
                tempx[j] = 1
                
            nbhood.append(tempx)
        return nbhood

    #flips m items of the 1flip solutions of the initial solution
    def gen_one_m_flip_neighbood(self,x, m):
        nbhood = []
        for i in range(0, self.n):
            nbhood.append(x[:])
            if nbhood[i][i] == 1:
                nbhood[i][i] = 0
            else:
                nbhood[i][i] = 1
            for _ in range(self.myPRNG.randint(0,m)):
                rand_int = self.myPRNG.randint(0,self.n-1)
                if nbhood[i][rand_int] == 1:
                    nbhood[i][rand_int] = 0
                else:
                    nbhood[i][rand_int] = 1
        return nbhood

    # swaps 2 items i.e., 1 into and other out of the knapsack
    def gen_swap_neighbood(self,x,m):
        nbhood = []
        for _ in range(m):
            tempx = x[:]
            i = self.myPRNG.randint(0,self.n-1)
            j = self.myPRNG.randint(0,self.n-1)
            tempx[i], tempx[j] = tempx[j], tempx[i]
            nbhood.append(tempx)
            
        return nbhood    