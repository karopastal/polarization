import matplotlib.pyplot as plt
from numpy import exp, loadtxt, pi, sqrt
from scipy import interpolate


font = {'family' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

from lmfit import Model
from lmfit.models import LinearModel

data = loadtxt('analysis/exp2_fernel.dat')

theta = data[:, 0]

r_sigma = data[:, 1]
r_sigma_err = data[:, 2]
r_sigma_calc = data[:, 3]

r_pi = data[:, 4]
r_pi_err = data[:, 5]
r_pi_calc = data[:, 6]

x = [theta[0], theta[1], theta[2]]
r_sigma_linear_data = [r_sigma[0], r_sigma[1], r_sigma[2]]
r_pi_linear_data = [r_pi[0], r_pi[1], r_pi[2]]

linear_r_sigma = interpolate.interp1d(x, r_sigma_linear_data, fill_value="extrapolate")
linear_r_pi = interpolate.interp1d(x, r_pi_linear_data, fill_value="extrapolate")

xnew = [0.0]
y0_sigma = linear_r_sigma(xnew)
y0_pi = linear_r_pi(xnew)

print(y0_sigma)
print(y0_pi)
print(((y0_sigma[0]+y0_pi[0])/2))

x.insert(0, xnew[0])

r_sigma_linear_data.insert(0, (y0_sigma[0]+y0_pi[0])/2)
r_pi_linear_data.insert(0, (y0_sigma[0]+y0_pi[0])/2)

fig, ax = plt.subplots()

ax.set_xlabel(r'theta [rad]', fontsize=18)
ax.set_ylabel(r'R', fontsize=18)
plt.title('R sigma & R pi Vs theta', fontsize=20)

plt.plot(x, r_sigma_linear_data, 'C3--x', label='R sigma')
plt.plot(x, r_pi_linear_data, 'C0--x', label='R pi')

plt.legend()
plt.show()
