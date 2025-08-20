"""
Variant Annotation Software Tools Automated Pipeline

Author: Martina Debnath
GitHub: https://github.com/marti-dotcom
License: MIT
"""
__author__ = "Martina Debnath"
__version__ = "1.0.0"
__license__ = "MIT"

import subprocess
import os
import sys

def run_command(command):
    print(f"Running: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"An error has occurred: {e.stderr.decode()}")
        sys.exit(1)

def run_annovar(input_vcf, output_prefix):
    annovar_path = "/home/martina/annovar"
    humandb_path = "/home/martina/annovar/humandb"

    annovar_command = [
        "perl", f"{annovar_path}/table_annovar.pl", input_vcf, humandb_path,
        "-buildver", "hg38", "-out", output_prefix, "-remove", "-protocol", "refGene,gnomad211_exome",
        "-operation", "g,f", "-nastring", ".", "-vcfinput"
    ]
    run_command(annovar_command)

def run_snpeff(input_vcf):
    snpeff_path = "/home/martina/snpEff"
    genome_version = "GRCh38.86"

    snpeff_command = [
        "java", "-Xmx4g", "-jar", f"{snpeff_path}/snpEff.jar", genome_version, input_vcf
    ]
    run_command(snpeff_command)

def run_vep(input_vcf, output_vcf):
    vep_command = [
        "vep",
        "-i", input_vcf,
        "-o", output_vcf,
        "--vcf",
        "--cache",
        "--offline",
        "--species", "homo_sapiens",
        "--assembly", "GRCh38",
        "--force_overwrite"
    ]
    run_command(vep_command)

def run_bcftools_csq(input_vcf, output_vcf):
    fasta = "/home/martina/clinvar_project/reference/Homo_sapiens.GRCh38.dna.primary_assembly.fa"
    gff3 = "/home/martina/Homo_sapiens.GRCh38.113.gff3"
    fai = fasta + ".fai"

    for path in [input_vcf, fasta, fai, gff3]:
        if not os.path.exists(path):
            print(f"[ERROR] Required file not found: {path}")
            sys.exit(1)

    bcftools_command = [
        "bcftools", "csq",
        "-f", fasta,
        "-g", gff3,
        "-o", output_vcf,
        input_vcf
    ]
    run_command(bcftools_command)

def run_fathmm(input_vcf):
    converter_script = "/home/martina/fathmm-MKL/vcf_to_fathmm_input.py"
    input_txt = "/home/martina/fathmm-MKL/omim_fathmm_input.txt"
    output_txt = "/home/martina/fathmm-MKL/output_predictions.txt"
    fathmm_script = "/home/martina/fathmm-MKL/fathmm-MKL.py"
    fathmm_db = "/home/martina/fathmm-MKL/fathmm-MKL_Current.tab.gz"

    # Convert VCF to FATHMM input format
    run_command(["python", converter_script, input_vcf, input_txt])

    # Run FATHMM-MKL
    run_command(["python", fathmm_script, input_txt, output_txt, fathmm_db])

def main(input_vcf):
    print("Running ANNOVAR annotation...")
    run_annovar(input_vcf, "output_annovar")

    print("Running SnpEff annotation...")
    run_snpeff(input_vcf)

    print("Running VEP annotation...")
    run_vep(input_vcf, "output_vep.vcf")

    print("Running BCFtools csq annotation...")
    run_bcftools_csq(input_vcf, "output_bcftools_csq.vcf")

    print("Running FATHMM-MKL annotation...")
    run_fathmm(input_vcf)
#output for FATHMM-MKL found in : output_predictions.txt
    print("Annotation pipeline completed. YAY!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} input.vcf")
        sys.exit(1)

    input_vcf = sys.argv[1]
    main(input_vcf)
