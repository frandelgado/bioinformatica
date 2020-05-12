from Bio import SeqIO
from Bio import SeqRecord
import re

GENE = "huntingtin"
TABLE = 1
MIN_PRO_LEN = 50
ONLY_SAVE_LONGEST = True

gbk_filename = "sequences/" + GENE + ".gb"
fas_filename = "sequences/" + GENE + "_translated.fasta"

with open(gbk_filename, 'r') as gb_handle:
    with open(fas_filename, 'w') as fas_handle:
        for record in SeqIO.parse(gb_handle, "genbank"):
            longest_pro = (0, None)
            for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
                for frame in range(3):
                    length = 3 * ((len(record) - frame) // 3)  # Multiple of three
                    for trans in nuc[frame:frame + length].translate(TABLE).split("*"):
                        for m in re.finditer('M', str(trans)):
                            pro = trans[m.start():]
                            pro_len = len(pro)
                            if pro_len >= MIN_PRO_LEN:
                                if pro_len > longest_pro[0]:
                                    longest_pro = (pro_len, pro)
                                elif not ONLY_SAVE_LONGEST:
                                    r = SeqRecord.SeqRecord(pro, id=record.id,
                                        description=record.description+' translation - frame {0}'%(frame*strand))
                                    fas_handle.write(r.format('fasta'))
            if longest_pro[1] is not None:
                r = SeqRecord.SeqRecord(longest_pro[1], id=record.id,
                    description=record.description+' translation')
                fas_handle.write(r.format('fasta'))
