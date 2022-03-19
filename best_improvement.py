import local_search
import numpy as np


ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)

solutionsChecked = 0 
ls.initialize_values()
ls.initialize_weights()
curr_sol = ls.initialize_randn_solution()
curr_sol = ls.remove_infeasibility(curr_sol)

best_sol = curr_sol[:]

change = True

while change:
    
    neighbors = ls.get_1flip_neighborhood(curr_sol)
    feasible_sols = [ls.remove_infeasibility(sol) for sol in neighbors]
    
    solutionsChecked +=len(feasible_sols) 
    better_sol =sorted(feasible_sols, key= lambda x: -ls.get_total_value(x))[0]
    if ls.get_total_value(better_sol) > ls.get_total_value(best_sol):
        best_sol = better_sol[:]
        curr_sol = better_sol[:]
        
    elif ls.get_total_value(better_sol) == ls.get_total_value(best_sol):
        change = False



print("*************** LOCAL SEARCH WITH BEST IMPROVEMENT ******************")             
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", ls.get_total_value(best_sol))
print ("Weight is: ", ls.get_total_weight(best_sol))
print ("Total number of items selected: ", np.sum(best_sol))
print ("Best solution: ", best_sol)
