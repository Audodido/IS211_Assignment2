import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Number", type=int)
args = parser.parse_args()


print(args.Number + 100)