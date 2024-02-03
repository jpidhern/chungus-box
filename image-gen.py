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
m.title("Sound to Art Converter")
C = tk.Canvas(m,width=700,height=700,background="black")
C.pack()

#starting number of points
n=3
dn=0
#starting radius in pixels
r=50
dr=0
#starting rotation factor
rot=0
drot=0.05
num_frames = len(volumeList)

def create_shape(Cv,coordList, color):
    Cv.create_polygon(coordList, fill="", width=3, outline=color)

k=0
colorList=["red","orange","yellow","green","blue","white"]
while k<num_frames:
    coords=[]
    if k%10==0: 
        n+=dn
        r+=dr
    else:
        r+=dr
    rot+=drot

    for i in range(n):
        coords.append(350+r*math.cos((rot+2*math.pi*i)/n))
        coords.append(350+r*math.sin((rot+2*math.pi*i)/n))


    create_shape(C,coords,colorList[k%6])
    m.update()
    time.sleep(animation_refresh_seconds)
    k+=1


m.mainloop()