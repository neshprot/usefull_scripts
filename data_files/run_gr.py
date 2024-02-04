import matplotlib.pyplot as plt
import numpy as np

run_num = '5'
inp_file = f'test_run{run_num}'
probs = []
config_weight = [None, None]
ox = []
BLA = []
pka215 = []
pka207 = []


with open(inp_file) as file:
    lines = file.readlines()
    new_data = True
    counter_data = 0
    counter_lines = [0]
    for i, line in enumerate(lines):
        if len(line) <= 1:
            new_data = True
            counter_data += 1
            counter_lines.append(0)
            continue
        if new_data:
            params = lines[i].split()
            probs.append((params[0], params[1]))
            config_weight[0] = params[2]
            config_weight[1] = params[3]
        else:
            values = line.split()
            BLA.append(float(values[0]))
            pka215.append(float(values[1]))
            pka207.append(float(values[2]))
            counter_lines[counter_data] += 1
        new_data = False

lines_before = 0
for i, num in enumerate(counter_lines):
    ox = np.linspace(1, num, num)
    temp_BLA = BLA[lines_before:(num + lines_before)]
    temp_pka215 = pka215[lines_before:(num + lines_before)]
    temp_pka207 = pka207[lines_before:(num + lines_before)]
    lines_before += num

    delta_pka = [pka215 - pka207 for pka215, pka207 in zip(temp_pka215, temp_pka207)]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax2.set_title(f'cros prob: {probs[0]}, mut prob: {probs[1]}')
    ax2.set_xlabel(f'population')
    ax2.set_ylabel('pka values')
    ax2.plot(ox, temp_pka215, label='pka215')
    ax2.plot(ox, temp_pka207, label='pka207')
    ax2.plot(ox, delta_pka, 'ko', label='pka215 - pka207')

    ax1.set_xlabel(f'population')
    ax1.set_ylabel('difference between pka215 and pka207')
    ax1.plot(ox, delta_pka, 'ko', label='pka215 - pka207')
    fig.set_figheight(5)
    fig.set_figwidth(10)

    plt.legend()
    plt.savefig(f'graph5_{i+1}.png')
