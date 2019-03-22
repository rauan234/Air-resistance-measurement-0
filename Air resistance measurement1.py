import matplotlib.pyplot as plt



input_data = '''00 572
01 591
04 617
05 623
06 628
07 633
08 638
09 643
10 649
11 654
12 659
13 663
14 668
15 673
16 678
17 683
18 688
19 694'''

framerate = 30
floor_height = 3

g = 9.81
M = 0.6



input_list = input_data.split('\n')

times = []
heights = []
for frame in input_list:
    times.append(int(frame.split(' ')[1]) / framerate)
    heights.append(int(frame.split(' ')[0]) * floor_height)
tmin = min(times)
for ind in range(len(times)):
    times[ind] -= tmin



def F(v):
    return v**2 * 0.01

tlist = []
approx = []
time = 0
dt = 0.001
v = 0
h = 0
while(time < max(times)):
    tlist.append(time)
    approx.append(h)
    
    h += v * dt
    v += (g - F(v) / M) * dt

    time += dt




plt.plot(times, heights, color='b')
plt.plot(tlist, approx, color='r')
plt.xlabel('time')
plt.ylabel('height')
plt.title('Blue - real graph, Red - approximating line:\ndH/dt = V    dV/dt = F / M    F = Mg - v**2 * 0.01')
plt.show()



smax = (heights[-1] - heights[-2]) / (times[-1] - times[-2])

speeds = []
forces = []
s = 0
ds = 0.001
while(s < smax):
    speeds.append(s)
    forces.append(F(s))
    s += ds

plt.plot(speeds, forces, color='g')
plt.xlabel('speed')
plt.ylabel('force')
plt.title('Force of air resistance for a ball')
plt.show()
