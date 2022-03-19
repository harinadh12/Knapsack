import local_search
import numpy as np



ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 1500)

ls.initialize_values()
ls.initialize_weights()


#monitor the number of solutions evaluated
solutionsChecked = 0

best_sol = ls.remove_infeasibility(initial_rand_solution())
best_val = total_value(best_sol)
curr_sol = best_sol[:]

max_k = 4 # k- neoghborhood operators
while solutionsChecked < 2000:
    k = 1
    while k <= max_k:
        if k == 1:
            nborhood = ls.gen_one_flip_neighbood(curr_sol) # get 1 flip neighborhood
        elif k== 2:
            nborhood = ls.gen_2_flip_neighbood(curr_sol) # get 2 flip neighborhood
        elif k== 3:
            nborhood = ls.gen_one_m_flip_neighbood(curr_sol,k) # get m flip neighborhood of initial 1 flip neighborhood
        elif k== 4:
            nborhood = ls.gen_swap_neighbood(curr_sol,20) # swap some random items 20 times in the knapsack

        nbor = ls.myPRNG.choice(nborhood) # randomly get a neighbor
        if solutionsChecked >= 2000: # checking for maximum number of solutions checked
            k = 5 
        else:
            solutionsChecked +=1

        if ls.get_total_weight(nbor) <= ls.max_weight: # checking for feasible solution
            if ls.get_total_value(nbor)>= ls.get_total_value(curr_sol): # if total value is increasing then move to the neighbor
                curr_sol = nbor[:]
                k = 1
            else:
                k += 1
        

print("*************** VARIABLE NEIGHBORHOOD SEARCH ******************")
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ",ls.get_total_value(curr_sol))
print ("Weight is: ", ls.get_total_weight(curr_sol))
print ("Total number of items selected: ", np.sum(curr_sol))
print ("Best solution: ", curr_sol)    