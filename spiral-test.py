import tkinter as tk
import time
 
# width of the animation window
animation_window_width=800
# height of the animation window
animation_window_height=600
# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 30
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.01
 
# The main window of the animation
def create_animation_window():
  window = tk.Tk()
  window.title("Tkinter Animation Demo")
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window
 
# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
  canvas = tk.Canvas(window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas
 
# Create and animate ball in an infinite loop
def animate_ball(window, canvas,xinc,yinc):
  ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
            animation_ball_start_ypos-animation_ball_radius,
            animation_ball_start_xpos+animation_ball_radius,
            animation_ball_start_ypos+animation_ball_radius,
            fill="blue", outline="white", width=4)
  while True:
    canvas.move(ball,xinc,yinc)
    window.update()
    time.sleep(animation_refresh_seconds)
    ball_pos = canvas.coords(ball)
    # unpack array to variables
    xl,yl,xr,yr = ball_pos
    if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
      xinc = -xinc
    if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
      yinc = -yinc
 
# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_ball(animation_window,animation_canvas, animation_ball_min_movement, animation_ball_min_movement)

m = tk.Tk()
m.geometry("700x700")
#m.background("gray")
m.title("Hey")

def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
m.bind('<Motion>',callback)

C = tk.Canvas(m,width=700,height=700)
#define the endpoints of a ngon
n=4
x1=100
y1=100
x2=200
y2=100
x3=200
y3=200
x4=100
y4=200
C.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4, fill="white", outline='black')
C.pack()

C = tk.Canvas(m,width=700,height=700)

m.mainloop()