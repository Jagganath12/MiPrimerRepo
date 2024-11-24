import re
from selectors import SelectSelector

# Ruta al archivo
file_path = "../pythonProject1/Bsubtilis_CDS.fna.txt"

# Expresión regular para buscar el atributo gene
pattern = re.compile(r"\[gene=([^\]]+)\]")

# Lista para almacenar los nombres de los genes
genes = []

# Leer el archivo y extraer los valores de gene
with open(file_path, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            genes.append(match.group(1))

# Mostrar los genes encontrados
print("Los genes encontrados son:")
print("\n".join(genes))

# Opcional: guardar en un archivo
with open("genes_extraidos.txt", "w") as output_file:
    output_file.write("\n".join(genes))
