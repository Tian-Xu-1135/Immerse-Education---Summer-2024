fibonacci = [0, 1, 1]


while fibonacci[-1] < 1000:
    num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(num)
    print(fibonacci[-1]/fibonacci[-2])

print(fibonacci)