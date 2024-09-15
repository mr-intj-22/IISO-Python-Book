# Fly The TELLO Drone and Monitor Its States

Tello Drone is a toy drone that can be controlled using Python commands. In this tutorials, we will connect to the drone, fly it, and plot the states.

## STEP 0: INSTALL AND IMPORT REQUIRED MODULES

1. Time: This function is used to count the number of seconds elapsed since the start.
2. `djitellopy`: a library (module) that helps connecting to the drone and controlling it. To install it, type in the terminal:
```shell
pip3 install djitellopy
```
3. `numpy`: Numpy (Numerical Python) is a library that can store and manipulate numerical data. To install it, type in the terminal:
```shell
pip3 install numpy
```
4. `matplotlib`: This is a plotting libray used to make plot and visualize data in Python. To install it, type in the terminal:
```shell
pip3 install matplotlib
```

After installing all required library`modules, let's import them.

* Make a new script and name it `tello.py`.
* write this code in the top of the new/empty script
```Python
import time
from djitellopy import Tello
import numpy as np
import matplotlib.pyplot as plt
```

## STEP 1: CONNECT THE DRONE
Create a Python TELLO Object
```Python
# Initialize Tello object
tello = Tello()
```
This object will be like the real drone by in Python, it will connect to the drone, control it, and read the data.
After creating the `Tello Object`, connect the Tello Drone:
* Make sure you are connected to the Drone's WIFI (done at the end before running the code)
* Write the following code in the script:
```Python
# Connect to Tello
tello.connect()
```
If the drone is not connected for any reason, the program will terminate with an error.

## Step 2: Take-Off
Once the drone is connected, it is time to fly (remember, it was not made to stay on the ground!)
```Python
# Take-off (fly)
tello.takeoff()
time.sleep(3) # wait 3 seconds for the drone to respond
```
If everything is done right, the Drone will take off vertically.

## STEP 3: SEND COMMANDS
The Tello Drone modules is designed such that if it does not recieve any command with in some time (~7 seconds), it will land automatically (for safety). To ensure that we constantly send command (and read data later), let's make an infinite while loop that will keep the drone flying:
```Python
while True:
    tello.move_right(20)
    time.sleep(3) # wait 5 seconds for it to respond
    tello.move_left(20)
    time.sleep(3) # wait 5 seconds for it to respond
```
Observe how the Drone is moving left and right. Remember, the loop is infinite, that means it will go forever unless we interrupt it.Press `CTRL+C` in the terminal to end the loop.

## STEP 4: READ STATES
In this tutorial we will read and plot some of the state of the Drone. To see what states are available, modify the previos loop to:
```Python
while True:
    state = tello.get_current_state()
    print(type(state), states.keys(), sep='\n')
    break
```
`state` is of type `dict` or a Dictionary in python, where it holds pairs of `key-value` and here were are interested in finding the available keys (states).

If you run the previous code you will find it prints:
```
dict_keys(['pitch', 'roll', 'yaw', 'vgx', 'vgy', 'vgz', 'templ', 'temph', 'tof', 'h', 'bat', 'baro', 'time', 'agx', 'agy', 'agz'])
```
Which are the available state that we can plot over time as the Drone flies.

## STEP 4: PLOT THE ORIENTATION (ROLL, PITCH, YAW) AND ALTITUDE (h)
We will command the drone to a command and plot the orientation and altitude of the drone as it does it. Please remove the code written in (STEP 3)
To do that, let's prepare our plotting figure, add some variable to track flight history
```Python
init_time = time.time() # keep track of starting time
times = [] # list to hold the time when we read the states
states = [] # list holding all the states of the drone
```
then let's make some plots to plot the data as the drone flies. The following code make empty plots and sets the legend for each state of interest.
```Python
# Enable interactive mode
plt.ion()

fig, axs = plt.subplots(4,1)

# Initial plot
roll_line, = axs[0].plot([],[], "r-", label="Roll [deg]")
axs[0].grid()
axs[0].legend()
pitch_line, = axs[1].plot([],[], "g-", label="Ptich [deg]")
axs[1].grid()
axs[1].legend()
yaw_line, = axs[2].plot([],[], "b-", label="Yaw [deg]")
axs[2].grid()
axs[2].legend()
h_line, = axs[3].plot([],[], "k-", label="altitude [h]")
axs[3].grid()
axs[3].legend()

plt.suptitle("Drone Attitude (Pitch, Roll, Yaw, Altitude)")
plt.show()
```
Now let's move the drone to some position x,y,z with speed s (here only go up 50cm with speed on 20cm/s):
```Python
tello.go_xyz_speed(0,0,50,20)
```
Now, let's make the loop
```Python
while True:
    # Get current state from Tello
    state = tello.get_current_state()

    # Skip if state is empty
    if (len(state.keys())==0):
        continue

    # Append state and time to history
    states.append(state)
    times.append(time.time()-init_time)
    
    # Convert roll, pitch, yaw from radians to degrees and update the lines
    roll_line.set_data(times, [np.rad2deg(s['roll']) for s in states])
    pitch_line.set_data(times, [np.rad2deg(s['pitch']) for s in states])
    yaw_line.set_data(times, [np.rad2deg(s['yaw']) for s in states])
    h_line.set_data(times, [s['h'] for s in states])
    
    # Rescale x-axis dynamically
    axs[0].set_xlim(0, max(times) + 1)
    axs[1].set_xlim(0, max(times) + 1)
    axs[2].set_xlim(0, max(times) + 1)
    axs[3].set_xlim(0, max(times) + 1)

    # Rescale y-axis for roll, pitch, and yaw
    axs[0].set_ylim(min([np.rad2deg(s['roll']) for s in states]), max([np.rad2deg(s['roll']) for s in states]) + 1)
    axs[1].set_ylim(min([np.rad2deg(s['pitch']) for s in states]), max([np.rad2deg(s['pitch']) for s in states]) + 1)
    axs[2].set_ylim(min([np.rad2deg(s['yaw']) for s in states]), max([np.rad2deg(s['yaw']) for s in states]) + 1)
    axs[3].set_ylim(min([s['h'] for s in states]), max([s['h'] for s in states]) + 1)
```
This code has a tiny problem, there is no command for it to land safely! so let's add it. We will add a try-catch block to break the loop when `CTRL+C` is pressed.
```Python
while True:
    try:
        # Get current state from Tello
        state = tello.get_current_state()

        # Skip if state is empty
        if (len(state.keys())==0):
            continue

        # Append state and time to history
        states.append(state)
        times.append(time.time()-init_time)
        
        # Convert roll, pitch, yaw from radians to degrees and update the lines
        roll_line.set_data(times, [np.rad2deg(s['roll']) for s in states])
        pitch_line.set_data(times, [np.rad2deg(s['pitch']) for s in states])
        yaw_line.set_data(times, [np.rad2deg(s['yaw']) for s in states])
        h_line.set_data(times, [s['h'] for s in states])
        
        # Rescale x-axis dynamically
        axs[0].set_xlim(0, max(times) + 1)
        axs[1].set_xlim(0, max(times) + 1)
        axs[2].set_xlim(0, max(times) + 1)
        axs[3].set_xlim(0, max(times) + 1)

        # Rescale y-axis for roll, pitch, and yaw
        axs[0].set_ylim(min([np.rad2deg(s['roll']) for s in states]), max([np.rad2deg(s['roll']) for s in states]) + 1)
        axs[1].set_ylim(min([np.rad2deg(s['pitch']) for s in states]), max([np.rad2deg(s['pitch']) for s in states]) + 1)
        axs[2].set_ylim(min([np.rad2deg(s['yaw']) for s in states]), max([np.rad2deg(s['yaw']) for s in states]) + 1)
        axs[3].set_ylim(min([s['h'] for s in states]), max([s['h'] for s in states]) + 1)

        # Pause to update the plot in real-time
        plt.pause(0.1)
    except:
        break
```
Finally, let's command it to land at the end of the script.
```Python
tello.land()
```

This Gives us a working script that:
* Connects to Tello Drone.
* Take-off
* Move to a position (x,y,z)
* monitor the states
* land safely

Next time, we will keep sending commands as it flys:
* follow a path
* do acrobatic flips
*　Something else?