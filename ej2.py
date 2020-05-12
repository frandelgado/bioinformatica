from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

ONLINE = True
BLAST_EXECUTABLE = "/usr/bin/blastp"
E_VALUE_THRESH = 10
PROT_DB = "blast/ncbi-blast-2.10.0+/data/swissprot"


FASTA_FILE = "sequences/huntingtin.fasta"
RESULTS_XML = "blast_reports/my_blast.xml"

if ONLINE:
    fasta_string = open(FASTA_FILE).read()
    result_handle = NCBIWWW.qblast("blastp", "swissprot", fasta_string, expect=10)
    with open(RESULTS_XML, "w+") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    result_handle = open(RESULTS_XML)
else:
    blastx_cline = NcbiblastxCommandline(
        cmd=BLAST_EXECUTABLE,
        query=FASTA_FILE,
        db=PROT_DB,
        evalue=E_VALUE_THRESH,
        out=RESULTS_XML,
        outfmt=5
        )
    stdout, stderr = blastx_cline()
    result_handle = open(RESULTS_XML)

blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print("****Alignment****")
                print("sequence:", alignment.title)
                print("length:", alignment.length)
                print("e value:", hsp.expect)
                print("gaps:", hsp.gaps)
                print("identities:", hsp.identities)
                print("positives:", hsp.positives)
                print("score:", hsp.score)
                print(hsp.query[0:75] + "...")
                print(hsp.match[0:75] + "...")
                print(hsp.sbjct[0:75] + "...")
