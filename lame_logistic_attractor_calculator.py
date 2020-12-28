# Lame attractor cycle points calculator for the logistic map.
# I iterate recursively the logistic map with a rate r and any
# number x in (0,1) and save the whole orbit in a list with rounded
# precision. After that, I just take the unique values that appeared
# more than 1 time in the list for that r. 
# The remaining set with unique values is the atractor up to 10 digits 
# of precision for the rate r.
# Yes, lame but works, then the classical graph is: x=r and y={attractor points}.

# Wanna see the output? (need gnuplot)
# python lame_logistic_attractor_calculator.py  | gnuplot -p -e "plot '<cat' w points;pause 300"
#
# Eduardo Ruiz Duarte
# toorandom@gmail.com
import numpy as np
import sys

def logistic(x,r):
    xf = r*x*(1-x)
    return xf


def lconvergence(r):
    x = list()
    fixedpts = list()
    x.append(logistic(np.double(0.9),r))
    d = np.double(1)
    n = 0
    while n <800:
       x.append(round(logistic(x[n],r),10))
       n = n+1
    uniq = {i:x.count(i) for i in x}
    for k in uniq:
        if uniq[k]>1:
            fixedpts.append(k)
    return list(set(fixedpts))

for r in np.arange(0.5,3.9,0.01):
    for f in lconvergence(r):
         print(str(r)+" "+str(f))
