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

m.title("Hey")

C = tk.Canvas(m,width=700,height=700,background="black")
C.pack()

#number of points
n=3
#radius in pixels
r=50
dr=-5
#rotation factors
rot=0

def create_shape(Cv,coordList, color):
    Cv.create_polygon(coordList, fill="", width=3, outline=color)

k=0
colorList=["red","orange","yellow","green","blue","white"]
while k<700:
    coords=[]
    if r==300 or r==50: dr=-dr
    if k%10==0 : 
        n+=1
        r+=dr
    else:
        r+=dr
    
    print(r,dr)
    rot+=0.05

    for i in range(n):
        coords.append(350+r*math.cos((rot+2*math.pi*i)/n))
        coords.append(350+r*math.sin((rot+2*math.pi*i)/n))


    C.create_polygon(coords, fill="", width=3, outline=colorList[k%6], tag=f"{k}")
    if k>30: C.delete(f"{k-30}")
    m.update()
    time.sleep(animation_refresh_seconds)
    k+=1


m.mainloop()