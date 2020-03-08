import numpy as np

def bh_all_combos():
    snpfile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/q3.cis.eqtl.txt"
    pvals = np.array(np.loadtxt(snpfile, skiprows=1, usecols=4))
    pvals = np.sort(pvals)
    ranks = range(1, len(pvals)+1)
    fdr = 0.05
    nSNPcands = 3661543
    bh = (ranks/nSNPcands)*fdr
    assert(len(pvals) == len(bh))
    for i in range(len(bh)):
        if pvals[len(bh)-1-i] < bh[len(bh)-1-i]:
            print("%d eQTL's identified" % len(bh)-1-i)


def main():
    bh_all_combos()


if __name__=="__main__":
    main()
