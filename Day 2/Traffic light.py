import time

while True:
    redST = time.time()

    print("red")
    time.sleep(1)
    print(time.time()-redST)
    time.sleep(1)
    print(time.time()-redST)

    print("green")
    greenST = time.time()
    time.sleep(1)
    print(time.time()-greenST)
    time.sleep(1)
    print(time.time()-greenST)

    print("yellow")
    yellowST = time.time()
    time.sleep(1)
    print(time.time()-yellowST)
    time.sleep(1)
    print(time.time()-yellowST)