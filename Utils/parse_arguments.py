import argparse

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="StackOverflow Scraper")
    parser.add_argument("--tags",
                        type = str,
                        nargs = "+",
                        required = True,
                        default=None,
                        help="Stackoverflow tags to scrape")

    parser.add_argument("--pages",
                        type=int,
                        nargs="+",
                        default=[1],
                        help="Specify the page numbers")
    return parser.parse_args()