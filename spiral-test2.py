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
n=4
#radius in pixels
r=100
#rotation factor
rot=0

def create_shape(n,C,x_coords,y_coords, color):
    if n==3:
        C.create_polygon(x_coords[0],y_coords[0],x_coords[1],y_coords[1],x_coords[2],y_coords[2],x_coords[3],y_coords[3], fill="", outline=color)
    if n==4:
        C.create_polygon(x_coords[0],y_coords[0],x_coords[1],y_coords[1],x_coords[2],y_coords[2],x_coords[3],y_coords[3], fill="", outline=color)


x_coords=[]
y_coords=[]
for i in range(4):
    x_coords.append(350+r*math.cos((2*math.pi*i)/n))
    y_coords.append(350+r*math.sin((2*math.pi*i)/n))
print(x_coords,y_coords)


k=0
while k<150:
    x_c=[]
    y_c=[]
    r+=10
    rot+=1
    for i in range(n):
        x_c.append(350+r*math.cos((rot+2*math.pi*i)/n))
        y_c.append(350+r*math.sin((rot+2*math.pi*i)/n))

    C.create_polygon(x_c[0],y_c[0],x_c[1],y_c[1],x_c[2],y_c[2],x_c[3],y_c[3], fill="", outline='black')
    m.update()
    time.sleep(animation_refresh_seconds)
    k+=1


'''
k=0
while k<150:
    C.create_line(350+10*k,0,350+10*k,700, fill="black", width=1)
    m.update()
    time.sleep(animation_refresh_seconds)
    k+=1
'''   

m.mainloop()