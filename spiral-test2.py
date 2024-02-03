import tkinter as tk
import time
import math

m = tk.Tk()
m.geometry("700x700")
#m.background("gray")
m.title("Hey")

C = tk.Canvas(m,width=700,height=700)

#number of points
n=4
#radius in pixels
r=100

x_coords=[]
y_coords=[]
for i in range(4):
    x_coords.append(r*math.cos((2*math.pi*i)/n))
    y_coords.append(r*math.sin((2*math.pi*i)/n))
print(x_coords,y_coords)

C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill="white", outline='black')

C.pack()
m.mainloop()