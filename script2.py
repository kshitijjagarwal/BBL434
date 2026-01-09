import sys

def read_fasta(filename):
    seq = ""
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq

def count_kmers(seq, k):
    kmers = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python kmer_count.py <fasta_file> <k>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    k = int(sys.argv[2])

    sequence = read_fasta(fasta_file)
    kmer_dict = count_kmers(sequence, k)

    print(kmer_dict)
