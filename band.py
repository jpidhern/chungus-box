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
samplesLeft = data1.shape[0]
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
frameList = []
for i in range(0,framesTotal) :
    frameList.append(i)
    if frequencyList1[i] < 50:
        volumeList1[i] = 0
    if volumeList1[i] < 50000:
        qualityList1[i] = 0

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
frameList = []
for i in range(0,framesTotal) :
    frameList.append(i)
    if frequencyList2[i] < 50:
        volumeList2[i] = 0
    if volumeList2[i] < 50000:
        qualityList2[i] = 0

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
frameList = []
for i in range(0,framesTotal) :
    frameList.append(i)
    if frequencyList3[i] < 50:
        volumeList3[i] = 0
    if volumeList3[i] < 50000:
        qualityList3[i] = 0