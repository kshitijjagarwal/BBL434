import sys

def get_fasta_seq_length(filename):
    seq = ""
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return len(seq)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python seq_length.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    length = get_fasta_seq_length(fasta_file)
    print(f"Sequence length: {length}")
