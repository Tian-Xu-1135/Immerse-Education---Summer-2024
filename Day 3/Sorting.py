"""
#swapping
a = 5
b = 3

#swaps the two in one line 
b,a = a,b
"""

#array = [12, 76, 3, 4, 35, 2, 10, 8]


num = int(input("length of your array:"))
bob = []

for i in range (0, num):
    bob.append(int(input(":")))

print("before sort:", bob)

def sorting (x):
    for i in range (len(x)-1):
        for i in range (len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    print("after sort:", x)


sorting(bob)