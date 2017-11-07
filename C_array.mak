# ---- Link ---------------------------
_C_array.so:  C_array.o  C_array.mak
	gcc -bundle -flat_namespace -undefined suppress -o _C_array.so  C_array.o

# ---- gcc C compile ------------------
C_array.o:  C_array.c C_array.h C_array.mak
	gcc -c C_array.c -I/Users/edgarfigueiras/anaconda/envs/env_2.7/include/python2.7 -I/Users/edgarfigueiras/anaconda/envs/env_2.7/lib/python2.7/site-packages/numpy/core/include/numpy

#-I/Users/edgarfigueiras/anaconda/include/python3.6
#-I/Users/edgarfigueiras/anaconda/lib/python3.6/site-packages/numpy/core/include/numpy

#Original source
#gcc -c C_arraytest.c -I/Library/Frameworks/Python.framework/Versions/2.4/include/python2.4
#-I/Library/Frameworks/Python.framework/Versions/2.4/lib/python2.4/site-packages/numpy/core/include/numpy