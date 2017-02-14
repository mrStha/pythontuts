import sys

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,55]

c=[i for i in a if i in b ]
"""count =0
d=[]
print  a
for num in a:
    for i in b:
    '
    '
            if (num == i ):
                c.append(num)


for i in range(len(c)):
                    if c [i]!=c[i+1]:
                       d.append(c[i])

print " final array is ", d
"""
print c

#for j in range(len(c)):
#c = [i for i in c if c.count(i)<=1]
#print c
d= [nums for nums in b if nums in a]
print d
