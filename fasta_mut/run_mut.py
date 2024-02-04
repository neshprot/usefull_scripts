# read Infos.dat
with open('Infos.dat', "r", ) as file:
    lines = file.readlines()
    project = lines[0].split()[1]
    template = lines[1].split()[1]

with open('mutants.txt', 'r') as file:
    muts = {}
    for line in file.readlines():
        mut = line.split()
        mut = ''.join(str(x) for x in mut)
        muts.update({int(mut[1:-1]): mut[-1]})

# read file.fasta and write mutant.fasta
with open(f'{project}_{template}.fasta', 'r') as file, open(f'mutant.fasta', 'w') as file_mut:
    lines = file.readlines()
    file_mut.write(lines[0])
    index = 0
    target = list(lines[1])
    for i, aa in enumerate(target):
        if aa == '-':
            continue
        index += 1
        if index in muts.keys():
            target[i] = muts[index]

    file_mut.write(''.join(target))
    for line in lines[2:]:
        file_mut.write(line)
