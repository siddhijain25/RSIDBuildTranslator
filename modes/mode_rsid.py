import pandas as pd
import sqlite3
from cli import logger
from utils import read_input_file


def run(args):
    """Handles Mode "rsid" logic."""

    input_data = read_input_file(args.input)
    
    cursor = conn.cursor()
    cursor.execute(query, rsid_batch)
    results = cursor.fetchall()
    conn.close()