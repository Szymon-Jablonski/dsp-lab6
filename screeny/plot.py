import matplotlib.pyplot as plt
import re
import numpy as np

def parse_fft_file(filename):
    values = []
    pattern = re.compile(r'float32_t\s+([+-]?\d+(?:\.\d+)?)')

    with open(filename, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                values.append(float(match.group(1)))

    return np.array(values, dtype=float)


fs = 50000
n = 1024

values = parse_fft_file('./1khz-bezdc.txt')

#t = [i/n * 1000 / 0.08 for i in range(len(values))] # experimental values when I already knew the frequency of the signal, idk how do I get this

f = np.arange(len(values)) *  fs / n

plt.figure(figsize=(10,4))
plt.plot(f, values)
plt.xlabel("f")
plt.ylabel("Magnitude")
plt.title("Signal FFT")
plt.grid(True)
plt.show()
