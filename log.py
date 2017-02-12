#Let's log some stuff

import datetime
from datetime import datetime

def log(text):
	log_file = open("tRump.log", "a+")

	text = str(datetime.now()) + ": " + text

	log_file.write(text + "\n")

	log_file.close()