import numpy as np

# load snp file
snpfile = "/work-zfs/abattle4/lab_data/GTEx_v8_eqtl_practice/matrix_eqtl/Whole_Blood.v8.snp_location.chr10.txt"
snplocs = np.loadtxt(snpfile, dtype=int, skiprows=1, usecols=2)
snplocs = np.array(snplocs)

# select from this array only the snps that passed the MAF threshold
maf_file = open("snps.passed", "r")
fl = maf_file.readlines()
maf_snps = [f.strip() for f in fl[1:]]

allsnp_file = open(snpfile, "r")
fl = allsnp_file.readlines()
all_snps = [f.strip().split()[0] for f in fl[1:]]

assert(len(all_snps) == len(snplocs))
assert(len(maf_snps) == 339919)

_, inds, _ = np.intersect1d(all_snps, maf_snps, return_indices=True)
snplocs = np.take(snplocs, inds)

# load gene file
genefile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/data/chr10genelocs.txt"
genelocs = np.loadtxt(genefile, dtype=int, skiprows=0, usecols=(2,3))
genelocs = np.array(genelocs)

generanges = np.zeros(genelocs.shape)
generanges[:, 0] = genelocs[:, 0] - 1e6
generanges[:, 0] = [i if i>=1 else 1 for i in generanges[:,0]]  # i think they use one-indexing?

chr10len = 133797422
generanges[:, 1] = genelocs[:, 1] + 1e6
generanges[:, 1] = [i if i<=chr10len else chr10len for i in generanges[:,1]]

snpcount = np.zeros(len(generanges), dtype=int)
startSNP = 0
for i in range(len(generanges)):
    g = generanges[i]
    for j in range(startSNP, len(snplocs)):
        snploc = snplocs[j]
        if snploc < g[0]:
            startSNP = j
        elif g[0] <= snploc <= g[1]:
            snpcount[i] += 1
        else:
            break

np.savetxt("snpcounts.chr10.maffiltered.txt", snpcount, fmt="%d")
