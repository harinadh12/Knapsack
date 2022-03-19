import local_search
import numpy as np



ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 1500)

ls.initialize_values()
ls.initialize_weights()

#monitor the number of solutions evaluated
solutionsChecked = 0
n_iters = 400
rand_sum = 0
random_restarts = 2 #Number of random restarts variable
restarts = 1        #count variable for random restarts
number_parallel_searches = 3 # Number of parallel searches
parallel_search = 1  # count variable
temp1 = 30
temp = temp1
alpha = 4
final_temp = 1
beta = 0.1
c = 0
best_solutions_list = []
best_values_list = []
while restarts <= random_restarts: # Condition for total random restarts
    restart_temp =  temp
    print('Random restart temp', temp)
    verified_solutions_list = []
    while parallel_search <= number_parallel_searches or restarts<= random_restarts : # parallel searches at different locations
        if(parallel_search <= number_parallel_searches):
            best_sol = ls.remove_infeasibility(ls.initialize_randn_solution())
            best_val = ls.get_total_value(best_sol)
            curr_sol,curr_val = best_sol,best_val
        else:
            best_val = max(best_values_list)
            index = best_values_list.index(best_val)
            best_sol = best_solutions_list[index]
            curr_sol,curr_val = best_sol,best_val
            for i in range(n_iters):           #hill climbing
                neighbor = ls.gen_neighb(curr_sol)
                rand_ngh = ls.remove_infeasibility(neighbor)
                solutionsChecked +=1
                if (total_value(rand_ngh)) > ls.get_total_value(curr_sol):
                    curr_sol = rand_ngh[:]
                else:
                    continue
        
        while temp > final_temp and parallel_search <= number_parallel_searches:    
            for i in range(n_iters):
                neighbor = ls.gen_neighb(curr_sol)
                rand_ngh = ls.remove_infeasibility(neighbor)
                while rand_ngh in verified_solutions_list: # Eliminating recycling
                    neighbor = ls.gen_neighb(curr_sol)
                    rand_ngh = ls.remove_infeasibility(neighbor)
                verified_solutions_list.append(rand_ngh)
                solutionsChecked +=1
                val_diff = ls.get_total_value(curr_sol) - ls.get_total_value(rand_ngh) 
                if val_diff < 0:
                    curr_sol = rand_ngh[:]
                elif ls.myPRNG.random() < np.exp(-val_diff / temp):
                    curr_sol = rand_ngh[:]
            temp = temp - 0.1*temp
        temp = restart_temp
        best_solutions_list.append(curr_sol)
        best_values_list.append(ls.get_total_value(curr_sol))
        parallel_search = parallel_search + 1
        if( parallel_search > number_parallel_searches):
            break  
    temp = temp1
    restarts = restarts + 1

best_solutions = zip(best_values_list, best_solutions_list)
sorted_solutions = sorted(best_solutions,reverse=True)
x = [ element for _, element in  sorted_solutions]
print(best_values_list)
best_sol = x[0]
print(sum(best_sol))
print("####### solutions checked #########",solutionsChecked)
print("########## Total Weight ##########",ls.get_total_weight(best_sol))
print (ls.get_total_value(best_sol))