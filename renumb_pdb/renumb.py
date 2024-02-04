with open('6GUX_t.pdb', 'r') as inp, open('6GUX_t_ren.pdb', 'w') as out:
    for i, line in enumerate(inp.readlines()):
        text = line.split()
        text[1] = str(i+1)
        new_text = ' '.join(text)
        out.write(f'{new_text}\n')