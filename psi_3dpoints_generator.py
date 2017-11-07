#!/usr/local/bin/pythonw

import _C_array
import numpy as np
import random
import os.path
from math import sin 
from time import time
from datetime import timedelta
import sys
	

# #### Run code ##################################################
if __name__ == '__main__':
	
	path="/Users/edgarfigueiras/Desktop/3d_Python_C/dataVortex/"

	psi_files_number=0

	while (os.path.isfile(path+ str(psi_files_number) +"psi")):
		psi_files_number += 1

	print("psi_files_number: ", psi_files_number-1)

	#number of 3D points for each step
	number_of_points=10000

	#3D matrix creation
	matrix_3d = np.zeros((psi_files_number,number_of_points,4))

	for cont_file in range(0, psi_files_number):

		file_with_binary_data = open(path+ str(cont_file) +"psi", 'rb+') #File with binary data

		array_with_all_data = np.load(file_with_binary_data) #Gets the binary data as an array with 6 vectors (x_data, x_probability, y_data, y_probability, z_data, z_probability)

		#Matrix with the data of the 2D grid
		Z = array_with_all_data['arr_0'] 
		N = len(Z[0])   #Size of the matrix


		#start = time()
		matrix_3d[cont_file]=_C_array.psi2Dprob(Z, number_of_points)

		sys.stdout.write(str(cont_file) + '-')
		sys.stdout.flush()
		
	
	f = open(path + '3dData.3d', 'wb+')
	np.savez(f, matrix_3d)
	f.close()
	
	

	
# ###### STOP HERE ################################################
	sys.exit()





#  EOF
