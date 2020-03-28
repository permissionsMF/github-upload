# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def PMT(Pv, APR, nP, termYears):
    """   
    where   
        P = Monthly Payment
        Pv = Present Value (starting value of the loan)
        APR = Annual Percentage Rate
        R = Periodic Interest Rate = APR/number of interest periods per year
        n = Total number of interest periods (interest periods per year * number of years)   
    """
    R = APR / nP
    n = nP * termYears
    return (Pv * R) / (1 - (1 + R)**(-n))
    

#IPMT = pmt + (1+ir)^(n-1) *(pv * ir - pmt)

def IPMT(Pv, APR, nP, termYears, period):
    R = APR / nP
    functPMT = PMT(Pv, APR, nP, termYears)
    return functPMT + (1 + R)**(period - 1) * (Pv * R - functPMT)
 
    
    


Pv = 525000 / 1.1
APR = 1.89 / 100
nP = 12
termYears = 30

print('PMT is: {}'.format(PMT(Pv, APR, nP, termYears)))
print('IPMT is: {}'.format(IPMT(Pv, APR, nP, termYears)))

periodInputs= np.array([])
periodOutputs= np.array([])