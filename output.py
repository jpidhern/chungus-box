import numpy as np
import math
from scipy.io import wavfile
import simpleaudio as sa
from threading import Thread

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
# samplerate, data = wavfile.read("C:\\Users\\jackj\\Downloads\\Cute Bell Sound Effect.wav")
# print(samplerate)
# print(data.shape[0])
# n = 0
#samplerate, data = wavfile.read("C:\\Users\\jackj\\OneDrive\\Documents\\sound files\\C.wav")
samplerate, data = wavfile.read("/Users/henrysiegel/Downloads/piano.wav")
#samplerate, data = wavfile.read("D:\\tartnhack\\testingnowork.wav")
#samplerate, data = wavfile.read("D:\\tartnhack\\c scale.wav")

#samplerate, data = wavfile.read("D:\\tartnhack\\track.wav")
#samplerate, data = wavfile.read("D:\\tartnhack\\Major Scale.wav")
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(data.shape[0])
fps = 30
timePerFrame = 1/fps
samplesLeft = data.shape[0]
samplesPerFrame = samplerate//fps
framesTotal = math.floor(fps*length) #imprecise?
currentFrame = 0
# cLight = 299,792,458
#while we are still in a whole frame, do this
volumeList = []
frequencyList = []
nList = []
qualityList = []
maxPtsList = []
turningPointReady = True
print(samplesPerFrame)
while currentFrame != framesTotal : 
    currentVolume = 0
    sampleList1d = []
    # sampleList1dR = []
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        sampleList1d.append(data[i][0])
    for i in range(0,samplesPerFrame):
        currentVolume = currentVolume + np.abs(sampleList1d[i])  #mono
    
    #print(sampleList1d)
    # turningPtsPerFrameL = turningPoints(sampleList1dL)
    # turningPtsPerFrameR = turningPoints(sampleList1dR)
    # turningPtsPerFrame = (turningPtsPerFrameL+turningPtsPerFrameR)//2
    #print("This?")
    currentQuality = turningPointsSum(sampleList1d)
    # currentQuality = (qualityR + qualityL)//2
    turningPtsPerFrameList = turningPoints(sampleList1d)
    # turningPtsPerFrameR = turningPoints(sampleList1dR)
    turningPtsPerFrame = 0
    maxPts = 0

    
    for i in range(0,samplesPerFrame-2): #this is okay because there are a lot of samples
        if turningPtsPerFrameList[i] and sampleList1d[i] > 3000 and turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
            if sampleList1d[i] > 10000: #what is a "high" volume?
                maxPts = maxPts + 1
        if turningPtsPerFrameList[i] and sampleList1d[i] < 3000 and not turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
    turningPtsPerFrame = turningPtsPerFrame//2
    nList.append(turningPtsPerFrame)
    if (turningPtsPerFrame >= 1) :
        period = timePerFrame/(turningPtsPerFrame)
        frequencyList.append(1//period)
    else :
        frequencyList.append(0)
    if (maxPts > 5) :
        maxPtsList.append(True)
    else :
        maxPtsList.append(False)
    volumeList.append(currentVolume)
    qualityList.append(currentQuality)
    currentFrame=currentFrame+1
frameList = []
for i in range(0,framesTotal) :
    frameList.append(i)
    if frequencyList[i] < 50:
        volumeList[i] = 0
    if volumeList[i] < 50000:
        qualityList[i] = 0


# import matplotlib.pyplot as plt
# import numpy as np
# plt.plot(frameList, frequencyList, label="Left channel")
# plt.legend()
# plt.xlabel("frame")
# plt.ylabel("frq")
# plt.show()

import tkinter as tk
import time
import math

def frequencyToRGB(frequency):
   if (frequency > 2000):
      return (0,0,255)
   elif (frequency < 1000):
      return (255-(frequency/1000 * 255), (frequency/1000 * 255), 0)
   else: 
      return (0, 255-((frequency-1000)/1000 * 255),  ((frequency-1000)/1000 * 255))

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
print(volumeList)
while k<num_frames:
    t1=time.time()
    r=(volumeList[k]//100000) +200
    print(f"r is {r}")
    n=nList[k]
    #color = freq_to_color(frequencyList[k])
    rot+=0.05
    if n<3:n=3

    coords=[]
    for i in range(n):
        coords.append(350+r*math.cos((rot+2*math.pi*i)/n))
        coords.append(350+r*math.sin((rot+2*math.pi*i)/n))

    C.create_polygon(coords, fill="", width=3, outline=colorList[k%6], tag=f"{k}")
    if k>30: C.delete(f"{k-30}")
        
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