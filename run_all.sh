#!/usr/bin/env bash
set -e

# Install dependencies (optional, for fresh environments)
# pip install -r requirements.txt

# Run the workflow via Snakemake
snakemake -s workflow/Snakefile --cores 1