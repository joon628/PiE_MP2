import serial
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def retrieve_data():
    arduinoComPort = "/dev/cu.usbmodem14301"
    baudRate = 9600

    serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

    # main loop to read data from the Arduino, then display it
    x, y = [], []
    try:
        while True:
          # ask for a line of data from the serial port, the ".decode()" converts the
          # data from an "array of bytes", to a string
          lineOfData = serialPort.readline().decode()
          if lineOfData != '':
              if lineOfData.strip() != "done":
                  data = lineOfData.split(',')
                  if len(data) == 2 and data[0] != '' and data[1] != '':

                      xy = pol2cart(int(data[0]), np.deg2rad(int(data[1])))
                      x.append(xy[0])
                      y.append(xy[1])
                      print(xy[0], xy[1])

                  else:
                      print("Error, Skipping")
              else:
                  break
    except KeyboardInterrupt:
        pass

    return x, y

def pol2cart(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return(x, y)

def plot(pan, depth):
    plt.scatter(pan, depth)
    # Make data.
    # Plot the surface.
    plt.title("2D plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

pan, depth = retrieve_data();
plot(pan, depth)
