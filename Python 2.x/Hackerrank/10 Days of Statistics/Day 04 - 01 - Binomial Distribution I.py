# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nChoosek(x, n):
    x_factorial = math.factorial(x)
    n_factorial = math.factorial(n)
    n_x_factorial = math.factorial(n - x)
    return n_factorial/(x_factorial*n_x_factorial)

ratio = raw_input().split(' ');
ratio = [float(ratioel) for ratioel in ratio]
p = ratio[0]/sum(ratio)

cumprob = 0

for k in range(3, 7):
    cumprob = cumprob + nChoosek(k, 6) * p ** (k) * (1 - p) ** (6 - k)

print round(cumprob, 3)