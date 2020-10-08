from itertools import cycle
from sys import argv

my_list = [1, "a", 2, "b", True, "3" ]

name, stop = argv
stop = int(stop)


def my_func(n):
	count_num = 0
	for i in cycle(my_list):
		if count_num < n:
			print(i)
		count_num +=1

gen = my_func(stop)
gen()