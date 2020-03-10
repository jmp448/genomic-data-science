import numpy as np

def bh_all_combos():
    qtlfile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/q3.cis.eqtl.txt"
    pvals = np.array(np.loadtxt(qtlfile, skiprows=1, usecols=4))
    pvals = np.sort(pvals)
    ranks = np.zeros(len(pvals), dtype=int)
    ranks[0] = 1
    for i in range(1, len(pvals)):
        if pvals[i] = pvals[i-1]:
            ranks[i] = ranks[i-1]
        else:
            ranks[i] = ranks[i-1]+1
    fdr = 0.05
    nSNPcands = 3663907
    bh = [(r/nSNPcands)*fdr for r in ranks]
    assert(len(pvals) == len(bh))
    for i in range(len(bh)):
        pos=len(bh)-1-i
        if pvals[pos] < bh[pos]:
            print("%d eQTL's identified" % (pos+1))
            found=True
            return
    print("0 eQTL's identified")

def gene_to_ncands():
    gene_names =
    snp_counts = np.array(np.loadtxt(qtlfile, skiprows=1, usecols=4))
    return dict(gene_names, snp_counts)

def bonferroni_bh(gene2count):
    qtlfile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/q3.cis.eqtl.txt"
    pvals = np.sort(pvals)



def main():
    # bh_all_combos()
    gene2count = gene_to_ncands()
    bonferroni_bh(gene2count)


if __name__=="__main__":
    main()
