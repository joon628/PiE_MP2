import serial
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import astropy.coordinates as ac

def retrieve_data():
    arduinoComPort = "/dev/cu.usbmodem14401"
    baudRate = 9600

    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

    # main loop to read data from the Arduino, then display it
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
                      if int(data[0]) > 60:
                          continue

                      xyz = ac.spherical_to_cartesian(int(data[0]), np.deg2rad(int(data[2])), np.deg2rad(int(data[1])))
                      x.append(xyz[0])
                      y.append(xyz[1])
                      z.append(xyz[2])
                      print(xyz[0], xyz[1], xyz[2])

                  else:
                      print("Error, Skipping")
              else:
                  break
    except KeyboardInterrupt:
        pass

    return x, y, z


def plot(tilt, pan, depth):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Make data.
    # Plot the surface.
    surf = ax.scatter(tilt, pan, depth, linewidth=0, antialiased=False)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

tilt, pan, depth = retrieve_data();
# df = pd.DataFrame(list(zip(depth, tilt, pan)))
# df.to_csv("1.csv")
plot(tilt, pan, depth)
