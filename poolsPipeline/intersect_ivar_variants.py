#!/usr/bin/env python

import argparse
import sys

def parse_args(args=None):
	Description = 'Filter ivar tsv files across replicates.'
	Epilog = """Example usage: python intersect_ivar_variants.py -f1 <FILE_IN_1> -f2 <FILE_IN_2> -fm <FILE_IN_M> -o <FILE_OUT>"""
	parser = argparse.ArgumentParser(description=Description, epilog=Epilog)
	parser.add_argument('-f1', '--FILE_IN_1',dest="FILE_IN_1", help="Input tsv file 1.")
	parser.add_argument('-f2', '--FILE_IN_2',dest="FILE_IN_2", help="Input tsv file 2.")
	parser.add_argument('-fm', '--FILE_IN_M',dest="FILE_IN_M", help="Input tsv file Merged.")
	parser.add_argument('-o', '--FILE_OUT', dest="FILE_OUT", help="Full path to output vcf file.")

	return parser.parse_args(args)


def intersect_variant_files(file1, file2, fileM, fileout):
	with open(file1) as fin:
		header1 = fin.readline()
		data1 = [line.split() for line in fin]
		keys1 = [l[0] +"|"+ l[1] + "|" + l[2] + "|" + l[3] for l in data1]

	with open(file2) as fin:
		header2 = fin.readline()
		data2 = [line.split() for line in fin]
		keys2 = [l[0] +"|"+ l[1] + "|" + l[2] + "|" + l[3] for l in data2]

	with open(fileM) as fin:
		headerm = fin.readline()
		datam = [line.split() for line in fin]
		keysm = [l[0] +"|"+ l[1] + "|" + l[2] + "|" + l[3] for l in datam]

	key_intersection = set(keysm).intersection(set(keys1)).intersection(set(keys2))

	with open(fileout, "w") as fout:
		fout.write(headerm)
		for (keysm, line) in zip(*(keysm, datam)):
			if keysm in key_intersection:
				fout.write("\t".join(line)+"\n")



def main(args=None):
	args = parse_args(args)
	intersect_variant_files(args.FILE_IN_1, args.FILE_IN_2, args.FILE_IN_M, args.FILE_OUT)



if __name__ == '__main__':
	sys.exit(main())
