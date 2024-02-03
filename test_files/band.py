import numpy as np
import math
from scipy.io import wavfile
#GOALS:
#GENERATE A LIST OF FREQUENCY, VOLUME FOR EVERY FRAME
def roots(lst):
    rootNo = 0
    for i in range(0,len(lst)):
        if abs(lst[i]) < 75 : #low amplitude..?
            rootNo=rootNo+1
    return rootNo

def turningPoints(lst):
    dx = np.diff(lst)
    return dx[1:] * dx[:-1] < 0
def turningPointsSum(lst):
    dx = np.diff(lst)
    return np.sum(dx[1:] * dx[:-1] < 0)

samplerate1, data1 = wavfile.read("D:\\tartnhack\\vocals.wav")
samplerate2, data2 = wavfile.read("D:\\tartnhack\\piano.wav")
samplerate3, data3 = wavfile.read("D:\\tartnhack\\guitar.wav")
length = data1.shape[0] / samplerate1
print(f"length = {length}s")
fps = 30
timePerFrame = 1/fps
samplesPerFrame = samplerate1//fps
framesTotal = math.floor(fps*length) #imprecise?
currentFrame = 0
# cLight = 299,792,458
#while we are still in a whole frame, do this
volumeList1 = []
frequencyList1 = []
nList1 = []
qualityList1 = []
turningPointReady = True
while currentFrame != framesTotal : 
    currentVolume = 0
    sampleList1d1 = []
    # sampleList1dR = []
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        sampleList1d1.append(data1[i][0])
    for i in range(0,samplesPerFrame):
        currentVolume = currentVolume + np.abs(sampleList1d1[i])  #mono
    
    #print(sampleList1d)
    # turningPtsPerFrameL = turningPoints(sampleList1dL)
    # turningPtsPerFrameR = turningPoints(sampleList1dR)
    # turningPtsPerFrame = (turningPtsPerFrameL+turningPtsPerFrameR)//2
    #print("This?")
    currentQuality = turningPointsSum(sampleList1d1)
    # currentQuality = (qualityR + qualityL)//2
    turningPtsPerFrameList = turningPoints(sampleList1d1)
    # turningPtsPerFrameR = turningPoints(sampleList1dR)
    turningPtsPerFrame = 0
    maxPts = 0

    
    for i in range(0,samplesPerFrame-2): #this is okay because there are a lot of samples
        if turningPtsPerFrameList[i] and sampleList1d1[i] > 3000 and turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
        if turningPtsPerFrameList[i] and sampleList1d1[i] < 3000 and not turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
    turningPtsPerFrame = turningPtsPerFrame//2
    nList1.append(turningPtsPerFrame)
    if (turningPtsPerFrame >= 1) :
        period = timePerFrame/(turningPtsPerFrame)
        frequencyList1.append(1//period)
    else :
        frequencyList1.append(0)
    volumeList1.append(currentVolume)
    qualityList1.append(currentQuality)
    currentFrame=currentFrame+1
for i in range(0,framesTotal) :
    if frequencyList1[i] < 50:
        volumeList1[i] = 0
    if volumeList1[i] < 50000:
        qualityList1[i] = 0
#print(len(sampleList1d1))
currentFrame = 0
volumeList2 = []
frequencyList2 = []
nList2 = []
qualityList2 = []
turningPointReady = True
while currentFrame != framesTotal : 
    currentVolume = 0
    sampleList1d2 = []
    
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        sampleList1d2.append(data2[i][0])
    for i in range(0,samplesPerFrame):
        currentVolume = currentVolume + np.abs(sampleList1d2[i])  #mono
    #print(len(sampleList1d2))
    currentQuality = turningPointsSum(sampleList1d2)
    turningPtsPerFrameList = turningPoints(sampleList1d2)
    turningPtsPerFrame = 0
    maxPts = 0

    
    for i in range(0,samplesPerFrame-2): #this is okay because there are a lot of samples
        if turningPtsPerFrameList[i] and sampleList1d2[i] > 3000 and turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
        if turningPtsPerFrameList[i] and sampleList1d2[i] < 3000 and not turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
    turningPtsPerFrame = turningPtsPerFrame//2
    nList2.append(turningPtsPerFrame)
    if (turningPtsPerFrame >= 1) :
        period = timePerFrame/(turningPtsPerFrame)
        frequencyList2.append(1//period)
    else :
        frequencyList2.append(0)
    volumeList2.append(currentVolume)
    qualityList2.append(currentQuality)
    currentFrame=currentFrame+1
for i in range(0,framesTotal) :
    #print(len(frequencyList2))
    if frequencyList2[i] < 50:
        volumeList2[i] = 0
    if volumeList2[i] < 50000:
        qualityList2[i] = 0
currentFrame = 0
volumeList3 = []
frequencyList3 = []
nList3 = []
qualityList3 = []
turningPointReady = True
while currentFrame != framesTotal : 
    currentVolume = 0
    sampleList1d3 = []
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        sampleList1d3.append(data2[i][0])
    for i in range(0,samplesPerFrame):
        currentVolume = currentVolume + np.abs(sampleList1d3[i])  #mono
    currentQuality = turningPointsSum(sampleList1d3)
    turningPtsPerFrameList = turningPoints(sampleList1d3)
    turningPtsPerFrame = 0
    maxPts = 0

    
    for i in range(0,samplesPerFrame-2): #this is okay because there are a lot of samples
        if turningPtsPerFrameList[i] and sampleList1d3[i] > 3000 and turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
        if turningPtsPerFrameList[i] and sampleList1d3[i] < 3000 and not turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
    turningPtsPerFrame = turningPtsPerFrame//2
    nList3.append(turningPtsPerFrame)
    if (turningPtsPerFrame >= 1) :
        period = timePerFrame/(turningPtsPerFrame)
        frequencyList3.append(1//period)
    else :
        frequencyList3.append(0)
    volumeList3.append(currentVolume)
    qualityList3.append(currentQuality)
    currentFrame=currentFrame+1
for i in range(0,framesTotal) :
    if frequencyList3[i] < 50:
        volumeList3[i] = 0
    if volumeList3[i] < 50000:
        qualityList3[i] = 0
#print(len(sampleList1d3))
        
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
    return '#' + intToHex(int(r)) + intToHex(int(g)) + intToHex(int(b))

def volumeToRadius(n):
    n=int(n)
    if n < 2*10**6:
        return 50
    elif n > 7*10**6:
        return 300
    else:
        return 50 + 50*(n-2*10**6)*10**-6

def volumeToRadius2(n):
    n=int(n)
    if n < 2*10**6:
        return 25
    elif n > 7*10**6:
        return 200
    else:
        return 20 + 35*(n-2*10**6)*10**-6

# delay between successive frames in seconds
animation_refresh_seconds = 1/30

m = tk.Tk()
m.geometry("700x700")
m.title("Sound to Art Converter")
C = tk.Canvas(m,width=700,height=700,background="black")
C.pack()

#starting number of points
n1=3
n2=3
n3=3
#starting radius in pixels
r1=50
r2=50
r3=50
#starting rotation factor
rot1=0
rot2=0
rot3=0

num_frames = len(volumeList1)
max_vol = max(volumeList1)
min_vol = min(volumeList1)
#print(f"max vol is: {max_vol}")
k=0
colorList=["red","orange","yellow","green","blue","white"]
while k<num_frames:
    t1=time.time()
    r1=volumeToRadius(volumeList1[k])
    n1=nList1[k]
    if n1<3: n1=3
    color1 = frequencyToRGB(frequencyList1[k])
    rot1+=0.05
    if n1<3:n1=3

    r2=volumeToRadius2(volumeList2[k])
    n2=nList2[k]
    if n2<3: n2=3
    color2 = frequencyToRGB(frequencyList2[k])
    rot2+=0.05
    if n2<3:n2=3

    r3=volumeToRadius2(volumeList3[k])
    n3=nList3[k]
    if n3<3: n3=3
    color3 = frequencyToRGB(frequencyList3[k])
    rot3+=0.05
    if n3<3:n3=3

    coords1=[]
    coords2=[]
    coords3=[]
    for i in range(n1):
        coords1.append(350+r1*math.cos((rot1+2*math.pi*i)/n1))
        coords1.append(400+r1*math.sin((rot1+2*math.pi*i)/n1))
    for i in range(n2):
        coords2.append(200+r2*math.cos((rot2+2*math.pi*i)/n2))
        coords2.append(200+r2*math.sin((rot2+2*math.pi*i)/n2))
    for i in range(n3):
        coords3.append(200+r3*math.cos((rot3+2*math.pi*i)/n3))
        coords3.append(500+r3*math.sin((rot3+2*math.pi*i)/n3))

    C.create_polygon(coords1, fill="", width=3, outline=colorList[k%6], tag=f"{k}1")
    C.create_polygon(coords2, fill="", width=3, outline=colorList[k%6], tag=f"{k}2")
    C.create_polygon(coords3, fill="", width=3, outline=colorList[k%6], tag=f"{k}3")
    if k>30: 
        C.delete(f"{k-30}1")
        C.delete(f"{k-30}2")
        C.delete(f"{k-30}3")
        
    m.update()
    t2 = time.time()
    delta_t = t2-t1
    print(f"delta is {delta_t}")
    if k>0:
        if animation_refresh_seconds-delta_t > 0:
            time.sleep(animation_refresh_seconds-delta_t)
    else:
        filename = "/Users/henrysiegel/Downloads/piano.wav"
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
    k+=1


m.mainloop()