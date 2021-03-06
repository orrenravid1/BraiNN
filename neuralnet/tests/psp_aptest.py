import math
import numpy as np
import matplotlib.pyplot as plt
import random

N = 20
incount = 30
threshold = .5
potential = 1
t_max = 2
t = np.linspace(0.0,t_max,num = N)
precision = .97

ins = np.array([[random.randrange(0,9)/10 for i in range(N)]
                for j in range(incount)])

def psp(ins):
    s = sum(ins)
    psp = 1/math.exp(-s)

def ap(t):
    beta = math.log(1-precision)/t_max
    return potential*math.exp(beta*t)

psps = psp(ins)
ap

for i in range(N):
    s = 0
    for j in range(incount):
        s += ins[j][i]
    f[i] = (f[i] + s/(incount))/(potential + 1)
    
plt.plot(t,f)

plt.ylim([0,potential])

plt.show()
