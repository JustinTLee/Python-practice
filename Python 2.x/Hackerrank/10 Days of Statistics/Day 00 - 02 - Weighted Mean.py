n = input()
str_x = raw_input().split(' ')
str_w = raw_input().split(' ')

x = [float(xelement) for xelement in str_x]
w = [float(welement) for welement in str_w]

weights_sum = sum(w)

weighted_sum = 0
for k in range(n):
    weighted_sum = weighted_sum + x[k]*w[k]

weighted_average = round(weighted_sum/weights_sum, 1)

print weighted_average