BLA = []
pka215 = []
pka207 = []
mutants = []
with open('bests', 'r') as file:
    for line in file.readlines():
        split_line = line.split(" ", 6)
        BLA.append(split_line[1])
        pka215.append(float(split_line[3]))
        pka207.append(float(split_line[5]))
        mutants.append(split_line[6])



with open('table', 'w') as ouf:
    ouf.write(f'|delta pka | pka 215| pka 207| mutants |\n')
    ouf.write(f'| -------- | ------ | ------ | ------- |\n')
    for bla, p215, p207, muts in zip(BLA, pka215, pka207, mutants):
        ouf.write(f'| {p215 - p207:.2f} | {p215} | {p207} | {muts} |\n')