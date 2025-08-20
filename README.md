# Variant Annotation Pipeline

## Overview

This repository contains an automated annotation pipeline for processing human VCF files using multiple annotation tools, listed below:

* **ANNOVAR**
* **SnpEff**
* **Ensembl VEP**
* **BCFtools/csq**
* **FATHMM-MKL**

The pipeline (five_tools.py) was developed to evaluate variant annotations from curated ClinVar and OMIM datasets, especially for SNVs which are related to Mendelian and complex disorders. The files can be found in this GitHub page above, named Clinvar_SNVs.vcf.gz and OMIM_SNVs.vcf.gz.

---

## Dependencies

Please make sure that the following tools are installed and accessible:

* `perl` (for ANNOVAR)
* `python ≥ 3.8`
* `java ≥ 8` (for SnpEff)
* `bcftools ≥ 1.9`
* `samtools`
* `tabix`
* [ANNOVAR](http://www.openbioinformatics.org/annovar/)
* [SnpEff](https://pcingola.github.io/SnpEff/)
* [Ensembl VEP](https://www.ensembl.org/info/docs/tools/vep/index.html)
* [FATHMM-MKL](http://fathmm.biocompute.org.uk/fathmmMKL.htm)

---

## Setting up your Environment

It is recommended to run this pipeline in a conda environment (especially for VEP) to manage tool dependencies and avoid any errors and conflicts:

```bash
conda create -n variant_env python=3.10
conda activate variant_env
conda install -c bioconda ensembl-vep bcftools samtools
```

Also, please make sure that the following tools are downloaded manually and placed in your home directory:

```bash
~/annovar/
~/snpEff/
~/fathmm-MKL/
```

---

## Directory Structure

Your directory should be structured like this:

```
/home/user/
├── annovar/
├── snpEff/
├── fathmm-MKL/
├── input.vcf
└── five_tools.py
```

## Usage

To run the pipeline, simply call the following from the command line:

```bash
python five_tools.py /full/path/to/input.vcf
```

This will sequentially run:

1. ANNOVAR annotation
2. SnpEff annotation
3. Ensembl VEP annotation
4. BCFtools/csq annotation
5. FATHMM-MKL prediction

---

## Output

The following output annotated files will be generated in your working directory:

* `output_annovar.hg38_multianno.txt`
* `output_vep.vcf`
* `output_bcftools_csq.vcf`
* `output_predictions.txt` (for FATHMM-MKL)

---


## License

This project is for academic and research use only. Please cite the original tools (ANNOVAR, SnpEff, VEP, etc.) in any publications.

---

## Contact

Developed by: **Martina**
GitHub: [@marti-dotcom](https://github.com/marti-dotcom)

---
