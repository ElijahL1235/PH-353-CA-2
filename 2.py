# PH-353 CA-2


import numpy as np
import matplotlib.pyplot as plt


# We define a Hamiltonian 
# H(x) = x^2
# Beta = 1/(kB*T) = 1/(k*T)


# Thermalisation => allow system to settle to its equilibrium value;
# the first few guesses will not be close to equilibrium thus we discard


# Binning => because x_n+1 and x_n are correlated (the next guess is dependent
# on the previous one etc), the data is not independant and thus the error we find
# is not the 'true error'. So, we place the data into 'bins', ideally the width
# is the same as the 'correlation length' for the best results


# Reweighting => allows us to extrapolate for some B' near B




# Do some for loop stuff here to make it run itself properly



# Markov Chain WIP

#kB = 1
#T = 2
#B = 1/(kB*T)
B = 1

x = 2    #np.random.uniform(0,1)
x_test = np.random.uniform(-1,1)
x_prime = x + x_test

H = x**2

H_prime = x_prime**2

DH = H_prime - H

expo = np.exp(-B*DH)


# Metropolis Algorithm WIP

P_metro = 0

if expo > 1: # Energy decreases
    P_metro += 1
elif expo < 1: # Energy increases
    P_metro += expo
    x
    
