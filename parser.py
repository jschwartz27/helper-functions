import os
import argparse
from typing import List
# import mimetypes


def get_args() -> object:
    parser = argparse.ArgumentParser(description="Key phrase search")
    parser.add_argument("-k", "--key", required=True, type=str,
                        help="Phrase to search for")
    parser.add_argument("-e", "--extensions", required=False, nargs='+',
                        help='File extensions to search by: -e py ts')
    parser.add_argument("-c", "--context", required=False, type=bool,
                        help="Context window")
    parser.add_argument("-f", "--file_type", required=True,
                        help='File types to search')
    parser.add_argument("-d", "--destination_file", required=True,
                        help='Directory to delve into')
    # caps on caps off option
    return parser.parse_args()


def parser_files(d: str, file_type: List[str]) -> List[str]:
    fs: List[str] = list()
    for f in os.listdir(d):
        file_name = d + "\\" + f
        if file_type and os.path.isfile(file_name):
            typ = file_name.split(".")[-1]
            if typ not in file_type:
                continue
            else:
                fs.append(file_name)
        elif ".gif" in file_name:
            continue
        elif os.path.isfile(file_name):
            fs.append(file_name)
        else:
            fs.extend(parser_files(file_name, file_type))
    return fs


def read_file(file: str, context: bool) -> str:
    f = open(file, encoding="utf8")
    text = f.read()
    f.close()
    return text


def main():
    args = get_args()
    # args = <class 'argparse.Namespace'>

    if args.file_type:
        args.file_type = args.file_type.split(" ")

    current_dir = os.path.dirname(os.path.realpath(__file__))
    # the_D = current_dir + "\\profile-map\\src\\app"
    the_D = current_dir + args.destination_file

    files: List[str] = parser_files(the_D, args.file_type)  #".")
    # files.remove("./" + __file__)  # remove current file from results

    desired: List[str] = list(filter(
        lambda x: args.key in read_file(x, args.context), files))

    print()
    if len(desired) == 0:
        print("\tNo files found containing your query...")
    else:
        for i, file_name in enumerate(desired):
            print("\t{} - {}".format(i+1, file_name))

if __name__ == '__main__':
    main()


'''
mimetypes.guess_type("filepath")[0] == 'text/html'
but doesn't for for .ts files

# !! parser must simply ignore all non-text files
# TODO case sensitive
# TODO context function
    - print line before and line after
# TODO if result len == 1 simply open the file
'''