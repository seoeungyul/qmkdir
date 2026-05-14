import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", default=os.getcwd(), help="directory path")
args = parser.parse_args()

n = os.urandom(3).hex()
print(n)
os.mkdir(os.path.join(args.d, n))

