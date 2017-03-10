# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def nChoosek(x, n):
    x_factorial = math.factorial(x)
    n_factorial = math.factorial(n)
    n_x_factorial = math.factorial(n - x)
    return n_factorial/(x_factorial*n_x_factorial)

p = raw_input().split(' ')
p = [float(pel) for pel in p]
n = p[1]
p = p[0]/100

nomorethantwo = 0
for k in range(0, 3):
    nomorethantwo = nomorethantwo + nChoosek(k, n) * p ** (k) * (1 - p) ** (n - k)
    
atleasttwo = 0
for k in range(2, 11):
    atleasttwo = atleasttwo + nChoosek(k, n) * p ** (k) * (1 - p) ** (n - k)

print round(nomorethantwo, 3)
print round(atleasttwo, 3)