import numpy as np

fname = 'data/exp2.csv'
foutname = 'analysis/exp2_fernel.dat'

outfile = open(foutname, "w+")

outfile.write("# theta Rsigma Rsigma_err Rsigma_calc Rpi Rpi_err Rpi_calc theta_prime theta_prime_delta\n")

I_0 = 16.50
I_delta = 0.01
theta_delta = np.radians(1)


def I_normal(I):
    return I/I_0

def I_normal_delta(I):
    dI = (I_delta/I_0)
    dI_0 = (I_delta*I)/(I_0*I_0)

    formula = np.power(dI, 2) + np.power(dI_0, 2)

    return np.sqrt(formula)

def fernel_Rsigma(theta):
    sin_sub = (np.sin(theta - theta_prime(theta)))
    sin_add = (np.sin(theta + theta_prime(theta)))

    return np.power(sin_sub, 2)/np.power(sin_add, 2)

def fernel_Rpi(theta):
    tan_sub = (np.tan(theta - theta_prime(theta)))
    tan_add = (np.tan(theta + theta_prime(theta)))

    return np.power(tan_sub, 2)/np.power(tan_add, 2)

def theta_prime(theta):
    return np.arcsin(np.sin(theta)/1.5)

def theta_prime_delta(theta):
    dinom = 1 - np.power(((2/3)*(np.sin(theta))), 2)
    formula = ((2/3)*np.cos(theta)*theta_delta)/np.sqrt(dinom)

    return np.abs(formula)

with open(fname) as f:
    content = f.readlines()

for row in content:
    row_data = row.split(",")

    theta = np.radians(float(row_data[0]))
    r_sigma = float(row_data[1])
    r_pi = float(row_data[2])

    Rsigma_normal = I_normal(r_sigma)
    Rsigma_normal_delta = I_normal_delta(r_sigma)
    Rsigma_calc = fernel_Rsigma(theta) 

    Rpi_normal = I_normal(r_pi)
    Rpi_normal_delta = I_normal_delta(r_pi)
    Rpi_calc = fernel_Rpi(theta)

    theta_p = theta_prime(theta)
    theta_p_delta = theta_prime_delta(theta)

    str1 = str(theta) + " " + str(Rsigma_normal) + " " + str(Rsigma_normal_delta) + " " + str(Rsigma_calc) + " "
    str2 = str(Rpi_normal) + " " + str(Rpi_normal_delta) + " " + str(Rpi_calc) + " " + str(theta_p) + " " + str(theta_p_delta) + "\n"

    outfile.write(str1 + str2)

outfile.close()