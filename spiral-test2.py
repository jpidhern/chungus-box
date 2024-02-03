import tkinter as tk
import time
import math


'''
volume=how fast r increases
frequency= color
quality=saturation
nList= n. Not one to one. if nList between 20-30, n=6 for example
maxPoints = fireworks??
'''

# delay between successive frames in seconds
animation_refresh_seconds = 0.01

m = tk.Tk()
m.geometry("700x700")
#m.background("gray")
m.title("Hey")

C = tk.Canvas(m,width=700,height=700)
C.pack()

#number of points
n=3
#radius in pixels
r=50
#rotation factors
rot=0

def create_shape(n,Cv,coordList, color):
    Cv.create_polygon(coordList, fill="", width=3, outline=color)

k=0
while k<70:
    coords=[]
    r+=5
    rot+=0.05
    if k%10==0 : n+=1

    for i in range(n):
        coords.append(350+r*math.cos((rot+2*math.pi*i)/n))
        coords.append(350+r*math.sin((rot+2*math.pi*i)/n))


    create_shape(n,C,coords,"black")
    m.update()
    time.sleep(animation_refresh_seconds)
    k+=1
    print(n)


m.mainloop()