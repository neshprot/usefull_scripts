import matplotlib.pyplot as plt

N = 5
top_bests = 20
name = f'freq_top_{top_bests}'

ox = []
oy = []
a = [1, 2, 3, 4, 5, 6, 7]


with open(f'freq_{N}', 'r') as file:
    for line in file.readlines()[:top_bests:]:
        value = line.split()
        ox.append(value[0])
        oy.append(float(value[1]))


fig, ax1 = plt.subplots()
ax1.bar(ox, oy)
ax1.set_xlabel('аминокислотная замена')
ax1.set_ylabel('частота появления')
plt.xticks(rotation=90, size=6.5)
plt.savefig(name)
