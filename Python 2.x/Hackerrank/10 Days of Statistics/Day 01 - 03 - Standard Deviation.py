# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
str_x = raw_input().split(' ')
x = [float(xelement) for xelement in str_x]

mean = sum(x)/n

second_moment_sum = 0
for k in range(n):
    second_moment_sum = second_moment_sum + (x[k] - mean)**2

std = (second_moment_sum/n) ** 0.5

print std