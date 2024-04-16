# CA2 


import numpy as np
import matplotlib.pyplot as plt


#kB = 1
#T = 2
#B = 1/(kB*T)
B = 100                                 # NB for B around 10 it takes too long to thermalise

n = 10000                               # Number of iterations

# for reweighting, consider removing the first 1000 results 
# then for the gaussian system bit, we take the mean of the remaining n-1000 points
# due to autocorrelation, we should bin the remaining 9000 points first
# before we average. let's try bin size of 18 as that yields 500 bins from 9000 points

x = 10                                  # Initial condition

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
    
    dx = np.random.uniform(-1,1)  # Generating the random change in x
    x_prime = x + dx                    # New x = starting x + change in x
    
    P_metro = Metro(H(x),H(x_prime),B)  # metro probability given by metro function passing H(old x), H(new x), beta
    
    if Accept(P_metro) == True:         # If the accept function gives out 'true' for the metro probability, we accept...
        accepted = np.append(accepted, x_prime**2)
        x = x_prime                     # the new x into the list of accepted changes, and we set the x' to be the...
        hits +=1                        # starting x for the next iteration. We also 'count' the change by adding 1 to 'hits'
        
plt.plot(accepted)                      # plot the accepted x's 


# Removing the first 1000 values:

accepted = accepted[1000:]

plt.figure()
plt.plot(accepted)
plt.grid()
plt.title('Thermalised data set')


# BINNING

n_per_bin = 18

bins = np.zeros(9000)                  #9000 is the length of accepted after trimming
for a in range(9000):
    in_the_bin = 0
    for b in range(n_per_bin):
        dx = np.random.uniform(-0.01, 0.01)
        
    