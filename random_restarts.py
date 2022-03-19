import local_search
import numpy as np


ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)

ls.initialize_values()
ls.initialize_weights()

rand_restarts = 3 


solutionsChecked = 0 
optimal_solution = [0,0] # assuming initial optimal solution


        
for i in range(rand_restarts):
    x_curr = ls.remove_infeasibility(ls.initialize_randn_solution())  #x_curr will hold the current solution
    x_best = x_curr[:]           
    f_curr = ls.evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
    f_best = f_curr[:]
                                #begin local search overall logic ----------------
    done = 0

    while done == 0:

        Neighborhood = ls.get_1flip_neighborhood(x_curr)   #create a list of all neighbors in the neighborhood of x_curr
        Neighborhood = [ls.remove_infeasibility(s) for s in Neighborhood]
        for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            eval_val = ls.evaluate(s)
            if eval_val[0] > f_best[0] :
                x_best = s[:]                 #find the best member and keep track of that solution
                f_best = ls.evaluate(s)[:]       #and store its evaluation  
                
        if f_best == f_curr:               #if there were no improving solutions in the neighborhood
            done = 1
        else:

            x_curr = x_best[:]         #else: move to the neighbor solution and continue
            f_curr = f_best[:]         #evalute the current solution

            print ("\nTotal number of solutions checked: ", solutionsChecked)
            print ("Best value found so far: ", f_best)  
        
        if optimal_solution[0] < f_best[0]: # checking if optimal value is less than best value in this iteration
            optimal_solution=f_best[:]      # assigning best optimal weight and values to optimal_solution
            optimal=x_best[:]               # assigning best selection of items to optimal
            
print("*************** LOCAL SEARCH WITH RANDOM RESTARTS ******************")
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", optimal_solution[0])
print ("Weight is: ", optimal_solution[1])
print ("Total number of items selected: ", np.sum(optimal))
print ("Best solution: ", optimal)