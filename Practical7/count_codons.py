import matplotlib.pyplot as plt
from collections import Counter
import os

def read_fasta(filename):
    """Read FASTA file and return gene dictionary"""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Error: File not found - {filename}")
    
    genes = {}
    gene_name = None
    sequence = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if gene_name:
                    genes[gene_name] = ''.join(sequence)
                gene_name = line[1:].split()[0]
                sequence = []
            else:
                sequence.append(line)
        if gene_name:
            genes[gene_name] = ''.join(sequence)
    return genes

def get_longest_orf_codons(sequence, target_stop):
    """Extract codons from the longest ORF ending with target stop codon"""
    stop_codons = {'TAA', 'TAG', 'TGA'}
    best_codon_list = []
    max_orf_length = 0
    start_positions = [i for i in range(len(sequence)-2) if sequence[i:i+3] == 'ATG']
    
    for start in start_positions:
        codons = []
        found_stop = None
        
        for i in range(start, len(sequence)-2, 3):
            current_codon = sequence[i:i+3]
            if current_codon in stop_codons:
                found_stop = current_codon
                break
            codons.append(current_codon)
        
        if found_stop == target_stop:
            if len(codons) > max_orf_length:
                max_orf_length = len(codons)
                best_codon_list = codons
    return best_codon_list

# Main execution
if __name__ == "__main__":
    # 👇 这里直接写死了你电脑的完整绝对路径，不用改！
    fasta_file = r"C:\Users\23321\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    
    # Get valid stop codon from user
    target_stop = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
    while target_stop not in {'TAA', 'TAG', 'TGA'}:
        target_stop = input("Please enter valid codon (TAA/TAG/TGA): ").strip().upper()
    
    # Read genes and collect codons
    genes = read_fasta(fasta_file)
    all_codons = []
    for seq in genes.values():
        codons = get_longest_orf_codons(seq, target_stop)
        all_codons.extend(codons)
    
    # Count codon frequency
    codon_count = Counter(all_codons)
    
    # Print results
    print(f"\nCodon counts upstream of {target_stop}:")
    for codon, count in sorted(codon_count.items()):
        print(f"{codon}: {count}")
    
    # Generate pie chart
    labels = list(codon_count.keys())
    sizes = list(codon_count.values())
    
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
    plt.title(f'Codon Distribution Upstream of {target_stop}', fontsize=14)
    plt.tight_layout()
    # 👇 饼图会直接保存在Practical7文件夹里
    plt.savefig(r"C:\Users\23321\Desktop\IBI\IBI1_2025-26\IBI1_2025-26\Practical7\codon_pie.png", dpi=300, bbox_inches='tight')
    plt.close()
    
    print("\nPie chart saved successfully as 'codon_pie.png'")