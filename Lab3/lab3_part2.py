__author__ = 'austin'

import os
import json


def file_len(fname):
    with open(fname, 'r') as f:
        # enumerate returns tuples of lines
        for index, line in enumerate(f):
            pass
        return index + 1


def generate_stats():
    length_dict = {}
    for file in os.listdir():
        print(file, 'is a directory?', os.path.isdir(file))
        if not os.path.isdir(file):
            length_dict[file] = file_len(file)

    print(length_dict)

    directory_stats = [os.getcwd(), length_dict]

    print(directory_stats)

    with open('file_info.txt', 'w') as write_file:
        json.dump(directory_stats, write_file)


if __name__ == '__main__':
    generate_stats()