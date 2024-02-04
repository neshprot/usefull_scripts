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


def calc_dihedral(u1, u2, u3, u4):
    """ Calculate dihedral angle method. From bioPython.PDB
    (adapted to np.array)
    Calculate the dihedral angle between 4 vectors
    representing 4 connected points. The angle is in
    [-pi, pi].
    """

    a1 = u2 - u1
    a2 = u3 - u2
    a3 = u4 - u3

    v1 = np.cross(a1, a2)
    v1 = v1 / (v1 * v1).sum(-1) ** 0.5
    v2 = np.cross(a2, a3)
    v2 = v2 / (v2 * v2).sum(-1) ** 0.5
    porm = np.sign((v1 * a3).sum(-1))
    rad = np.arccos((v1 * v2).sum(-1) / ((v1 ** 2).sum(-1) * (v2 ** 2).sum(-1)) ** 0.5)
    if not porm == 0:
        rad = rad * porm

    return rad


def dihedral(geom, positions):
    p1 = geom[positions[0]]
    p2 = geom[positions[1]]
    p3 = geom[positions[2]]
    p4 = geom[positions[3]]

    alpha_rod = calc_dihedral(p1, p2, p3, p4)
    alpha_degrees = alpha_rod * 180/3.1415
    if alpha_degrees < 0:
        alpha_degrees = 180 - abs(alpha_degrees)
    if alpha_degrees > 90:
        alpha_degrees = 180 - alpha_degrees
    return alpha_degrees


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


def check_dih():
    stand_dih = 2
    dihedrals = [[12, 13, 15, 17],
                 [13, 15, 17, 18],
                 [15, 17, 18, 20],
                 [17, 18, 20, 22],
                 [18, 20, 22, 24],
                 [20, 22, 24, 25]]
    geom = read_inp(f'protein12_9_2.inp')
    dih_angles = []
    for k in dihedrals:
        a1 = int(k[0])
        b1 = int(k[1])
        c1 = int(k[2])
        d1 = int(k[3])
        a = a1 - 1
        b = b1 - 1
        c = c1 - 1
        d = d1 - 1
        positions = (a, b, c, d)
        dih_angles.append(dihedral(geom, positions))
    print(dih_angles)
    if max(dih_angles) > stand_dih:
        return False
    return True


if __name__ == "__main__":
    checker = check_dih()
    write_out('flat_ret.out', 1 if checker else 0)
