import numpy as np

exp_file = "exp.data.txt"


def load_file(fname):
    expmat = np.loadtxt(exp_file)
    genes = expmat[1:, 0]
    inds = expmat[0,1:]
    expmat = expmat[1:,1:]
    return inds, genes, expmat


def main():
    expmat, genes, inds = load_file(exp_file)
    print(expmat[0,:])
    print(genes)
    print(inds)


if __name__=="__main__":
    main()
