import pandas as pd
import sqlite3
from cli import logger


def run(args):
    """Handles Mode "rsid" logic."""
    try:
        df = pd.read_csv(args.input)
        logger.info("Input file read successfully.")
    except Exception as e:
        logger.error(f"An error has occured: {e}")
    try:
        gtex_file =sqlite3.connect("data/GTEX_v10.sqlite")
        logger.info("GTEx database read successfully.")
    except Exception as e:
        logger.error(f"An error has occured: {e}")
    