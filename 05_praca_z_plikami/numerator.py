"""
Napisz skrypt, który ponumeruje linie w pliku, np.

python numerator.py emaile.txt
"""

import sys

def main(file_name):
    n = 0
    with open(file_name) as f:
        for line in f:
            n += 1
            print(f"{n:3}: {line}", end="")

main(sys.argv[1])