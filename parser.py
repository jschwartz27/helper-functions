import os
import argparse
from typing import List


def get_args() -> object:
    parser = argparse.ArgumentParser(description="Key phrase search")
    parser.add_argument("-k", "--key", required=True, type=str,
                        help='Phrase to search for')
    parser.add_argument("-c", "--context", required=False, type=bool,
                        help='Context window')
    return parser.parse_args()


def parser_files(d: str) -> List[str]:
    fs: List[str] = list()
    for f in os.listdir(d):
        file_name = d + "/" + f
        if os.path.isfile(file_name):
            fs.append(file_name)
        else:
            fs.extend(parser_files(file_name))
    return fs


def read_file(file: str, context: bool) -> str:
    f = open(file, "r")
    text = f.read()
    f.close()
    return text


def main():
    args = get_args()
    # args = <class 'argparse.Namespace'>

    # current_dir = os.path.dirname(os.path.realpath(__file__))
    files: List[str] = parser_files(".")
    files.remove("./" + __file__)  # remove current file from results

    desired: List[str] = list(filter(
        lambda x: args.key in read_file(x, args.context), files))

    for i, file_name in enumerate(desired):
        print("\t{} - {}".format(i+1, file_name))

if __name__ == '__main__':
    main()
