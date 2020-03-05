import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt

exp_file = "data/exp.data.txt"


def load_file(fname):
    expmat = np.loadtxt(exp_file)
    return expmat


def get_PCs(data, npcs):
    U, svals, _ = svd(data)
    evals = [s**2 for s in svals]
    tot_var = sum(evals)
    pve = [evals[i]/tot_var for i in range(len(evals))]
    return U[:, :npcs], pve[:npcs]


def get_loadings(data, pcs):
    return np.matmul(np.transpose(data), pcs)


def create_scree_plot(pve):
    plt.scatter(range(len(pve)), pve)
    plt.xlabel('PCs')
    plt.ylabel('PVE')
    plt.savefig('scree.png')


def main():
    expmat = load_file(exp_file)
    U, pve = get_PCs(expmat, 30)
    np.savetxt("expressionPCs_1_30.txt", U)
    create_scree_plot(pve)
    loadings = get_loadings(expmat, U)
    np.savetxt("loadings_1_30.txt", loadings)


if __name__=="__main__":
    main()
