#!/usr/bin/env python

import argparse
import sys
import os

import numpy as np
import pandas as pd 

import openpyxl

from scipy.stats import binom_test, fisher_exact, chi2_contingency


def parse_args(args=None):
	Description = 'Filter ivar tsv files across replicates.'
	Epilog = '''Example usage: python postAnalysis.py -s <STATS> -x <xlim> -y <xlim> -l <logscale> -p <prefix>'''
	parser = argparse.ArgumentParser(description=Description, epilog=Epilog)
	parser.add_argument('-i', '--ivar_folder', dest='ivar_folder', default='ivar_variants', help='Where is the ivar folder?')
	parser.add_argument('-x', '--mutations_prefix', default='allMutations', dest='mutations', help='How to name my mutations output?')
	parser.add_argument('-c', '--intersection', default="true", type=str, dest='intersection', help='Use intersections?')
	parser.add_argument('-t', '--timepointsort', dest='timepointsort', default="true", type=str, help='Should I sort the tables by timepoint? (not applicable for assemblies)')

	parser.add_argument('-s', '--selection', dest='selection', default="selectedMutations", type=str, help='Where do i put the mutation occurence table?')
	parser.add_argument('-k', '--keyset', dest='keyset', default='default', help="Select keyset; defaults for BoJo, NeMa nad PaCo.")

	return parser.parse_args(args)

def readWrite_MutationsData2excel(ivar_folder, intersection, mutations, timepointsort):
	# print(intersection)
	if intersection == "true":
		if timepointsort == "true":
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
		if timepointsort == "true":
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
	# print(samples)
	for (fl, sample) in zip(*(flst, samples)):
		with open(ivar_folder + '/'+fl) as fin:
			header = fin.readline().strip().split()
			lines = [line.strip().split() for line in fin]
			if timepointsort == "true":
				timepoint = int(sample.lstrip('P').lstrip('T'))
				data += [[sample] + [timepoint] + ['|'.join(line[0:4])] + line for line in lines]
			else:
				data += [[sample] + ['|'.join(line[0:4])] + line for line in lines]
	if timepointsort == "true":
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

def create_mutationOccurenceTables(data, keyset):
	
	samples = data.Sample.drop_duplicates().to_list()
	import mutation_dicts as md

	mutations_present = {}
	mutations_uniq = {}
	mutations_freq = {}

	mutations_altCount = {}
	mutations_altRever = {}
	mutations_altRevPr = {}

	mutations_refCount = {}
	mutations_refRever = {}
	mutations_refRevPr = {}

	mutations_SBp = {}

	keys = md.keys[keyset]

	for key in keys:
		print(key)

		positions = md.positions_dict[key]

		mutations_present[key] = []
		mutations_uniq[key] = []
		mutations_freq[key] = []


		mutations_altCount[key] = []
		mutations_altRever[key] = []
		mutations_altRevPr[key] = []

		mutations_refCount[key] = []
		mutations_refRever[key] = []
		mutations_refRevPr[key] = []

		mutations_SBp[key] = []

		for sample in samples:

			subset = data[data.Sample==sample]

			present = [""]*len(positions)
			uniq = [""]*len(positions)
			freq = [0.0]*len(positions)

			altCount = [0.0]*len(positions)
			altRever = [0.0]*len(positions)
			altRevPr = [0.0]*len(positions)

			refCount = [0.0]*len(positions)
			refRever = [0.0]*len(positions)
			refRevPr = [0.0]*len(positions)

			sb_p = [0.0]*len(positions)

			for i, pos in enumerate(positions):
				if pos[2].startswith("del"):
					sub = subset[(subset.Scodon==pos[3]) & (subset.REF==pos[0]) & (subset.ALT==pos[1])]
				else:
					sub = subset[(subset.Scodon==pos[3]) & (subset.REF_AA==pos[4]) & (subset.ALT_AA==pos[5])]

				if len(sub.Sample.values) != 0:
						present[i] = "x"
						uniq[i] = sub.Uniq.values[0]
						freq[i] = float(sub.ALT_FREQ.values[0])

						altCount[i] = float(sub.ALT_DP.values[0])
						altRever[i] = float(sub.ALT_RV.values[0])
						altRevPr[i] = altRever[i]/altCount[i]

						refCount[i] = float(sub.REF_DP.values[0])
						refRever[i] = float(sub.REF_RV.values[0])
						refRevPr[i] = refRever[i]/refCount[i]
						
						oddsratio , pvalue = fisher_exact([[altRever[i], altCount[i]-altRever[i]],[refRever[i], refCount[i]-refRever[i]]]) #if (altRever[i] > 0.0) or (refRever[i] > 0.0) else 0.0, 1.0
						# oddsratio , pvalue, bla1, bla2 = chi2_contingency([[altRever[i], altCount[i]-altRever[i]],[refRever[i], refCount[i]-refRever[i]]])

						sb_p[i] = pvalue

		print("\t".join([sample]+present))

		mutations_present[key].append(present)
		mutations_uniq[key].append(uniq)
		mutations_freq[key].append(freq)

		mutations_altCount[key].append(altCount)
		mutations_altRever[key].append(altRever)
		mutations_altRevPr[key].append(altRevPr)

		mutations_refCount[key].append(refCount)
		mutations_refRever[key].append(refRever)
		mutations_refRevPr[key].append(refRevPr)

		mutations_SBp[key].append(sb_p)

	mutations = [
		mutations_present,
		mutations_uniq,
		mutations_freq,
		mutations_altCount,
		mutations_altRever,
		mutations_altRevPr,
		mutations_refCount,
		mutations_refRever,
		mutations_refRevPr,
		mutations_SBp
	]

	return mutations, samples

def write_mutationOccurenceTables(mutations, samples, keyset, destination_prefix):

	mutations_present, mutations_uniq, mutations_freq, mutations_altCount, mutations_altRever, mutations_altRevPr, mutations_refCount, mutations_refRever, mutations_refRevPr, mutations_SBp = mutations
	import mutation_dicts as md

	####### Prepare tables ######

	## Prepare column index names

	tuples = []
	keys = md.keys[keyset]
	for key in keys:
		key_tuples = [(key, i) for i in list(zip(*md.positions_dict[key]))[2]]
		tuples += key_tuples

	columns = pd.MultiIndex.from_tuples(tuples, names=["Variants", "Mutation"])
	# print(columns)

	## Prepare data 

	mut_present = []
	mut_uniq = []
	mut_freq = []

	mut_altCount = []
	mut_altRever = []
	mut_altRevPr = []

	mut_refCount = []
	mut_refRever = []
	mut_refRevPr = []

	mut_SBp = []

	for key in keys:
		present = list(zip(*mutations_present[key]))
		uniq = list(zip(*mutations_uniq[key]))
		freq = list(zip(*mutations_freq[key]))

		altCount = list(zip(*mutations_altCount[key]))
		altRever = list(zip(*mutations_altRever[key]))
		altRevPr = list(zip(*mutations_altRevPr[key]))

		refCount = list(zip(*mutations_refCount[key]))
		refRever = list(zip(*mutations_refRever[key]))
		refRevPr = list(zip(*mutations_refRevPr[key]))

		sbp = list(zip(*mutations_SBp[key]))


		mut_present += present
		mut_uniq += uniq
		mut_freq += freq

		mut_altCount += altCount
		mut_altRever += altRever
		mut_altRevPr += altRevPr

		mut_refCount += refCount
		mut_refRever += refRever
		mut_refRevPr += refRevPr

		mut_SBp += sbp

	mut_present = list(zip(*mut_present))
	mut_uniq = list(zip(*mut_uniq))
	mut_freq = list(zip(*mut_freq))

	mut_altCount = list(zip(*mut_altCount))
	mut_altRever = list(zip(*mut_altRever))
	mut_altRevPr = list(zip(*mut_altRevPr))

	mut_refCount = list(zip(*mut_refCount))
	mut_refRever = list(zip(*mut_refRever))
	mut_refRevPr = list(zip(*mut_refRevPr))

	mut_SBp = list(zip(*mut_SBp))


	df1 = pd.DataFrame(mut_present, columns=columns, index=samples)
	df2 = pd.DataFrame(mut_uniq, columns=columns, index=samples)
	df3 = pd.DataFrame(mut_freq, columns=columns, index=samples)
	df4 = pd.DataFrame(mut_altCount, columns=columns, index=samples)
	df5 = pd.DataFrame(mut_altRever, columns=columns, index=samples)
	df6 = pd.DataFrame(mut_altRevPr, columns=columns, index=samples)
	df7 = pd.DataFrame(mut_refCount, columns=columns, index=samples)
	df8 = pd.DataFrame(mut_refRever, columns=columns, index=samples)
	df9 = pd.DataFrame(mut_refRevPr, columns=columns, index=samples)
	df10 = pd.DataFrame(mut_SBp, columns=columns, index=samples)

	df1.index.name = "Pools"
	df2.index.name = "Pools"
	df3.index.name = "Pools"
	df4.index.name = "Pools"
	df5.index.name = "Pools"
	df6.index.name = "Pools"
	df7.index.name = "Pools"
	df8.index.name = "Pools"
	df9.index.name = "Pools"
	df10.index.name = "Pools"
	
	writer = pd.ExcelWriter(destination_prefix + ".xlsx")

	df1.to_excel(writer, sheet_name="Presence")
	df2.to_excel(writer, sheet_name="NtMutStr")
	df3.to_excel(writer, sheet_name="Freq")
	df4.to_excel(writer, sheet_name="AltDP")
	df5.to_excel(writer, sheet_name="AltRV")
	df6.to_excel(writer, sheet_name="AltRV_AltDP")
	df7.to_excel(writer, sheet_name="RefDP")
	df8.to_excel(writer, sheet_name="RefRV")
	df9.to_excel(writer, sheet_name="RefRV_RefDP")
	df10.to_excel(writer, sheet_name="SB")

	writer.save()


def main(args=None):
	args = parse_args(args)
	data = readWrite_MutationsData2excel(args.ivar_folder, args.intersection, args.mutations, args.timepointsort)
	mutations, samples = create_mutationOccurenceTables(data, args.keyset)
	print(args.selection)
	write_mutationOccurenceTables(mutations, samples, args.keyset, args.selection)

if __name__ == '__main__':
	sys.exit(main())
