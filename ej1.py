from Bio import SeqIO

gbk_filename = "sequences/NC_000207-3.gbk"
fas_filename = "sequences/NC_000207-3_translated.fas"

with open(gbk_filename, 'r') as gb_handle:
    with open(fas_filename, 'w') as fas_handle:
        for gb_record in SeqIO.parse(gb_handle, "genbank"):
            protein = gb_record.translate(table=1)
            fas_handle.write(protein.format("fasta"))
