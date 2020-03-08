import numpy as np
import csv


def main():
    files=["covs15.txt", "covs110.txt", "covs120.txt", "covs130.txt"]
    fout = ["ecov2.txt", "ecov3.txt", "ecov4.txt", "ecov5.txt"]
    for f in range(len(files)):
        t = np.loadtxt(files[f], dtype="str")
        t2 = np.transpose(t)
        with open(fout[f], 'wt') as out_file:
            tsv_writer = csv.writer(out_file, delimiter='\t')
            for r in t2:
                tsv_writer.writerow(r)


if __name__=="__main__":
    main()
