
1. Figuring out how to calculate N50
- Initially, I was confused by the difference by NGA50 and N50 (I thought we had to calculate NGA50). I calculated my numbers by adding the contig length, dividing the sum by 2, and then iterating through the contigs until sum/2 was surpassed. I also had to alter my recursion limit, but had problems with that (apparently, the settings on my Mac do not have a high enough recursion limit), and Google advised me not to increase the hard limit manually. Because of this, I'm actually not sure if my data4 N50 is correct. 

2. I was not able to run the datasets using codon (unless something changes before the due date). I first created new files dbgc.py, mainc.py to try and run codon in. I then changed libraries in these files according to the Codon handbook that was provided (https://docs.exaloop.io/integrations/python/python-from-codon/?h=matplotlib#import-python-modules-in-codon). Then, I started having errors with the typesetting of my Node. They looked something like this: 

dict.codon:8 (9-23): error: 'NoneType' object has no attribute '__hash__'
├─ dict.codon:258 (17-27): error: during the realization of _dict_hash(key: NoneType)
├─ dict.codon:88 (16-33): error: during the realization of _kh_get(self: Dict[NoneType,NoneType], key: NoneType)
├─ dbgc.py:79 (12-37): error: during the realization of __contains__(self: Dict[NoneType,NoneType], key: NoneType)
├─ dbgc.py:88 (16-37): error: during the realization of _add_node(self: DBG[int,Dict[NoneType,NoneType],int,Dict[NoneType,NoneType]], kmer: str)
├─ dbgc.py:65 (21-92): error: during the realization of _add_arc(self: DBG[int,Dict[NoneType,NoneType],int,Dict[NoneType,NoneType]], kmer1: str, kmer2: str)
├─ dbgc.py:53 (9-31): error: during the realization of _build(self: DBG[int,Dict[NoneType,NoneType],int,Dict[NoneType,NoneType]], data_list: List[List[str]])
╰─ mainc.py:14 (11-54): error: during the realization of __init__(self: DBG[int,Dict[NoneType,NoneType],int,Dict[NoneType,NoneType]], k: int, data_list: List[List[str]])

OR:

dbgc.py:86 (13-53): error: 'Node[Set[int],int,int,str,Optional[NoneType],bool]' does not match expected type 'Node[NoneType,NoneType,NoneType,NoneType,NoneType,NoneType]'
├─ dbgc.py:93 (16-37): error: during the realization of _add_node(self: DBG[int,Dict[str,int],int,Dict[int,Node[NoneType,NoneType,NoneType,NoneType,NoneType,NoneType]]], kmer: str)
├─ dbgc.py:69 (21-92): error: during the realization of _add_arc(self: DBG[int,Dict[str,int],int,Dict[int,Node[NoneType,NoneType,NoneType,NoneType,NoneType,NoneType]]], kmer1: str, kmer2: str)
├─ dbgc.py:57 (9-31): error: during the realization of _build(self: DBG[int,Dict[str,int],int,Dict[int,Node[NoneType,NoneType,NoneType,NoneType,NoneType,NoneType]]], data_list: List[List[str]])
╰─ mainc.py:14 (11-54): error: during the realization of __init__(self: DBG[int,Dict[str,int],int,Dict[int,Node[NoneType,NoneType,NoneType,NoneType,NoneType,NoneType]]], k: int, data_list: List[List[str]])

- I was unfortunately not able to figure this error out. I used AI (ChatGPT, Sep 15 ver.) to troubleshoot and it suggested I typeset attributes of the Node class, defining the Node class as non-generic, and resetting the cache. I tried all of these, and they did not work. I decided to move on to step 3 and try to format the files so I could at least get some partial marks.

3. I created a bash file, and used the Biostar handbook as orientation. I tried to code a bit in bash, then asked AI (ChatGPT, Sep 16 ver.) to help me write a bash script I was unfamiliar with due to the difference in language. Then, I was having errors with my bash debugger where each line of input was printed. I could not find a reason for this on Google, but I then realized that the -x in the "set -euxo pipefail" line may have caused the problem. I could not find a way to fix the formatting otherwise, so I deleted the "x" in -euxo. Now I have -euo, but my output looks the way I want it to. 


BONUS:

I think these are the organisms which each dataset belongs to. I used the BLAST database and the first sequence in the long.fasta file to search them up!

data1: Porphyromonas gingivalis (gram-negative bacteria)
data2: Porphyromonas gingivalis (same as data1)
data3: Parabacteroides distasonis (gram-negative bacteria)
data4: Lacrimispora saccharolytica (bacteria)

