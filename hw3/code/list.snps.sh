#!/bin/bash

parent="/work-zfs/abattle4/lab_data/GTEx_v8_trans_eqtl_data_processed_by_brian/processed_genotypes"

files={
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr10_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr11_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr12_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr13_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr14_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr15_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr16_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr17_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr18_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr19_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr1_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr20_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr21_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr22_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr2_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr3_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr4_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr5_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr6_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr7_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr8_dosage_MAF_05.txt",
  $parent"GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr9_dosage_MAF_05.txt"
}

for fname in files
do
  if [ "${fname}" == "GTEx_Analysis_2017-06-05_v8_WholeGenomeSeq_838Indiv_chr10_dosage_MAF_05.txt" ]
  then
    cat ${fname} > all.snps.txt
  else
    nrow={awk 'END {print NR}' ${fname} }
    tail -n $(($nrow-1)) ${fname} >> all.snps.txt
  fi
done
