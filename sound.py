import matplotlib.pyplot as plt
from scipy.fft import fft, rfft, fftfreq
from scipy.io import wavfile # get the api

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds
_, data = wavfile.read('/Users/emilianozetune/Downloads/cfbc.wav')


RGB = (255,255,255)

def frequencyToRGB(frequency):
    # min: 0
    # max: 2000

    if (frequency > 2000):
        return (0,0,255)
    elif (frequency < 1000):
        return (255-(frequency/1000 * 255), (frequency/1000 * 255), 0)
    else: 
        return (0, 255-((frequency-1000)/1000 * 255),  ((frequency-1000)/1000 * 255))