#clean up stuff

import os
import glob
import log

def clean():
	filenames = glob.glob("trump_exec_order_*")
	print(filenames)

	for filename in filenames:
		print(os.path.exists(filename))
		if(os.path.exists(filename)):
			log.log("Removing: " + filename)
			os.remove(filename)
