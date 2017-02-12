#clean up stuff

import os
import glob
import log

def clean():
	filenames = glob.glob("trump_exec_order_*")

	for filename in filenames:
		if(os.path.exists(filename)):
			log.log("Removing: " + filename)
			os.remove(filename)
