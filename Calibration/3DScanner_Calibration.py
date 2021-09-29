import matplotlib.pyplot as plt
import numpy as np;
import scipy.optimize as opt;



calibration_dist = np.array([20,30,40,50,60,70,80,90,100])
voltage_out = np.array([480,380,286,230,188,162,141,127,115])



def exponential(x, a, b, c):
     return a * np.exp(-b * x) + c

def log(x, a, b):
        return a * np.log(x) + b

def quadratic(x, a, b, c):
	return a * x + b * x**2 + c

def power_law(x, a, b):
    return a*np.power(x, b)


plt.plot(calibration_dist, voltage_out)
optimizedParameters, _ = opt.curve_fit(quadratic, calibration_dist, voltage_out);
print(optimizedParameters)

#1.96064177e+02 3.42264651e-02 2.27241459e+01

# Use the optimized parameters to plot the best fit
plt.plot(calibration_dist, quadratic(calibration_dist, *optimizedParameters), label="fit");
plt.title("Calibration Plot")
plt.xlabel("Calibration Distance (cm)")
plt.ylabel("Voltage Out (mapped output volts)")

# Show the graph
plt.legend();
plt.show();
