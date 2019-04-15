import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

font = {'family' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp5_scattering.dat')

cos_sqr = data[:, 4]
cos_sqr_delta = data[:, 5]
I_n = data[:, 2]
I_n_delta = data[:, 3]

weights_I_n = (1/I_n_delta)

print(weights_I_n)

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result = linear_model.fit(I_n, weights=weights_I_n, x=cos_sqr, a=1, b=1)

a = result.params['a'].value
b = result.params['b'].value

print(result.fit_report())
print(result.chisqr)

fig, ax = plt.subplots()

ax.set_xlabel(r'cos^2(theta)', fontsize=18)
ax.set_ylabel(r'I normal', fontsize=18)
plt.title('I normal vs cos^2(theta)', fontsize=20)

ax.errorbar(cos_sqr, I_n, xerr=cos_sqr_delta, fmt='C2o')
ax.errorbar(cos_sqr, I_n, yerr=I_n_delta, fmt='C3o')

plt.plot(cos_sqr, a*cos_sqr + b, 'C0--', label='y(x) = a*cos^2(theta) + b')

plt.legend()
plt.show()