import os
from datetime import datetime

def sorting():
	date_list = []
	list = os.listdir('.')
	for i in range(len(list)-1):
		date_list.append((list[i],os.path.getmtime(list[i])))
	sort_list = sorted(date_list, key=lambda x: x[1])
	for file,date in sort_list:
		print(file,datetime.fromtimestamp(date))

print(sorting())
