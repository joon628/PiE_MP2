import serial
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd


def retrieve_data():
    arduinoComPort = "/dev/cu.usbmodem14301"
    baudRate = 9600

    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

    # main loop to read data from the Arduino, then display it
    tilt, pan, depth = [], [], []
    x, y, z = [], [], []
    try:
        while True:
          # ask for a line of data from the serial port, the ".decode()" converts the
          # data from an "array of bytes", to a string
          lineOfData = serialPort.readline().decode()
          if lineOfData != '':
              if lineOfData.strip() != "done":
                  data = lineOfData.split(',')
                  if len(data) == 3 and data[0] != '' and data[1] != '' and data[2] != '':
                     #depth_p, tilt_p, pan_p = polar_to_cartesian(int(data[0]), int(data[1]), int(data[2]))
                      tilt.append(int(data[1]))
                      pan.append(int(data[2]))
                      depth.append(int(data[0]))
                      xyz = polar_to_cartesian(int(data[0]), np.deg2rad(int(data[2])), np.deg2rad(int(data[1])))
                      x.append(xyz[0])
                      y.append(xyz[1])
                      z.append(xyz[2])
                  else:
                      print("Error, Skipping")
              else:
                  break
    except KeyboardInterrupt:
        pass
    return x, y, z



def polar_to_cartesian(dist, tilt, pan):
    """Returns the 3D point for the corresponding length and angle values
    Inputs:
        dist: Distance from the sensor to the object
        pitch: Pitch angle of the sensor, in radians
        yaw: Yaw angle of the sensor, in radians
    """

    return (dist * np.array([np.cos(-(tilt - np.pi / 2)) * np.sin(-pan),
                             np.cos(-(tilt - np.pi / 2)) * np.cos(-pan),
                             np.sin(-(tilt - np.pi / 2))]))

def plot(tilt, pan, depth):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Make data.
    # Plot the surface.
    surf = ax.scatter(depth, tilt, pan, linewidth=0, antialiased=False)
    plt.xlabel("depth")
    plt.ylabel("tilt")
    # Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    plt.show()

tilt, pan, depth = retrieve_data();
df = pd.DataFrame(list(zip(depth, tilt, pan)))
df.to_csv("wall.csv")

plot(tilt, pan, depth)
