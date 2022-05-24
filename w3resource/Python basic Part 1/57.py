import time

def sum():
	sum = 0 
	for i in range(1000000):
	    sum += i
	return sum

start_time = time.time()

summary = sum()

stop_time = time.time()

time_stamp = stop_time - start_time

print(time_stamp)