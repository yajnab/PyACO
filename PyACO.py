import numpy as np
import random
class PyACO:
	n_val = int(input("Enter the Number of Variables")); #Number of Variables for the Problem to be Optimized
	maxiter = input("Enter the maximum Iterations"); #Maximum number of Iterations
	maxroute = input("Enter the maximum amount of routes"); #Maximum number of route the ants can make
	'''
	 bounds Array to Store bounds where bounds (n_val,0) is the lower limit of the variable and (n_val,1) is the upper bound
	'''
	bounds = np.ones((n_val,2), dtype=np.float64) 
	print("Enter the Lower and Upper bounds of each variable \n")
	for i in range(n_val):
		for j in range(2):
			bounds[i,j]=input("Enter");
	phe = np.float64(input("Enter Pheromonoe Evaporation rate")); #Pheronome Evaporation Rate

	res = np.zeros(maxiter, dtype=np.float64); #Value Array for all the iterations

	#Code for the Solution generation
	for gi in range(maxiter):

		res_route = np.zeros(maxiter, dtype=np.float64); #Value Array for all the Routes
		res_route_phe = np.zeros(maxiter, dtype=np.float64); #Pheromone Value Array for all the Routes

		for rc in range(maxroute):
			tval = np.zeroes(n_val, dtype=np.float64);

			for i in range(n_val):
				tval[i]=random.uniform(bounds[i,0],bounds[i,1])
