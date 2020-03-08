import numpy as np

snpfile = "/work-zfs/abattle4/lab_data/GTEx_v8_eqtl_practice/matrix_eqtl/Whole_Blood.v8.snp_location.chr10.txt"
snplocs = np.loadtxt(snpfile, dtype=int, skiprows=1, usecols=2)
snplocs = np.array(snplocs)

genefile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/data/chr10genelocs.txt"
genelocs = np.loadtxt(genefile, dtype=int, skiprows=1, usecols=(2,3))
genelocs = np.array(genelocs)

generanges = np.zeros(genelocs.shape)
generanges[:, 0] = genelocs[:, 0] - 1e6
generanges[:, 0] = [i if i>=1 else 1 for i in genelocs[:,0]]  # i think they use one-indexing?

chr10len = 133797422
generanges[:, 1] = genelocs[:, 1] + 1e6
generanges[:, 1] = [i if i<=chr10len else chr10len for i in genelocs[:,1]]

snpcount = np.zeros(len(generanges), dtype=int)
startSNP = 0
for i in range(len(generanges)):
    print("STARTSNP is %d" % startSNP)
    g = generanges[i]
    print("Gene %d runs from %d to %d " % (i, g[0], g[1]))
    for j in range(len(snplocs[startSNP:])):
        snploc = snplocs[j]
        if snploc < g[0]:
            startSNP = j
        elif g[0] <= snploc < g[1]:
            snpcount[i] += 1
            print("FOUND SNP FOR GENE %d")
        else:
            break

np.savetxt("snpcounts.chr10.txt", snpcount, fmt="%d")
