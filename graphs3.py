from math import *
from sympy import *
i = Symbol('i')
functions = list(map(list, enumerate([
    log(i, 3), 
    sqrt(i), 
    log(i, 2) ** log(i, 2),
    3 ** log(i, 2), 
    i ** 2, 
    7 ** log(i, 2), 
    4 ** i, 
    2 ** (2 ** i), 
    2 ** (3 * i), 
    log(factorial(i), 2), 
    log(log(i, 2), 2), 
    (log(i, 2)) ** 2, 
    2 ** i, 
    sqrt(log(i, 4)), 
    factorial(i), 
    i / (log(i, 5)), 
    i ** log(i, 2), 
    i ** sqrt(i)
])))

for y in range(len(functions)):
    for z in range(1, len(functions)):
        if limit(functions[z - 1][1] / functions[z][1], i, oo) == oo:
            functions[z - 1], functions[z] = functions[z], functions[z - 1]
for n in range(len(functions)):
    print(n + 1, '. ', functions[n][0] + 1, '. ', functions[n][1], sep='')
