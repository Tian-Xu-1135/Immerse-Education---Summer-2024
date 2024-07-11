from tkinter import*
import time

win = Tk() #create window object
win.geometry("800x600") #make window that is 800x600

c = Canvas(win,width=800, height=600, bg = "white") #specify background as whilte 
c.pack() #prints canvace window 

one = c.create_rectangle(600, 300, 700, 550, fill = "black") #specify a rectangle of the trafficlight box and fill in black
light2 = c.create_rectangle(200, 300, 300, 550, fill = "black")

radius = 25 #define light of the radus 

#x of one
x = 650 

#x of light2
a = 250

#cordinates of the centre of the top light
topyxcentre = 350 

#cordinates of the centre of the mid light
midyxcentre = 420

#cordinates of the centre of the bot light
botyxcentre = 500

#box1 make circles 
one = c.create_oval(x-radius, botyxcentre-radius, x+radius, botyxcentre+radius, fill="black")
one = c.create_oval(x-radius, midyxcentre-radius, x+radius, midyxcentre+radius, fill="black")
one = c.create_oval(x-radius, topyxcentre-radius, x+radius, topyxcentre+radius, fill="black")
#box2 make circles 
two = c.create_oval(a-radius, botyxcentre-radius, a+radius, botyxcentre+radius, fill="black")
two = c.create_oval(a-radius, midyxcentre-radius, a+radius, midyxcentre+radius, fill="black")
two = c.create_oval(a-radius, topyxcentre-radius, a+radius, topyxcentre+radius, fill="black")

while True:
    def light():
    
        #1 green 3 seconds
        one = c.create_oval(x-radius, botyxcentre-radius, x+radius, botyxcentre+radius, fill="green") #define top and fill with green
        two = c.create_oval(a-radius, topyxcentre-radius, a+radius, topyxcentre+radius, fill="red")
        win.update()
        time.sleep(3)
        
        #1 goes yellow, green off
        one = c.create_oval(x-radius, midyxcentre-radius, x+radius, midyxcentre+radius, fill="yellow")
        one = c.create_oval(x-radius, botyxcentre-radius, x+radius, botyxcentre+radius, fill="black")
        win.update()
        time.sleep(1)

        #1 yellow turn off
        #2 red goes off
        one = c.create_oval(x-radius, midyxcentre-radius, x+radius, midyxcentre+radius, fill="black")
        two = c.create_oval(a-radius, topyxcentre-radius, a+radius, topyxcentre+radius, fill="black")
        win.update()

        #2 green 6 seconds
        one = c.create_oval(a-radius, botyxcentre-radius, a+radius, botyxcentre+radius, fill="green") 
        two = c.create_oval(x-radius, topyxcentre-radius, x+radius, topyxcentre+radius, fill="red")
        win.update()
        time.sleep(6)

        #2 goes yellow, green off
        two = c.create_oval(a-radius, midyxcentre-radius, a+radius, midyxcentre+radius, fill="yellow")
        two = c.create_oval(a-radius, botyxcentre-radius, a+radius, botyxcentre+radius, fill="black")
        win.update()
        time.sleep(1)
        
        #2 yellow turn off
        #1 red goes off
        two = c.create_oval(a-radius, midyxcentre-radius, a+radius, midyxcentre+radius, fill="black")
        one = c.create_oval(x-radius, topyxcentre-radius, x+radius, topyxcentre+radius, fill="black")
        win.update()

        """
        1
        red:    one = c.create_oval(x-radius, topyxcentre-radius, x+radius, topyxcentre+radius, fill="red")
        yellow: one = c.create_oval(x-radius, midyxcentre-radius, x+radius, midyxcentre+radius, fill="yellow")
        green:  one = c.create_oval(x-radius, botyxcentre-radius, x+radius, botyxcentre+radius, fill="green")

        2
        red:    two = c.create_oval(a-radius, topyxcentre-radius, a+radius, topyxcentre+radius, fill="red")
        yellow: two = c.create_oval(a-radius, midyxcentre-radius, a+radius, midyxcentre+radius, fill="yellow")
        green:  two = c.create_oval(a-radius, botyxcentre-radius, a+radius, botyxcentre+radius, fill="green")
     
        """

    light()

win.mainloop()
