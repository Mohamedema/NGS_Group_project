#this_python_script_to_solve_issue4
#please_check_issue"not in gzip format - error"
#import_listdirectory_and_rename_from_os_python_library
from os import listdir,rename
#list_all_fastq_files_in_thefolder
files = listdir()
#define_function_to_replace_gz.1_to_.1
def new_n(src):
	w = src.split(".")[:-1] 
    	dst = ".".join(w) 
	return dst
#loop_to_all_fastq_files
for f in files:
	os.rename(f,new_n(f))
