import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# parameters 

u = float(input("Enter projection velocity: "))                                    # initial velocity (m/s)
theta = np.deg2rad(float(input("Enter angle made with horizontal (deg): ")))       # projection angle (deg)
x = np.array([float(input("Enter initial x coordinate: "))], dtype=float)          # initial x-position (m)
y = np.array([float(input("Enter initial y coordinate: "))], dtype=float)          # initial y-position (m)
g = 9.8                                                                            # acc. due to gravity (m/s^2)
dt = 10**-5                                                      # interval between consecutive parameter updates

# smaller dt results in a better approximation of the trajectory


# breaking motion along components 

vx = u*np.cos(theta)        # initial x-velocity
vy = u*np.sin(theta)        # initial y-velocity

# plot setup 

fig, ax = plt.subplots()
ax.set_xlabel("X")
ax.set_ylabel("Y")

# defining initial line element of plot

line, = ax.plot(x, y, color='black')


# simulation

frame_count = 1
t = dt   # initial time value (will be incremented by dt in each timestep)
x_new = x[0]
y_new = y[0]

while y_new >= 0:

    vy -= g*t
    
    x_new += vx*t
    y_new += vy*t

    x = np.append(x, [x_new], axis=0)
    y = np.append(y, [y_new], axis=0)

    t += dt
    frame_count += 1

ax.set_ylim(0, np.max(y))
ax.set_xlim(0, np.max(x))


# animation 

def frame_update(frame):
    global x, y, vx, vy
    
    line.set_data(x[:frame], y[: frame])

    return line, 


ani = animation.FuncAnimation(fig, frame_update, frames=frame_count, interval=20, blit=True)
ani.save('2d_projectile.gif')

#plt.show()