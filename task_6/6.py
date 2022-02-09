from itertools import cycle, count
n = 100
my_list = [i for i in range(6)]
counter = count()
cycler = cycle(my_list)
print([next(counter) for i in range(n)])
print([next(cycler) for i in range(n)])
