import argparse
import sys
import os
import csv

base_path = 'C:/Users/zc11/PycharmProjects/realpython1/part3'
output_path = base_path
input_csv_lines = 0


def check_for_input(f):
    full_path = os.path.join(base_path,f)
    if os.path.isfile(full_path):
        fileName, extension = os.path.splitext(full_path)
        if extension == '.csv':
            return 0
        else:
            return -1
    else:
        return -1


def validate_limit(r, icl):
    if r > icl:
        return -1
    else:
        return 0


def split_files(args, total_output_files):
    file_contents = []
    file_pointer = 0

    with open(os.path.join(base_path, args.input_file.name), "r") as input_file_handler:
        csv_input_file_handler = csv.reader(input_file_handler)
        header = next(csv_input_file_handler)
        for _ in range(total_output_files+1):
            file_contents.append([header])
        for var, row in zip(range(1, 1+input_csv_lines), csv_input_file_handler):
            file_contents[file_pointer].append(row)
            if var % (args.limit) == 0:
                file_pointer += 1

    for idx in range(len(file_contents)):
        with open(os.path.join(output_path, args.outfile+str(idx+1)+'.csv'), 'w') as output_file_handler:
            csv_output_file_handler = csv.writer(output_file_handler)
            csv_output_file_handler.writerows(file_contents[idx])
            print("Output file {} generated which contains {} rows".format(args.outfile+str(idx+1)+'.csv', len(file_contents[idx]) -1 ))


def validate_arguments(args):
    if check_for_input(args.input_file.name) != 0:
        print("******" * 5)
        print("validation ERROR :")
        print("Either the Input file doesn't exist or it is not a .csv file. Please check and try again!!")
        print("******" * 5)
        return -1

    with open(os.path.join(base_path, args.input_file.name), "r") as file_handle:
        csv_file_handler = csv.reader(file_handle)
        next(csv_file_handler)
        global input_csv_lines
        for _ in csv_file_handler:
            input_csv_lines += 1

    if validate_limit(args.limit, input_csv_lines) != 0:
        print("******" * 5)
        print("the chunk limit is too high, the limit should be less than {}".format(input_csv_lines))
        print("******" * 5)
        return -1
    else:
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='csv_split.py', description="For splitting the CSV files by the given chunk size")
    parser.add_argument('-i', '--input_file', help="input file name", type=argparse.FileType('r'), default=sys.stdin,
                    required=True)
    parser.add_argument('-o', '--outfile', help="output file name",
                    required=True)
    parser.add_argument('-r', '--limit', type=int, help="row limit to split", required=True)
    args = parser.parse_args()

    if validate_arguments(args) != 0:
        exit
    else:
        total_output_files = input_csv_lines//args.limit
        split_files(args, total_output_files)