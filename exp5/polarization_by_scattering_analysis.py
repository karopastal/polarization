import numpy as np

fname = 'data/exp5.csv'
foutname = 'analysis/exp5_scattering.dat'

outfile = open(foutname, "w+")

outfile.write("# theta I I_n I_n_delta cos_sqr cos_sqr_delta \n")

I_0 = 29.3
I_delta = 0.1
theta_delta = np.radians(5)

def I_normal_delta(I):
    dI = (I_delta/I_0)
    dI_0 = (I_delta*I)/(I_0*I_0)

    formula = np.power(dI, 2) + np.power(dI_0, 2)

    return np.sqrt(formula)

def cos_sqr(theta):
    return np.power(np.cos(theta), 2)

def cos_sqr_delta(theta):
    return np.abs(np.sin(2*theta)*theta_delta)

with open(fname) as f:
    content = f.readlines()

for row in content:
    row_data = row.split(",")

    theta = np.radians(float(row_data[0]))
    I = float(row_data[1])

    I_n = I/I_0
    I_n_delta = I_normal_delta(I) 
    cossqr = cos_sqr(theta)
    cossqr_delta = cos_sqr_delta(theta)

    str1 = str(theta) + " " + str(I) + " " + str(I_n) + " " + str(I_n_delta) + " "
    str2 = str(cossqr) + " " + str(cossqr_delta) + "\n"

    outfile.write(str1 + str2)

outfile.close()