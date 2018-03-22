# This will disamble a certain function and let you know how it works in C level.
import dis

def func():
	for i in xrange(100000):
		print i

dis.disco(func.__code__)




