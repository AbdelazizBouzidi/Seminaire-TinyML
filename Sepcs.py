# %%
from scipy.io import wavfile
from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

samplerate, data = wavfile.read('017c4098_nohash_2.wav')
# %%
data.size
# %%
slices = []
# window = signal.hann(480)
for i in range(41):
    slices.append(np.hanning(480)*data[i*480 - i*92:(i+1)*480 - i*92])
    # print(str(i*480 - i*92) + "-" +str((i+1)*480 - i*92))
# %%

# %%
frequencies = [np.abs(fft(x)) for x in slices]
# %%
plt.plot(np.abs(frequencies[30][0:256]))
# %%
plt.plot(slices[0])
# %%
