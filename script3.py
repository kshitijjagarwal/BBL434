import sys

def count_fasta_records(filename):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(">"):
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_fasta_records.py <multi_fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    num_records = count_fasta_records(fasta_file)

    print(f"Number of FASTA records: {num_records}")
