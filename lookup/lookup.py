import numpy as np
import scipy as sp
import math

import math

def generate_sine_lookup(samples=256, amplitude=1.0):
    table = []
    for i in range(samples):
        angle = 2 * math.pi * (i / samples)
        value = amplitude * math.sin(angle)
        table.append(value)
    return table

# Example usage:
lookup = generate_sine_lookup(16, 1.0)
for i, v in enumerate(lookup):
    print(f"{i}: {v:.4f}")
