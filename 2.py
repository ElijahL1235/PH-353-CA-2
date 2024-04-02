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

n = 100 #number of iterations

x = 20    #np.random.uniform(0,1)

dx = np.random.uniform(-0.1,0.1)
x_prime = x + dx

def H(x):
    return x**2


# Metropolis Algorithm WIP


accept =  np.array([])


def Metro(H, H_prime, B):
    DH = H_prime - H
    if np.exp(-B*DH) > 1:
        P_metro = 1
    else: 
        P_metro = np.exp(-B*DH)
    return P_metro

hits = 0

def accept(P_metro):
    p = np.random.uniform(0,1)
    #if P_metro > p:
        #accept.append(x_prime)
        #append stuff
        #volumes = np.append(volumes, val) is the structure 
#    else:
        #do not append stuff
        
    
a = Metro(H(x),H(x_prime),B)
print(a)



#if expo > 1: # Energy decreases
#    P_metro += 1
#elif expo < 1: # Energy increases
#    P_metro += expo
    

# Iteration loop WIP

#while hits <= n:
    #do markov chain
    
    
# Boolean accept WIP

def Accept(P_metro):
    p = np.random.uniform(0,1)
    if P_metro > p:
        return True
    else:
        return False
    
#while iteration condition
#   if accept(P_metro) = True
#       accept.append(x)
#       x = x_prime
#       hits +=1
#       
#   
    

    
    