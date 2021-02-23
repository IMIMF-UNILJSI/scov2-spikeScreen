#!/usr/bin/env python

import argparse
import sys
import os

import numpy as np
import pandas as pd 

import openpyxl


def parse_args(args=None):
	Description = 'Filter ivar tsv files across replicates.'
	Epilog = '''Example usage: python postAnalysis.py -s <STATS> -x <xlim> -y <xlim> -l <logscale> -p <prefix>'''
	parser = argparse.ArgumentParser(description=Description, epilog=Epilog)
	parser.add_argument('-i', '--ivar_folder', dest='ivar_folder', default='ivar_variants', help='Where is the ivar folder?')
	parser.add_argument('-x', '--mutations_prefix', default='allMutations', dest='mutations', help='How to name my mutations output?')
	parser.add_argument('-c', '--intersection', default="True", type=str, dest='intersection', help='Use intersections?')
	parser.add_argument('-t', '--timepointsort', dest='timepointsort', default="True", type=str, help='Should I sort the tables by timepoint? (not applicable for assemblies)')

	parser.add_argument('-s', '--selection', dest='selection', help='Where do i put the mutation occurence table?')

	return parser.parse_args(args)

def readWrite_MutationsData2excel(ivar_folder, intersection, mutations, timepointsort):
	print(intersection)
	if intersection == "True":
		if timepointsort == "True":
			flst = sorted(
				[
					fl for fl in os.listdir(ivar_folder) if fl.endswith('.raw.tsv') and fl.rstrip('.raw.tsv').endswith('_intersection')
				], 
				key=lambda x: int(x.lstrip('P').lstrip('T').rstrip('.tsv').rstrip('.raw').rstrip('_nodup').rstrip('_intersection'))
				)
		else:
			flst = sorted(
				[
					fl for fl in os.listdir(ivar_folder) if fl.endswith('.raw.tsv') and fl.rstrip('.raw.tsv').endswith('_intersection')
				])
	else:
		if timepointsort == "True":
			flst = sorted(
				[
					fl for fl in os.listdir(ivar_folder) if fl.endswith('.raw.tsv') and fl.rstrip('.raw.tsv').endswith('_nodup')
				], 
				key=lambda x: int(x.lstrip('P').lstrip('T').rstrip('.tsv').rstrip('.raw').rstrip('_nodup').rstrip('_nodup'))
				)
		else:
			flst = sorted(
				[
					fl for fl in os.listdir(ivar_folder) if fl.endswith('.raw.tsv') and fl.rstrip('.raw.tsv').endswith('_nodup')
				])

	samples = [fl.rstrip('.tsv').rstrip('.raw').rstrip('_nodup').rstrip('_intersection') for fl in flst]
	data = []
	print(samples)
	for (fl, sample) in zip(*(flst, samples)):
		with open(ivar_folder + '/'+fl) as fin:
			header = fin.readline().strip().split()
			lines = [line.strip().split() for line in fin]
			if timepointsort == True:
				timepoint = int(sample.lstrip('P'))
				data += [[sample] + [timepoint] + ['|'.join(line[0:4])] + line for line in lines]
			else:
				data += [[sample] + ['|'.join(line[0:4])] + line for line in lines]
	header = header
	if timepointsort == True:
		header = ['Sample', 'Timepoint', 'Uniq'] + header  
	else: 
		header = ['Sample', 'Uniq'] + header

	data = pd.DataFrame(data, columns=header)
	
	data.to_excel(mutations + '_CG.xlsx')
	
	data = data
	data['POS'] = data.POS.astype(int)
	data = data[(data.POS>=21563) & (data.POS<=25384)]
	data['SPOS'] = data.POS-21563
	data['Scodon'] = (1+data.SPOS/3).astype(int)

	data.to_excel(mutations + '_spike.xlsx')
	
	return data

# def create_mutationOccurenceTables():




def main(args=None):
	args = parse_args(args)
	data = readWrite_MutationsData2excel(args.ivar_folder, args.intersection, args.mutations, args.timepointsort)

if __name__ == '__main__':
	sys.exit(main())
