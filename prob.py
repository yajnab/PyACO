'''
 * Author - Yajnavalkya Bandyopadhyay
 * email- 	yajnab@gmail.com
 * Civil Engineering Student
 * Techno India College of Technology
'''
import numpy as np #Import Numpy

def func(a):
	x = a


	'''Change the part from here'''

	val = 2*x[0] + 4*x[1]/x[0] + x[0]*x[1]*x[2]  #Calculate the Value

	#Constraints goes here
	n_cnstr = 3 #Number of Constraints in the form of g(x) => 0
	cnstr = np.ones(n_cnstr, dtype=np.float64) #Declare the constraints array
	cnstr[0] = x[0]*x[1] - 1 #1st Constraints Goes Here
	cnstr[1] = 2*x[0] + x[1];#2nd Constraint Goes Here
	cnstr[2] = x[2]-85#3rd Constraint Goes Here
	
	'''Do Not Change any Code below'''
	validate = int(1)
	for i in range(n_cnstr):
		if (cnstr[i] < 0):
			validate = 0

	result = [validate, val, a]
	return result
	
