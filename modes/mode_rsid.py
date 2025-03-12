import re

from cli import logger
from utils import (
    cleanup_query_df,
    get_query,
    load_gtex_data,
    query_to_df,
    read_input_file,
)


def run(args):
    """Handles Mode "rsid" logic."""

    input_data = read_input_file(args.input)

    input_data.columns = [
        re.sub(r"[^a-zA-Z0-9\_ ]", "", col) for col in input_data.columns
    ]
    ids_to_search = input_data[args.rsid_col].tolist()

    # Perform checks on ids_to_search
    if not make_checks(ids_to_search, args.rsid_col):
        return

    # Load database safely
    with load_gtex_data() as gtex_con:
        if gtex_con:
            gtex_cur = gtex_con.cursor()

            # Construct and execute query safely
            query = get_query("GTEx_lookup", ids_to_search, "rsid_dbSNP155")

            results_df = query_to_df(query, ids_to_search, gtex_cur)

            final_df = cleanup_query_df(
                results_df, input_data, args.rsid_col, "rsid_dbSNP155"
            )

            print(final_df)


def make_checks(ids_to_search, rsid_col):
    if not ids_to_search:
        logger.warning(f"rsID column '{rsid_col}' is empty.")
        return False
    if not all(re.match(r"^rs[0-9]+$", i) for i in ids_to_search):
        logger.warning(f"IDs in rsID column '{rsid_col}' do not match rsID format")
        return False
    logger.info(f"rsID column '{rsid_col}' passed checks ✨")
    return True
