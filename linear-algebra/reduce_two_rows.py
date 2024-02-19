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

# Have file called row.txt in same folder as this SCRIPT
# Have it set up with two lines that have columns of 2 different reduce_two_rows

# ex) row1 = [1,2,3]   row2 = [4, 5, 6]; then have txt look like this

# | 1 2 3 |
# | 4 5 6 |

# The |'s above are just borders. Don't have them in your row.txt
# Ensure there's a single space between each column. Floats and negatives are okay
# check out the row.txt that comes with this for an example file input
# ENSURE BOTH ROWS ARE EQUAL LENGTH

# CALL SCRIPT such as:
# python3 ./reduce_two_rows.py -s1 n -s2 n2
# set n1 to the scalar for row1 and n2 for row2 scalar
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

    new_row2 = np.add(row1, row2)
    print(new_row2)


if __name__ == "__main__":
    main(parseArgs())
