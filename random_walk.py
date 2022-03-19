import local_search
import numpy as np


solutionsChecked = 0 


ls = local_search.LocalSearch(seed= 51132021,n= 150, max_weight= 2500)
ls.initialize_values()
ls.initialize_weights()

#varaible to record the number of solutions evaluated
p = 0.7       #probability initialization


x_curr = ls.remove_infeasibility(ls.initialize_randn_solution())  #x_curr will hold the current solution
x_best = x_curr[:]           #x_best will hold the best solution 
f_curr = ls.evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
f_best = f_curr[:]
done = 0

while done == 0:

    Neighborhood = ls.get_1flip_neighborhood(x_curr)   #create a list of all neighbors in the neighborhood of x_curr
    Neighborhood = [ls.remove_infeasibility(s) for s in Neighborhood]
    step = ls.myPRNG.random() # random value between 0 and 1
      
    if step >= p: # performing hill climbing if  random value is greater than given probability
        
        for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1

            eval_val = ls.evaluate(s)

            if eval_val[0] > f_best[0] :
                x_best = s[:]                 #find the best member and keep track of that solution
                f_best = eval_val[:]           #and store its evaluation  
                #break
        if f_best == f_curr:               #if there were no improving solutions in the neighborhood
            done = 1
        else:
            x_curr = x_best[:]         #else: move to the neighbor solution and continue
            f_curr = f_best[:]         #evalute the current solution

            print ("\nTotal number of solutions checked: ", solutionsChecked)
            print ("Best value found so far: ", f_best)  
        
    else:                                       # else selecting another random solution in the neighborhood for random walk
        x_best = ls.myPRNG.choice(Neighborhood)[:]
        f_best = ls.evaluate(x_best)[:]
        solutionsChecked = solutionsChecked + 1
 

   
print("*************** LOCAL SEARCH WITH RANDOM WALK ******************")        
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)