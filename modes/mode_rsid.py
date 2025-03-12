import re

from cli import logger
from utils import (
    cleanup_query_df,
    get_query,
    load_gtex_data,
    query_to_df,
    read_input_file,
    write_ouput_file,
)


def run(args):
    """Handles mode "rsid" logic."""

    input_data = read_input_file(args.input)

    input_data.columns = [re.sub(r"[^a-zA-Z0-9\_ ]", "", col) for col in input_data.columns]
    ids_to_search = input_data[args.rsid_col].tolist()

    if not make_checks(ids_to_search, args.rsid_col):
        return

    with load_gtex_data() as gtex_con:
        if gtex_con:
            gtex_cur = gtex_con.cursor()

            query = get_query("GTEx_lookup", ids_to_search, "rsid_dbSNP155")

            results_df = query_to_df(query, ids_to_search, gtex_cur)

            final_df = cleanup_query_df(results_df, input_data, args.rsid_col, "rsid_dbSNP155", args.exclude_ref_alt)

            print(final_df)
            write_ouput_file(final_df, args.output)


def make_checks(ids_to_search, rsid_col):
    """
    Checks if the rsID column specified has rsIDs in the correct format.

    Parameters:
    ids_to_search (list): The values from rsID column converted to a list.
    rsid_col (str): Name of the rsID column as provided by user.

    Returns:
    Logical value True or False
    """
    if not ids_to_search:
        logger.warning(f"rsID column '{rsid_col}' is empty.")
        return False
    if not all(re.match(r"^rs[0-9]+$", i) for i in ids_to_search):
        logger.warning(f"IDs in rsID column '{rsid_col}' do not match rsID format")
        return False
    logger.info(f"rsID column '{rsid_col}' passed checks ✨")
    return True
