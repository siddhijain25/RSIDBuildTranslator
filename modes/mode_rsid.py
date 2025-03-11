import pandas as pd
import sqlite3
from cli import logger
from utils import read_input_file, load_gtex_data, get_query
import re


def run(args):
    """Handles Mode "rsid" logic."""

    input_data = read_input_file(args.input)

    input_data.columns = [
        re.sub(r"[^a-zA-Z0-9\_ ]", "", col) for col in input_data.columns
    ]
    ids_to_search = input_data[args.rsid_col].tolist()

    # Load database safely
    with load_gtex_data() as gtex_con:
        if gtex_con:
            gtex_cur = gtex_con.cursor()

            # Construct and execute query safely
            query = get_query("GTEx_lookup", ids_to_search, "rsid_dbSNP155")
            gtex_cur.execute(query, ids_to_search)
            results = gtex_cur.fetchall()

    for row in results:
        print(row)
