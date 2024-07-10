def intro():
    name = "bob"
    age = 7
    weight = 12.1

    #print out variable name
    rint(name)

    #print the data type of weight --> float
    print(type(weight))

    #print data type of weit and then weight itself 
    print(type(weight),weight)

    #now weight has data type int 
    weight = int(12.1)

    adult = true

    if age < 18:
        adult = false 

    print (adult)


def conditional():
    temprature = float(input("temprature: \n"))

    if temprature > 24.0:
        print ("hot")
    elif temprature < 22.2:
        print ("cold")
    else:
        print("warm")


def loops():
    classroom = ["Gulce", "Harper", "Tarick", "Tian", "Gustavo"]

    for i in classroom:
        print(i)

    for i in range(5):
        print(classroom[i])


def forloopExercise1():
    name = "Tian"
    for i in range(4):
        print(name)

def forloopExercise2():
    numbers = [2,4,6,-2,5,4,7,9,15]
    newnumbers = []
    
    for i in numbers:
        #print(i+2) 
        newnumbers.append(i+2)
        #newnumbers=newnumebrs + [i+2] also works 

    x = [i+2 for i in numebrs]
    
    print (x)

def forloopExercise3():
    x = int(input())

    for i in range(x):
        print("*"*i)

    for i in range(x):
        print("*"*(x-i))

   #for i in range(x,0,-1):
       # print("*"*i)
   
    """
    for b in range(6):
        print
    """

def whileloopexercise1():
    x = -1
    while x != 10:
        x=x+1
        print (x)

def functions(name, surname):
    print("Welcome", name, surname)

#a = input()
#b = input()


def ex1():
    x = float(input())
    print(x * 273.15)

def ex2():
    a = int(intput())
    b = int(intput())

    print((a+b)*10)

def ex3():
    x = int(input())
    a = 1
    result = 1
    while a != x:
        result = result * (a+1)
        a = a + 1
    print(result)  

def ex4():
    x = float(input())
    print(x*1.6)


def ex5():
    x = int(input())
    
    for i in range(2, (x//2)+1):
        if (x % i) == 0:
            print("not prime")
            break
        else:
            print("prime")
            break
    else:
        print("prime")
        

ex3()
