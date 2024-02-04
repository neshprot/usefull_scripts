import numpy as np


def read_inp(filename):
    """
    read coordinates of carbons
    :param filename: name of input file
    :return: list of numpy arrays with coordinates
    """

    with open(filename, "r", encoding="utf-8") as inp_file:
        lines = inp_file.readlines()
    inp_file.close()
    lines = lines[48:-1:]
    geom = []
    for line in lines:
        cords = line.split()
        geom.append(np.array((float(cords[1]),
                             float(cords[2]),
                             float(cords[3]))))
    return geom


def check_dist(first_dot, second_dot, carbon_list, stand_dist):
    def dist_point_line(point, first_p, second_p):
        dist = np.linalg.norm(np.cross(second_p - first_p, first_p - point)) / np.linalg.norm(second_p - first_p)
        return dist
    for carbon in carbon_list:
        if stand_dist > dist_point_line(carbon, first_dot, second_dot):
            continue
        else:
            return False
    return True


def write_out(filename, value):
    """
    :param filename: name of out file
    :param value: bla
    :return: file with bla
    """
    with open(filename, 'w', encoding="utf-8") as out_file:
        out_file.write(str(value))


if __name__ == "__main__":
    deviation = 2
    xyz = read_inp('protein4.inp')
    ini_carbon = xyz[11]    #c6
    last_carbon = xyz[26]   #c15
    carbons = [xyz[12], xyz[14], xyz[16], xyz[17], xyz[19], xyz[21], xyz[23], xyz[24]]
    cheker = check_dist(ini_carbon, last_carbon, carbons, deviation)
    write_out('flat_ret.out', 1 if cheker else 0)
