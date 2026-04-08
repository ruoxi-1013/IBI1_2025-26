import os

def parse_fasta(filename):
    genes = []
    current_header = ""
    current_seq = ""

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_header:
                    genes.append((current_header, current_seq))
                current_header = line
                current_seq = ""
            else:
                current_seq += line
        if current_header:
            genes.append((current_header, current_seq))
    return genes

def has_in_frame_stop(seq):
    stop_codons = {"TAA", "TAG", "TGA"}
    found_stops = set()
    for j in range(0, len(seq) - 2, 3):
        codon = seq[j:j+3]
        if codon in stop_codons:
            found_stops.add(codon)
    if found_stops:
        return True, sorted(list(found_stops))
    return False, []

def main():
    input_fa = r"C:\Users\23321\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fa = r"C:\Users\23321\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\stop_genes.fa"

    print(f"Input file path: {input_fa}")
    print(f"File exists: {os.path.exists(input_fa)}")
    if not os.path.exists(input_fa):
        print("ERROR: File not found! Please check your file path.")
        return

    genes = parse_fasta(input_fa)
    print(f"Successfully loaded {len(genes)} sequences")

    with open(output_fa, 'w') as out:
        count = 0
        for header, seq in genes:
            has_stop, stops = has_in_frame_stop(seq)
            if has_stop:
                gene_name = header.split()[0][1:]
                stop_str = ",".join(stops)
                new_header = f">{gene_name} stop_codons:{stop_str}"
                out.write(new_header + "\n")
                out.write(seq + "\n")
                count += 1
    print(f"Task completed! {count} sequences with in-frame stop codons saved to {output_fa}")

if __name__ == "__main__":
    main()