# RSIDBuildTranslator

RSIDBuildTranslator is a tool that annotates genetic data with rsIDs, chromosome, and position from GRCh37 or GRCh38, using whichever is available in your data. The database used in this tool is based on GTEx v10 whole genome sequencing variants from 953 individuals, and has a coverage of roughly 48.5M variants. 

This tool can be used on tabular data; for example GWAS summary statistics. 

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)



## Installation

The latest version can be installed using pip, and requires Python version >=3.12.

`pip install RSIDBuildTranslator`

## Usage

Once installed, you can call the program from the command line for viewing all options available.

`RSIDBuildTranslator -h`

RSIDBuildTranslator can be run using 3 different modes; **rsid**, **chrpos37**, and **chrpos38**, dependent on what you have available in your dataframe. For mode specific options you can use the following commands:

```
RSIDBuildTranslator rsid -h

RSIDBuildTranslator chrpos37 -h

RSIDBuildTranslator chrpos38 -h
```

### General options:

| Flag | Description |
|-|-|
| -h, --help | Use this flag to retrieve all options and help |
| -i, --input | The name of the input file, with the path to the file (if required).
| -o, --output | A name for the output file, with the path where you want to place it (if required).
| --exclude-ref-alt (default=False)| Use this flag if you would like to exclude printing the ref and alt alleles from the databse to your output file.

### Mode specific options:

**`rsid`**

| Flag | Description |
|-|-|
| -rs, --rsid_col | Name of the column with rsIDs in your dataframe.

**`chrpos37`**

| Flag | Description |
|-|-|
| -chr37 | Name of the column with chromosome number in build GRCh37 (hg19) in your dataframe.
| -pos37 | Name of the column with position in build GRCh37 (hg19) in your dataframe.

**`chrpos38`**

| Flag | Description |
|-|-|
| -chr38 | Name of the column with chromosome number in build GRCh38 (hg38) in your dataframe.
| -pos38 | Name of the column with position in build GRCh38 (hg38) in your dataframe.