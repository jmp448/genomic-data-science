import numpy as np
from scipy.linalg import svd

exp_file = "data/exp.data.txt"


def load_file(fname):
    expmat = np.loadtxt(exp_file)
    return expmat


def get_PCs(data, npcs):
    U, _, _ = svd(expmat, full_matrices=F)
    return U[:, :npcs]


def get_loadings(data, pcs):
    return np.matmul(data, pcs)


def main():
    expmat = load_file(exp_file)
    expmat = np.transpose(expmat)  # I want it to be samples x genes
    U = get_PCs(expmat, 20)
    np.savetxt("expressionPCs_1_20.txt", U)
    loadings = get_loadings(expmat, U)
    np.savetxt("loadings_1_20.txt", loadings)


if __name__=="__main__":
    main()
