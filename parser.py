import os
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Key phrase search")
    parser.add_argument("-k", "--key", required=True, type=str,
                        help='Phrase to search for')
    return parser.parse_args()


def parser_files(d):
    fs = list()
    for f in os.listdir(d):
        file_name = d + "/" + f
        if os.path.isfile(file_name):
            fs.append(file_name)
        else:
            fs.extend(parser_files(file_name))
    return fs


def read_file(file):
    f = open(file, "r")
    text = f.read()
    f.close()
    return text


def main():
    args = get_args()
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    files = parser_files(".")
    files.remove("./parser.py")

    desired = list(filter(lambda x: args.key in read_file(x), files))
    for i, file_name in enumerate(desired):
        print("\t{} - {}".format(i+1, file_name))

if __name__ == '__main__':
    main()
