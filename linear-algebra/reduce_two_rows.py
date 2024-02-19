#!/usr/bin/env python3

import numpy as np
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(
        prog="Row Reduction"
    )
    parser.add_argument('--scale1', '-s1',
                        default=1.0, type=float)
    parser.add_argument('--scale2', '-s2',
                        default=1.0, type=float)

    args = parser.parse_args()
    return args

def main(args):
    row1 = []
    row2 = []
    scale1 = args.scale1
    scale2 = args.scale2

    f = open("row.txt")
    matrix_strings = f.readlines()
    f.close()
    for s in matrix_strings[0].split():
        row1.append(float(s))
    for s in matrix_strings[1].split():
        row2.append(float(s))

    row1 = np.array(row1)
    row1 = np.multiply(row1, scale1)

    row2 = np.array(row2)
    row2 = np.multiply(row2, scale2)

    new_row = np.add(row1, row2)
    print(new_row)


if __name__ == "__main__":
    main(parseArgs())
