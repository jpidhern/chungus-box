import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, rfft, fftfreq, rfftfreq
from scipy.io import wavfile # get the api

DURATION = 1/30  # Seconds
SAMPLE_RATE, data = wavfile.read("/Users/henrysiegel/Downloads/C.wav")
N = int(DURATION * SAMPLE_RATE)

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


print("data", data)
print("data.T", data.T)

sound_array = data.T[0] # this is a two channel soundtrack, I get the first track
normalized_array = np.int16((sound_array / sound_array.max()) * 32767)
yf = rfft(normalized_array) # calculate fourier transform (complex numbers list)
xf = fftfreq(N, 1 / SAMPLE_RATE)
plt.plot(xf, np.abs(yf)) 
plt.show()

# https://realpython.com/python-scipy-fft/
# https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
