import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt

exp_file = "data/exp.data.txt"


def load_file(fname):
    expmat = np.loadtxt(fname)
    return expmat


def get_PCs(data, npcs):
    U, svals, _ = svd(data)
    evals = [s**2 for s in svals]
    tot_var = sum(evals)
    evals = evals[:npcs]
    pve = [evals[i]/tot_var for i in range(len(evals))]
    return U[:, :npcs], pve[:npcs]


def get_loadings(data, pcs):
    return np.matmul(np.transpose(data), pcs)


def create_scree_plot(pve):
    plt.scatter(np.array(range(len(pve)))+np.ones(len(pve), dtype=int), pve*100)
    plt.xlabel('PCs')
    plt.ylabel('PVE')
    plt.savefig('./plots/scree.png')


def main():
    expmat = load_file(exp_file)
    U, pve = get_PCs(expmat, 30)
    np.savetxt("expressionPCs_1_30.txt", U)
    create_scree_plot(pve)
    loadings = get_loadings(expmat, U)
    np.savetxt("loadings_1_30.txt", loadings)


if __name__=="__main__":
    main()
