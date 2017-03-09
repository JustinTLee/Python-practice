# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = input()
x_str = raw_input().split(' ')
x = [int(xelement) for xelement in x_str]
freq_str = raw_input().split(' ')
freq = [int(freq_el) for freq_el in freq_str]

S = [];
for num in range(n):
    counter = 0
    while counter < freq[num]:
        S.append(x[num])
        counter += 1;

        
x.sort()
S.sort()

n_s = sum(freq)
if n_s % 2 == 0:
    lh_S = S[0:n_s/2]
    uh_S = S[n_s/2:]
    n_h = n_s/2
    
    if n_h % 2 == 0:
        n_q = int(n_h/2)
        Q1 = round(float((lh_S[n_q] + lh_S[n_q - 1])/2), 1)
        Q3 = round(float((uh_S[n_q] + uh_S[n_q - 1])/2), 1)
        iqr = Q3 - Q1
    else:
        n_q = int(math.floor(n_h/2))
        Q1 = round(lh_S[n_q], 1)
        Q3 = round(uh_S[n_q], 1)
        iqr = Q3 - Q1
else:
    n_h = int(math.floor(n_s/2))
    lh_S = S[0:n_h]
    uh_S = S[(n_h + 1):]
    
    if n_h % 2 == 0:
        n_q = int(n_h/2)
        Q1 = round(float((lh_S[n_q] + lh_S[n_q - 1])/2), 1)
        Q3 = round(float((uh_S[n_q] + uh_S[n_q - 1])/2), 1)
        iqr = Q3 - Q1
    else:
        n_q = int(math.floor(n_h/2))
        Q1 = round(lh_S[n_q], 1)
        Q3 = round(uh_S[n_q], 1)
        iqr = Q3 - Q1
    
print iqr