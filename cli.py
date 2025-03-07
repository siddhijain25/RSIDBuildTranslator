import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        prog="RSIDBuildTranslator",
        description="'Add chromosome and position for GRCh37 and GRCh38 based on rsIDs, or add rsIDs based on chromosome and position from either build."
    )
    # Define expected arguments
    parser.add_argument(
        "-m",
        "--mode",
        choices=["rsid", "chrpos37", "chrpos38"],
        help="Mode of operation: rsid or chrpos37 or chrpos38 (Based on what you have available in your dataset)",
        required=True
    )
    parser.add_argument("-i", "--input", help="Input file with path", required=True)
    parser.add_argument(
        "-o", "--output", help="Name of output file with path", required=True
    )
    parser.add_argument(
        "-d", "--database", help="Name of database to use (gtex or ukb)", required=True
    )
    return parser