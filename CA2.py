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
    DH = H_prime - H                    # Change in val of Hamiltonian = H(new x) - H(old x)
    if np.exp(-B*DH) > 1:               # If e^beta*delta H > 1 i.e. change should be accepted
        P_metro = 1                     # We set the value of the metropolis probability to be 1
    else:                               # If it is not fully accepted, we set the value of P_metro
        P_metro = np.exp(-B*DH)         # to be equal to e^beta*delta H > 1
    return P_metro

def Accept(P_metro):                    # Accept function
    p = np.random.uniform(0,1)          # random assigned probability 
    if P_metro > p:                     # If P_metro is larger than the random probability;
        return True                     # we accept the change by assigning a boolean i.e. the change is 'true'
    else:
        return False                    # If not, assign 'false'; the change is not accepted

    
accepted = np.array([])                 # Array of accepted changes, currently empty but will be appended to later

while hits <= n:                        # While the number of accepted changes is less than or   
                                        # equal to the number of desired iterations
    
    dx = np.random.uniform(-0.01,0.01)  # Generating the random change in x
    x_prime = x + dx
    
    P_metro = Metro(H(x),H(x_prime),B)
    
    if Accept(P_metro) == True:
        accepted = np.append(accepted, x_prime)
        x = x_prime
        hits +=1
        
plt.plot(accepted)