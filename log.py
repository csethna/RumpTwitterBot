#Let's log some stuff

import datetime
from datetime import datetime

def log(text):
	log_file = open("tRump.log", "w+")

	text = str(datetime.now()) + ": " + text

	log_file.write(text)

	log_file.close()