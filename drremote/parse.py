import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    # input_group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("-m",
                        "--mode",
                        help="operating mode",
                        type=str,
                        choices=["settimeline", "gettimeline"],
                        required=True)

    parser.add_argument("-p",
                        "--project",
                        help="name of project",
                        type=str,
                        default=None)

    parser.add_argument("-t",
                        "--timeline",
                        help="name of timeline",
                        type=str,
                        default=None)

    parser.add_argument("-o",
                        "--output-path",
                        help="name of output file",
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument("-d",
                        "--database",
                        help="database",
                        type=str,
                        default=None)

    args = parser.parse_args()
    if args.mode == "settimeline" and (args.project is None or args.timeline is None):
        parser.error("-m settimeline requires -p and -t")
    if args.mode == "gettimeline" and (args.output_path is None):
        parser.error("-m gettimeline requires -o")

    return args
