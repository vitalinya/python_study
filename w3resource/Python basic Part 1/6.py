def numbers(nums):

	print ('List: ',end='')
	print (nums.split(', '))
	print ('Tuple: ',end='')
	print (tuple(nums.split(', ')))

numbers('3, 5, 7, 23')