import pandas as pd
import sqlite3
from cli import logger


def read_input_file(path):
    try:
        df = pd.read_table(path, sep=None, engine="python")

        if df.empty:
            logger.warning(f"Input file '{path}' is empty.")
        elif len(df.columns) < 2:
            logger.warning(f"Input file '{path}' contains less than 2 columns.")
        else:
            logger.info(f"Input file '{path}' read successfully.")
        return df
    except Exception as e:
        logger.error(f"An error has occured while reading the input file: {e}")
        return None


def load_gtex_data():
    try:
        gtex_con = sqlite3.connect("data/GTEx_v10.db")
        # gtex_cur = gtex_con.cursor()
        logger.info("GTEx database read successfully.")
        return gtex_con  # , gtex_cur
    except Exception as e:
        logger.error(f"An error has occured while reading the GTEx database: {e}")
        return None  # , None


def get_query(table_name, ids_to_search, lookup_column):

    allowed_tables = {"GTEx_lookup"}
    allowed_lookup_columns = {"rsid_dbSNP155", "chrpos37", "chrpos38"}

    if table_name not in allowed_tables:
        raise ValueError(f"Invalid table name: {table_name}")
    if lookup_column not in allowed_lookup_columns:
        raise ValueError(f"Invalid column name: {lookup_column}")

    # Create the SQL query dynamically
    query = f"""
    SELECT * FROM {table_name}
    WHERE {lookup_column} IN ({', '.join(['?'] * len(ids_to_search))})
    """
    return query


def query_to_df(query, ids_to_search, cur, input_data, rsid_col, lookup_column):
    cur.execute(query, ids_to_search)
    columns = [desc[0] for desc in cur.description]
    results = []
    for value in cur.fetchall():
        tmp = {columns[index]: column for index, column in enumerate(value)}
        results.append(tmp)

    results_df = pd.DataFrame(results)

    final_df = pd.merge(
        input_data, results_df, how="left", left_on=rsid_col, right_on=lookup_column
    ).drop(columns=lookup_column)

    return final_df


# # # ###########
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
# # results = cursor.fetchall()
# # conn.close()


# columns = cursor.description
# result = []
# for value in cursor.fetchall():
#     tmp = {}
#     for index, column in enumerate(value):
#         tmp[columns[index][0]] = column
#     result.append(tmp)

# # Print the results
# for row in results:
#     print(row)
