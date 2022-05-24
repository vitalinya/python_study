import os
from datetime import datetime

file_creation = os.path.getctime('59.py')
file_modification = os.path.getmtime('59.py')

print (datetime.fromtimestamp(file_creation),datetime.fromtimestamp(file_modification),sep='\n')