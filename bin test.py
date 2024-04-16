#bin test

import numpy as np
from CA2.py import Metro, Accept, H

B = 100                                
n = 10000
x = 2 
hits = 0  
n_per_bin = 18

accepted = np.array([])  
accepted = accepted[1000:]

bins = np.zeros(9000)                  #9000 is the length of accepted after trimming
for a in range(9000):
    in_the_bin = 0
    for b in range(n_per_bin):
        dx = np.random.uniform(-0.01, 0.01)
        