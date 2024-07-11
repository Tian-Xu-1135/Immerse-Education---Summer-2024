import time

first_redST = time.time()

def reset():
    print("seconds road-1 \t road-2")
    first_redST = time.time()

def lights(time, colour1, colour2):
    for i in range(time):
        current_time = int(time.time() - first_redST)
        print(current_time, "\t ", colour1, "\t\t", colour2)
        time.sleep(1)

while True:

    reset()

    #road1 green first
    lights(3, "GREEN", "RED")
    reset()
    
    #road1 goes yellow 
    lights(1, "YELLOW", "RED")
    reset()

    #road2 goes green 
    lights(3, "RED", "GREEN")
    reset()
    
    #road2 goes yellow
    lights(1, "RED", "YELLOW")
    
    


