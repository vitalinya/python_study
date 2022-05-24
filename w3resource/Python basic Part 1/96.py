import traceback

def f1():
	return f2()

def f2():
	traceback.print_stack()

f1()