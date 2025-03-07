from cli import create_parser
from modes import mode_rsid, mode_chrpos37, mode_chrpos38

def main():
    parser = create_parser()
    args = parser.parse_args()

    # Select the correct mode
    mode_map = {
        "rsid": mode_rsid.run,
        "chrpos37": mode_chrpos37.run,
        "chrpos37": mode_chrpos38.run
    }

    selected_mode = mode_map.get(args.mode)
    if selected_mode:
        selected_mode(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()