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

Your directory should be structured as follows:

```
/home/user/
├── annovar/
├── snpEff/
├── fathmm-MKL/
├── input.vcf
└── vcf_annotation_tool.py
```

---

## Usage

To run the pipeline, simply call:

```bash
python vcf_annotation_tool.py /full/path/to/input.vcf
```

This will sequentially run:

1. ANNOVAR annotation
2. SnpEff annotation
3. Ensembl VEP annotation
4. BCFtools/csq annotation
5. FATHMM-MKL prediction

---

## Output

The following files will be generated in your working directory:

* `output_annovar.hg38_multianno.txt`
* `output_vep.vcf`
* `output_bcftools_csq.vcf`
* `output_predictions.txt` (FATHMM-MKL)

---

## Coming Soon

* Optional flags to toggle tools on/off
* Merged CSV summarizing all annotations per variant
* Web GUI for user uploads

---

## License

This project is for academic and research use only. Please cite the original tools (ANNOVAR, SnpEff, VEP, etc.) in any publications.

---

## Contact

Developed by: **Martina**
GitHub: [@marti-dotcom](https://github.com/marti-dotcom)

---
