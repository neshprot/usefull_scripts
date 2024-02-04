"""
Find bla for RET
"""

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


def find_bla(geom):
    """
    find system's bla
    :param geom: list of coords
    :return: bla value
    """

    c6c5 = np.sum(np.square(geom[10] - geom[11]))
    c7c6 = np.sum(np.square(geom[11] - geom[12]))
    c8c7 = np.sum(np.square(geom[12] - geom[14]))
    c9c8 = np.sum(np.square(geom[14] - geom[16]))
    c10c9 = np.sum(np.square(geom[16] - geom[17]))
    c11c10 = np.sum(np.square(geom[17] - geom[19]))
    c12c11 = np.sum(np.square(geom[19] - geom[21]))
    c13c12 = np.sum(np.square(geom[21] - geom[23]))
    c14c13 = np.sum(np.square(geom[23] - geom[24]))
    c15c14 = np.sum(np.square(geom[24] - geom[26]))

    av_single = np.mean((c15c14, c13c12, c11c10, c9c8, c7c6))
    av_double = np.mean((c14c13, c12c11, c10c9, c8c7, c6c5))

    bla_value = av_single - av_double

    return bla_value


def write_out(filename, value):
    """
    :param filename: name of out file
    :param value: bla
    :return: file with bla
    """
    with open(filename, 'w', encoding="utf-8") as out_file:
        out_file.write(str(value))
    out_file.close()


if __name__ == '__main__':
    xyz = read_inp('protein.inp')
    bla = find_bla(xyz)
    write_out('bla.out', bla)
