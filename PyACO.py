import numpy as np
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
			bounds[1,j]=input("Enter");
	phe = np.float64(input("Enter Pheromonoe Evaporation rate")); #Pheronome Evaporation Rate
