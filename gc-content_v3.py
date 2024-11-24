def gc_content(sequence):
    sequence = "ACTGACGAaacaaNNNN1\n"

    sequence = sequence.rstrip("\n")
    sequence = sequence.upper()
    G_count = sequence.count("G")
    C_count = sequence.count("C")
    gc_content = G_count + C_count
    gc_content = gc_content / len(sequence)
    gc_content = round(100 * gc_content, 2)


    return gc_content
    pass

sequence = "ACTGACGAaacaaNNNN1\n"

fasta_file = "Levadura.fasta"
output_file = fasta_file.split(".")[0]
output_file = output_file + "_gc_content.txt"
print(output_file)
file1 = open(output_file, "w")
file1.close()
sequence = str()

####### NO MODIFICAR########
with open(fasta_file) as file:
    for line in file:
        if line.startswith(">"):
            pass
        else:
            line = line.rstrip("\n")
            sequence += line
print(sequence)
print(gc_content(sequence))
gc_content = gc_content(sequence)

file1=open(output_file,"w")
file1.write(f"el contenido gc es {gc_content}\n")
file1.close()