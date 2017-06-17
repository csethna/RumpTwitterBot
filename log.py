#Let's log some stuff

import datetime
#from datetime import datetime
'''
"import datetime" references the datetime module, while "from datetime import 
datetime" references the datetime class. In this instance Python would always
refer to the class, because you listed it after the import datetime statement
on line 3.
The more 'Pythonic' way would be to import datetime, and for all the stuff that
said datetime.some-function change it to datetime.datetime.some-function.
'''
def log(text):
	log_file = open("tRump.log", "a+")

	text = str(datetime.datetime.now()) + ": " + text

	log_file.write(text + "\n")

	log_file.close()