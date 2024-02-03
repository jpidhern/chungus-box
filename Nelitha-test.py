import tkinter as tk

m = tk.Tk()
m.geometry("700x700")
#m.background("gray")
m.title("Hey")


C = tk.Canvas(m,width=700,height=700)
#oval = C.create_oval(80, 30, 140, 150, fill="blue")
#C.create_arc(150,200,550,500,extent =900,outline ="black",fill ="blue", width =2, style=tk.CHORD)
C.create_line(350,0,350,700, fill="black", width=1)
C.create_line(0,350,700,350, fill="black", width=1)
C.create_line(0,0,700,700, fill="black", width=1)
C.create_line(700,0,0,700, fill="black", width=1)

def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
m.bind('<Motion>',callback)


def create_circle(x,y,r,color):
   x1=x-r
   y1=y-r
   x2=x+r
   y2=y+r
   C.create_oval(x1,y1,x2,y2,fill=color, outline=color)

#C.create_arc(200,200,350,350,extent=330,outline ="blue",fill ="blue", width =2, style=tk.PIESLICE)
#C.create_oval(100,10,200,110)
def drawOval(x1,y1,x2,y2, c):
   C.create_oval(x1,y1,x2,y2,fill =c, outline=c)
   C.create_oval(y1,x1,y2,x2,fill =c, outline=c)
   C.create_oval(y1,700-x1,y2,700-x2,fill =c, outline=c)
   C.create_oval(x1,700-y1,x2,700-y2,fill =c, outline=c)
   C.create_oval(700-x1,700-y1,700-x2,700-y2,fill =c, outline=c)
   C.create_oval(700-y1,700-x1,700-y2,700-x2,fill =c, outline=c)
   C.create_oval(700-x1,y1,700-x2,y2,fill =c, outline=c)
   C.create_oval(700-y1,x1,700-y2,x2,fill =c, outline=c)

def drawCircle(x,y,r,c):
   create_circle(x,y,r,c)
   create_circle(y,x,r,c)
   create_circle(y,700-x,r,c)
   create_circle(x,700-y,r,c)
   create_circle(700-x,700-y,r,c)
   create_circle(700-y,700-x,r,c)
   create_circle(700-x,y,r,c)
   create_circle(700-y,x,r,c) 

drawOval(100,10,200,110,"blue")
drawOval(250,230,340,290,"red")   
drawOval(70,260,200,330,"green")
drawOval(0,300,40,320,"yellow")
drawOval(250,230,340,290,"orange")

C.pack()
m.mainloop()