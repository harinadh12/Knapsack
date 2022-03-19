import local_search
import numpy as np



ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)

ls.initialize_values()
ls.initialize_weights()
solutionsChecked=0

curr_sol = ls.remove_infeasibility(ls.initialize_randn_solution())  # initial random solution

n_iterations = 1000
best_sol = curr_sol[:]
for i in range(n_iterations):
    neighbors = ls.get_1flip_neighborhood(curr_sol)
    feasible_sols = [ls.remove_infeasibility(sol) for sol in neighbors]
    solutionsChecked +=len(feasible_sols)
    curr_sol  = ls.myPRNG.choices(feasible_sols, weights = [ls.get_total_value(s)-ls.get_total_value(curr_sol) for s in feasible_sols])[0]
    if ls.get_total_value(curr_sol) > ls.get_total_value(best_sol):
        best_sol = curr_sol[:]
            
print("*************** STOCHASTIC HILL CLIMBING ******************")
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ",ls.get_total_value(best_sol))
print ("Weight is: ", ls.get_total_weight(best_sol))
print ("Total number of items selected: ", np.sum(best_sol))
print ("Best solution: ", best_sol)
