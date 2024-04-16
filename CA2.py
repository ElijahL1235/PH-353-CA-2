# CA2 


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic as gravy

#kB = 1
#T = 2
#B = 1/(kB*T)

B = 100                                 # NB for B around 10 it takes too long to thermalise

n = 10000                               # Number of iterations

accepted = np.array([])                 # Array of accepted changes, currently empty but will be appended to later

x = 10                                   # Initial condition

hits = 0                                # Number of accepted x values


# for reweighting, consider removing the first 1000 results 
# then for the gaussian system bit, we take the mean of the remaining n-1000 points
# due to autocorrelation, we should bin the remaining 9000 points first
# before we average. let's try bin size of 18 as that yields 500 bins from 9000 points

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


while hits <= n:                        # While the number of accepted changes is less than or   
                                        # equal to the number of desired iterations
    dx = np.random.uniform(-0.1,0.1)    # Generating the random change in x
    x_prime = x + dx                    # New x = starting x + change in x
    
    P_metro = Metro(H(x),H(x_prime),B)  # Metro probability given by metro function passing H(old x), H(new x), beta    
    if Accept(P_metro) == True:         # If the accept function gives out 'true' for the metro probability, we accept...
        accepted = np.append(accepted, H(x_prime))
        x = x_prime                     # The new x into the list of accepted changes, and we set the x' to be the...
        hits +=1                        # starting x for the next iteration. We also 'count' the change by adding 1 to 'hits'
        
plt.plot(accepted)                      # Plot the accepted x's 

accepted = accepted[1001:]

no_bins = 500
length = len(accepted)
bin_size = length//no_bins
bin_analysis = []

# Try using the scipy.stats.binned_statistic function for binning?

for i in range(no_bins):
    Bin = np.zeros(bin_size)
    Bin = accepted[i*(bin_size) : i*(bin_size) + bin_size - 1]
    bin_mean = np.mean(Bin)
    bin_std = np.std(Bin)
    bin_analysis.append([bin_mean, bin_std])
    
print(Bin)
print(bin_analysis)

plt.figure()
plt.plot(accepted)
plt.plot()
plt.grid()
plt.title('Thermalised data set')


