import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy import exp, loadtxt, pi, sqrt

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

fig, ax = plt.subplots()

ax.set_xlabel(r'theta [rad]', fontsize=18)
ax.set_ylabel(r'R', fontsize=18)
plt.title('R sigma & R pi Vs theta', fontsize=20)

r_sigma_patch = mpatches.Patch(color='C3', label='R sigma')
r_sigma_calc_patch = mpatches.Patch(color='C1', label='R sigma claculated')
r_pi_patch = mpatches.Patch(color='C0', label='R pi')
r_pi_calc_patch = mpatches.Patch(color='C4', label='R pi calculated')

plt.legend(handles=[r_sigma_patch, r_sigma_calc_patch, r_pi_patch, r_pi_calc_patch])


plt.plot(theta, r_sigma, 'C3-o')
ax.errorbar(theta, r_sigma, yerr=r_sigma_err, fmt='C3', capthick=2)

plt.plot(theta, r_pi, 'C0-o')
ax.errorbar(theta, r_pi, yerr=r_pi_err, fmt='C0', capthick=2)

plt.plot(theta, r_sigma_calc, 'C1--o')
plt.plot(theta, r_pi_calc, 'C4--o')

plt.show()