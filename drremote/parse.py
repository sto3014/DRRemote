import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    # input_group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("-m",
                        "--mode",
                        help="operating mode",
                        type=str,
                        choices=["settimeline"],
                        required=True)

    parser.add_argument("-prj",
                        "--project",
                        help="name of project",
                        type=str,
                        default=None)

    parser.add_argument("-tl",
                        "--timeline",
                        help="name of timeline",
                        type=str,
                        default=None)

    args = parser.parse_args()
    if args.mode == "settimeline" and (args.project is None or args.timeline is None):
        parser.error("-m settimeline requires -prj and -tl")
    return args
