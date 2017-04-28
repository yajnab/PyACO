'''
 * Author - Yajnavalkya Bandyopadhyay
 * email- 	yajnab@gmail.com
 * Civil Engineering Student
 * Techno India College of Technology
'''
import numpy as np #Import Numpy
from PyACO import pyco
class prob:

	def func(x):
		val = 2*x[0] + 4*x[1]/x[0] + x[0]*x[1]*x[2]  #Calculate the Value
		return(val)
	#Constraints goes here
	#n_cnstr = 3
	#cnstr = np.ones(n_cnstr, dtype=np.float64) #Declare the constraints array
	#Number of Constraints in the form of g(x) => 0
	def cons(cnstr, x):
		cnstr[0] = x[0]*x[1] - 1 #1st Constraints Goes Here
		cnstr[1] = 2*x[0] + x[1];#2nd Constraint Goes Here
		cnstr[2] = x[2]-85#3rd Constraint Goes Here

	PyACO(func, cons, n_val, maxiter, maxroute, phe)
