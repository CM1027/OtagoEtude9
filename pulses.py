import matplotlib.pyplot as plt
import sys
import numpy as np
import scipy.signal
import math
from scipy.signal.signaltools import wiener
from scipy.signal import savgol_filter
from scipy.signal import butter







y = []
f_name = sys.argv[1]
f = open(f_name)
line_count = 0
data = f.readlines()
for line in data:
    y.append(int(line))
    if line:
        line_count += 1
f.close()

print(len(y))
print(y)

order = 2
sampling_freq = 10
cutoff_freq = 2
normalized_cutoff_freq = 2 * cutoff_freq / sampling_freq
numerator_coeffs, denominator_coeffs = scipy.signal.butter(order, normalized_cutoff_freq)
filtered_signal = scipy.signal.filtfilt(numerator_coeffs, denominator_coeffs, y)


print('Detect peaks with order (distance) filter.')
indexes = scipy.signal.argrelextrema(
    np.array(filtered_signal),
    comparator=np.greater,order=2
)



print('Peaks are: %s' % (indexes[0]))
print(len(indexes[0]))

plt.plot(y, label="original")
plt.plot(filtered_signal, label="filtered")
plt.legend()
plt.show()

