from Bio import SeqIO
from Bio import SeqRecord

gbk_filename = "sequences/NC_000207-3.gbk"
fas_filename = "sequences/NC_000207-3_translated.fasta"
table = 1
min_pro_len = 1
only_save_longest = True

with open(gbk_filename, 'r') as gb_handle:
    with open(fas_filename, 'w') as fas_handle:
        for record in SeqIO.parse(gb_handle, "genbank"):
            for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
                for frame in range(3):
                    length = 3 * ((len(record) - frame) // 3)  # Multiple of three
                    longest_pro = (0, None)
                    for pro in nuc[frame:frame + length].translate(table).split("*"):
                        pro_len = len(pro)
                        if pro_len >= min_pro_len:
                            if pro_len > longest_pro[0]:
                                longest_pro = (pro_len, pro)
                            elif not only_save_longest:
                                r = SeqRecord.SeqRecord(pro, id=record.id, description=record.description+' translation')
                                fas_handle.write(r.format('fasta'))
                    if longest_pro[1] is not None:
                        r = SeqRecord.SeqRecord(longest_pro[1], id=record.id, description=record.description + ' translation')
                        fas_handle.write(r.format('fasta'))
