#clean up stuff

import os
import glob

def clean():
	filenames = glob.glob("trump_exec_order_*")
	print(filenames)

	for filename in filenames:
		print(os.path.exists(filename))
		if(os.path.exists(filename)):
			os.remove(filename)
