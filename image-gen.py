import tkinter as tk
import time
import math

def intToHex(n):
    hexStr = ''
    while n>0:
        currDig = n%16
        #currHex = ''
        if currDig < 10:
            currHex = f'{currDig}'
        else:
            currHex = chr(ord('A')+currDig-10)
        hexStr = currHex + hexStr
        n //= 16
    
    if len(hexStr) > 1:
        return hexStr
    elif len(hexStr) == 1:
        return '0' + hexStr
    else:
        return '00'


def frequencyToRGB(frequency):
    if (frequency > 2000):
        r,g,b = (0,0,255)
    elif (frequency < 1000):
        r,g,b = (255-(frequency/1000 * 255), (frequency/1000 * 255), 0)
    else: 
        r,g,b = (0, 255-((frequency-1000)/1000 * 255),  ((frequency-1000)/1000 * 255))
    return '#' + intToHex(r) + intToHex(g) + intToHex(b)
'''
volume=how fast r increases
frequency= color ~200-1000
quality=saturation ~400-1000
nList= n. Not one to one. if nList between 20-30, n=6 for example. 3-30
maxPoints = fireworks??
'''

# delay between successive frames in seconds
animation_refresh_seconds = 1/30

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
max_vol = max(volumeList)
min_vol = min(volumeList)
#print(f"max vol is: {max_vol}")
k=0
colorList=["red","orange","yellow","green","blue","white"]
while k<num_frames:
    t1=time.time()
    r=(volumeList[k]) * (300/max_vol)
    n=nList[k]
    if n<3: n=3
    color = frequencyToRGB(frequencyList[k])
    rot+=0.05
    
    coords=[]
    for i in range(n):
        coords.append(350+r*math.cos((rot+2*math.pi*i)/n))
        coords.append(350+r*math.sin((rot+2*math.pi*i)/n))

    C.create_polygon(coords, fill="", width=3, outline=colorList[k%6], tag=f"{k}")
    if k>30: C.delete(f"{k-30}")
    
    m.update()
    t2 = time.time()
    delta_t = t2-t1
    #print(f"delta is {delta_t}")
    if k>0: time.sleep(animation_refresh_seconds-delta_t)
    else: time.sleep(animation_refresh_seconds)
    k+=1


m.mainloop()