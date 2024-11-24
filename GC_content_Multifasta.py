Count_A = 0
Count_C = 0
Count_G = 0
Count_T = 0
gc_content = 0
gene_name = ""

with open("Bsubtilis_CDS.fna.txt") as file:
    for line in file:
        if line.startswith(">"):
            print(gene_name)
            #print(line.rstrip())
            temp = line.split()
            #print(temp)
            #gene_name = temp[1][6:-1]
            gene_name = temp[1].split("=")[1][:-1]
            print(gene_name)
        else:
            print(line)





### PARA DIFERENCIAR UNA VARIABLE INTERNA DE PYTHON CON UNA VARIABLE PROPIA, SE LE AGREGA UNA GUION BAJO