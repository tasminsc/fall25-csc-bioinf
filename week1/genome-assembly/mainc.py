from dbgc import DBG
from utilsc import read_data
import os


def join_path(a: str, b: str) -> str:
    if a.endswith("/"):
        return a + b
    else:
        return a + "/" + b


if __name__ == "__main__":
    argv = os.sys.argv
    if len(argv) < 2:
        print("Usage: codon run mainc.py <data_folder>")
        raise SystemExit(1)

    # Read data
    data_folder = join_path("./genome-assembly/", argv[1])
    short1, short2, long1 = read_data(data_folder)

    k = 25
    dbg = DBG(k=k, data_list=[short1, short2, long1])

    total_len = 0
    contiglist = []

    # Write contigs to FASTA
    output_file = join_path(data_folder, "contig.fasta")
    with open(output_file, "w") as f:
        for i in range(20):
            c = dbg.get_longest_contig()
            
            if c == "":  # empty string means no contig
                break
            #print(i, len(c))
            total_len += len(c)
            contiglist.append(len(c))
            f.write(f">contig_{i}\n")
            f.write(f"{c}\n")

    # Compute N50
    if contiglist:
        contiglist.sort(reverse=True)
        tracker = 0
        for length in contiglist:
            tracker += length
            if tracker >= total_len / 2:
                print(length)
                break



