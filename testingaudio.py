import scipy
import numpy
import sys
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
# samplerate, data = wavfile.read("C:\\Users\\jackj\\Downloads\\Cute Bell Sound Effect.wav")
# print(samplerate)
# print(data.shape[0])
# n = 0
samplerate, data = wavfile.read("C:\\Users\\jackj\\OneDrive\\Documents\\sound files\\C.wav")
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
qualityList = []
turningPointReady = True
print(samplesPerFrame)
while currentFrame != framesTotal : 
    currentVolume = 0
    sampleList1dL = []
    sampleList1dR = []
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        currentVolume = currentVolume + np.abs(data[i][0]) + np.abs(data[i][1]) #both channels of stereo
    for i in range(samplesPerFrame*currentFrame,samplesPerFrame*(currentFrame+1)):
        sampleList1dL.append(data[i][0])
        sampleList1dR.append(data[i][1])
    # turningPtsPerFrameL = turningPoints(sampleList1dL)
    # turningPtsPerFrameR = turningPoints(sampleList1dR)
    # turningPtsPerFrame = (turningPtsPerFrameL+turningPtsPerFrameR)//2
    #print("This?")
    qualityL = turningPointsSum(sampleList1dL)
    qualityR = turningPointsSum(sampleList1dL)
    currentQuality = (qualityR + qualityL)//2
    turningPtsPerFrameL = turningPoints(sampleList1dL)
    turningPtsPerFrameR = turningPoints(sampleList1dR)
    turningPtsPerFrame = 0
    
    for i in range(0,samplesPerFrame-2): #this is okay because there are a lot of samples
        if turningPtsPerFrameL[i] and sampleList1dL[i] > 3000 and turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
        if turningPtsPerFrameR[i] and sampleList1dR[i] < 3000 and not turningPointReady :
            turningPtsPerFrame = turningPtsPerFrame + 1
            turningPointReady = not turningPointReady
    turningPtsPerFrame = turningPtsPerFrame//4
    if (turningPtsPerFrame > 2) :
        period = timePerFrame/(turningPtsPerFrame)
        #print(str(lambdaValue) + " lambda")
        frequencyList.append(1//period)
        #print(str(1/lambdaValue) + " frequency")
    else :
        frequencyList.append(0)
    volumeList.append(currentVolume)
    qualityList.append(currentQuality)
    currentFrame=currentFrame+1
for i in range(0,framesTotal) :
    if volumeList[i] < 50000:
        qualityList[i] = 0
print(volumeList)
print(frequencyList)
print(qualityList)