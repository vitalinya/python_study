from random import randint

operation = ['+','-','*','/']

for iter in range(10):

	choose_operation = operation[randint(0,3)]
	number1 = randint(0, 10)
	number2 = randint(0, 10)
	if choose_operation == '+':
		print ('%d %s %d = %f' % (number1,choose_operation,number2,number1+number2))
	elif choose_operation == '-':
		print ('%d %s %d = %f' % (number1,choose_operation,number2,number1-number2))
	elif choose_operation == '*':
		print ('%d %s %d = %f' % (number1,choose_operation,number2,number1*number2))
	elif choose_operation == '/':
		print ('%d %s %d = %f' % (number1,choose_operation,number2,number1/number2))

