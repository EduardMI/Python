from itertools import count
from sys import argv

name, start, stop= argv
start = int(start)
stop = int(stop)
def my_func(el):
	count_num = 0
	for i in count(el):
		if count_num < stop:
			print(i)
			count_num +=1

gen = my_func(start)
gen()