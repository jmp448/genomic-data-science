import numpy as np

def get_qtl_data(cov):
    """
    Input: indicator of which covariates to use (cov1, cov2, ..., or cov5)
    Output: snps (list of str), genes (list of str), pvals (ndarray of float)
            can assume all three are in the same order
    """

    fname = "/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/matrixeqtl/cis.eqtl." + cov + ".txt"
    f = open(fname, 'r')
    lines=f.readlines()
    snps = []
    genes=[]
    for l in lines[1:]:
        snps.append(l.split('\t')[0])
        genes.append(l.split('\t')[1])
    f.close()
    pvals = np.array(np.loadtxt(qtlfile, skiprows=1, usecols=4))
    assert(len(snps) == len(genes))
    assert(len(genes) == len(pvals))
    return snps, genes, pvals


def get_SNPs_per_gene():
    """
    Input: none
    Output: dictionary of gene names (list of str) to snp counts per gene (ndarray of int, calculated by cisSNPSpergene.py)
    """
    # get list of gene names
    f = open("/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/data/chr10genelocs.txt", 'r')
    lines=f.readlines()
    genes=[]
    for l in lines:
        genes.append(l.split('\t')[0])
    f.close()

    # get list of snp counts per gene
    qtlfile="/home-2/jpopp4@jhu.edu/work/josh/genomic-data-science/hw1/data/chr10genelocs.txt"
    snp_counts = np.array(np.loadtxt(qtlfile), dtype=int)

    gene2snpcount = dict(zip(gene_names, snp_counts))
    return gene2snpcount


def count_bh_significant_snps(pvals, outfile, ntest, fdr=0.05):
    """
    Input: pvals (ndarray of floats), outfile (str), ntest (int), [fdr (float)]
    Output: file located at outfile will contain one line saying how many eqtl's are
            identified by Benjamini-Hochberg procedure at the given false discovery
            rate
    """
    pvals = np.sort(pvals)
    ranks = np.zeros(len(pvals), dtype=int)
    ranks[0] = 1
    increment = 1
    for i in range(1, len(pvals)):
        if pvals[i] == pvals[i-1]:
            ranks[i] = ranks[i-1]
            increment += 1
        else:
            ranks[i] = ranks[i-1]+increment
            increment = 1
    bh = [(r/ntest)*fdr for r in ranks]
    assert(len(pvals) == len(bh))
    fout = open(outfile, "w+"")
    for i in range(len(bh)):
        pos=len(bh)-1-i
        if pvals[pos] < bh[pos]:
            fout.write("%d eQTL's identified" % (pos+1))
            found=True
            return
    print("0 eQTL's identified")
    fout.close()


def bh_all_combos():
    snps, genes, pvals = get_qtl_data("cov1")
    count_bh_significant_snps(pvals, "qtlcount/all_combos.txt", 3663907)


def bh_gene_level(cov):
    gene2count = get_SNPs_per_gene()
    snps, genes, pvals = get_qtl_data(cov)
    for i in range(len(genes)):
        pvals[i] *= gene2count[genes[i]]  # bonferroni adjust
    # take top pval for each gene
    ordered = np.argsort(pvals)
    pvals = pvals[ordered]
    genes = genes[ordered]
    snps = snps[ordered]

    genes, uniq = np.unique(np.array(genes), return_index=True)
    pvals = [pvals[u] for u in uniq]
    snps = [snps[u] for u in uniq]

    outfile="qtlcount/"+cov+".txt"
    count_bh_significant_snps(pvals, outfile, 3663907)


def main():
    bh_all_combos()
    bh_gene_level("cov1")
    bh_gene_level("cov2")
    bh_gene_level("cov3")
    bh_gene_level("cov4")
    bh_gene_level("cov5")


if __name__=="__main__":
    main()
