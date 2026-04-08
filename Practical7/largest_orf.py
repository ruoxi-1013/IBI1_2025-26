seq = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"
def find_longest_orf(seq):
    start_codon="AUG"
    stop_codon={"UAA","UAG","UGA"}
    max_len=0
    longest_orf=""
    for i in range(len(seq)-2):
        if seq[i:i+3]==start_codon:
            for j in range(i,len(seq)-2,3):
                codon=seq[j:j+3]
                if codon in stop_codon:
                    orf_seq=seq[i:j+3]
                    orf_len=len(orf_seq)
                    if orf_len>max_len:
                        max_len=orf_len
                    break
    return max_len
length=find_longest_orf(seq)
print("Length of longest ORF (nucleotides):",length)