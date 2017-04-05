import numpy as np
class PyACO:
	n_val = int(input("Enter the Number of Variables"));
	maxiter = input("Enter the maximum Iterations");
	maxroute = input("Enter the maximum amount of routes");
	bounds = np.ones((n_val,2), dtype=np.float64)
	print("Enter the Lower and Upper bounds of each variable \n")
	for i in range(n_val):
		for j in range(2):
			bounds[1,j]=input("Enter");
