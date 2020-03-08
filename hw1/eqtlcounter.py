import numpy as np

def bh_all_combos():
    snpfile = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/q3.cis.eqtl.txt"
    pvals = np.array(np.loadtxt(snpfile, skiprows=1, usecols=4))
    pvals = np.sort(pvals)
    ranks = range(1, len(pvals)+1)
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



def main():
    bh_all_combos()


if __name__=="__main__":
    main()
