import argparse
import sys


parser = argparse.ArgumentParser(prog='parse1.py', description="For splitting the CSV files by the given chunk size")
parser.add_argument('-i', '--input_file', help="input file name", type=argparse.FileType('r'), default=sys.stdin,
                    required=True)
parser.add_argument('-o', '--output_path', help="output directory", type=argparse.FileType('w'), default=sys.stdout,
                    required=True)
parser.add_argument('-r', '--limit', type=int, help="row limit to split", required=True)
args = parser.parse_args()


print(args.input_file.name)
print(args.output_path.name)
print(args.limit)

