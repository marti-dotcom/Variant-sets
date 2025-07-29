# Variant sets
ClinVar and OMIM SNV sets

This repository contains curated datasets extracted from ClinVar of single nucleotide variants (SNVs) of OMIM and ClinVar. These datasets serve as benchmarks for evaluating variant annotation tools in the context of Mendelian and complex disorders. 

## Dependencies

This tool requires the following tools to be installed and accessible in your environment:

- ANNOVAR
- Ensembl VEP
- SnpEff
- BCFtools
- FATHMM-MKL

## Setting up environment

It would be recommended to run this in a Conda environment, to allow VEP annotation tool to run:

```bash
conda create -n variant_env python=3.10



Please also make sure that ANNOVAR, SnpEff, and FATHMM-MKL are downloaded and configured in your working directory:

~/annovar/
~/snpEff/
~/fathmm-MKL/


## Directory Structure

You should place files as follows:

- VCF input: `/home/user/your_file.vcf`
- ANNOVAR: `/home/user/annovar/`
- SnpEff: `/home/user/snpEff/`
- FATHMM-MKL: `/home/user/fathmm-MKL/`

The output files will be written to the same working directory.
