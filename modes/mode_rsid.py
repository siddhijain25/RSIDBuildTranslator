import pandas as pd
import sqlite3


def run(args):
    """Handles Mode "rsid" logic."""
    df = pd.read_csv(args.input)
    gtex_file =sqlite3.connect("data/GTEX_v10.sqlite")