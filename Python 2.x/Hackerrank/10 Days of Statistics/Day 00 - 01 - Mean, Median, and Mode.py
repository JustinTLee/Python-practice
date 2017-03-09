N = input()
str_x = raw_input().split(' ')
x = [float(x_element) for x_element in str_x]

mean = round(float(sum(x)/N), 1)

x.sort()

if N % 2 == 0:
    median = round((x[N/2 - 1] + x[N/2])/2, 1)
else:
    median = x[N/2 - 1]
    
largest_tally = 0
hits = []
for item in x:
    tally = list(x).count(item)
    if largest_tally < tally:
        largest_tally = tally
        mode = int(item)

print mean
print median
print mode