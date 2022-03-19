import local_search
import numpy as np


ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)

ls.initialize_values()
ls.initialize_weights()



#varaible to record the number of solutions evaluated
solutionsChecked = 0

srchs = 10
curr_sols = [ls.initialize_randn_solution() for i in range(srchs)] # taking srchs# random initialisations  for srchs# parallel searches
curr_sols = [ls.remove_infeasibility(sol) for sol in curr_sols] # removing the infeasibility in initial solutions by 1 flip
n_iterations = 100
best_sol = curr_sols[0][:]

for i in range(n_iterations):
    
    neighbors = sum((ls.get_1flip_neighborhood(s) for s in curr_sols), []) # gathering the neighborhood for the initial solutions and combining into 1 single neighborhood
    
    feasible_sols = [ls.remove_infeasibility(sol) for sol in neighbors] # getting all feasible sols through infeasbility removal by 1 flip mechanism
    solutionsChecked +=len(feasible_sols) # solutions checked is number of iterations run
    curr_sols = []
    while len(curr_sols) < srchs:
        choice = ls.myPRNG.choices(feasible_sols, weights=[ls.get_total_value(s) for s in feasible_sols])[0]
        if choice not in curr_sols:
            curr_sols.append(choice)
    if curr_sols:            
        better_sol = sorted(curr_sols, key= lambda x: -ls.get_total_value(x))[0]
        if ls.get_total_value(better_sol) > ls.get_total_value(best_sol):
            best_sol = better_sol[:]
        

print("*************** STOCHASTIC BEAM SEARCH ******************")
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ",ls.get_total_value(best_sol))
print ("Weight is: ", ls.get_total_weight(best_sol))
print ("Total number of items selected: ", np.sum(best_sol))
print ("Best solution: ", best_sol)