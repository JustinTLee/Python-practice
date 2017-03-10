# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def geometric_dist(p, k):
    prob_k = (1 - p) ** (k - 1) * p
    return prob_k

stream1 = raw_input().split(' ')
k = input()
stream1 = [float(sel) for sel in stream1]
p = stream1[0]/stream1[1]

print round(geometric_dist(p, k), 3)