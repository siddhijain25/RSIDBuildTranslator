from cli import create_parser, logger
from modes import mode_rsid, mode_chrpos37, mode_chrpos38


def main():
    # # Step 1: Parse only --mode argument
    # base_parser = create_parser()
    # base_args, _ = base_parser.parse_known_args()

    # Step 2: Recreate parser with mode-specific arguments
    parser = create_parser()
    # parser = create_mode_specific_args(parser, base_args)
    args = parser.parse_args()  # Fully parse arguments

    # parser.print_help()
    logger.info(f"Running tool in mode: '{args.mode}'")

    # Select the correct mode
    mode_map = {
        "rsid": mode_rsid.run,
        "chrpos37": mode_chrpos37.run,
        "chrpos38": mode_chrpos38.run,
    }

    selected_mode = mode_map.get(args.mode)
    if selected_mode:
        selected_mode(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
