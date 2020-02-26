#this_python_script_to_solve_issue4
#please_check_issue"not in gzip format - error"

from os import listdir,rename
files = listdir()

def new_n(src):
	w = src.split(".")[:-1] 
    	dst = ".".join(w) 
	return dst
for f in files:
	os.rename(f,new_n(f))
