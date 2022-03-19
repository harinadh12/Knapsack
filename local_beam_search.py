import local_search
import numpy as np



ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)

ls.initialize_values()
ls.initialize_weights()
solutionsChecked=0

srchs = 10
curr_sols = [ls.initialize_randn_solution() for i in range(srchs)] # taking srchs# random initialisations  for srchs# parallel searches
curr_sols = [ls.remove_infeasibility(sol) for sol in curr_sols] # removing the infeasibility in initial solutions by 1 flip

change = True
while change:
    change= False
    neighbors = sum((ls.get_1flip_neighborhood(s) for s in curr_sols), []) # gathering the neighborhood for the initial solutions and combining into 1 single neighborhood
    neighbors += curr_sols  # adding initial sols to neighborhood so that they wont be missed in evaluation
    feasible_sols = [ls.remove_infeasibility(sol) for sol in neighbors] # getting all feasible sols through infeasbility removal by 1 flip mechanism
    solutionsChecked +=len(feasible_sols) # solutions checked is number of iterations run
    feasible_sols = sorted(feasible_sols, key = lambda sol: -ls.get_total_value(sol)) # sorting feasible sols by their total value
    
    if feasible_sols[:srchs] != curr_sols:
            curr_sols = feasible_sols[:srchs]
            change = True
            
best_sol = curr_sols[0]

print("*************** LOCAL BEAM SEARCH ******************")
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ",ls.get_total_value(best_sol))
print ("Weight is: ", ls.get_total_weight(best_sol))
print ("Total number of items selected: ", np.sum(best_sol))
print ("Best solution: ", best_sol)