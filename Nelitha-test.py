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




C.pack()
m.mainloop()