import numpy as np

"""
1. C6 C7 C8 C9
2. C7 C8 C9 CF
3. C8 C9 CF CI
4. C9 CF CI CJ
5. CF CI CJ C13
6 CI CJ C13 CK
7. CJ C13 CK CM
"""


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


""" Dihedral angles from coordinates. Get dihedral angles from 
    protein backbone coordinates.
    This script takes 4 vectors representing 4 points as input
    and returns the dihedral angle between them.

    The script was originally developed to calculate dihedral angles (phi,psi)
    from protein backbone atoms' coordinates in 3D (N-term, C-alhpa, Cterm).
"""


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


'''
12 13 15 17
13 15 17 18
15 17 18 20
17 18 20 22
18 20 22 24
20 22 24 25
22 24 25 27
'''

dihedrals = [[12, 13, 15, 17],
             [13, 15, 17, 18],
             [15, 17, 18, 20],
             [17, 18, 20, 22],
             [18, 20, 22, 24],
             [20, 22, 24, 25],
             [22, 24, 25, 27]]

out_name = 'dihedral'
inp_name = 'protein'
for i in range(1, 10):
    with open(f'{out_name}{i}.txt', 'w') as out:
        geom = read_inp(f'{inp_name}{i}.inp')
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
            dih_angle = dihedral(geom, positions)
            out.write(f'{str(dih_angle)}\n')

