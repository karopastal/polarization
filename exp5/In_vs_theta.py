import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

font = {'family' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp5_scattering.dat')

theta = data[:, 0]
cos_sqr_delta = data[:, 5]
I_n = data[:, 2]
I_n_delta = data[:, 3]

weights_I_n = (1/I_n_delta)

print(weights_I_n)

def cos_sqr(x, a, b):
    return a*np.power(np.cos(x), 2) + b

cos_sqr_model = Model(cos_sqr)
result = cos_sqr_model.fit(I_n, weights=weights_I_n, x=theta, a=1, b=1)

a = result.params['a'].value
b = result.params['b'].value

a_err = result.params['a'].stderr
b_err = result.params['b'].stderr

print(result.fit_report())
print(result.chisqr)

fig, ax = plt.subplots()

ax.set_xlabel(r'theta [rad]', fontsize=18)
ax.set_ylabel(r'I normal', fontsize=18)
plt.title('I normal vs theta', fontsize=20)

plt.plot(theta, cos_sqr(theta, a + a_err, b+b_err), 'C4--', label='upper limit')
plt.plot(theta, cos_sqr(theta, a, b), 'C0-o', label='y(x) = a*cos^2(theta) + b')
plt.plot(theta, cos_sqr(theta,a - a_err, b-b_err), 'C6--', label='lower limit')


plt.legend()
plt.show()