# CA2 


import numpy as np
import matplotlib.pyplot as plt


#kB = 1
#T = 2
#B = 1/(kB*T)
B = 100                                 # For B around 10 it takes too long to settle

n = 10000                               # Number of iterations

x = 2                                   # Initial condition

hits = 0                                # Number of accepted x values

def H(x):                               # Hamiltonian
    return x**2

def Metro(H, H_prime, B):               # Metropolis algorithm
    DH = H_prime - H
    if np.exp(-B*DH) > 1:
        P_metro = 1
    else: 
        P_metro = np.exp(-B*DH)
    return P_metro

def Accept(P_metro):
    p = np.random.uniform(0,1)
    if P_metro > p:
        return True
    else:
        return False

    
accepted = np.array([])

while hits <= n:
    
    dx = np.random.uniform(-0.01,0.01)
    x_prime = x + dx
    
    P_metro = Metro(H(x),H(x_prime),B)
    
    if Accept(P_metro) == True:
        accepted = np.append(accepted, x)
        x = x_prime
        hits +=1
        
plt.plot(accepted)

#test to see if stuff ported over onedrive properly