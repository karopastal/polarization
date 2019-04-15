import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, loadtxt, pi, sqrt, array
from lmfit import Model
from lmfit.models import LinearModel

font = {'family' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

data = loadtxt('analysis/exp2_fernel.dat')

theta = data[:, 0]

r_sigma = data[:, 1]
r_sigma_err = data[:, 2]
r_sigma_calc = data[:, 3]

r_pi = data[:, 4]
r_pi_err = data[:, 5]
r_pi_calc = data[:, 6]

r_sigma = data[:, 1]
r_sigma_err = data[:, 2]
r_sigma_calc = data[:, 3]

r_pi = data[:, 4]
r_pi_err = data[:, 5]
r_pi_calc = data[:, 6]

theta_linear = theta[:3]
r_sigma_linear_data = r_sigma[:3]
r_pi_linear_data = r_pi[:3]

weights_r_sigma = (1/r_sigma_err[:3])
weights_r_pi = (1/r_pi_err[:3])

print(weights_r_sigma, weights_r_pi)

def linear(x, a, b):
    return (a*x + b)

linear_model = Model(linear)
result_sigma = linear_model.fit(r_sigma_linear_data, weights=weights_r_sigma, x=theta_linear, a=0.04, b=0.04)
result_pi = linear_model.fit(r_pi_linear_data, weights=weights_r_pi, x=theta_linear, a=0.04, b=0.04)

print(result_sigma.fit_report())
print(result_sigma.chisqr)

print(result_pi.fit_report())
print(result_pi.chisqr)


fig, ax = plt.subplots()

ax.set_xlabel(r'theta [rad]', fontsize=18)
ax.set_ylabel(r'R', fontsize=18)
plt.title('R sigma & R pi Vs theta', fontsize=20)

plt.plot(theta_linear, r_sigma_linear_data, 'C3-x', label='R sigma')
plt.plot(theta_linear, r_pi_linear_data, 'C0-x', label='R pi')

theta_extrap = np.insert(theta_linear, 0, 0)

print(theta_extrap)

a_sigma = result_sigma.params['a']
b_sigma = result_sigma.params['b']
plt.plot(theta_extrap, a_sigma*theta_extrap + b_sigma, 'C3--x', label='R sigma: y(x) = a*x + b')

a_pi = result_pi.params['a']
b_pi = result_pi.params['b']
plt.plot(theta_extrap, a_pi*theta_extrap + b_pi, 'C0--x', label='R pi: y(x) = a*x + b')

plt.legend()
plt.show()