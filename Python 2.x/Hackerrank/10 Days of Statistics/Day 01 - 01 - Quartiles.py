# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = input()
x_str = raw_input().split(' ')
x = [float(xelement) for xelement in x_str]

x.sort()

if n % 2 != 0:
    median_index = int(math.ceil(n/2))
    num_in_each_half = int(math.floor(n/2))
    lower_half = x[0:median_index]
    upper_half = x[(median_index + 1):]

    Q1 = int((lower_half[num_in_each_half/2] + lower_half[num_in_each_half/2 - 1])/2)
    Q2 = int(x[median_index])
    Q3 = int((upper_half[num_in_each_half/2] + upper_half[num_in_each_half/2 - 1])/2)
else:
    half_index = n/2
    lower_half = x[0:half_index]
    upper_half = x[half_index:]
    if half_index % 2 != 0:
        Q1 = int(lower_half[int(math.floor(half_index/2))])
        Q3 = int(upper_half[int(math.floor(half_index/2))])
    else:
        Q1 = int((lower_half[half_index/2] + lower_half[half_index/2 - 1])/2)
        Q3 = int((upper_half[half_index/2] + upper_half[half_index/2 - 1])/2)
        
    Q2 = int((x[n/2] + x[n/2 - 1])/2)

print Q1
print Q2
print Q3