from Bio.Align.Applications import ClustalwCommandline

FASTA_FILE = "sequences/hemoglobin_multifasta.fasta"
OUT_FILE = "sequences/hemoglobin_multialign.txt"

clustalw_cline = ClustalwCommandline("clustalw", infile=FASTA_FILE, outfile=OUT_FILE)
stdout, stderr = clustalw_cline()