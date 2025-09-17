from dbgc import DBG
from utils import read_data
from python import sys
from python import os

sys.setrecursionlimit(1000000)


if __name__ == "__main__":
    argv = sys.argv
    short1, short2, long1 = read_data(os.path.join('./', argv[1]))

    k = 25
    dbg = DBG(k=k, data_list=[short1, short2, long1])
    # dbg.show_count_distribution()
    sum = 0
    contiglist = []
    with open(os.path.join('./', argv[1], 'contig.fasta'), 'w') as f:
        for i in range(20):
            c = dbg.get_longest_contig()
            if c is None:
                break
            print(i, len(c))
            sum += len(c)
            contiglist.append(len(c))
            f.write('>contig_%d\n' % i)
            f.write(c + '\n')
        tracker = 0
        contigf = 0
        for length in contiglist:
            if ((tracker + length) > sum/2):
                print('N50: '+ str(length))
                break
            else:
                tracker+=length


