import tkinter as tk

m = tk.Tk()
m.geometry("700x700")
#m.background("gray")
m.title("Hey")



C = tk.Canvas(m,width=700,height=700)

def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
m.bind('<Motion>',callback)


m.mainloop()

#define the endpoints of a ngon
n=4


C.create_polygon()