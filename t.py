L = [1,1]
n = 2
while L[-1] < 100:
    s = L[n-1] + L[n-2]
    L.append(s)
    n += 1
L.pop()
print(L)
print('1111')

