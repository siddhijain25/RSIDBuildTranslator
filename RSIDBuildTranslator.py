#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="'Add chromosome and position for GRCh37 and GRCh38 based on rsIDs, or add rsIDs based on chromosome and position from either build."
    )
    # Define expected arguments
    parser.add_argument(
        "-m",
        "--mode",
        help="Mode of operation: rsid or chrpos37 or chrpos38 (Based on what you have available in your dataset)",
        required=True,
    )
    parser.add_argument("-i", "--input", help="Input file with path", required=True)
    parser.add_argument(
        "-o", "--output", help="Name of output file with path", required=True
    )
    parser.add_argument(
        "-d", "--database", help="Name of database to use (gtex or ukb)", required=True
    )

    # Define arguments required conditionally based on mode
    parser.add_argument("-rs", "--rsid_col", help="Name of column with rsids")

    parser.add_argument(
        "-chr37", "--chr_col_b37", help="Name of column with chromosome in build GRCh37"
    )
    parser.add_argument(
        "-pos37", "--pos_col_b37", help="Name of column with position in build GRCh37"
    )
    parser.add_argument(
        "-chr38", "--chr_col_b38", help="Name of column with chromosome in build GRCh38"
    )
    parser.add_argument(
        "-pos38", "--pos_col_b38", help="Name of column with position in build GRCh38"
    )
    args = parser.parse_args()

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
