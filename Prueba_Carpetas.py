import gzip

sequence_file = "../carpeta1/uniprotkb_saccharomyces_AND_reviewed_tr_2024_11_14.tsv.gz"



with gzip.open(sequence_file,"rt") as file:
    for line in file:
        print(line)