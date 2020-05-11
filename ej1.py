from Bio import SeqIO
from Bio import SeqRecord
import re

gen = "hemoglobin"
gbk_filename = "sequences/"+gen+".gbk"
fas_filename = "sequences/"+gen+"_translated.fasta"
table = 1
min_pro_len = 50
only_save_longest = True

with open(gbk_filename, 'r') as gb_handle:
    with open(fas_filename, 'w') as fas_handle:
        for record in SeqIO.parse(gb_handle, "genbank"):
            for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
                for frame in range(3):
                    length = 3 * ((len(record) - frame) // 3)  # Multiple of three
                    longest_pro = (0, None)
                    for trans in nuc[frame:frame + length].translate(table).split("*"):
                        for m in re.finditer('M', str(trans)):
                            pro = trans[m.start():]
                            pro_len = len(pro)
                            if pro_len >= min_pro_len:
                                if pro_len > longest_pro[0]:
                                    longest_pro = (pro_len, pro)
                                elif not only_save_longest:
                                    r = SeqRecord.SeqRecord(pro, id=record.id,
                                        description=record.description+' translation - frame {0}'%(frame*strand))
                                    fas_handle.write(r.format('fasta'))
                    if longest_pro[1] is not None:
                        r = SeqRecord.SeqRecord(longest_pro[1], id=record.id,
                            description=record.description+' translation')
                        fas_handle.write(r.format('fasta'))
