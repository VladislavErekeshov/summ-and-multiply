f = open('input.txt')
ggd = f.readline()
n = f.readline()
n = n.split(' ')
n = [int(i) for i in n]
ans1 = 0
ans2 = 1
for i in n:
    if i > 0:
        ans1 = ans1 + i
a = min(n)
b = max(n)
imin = n.index(min(n))
imax = n.index(max(n))
if imax < imin:
    l = n[imax + 1:imin]
    for i in l:
        ans2 = ans2 * i
else:
    l = n[imin + 1:imax]
    for i in l:
        ans2 = ans2 * i
ans1 = str(ans1)
ans2 = str(ans2)
with open('output.txt', 'w') as f:
    f.write(ans1)
    f.write(' ')
    f.write(ans2)