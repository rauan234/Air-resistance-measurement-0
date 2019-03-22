import matplotlib.pyplot as plt



baloon_movement_input_data = '''92 2:27,03 2:28,00
92 2:57,25 2:58,23
92 4:08,15 4:09,11
88 5:53,07 5:54,03
88 6:45,18 6:46,12
88 7:13,20 7:14,13
84 9:08,25 9:09,20
84 9:42,18 9:43,12
84 10:10,29 10:11,22
80.5 11:18,14 11:19,06
80.5 12:10,18 12:11,10
80.5 13:08,22 13:09,15
80.5 16:57,11 16:58,04
77.5 20:24,13 20:25,05
73.5 22:13,19 22:14,11
73.5 23:20,08 23:21,00
71 26:40,21 26:41,12
71 29:49,25 29:50,15
68.5 33:06,25 33:07,14
68.5 34:02,17 34:03,06
65 36:54,15 36:55,03
62 38:19,29 38:20,16
62 38:38,23 38:39,12
62 39:09,23 39:10,12
62 39:47,27 39:48,15
58.5 41:08,13 41:08,29
58.5 42:06,01 42:06,17
58.5 43:08,29 43:09,15
58.5 45:31,26 45:32,13
56 46:52,10 46:52,26
56 48:31,03 48:31,18
56 49:43,28 49:44,14
56 50:52,11 50:52,27
56 52:00,28 52:01,13
52.5 53:10,12 53:10,28
52.5 54:01,01 54:01,16
50 56:47,27 56:48,10
50 57:40,09 57:40,23
50 58:14,08 58:14,21
47 60:25,19 60:26,01
47 61:48,11 61:48,23
47 62:40,01 62:40,13
44 65:50,20 65:51,01
44 67:14,11 67:14,22
44 68:10,18 68:10,28
40.5 71:07,14 71:07,22
40.5 71:59,16 71:59,25
40.5 73:30,26 73:31,05
40.5 74:31,01 74:31,10
36 77:05,07 77:05,15
36 77:59,19 77:59,27
36 78:47,10 78:47,18
36 79:20,28 79:21,05
36 80:13,10 80:13,18
33 83:53,22 83:53,27
33 84:44,07 84:44,13
33 85:47,27 85:48,03
34.5 87:33,29 87:34,06
34.5 88:43,07 88:43,14
34.5 89:27,18 89:27,25'''

g = 9.81

L = 0.33     # height of the baloon
P = 0.352    # weight of the baloon
M = P / g    # mass of the baloon



def get_time(inp):
    try:
        minutes = int(inp.split(':')[0])
        seconds = int(inp.split(':')[1].split(',')[0])
        frames  = int(inp.split(':')[1].split(',')[1])

    except Exception:
        print("ERROR:")
        input(inp)

        return 0

    return 60 * minutes + seconds + 1 /30 * frames

def flip(inp):
    out = {}

    for key in inp:
        out[inp[key]] = key

    return out



def Height_time_dict(inp):
    out = {}

    for sentence in inp.split('\n'):
        data = sentence.split(' ')

        height = float(data[0]) / 100 - L
        start_time = get_time(data[1])
        end_time = get_time(data[2])

        if(height not in out):
            out[height] = []

        out[height].append(end_time - start_time)

    return out

def Average(inp):
    out = {}

    for key in inp:
        out[key] = sum(inp[key]) / len(inp[key])

    return out

def Draw_height_time_graph(averaged_time_height_dict):
    times = []
    heights = []
    for time in averaged_time_height_dict:
        times.append(time)
        heights.append(averaged_time_height_dict[time])

    tmin = min(times)
    for ind in range(len(times)):
        times[ind] -= tmin

    tmax = max(times)
    hmax = max(heights)

    approx = []
    tlist = []
    time = 0
    dt = 0.001
    v = 0
    h = 0
    while(time < tmax):
        f = M * g - v**2 * 0.3 - v * 0.11

        v += dt * f / M

        h += v * dt

        tlist.append(time)
        approx.append(h)
        
        time += dt
        
    plt.plot(times, heights, color='b')
    plt.plot(tlist, approx, color='r')
    plt.xlabel('time')
    plt.ylabel('height')
    plt.title('Blue - real graph, Red - approximating line:\ndH/dt = V    dV/dt = F / M    F = Mg - (v * 0.11 + v^2 * 0.3)')
    plt.show()



height_time_dict = Height_time_dict(baloon_movement_input_data)
averaged_height_time_dict = Average(height_time_dict)

averaged_time_height_dict = flip(averaged_height_time_dict)

Draw_height_time_graph(averaged_time_height_dict)
