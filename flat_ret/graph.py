import matplotlib.pyplot as plt
import matplotlib.colors as colors

colors_list = list(colors._colors_full_map.values())


def graph(file_name, step):
    ox = []
    oy = []
    with open(file_name) as file, open('without_mut.txt', 'r') as ideal:
        for y, line in enumerate(file.readlines()):
            line_list = line.split()
            ox.append(float(line_list[0]))
            oy.append(y)
        for y, line in enumerate(ideal.readlines()):
            line_list = line.split()
            ox[y] -= float(line_list[0])
    file.close()
    plt.plot(oy, ox, 'o', color=colors_list[step], label=f'{step}')
    plt.legend()


for i in range(1, 10):
    graph('dihedral%s.txt' % i, i)

#plt.savefig('graph.png')
plt.show()
plt.clf()

