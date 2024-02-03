import scipy
import numpy
import sys
from scipy.io import wavfile

# samplerate, data = wavfile.read("C:\\Users\\jackj\\Downloads\\[FULL VER.] TELECASTER B BOY Wonderlands×Showtime COVER [COLOR CODED LYRICS] KANROMENG.wav")
# print(samplerate)
# print(data.size)
samplerate, data = wavfile.read("C:\\Users\\jackj\\Downloads\\Cute Bell Sound Effect.wav")
print(samplerate)
print(data.shape[0])
import sys
import numpy
n = 0
samplerate, data = wavfile.read("C:\\Users\\jackj\\Downloads\\Cute Bell Sound Effect.wav")
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(data.shape[0])
import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()