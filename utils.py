import pandas as pd
import sqlite3
from cli import logger


def read_input_file(path):
    try:
        df = pd.read_table(path, sep=None, engine='python')
        
        if df.empty:
            logger.warning("Input file is empty.")
        elif len(df.columns) < 2:
            logger.warning("Input file contains less than 2 columns.")
        else:
            logger.info("Input file read successfully.")
        return df
    except Exception as e:
        logger.error(f"An error has occured while reading the input file: {e}")
        return None


def load_gtex_data():
    try:
        gtex_con = sqlite3.connect("data/GTEX_v10.db")
        gtex_cur = gtex_con.cursor()
        logger.info("GTEx database read successfully.")
        return gtex_con, gtex_cur
    except Exception as e:
        logger.error(f"An error has occured while reading the GTEx database: {e}")
        return None, None


def get_query(database, ids_to_search, lookup_column):
    # Create the SQL query dynamically
    query = f"""
    SELECT * FROM {database} 
    WHERE {lookup_column} IN ({', '.join(['?']*len(ids_to_search))})
    """
    return query


# ###########
# import sqlite3

# # Connect to the database (replace 'GTEX_file.db' with your actual database path)
# conn = sqlite3.connect("GTEx_v10.db")

# # Sample list of RSIDs (same as `rsid_batch` in R)
# rsid_batch = ["rs554008981", "rs28507908", "rs1557427439"]

# # Create the SQL query dynamically
# query = f"""
# SELECT * FROM GTEx_lookup
# WHERE rsid_dbSNP155 IN ({', '.join(['?']*len(rsid_batch))})
# """
# cursor = conn.cursor()
# cursor.execute(query, rsid_batch)
# results = cursor.fetchall()
# conn.close()

# # Print the results
# for row in results:
#     print(row)
