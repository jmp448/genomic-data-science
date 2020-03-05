import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt

exp_file = "data/exp.data.txt"


def load_file(fname):
    expmat = np.loadtxt(exp_file)
    return expmat


def get_PCs(data, npcs):
    U, svals, _ = svd(expmat)
    evals = [s**2 for s in svals]
    tot_var = sum(evals)
    pve = [evals[i]/tot_var for i in range(len(evals))]
    return U[:, :npcs], pve


def get_loadings(data, pcs):
    return np.matmul(data, pcs)


def create_scree_plot(pve):
    plt.plot(range(len(pve)), pve)
    plt.xlabel('PCs')
    plt.ylabel('PVE')
    plt.savefig('scree.png')


def main():
    expmat = load_file(exp_file)
    expmat = np.transpose(expmat)  # I want it to be samples x genes
    U, pve = get_PCs(expmat, 20)
    np.savetxt("expressionPCs_1_20.txt", U)
    create_scree_plot(pve)
    loadings = get_loadings(expmat, U)
    np.savetxt("loadings_1_20.txt", loadings)


if __name__=="__main__":
    main()
