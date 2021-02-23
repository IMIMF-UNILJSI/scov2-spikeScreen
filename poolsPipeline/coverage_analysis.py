#!/usr/bin/env python

import argparse
import sys
import os

import numpy as np
import pylab as plt


def parse_args(args=None):
	Description = 'Filter ivar tsv files across replicates.'
	Epilog = """Example usage: python postAnalysis.py -s <STATS> -x <xlim> -y <xlim> -l <logscale> -p <prefix>"""
	parser = argparse.ArgumentParser(description=Description, epilog=Epilog)
	parser.add_argument('-s', '--stats_folder', dest="stats_folder", default="stats", help="Where is the stats folder?")
	parser.add_argument('-x', '--xlim', default=None, dest="xlim", help="Xlim interval?")
	parser.add_argument('-y', '--ylim', default=None, dest="ylim", help="Ylim interval?")	
	parser.add_argument('-l', '--logscale', default="false", type=str, dest="logscale", help="Use logscale?")
	parser.add_argument('-p', '--prefix', default="spikeGene", dest="prefix", help="How to name my output?")
	parser.add_argument('-r', '--runmerged', default="true", dest="runmerged", help="Do i draw graphs for merged files?")


	return parser.parse_args(args)

def draw_coverage_profiles(stats_folder, prefix, xlim, ylim, logscale, merged=False):
	
	plt.rcParams["figure.figsize"] = (12,8)
	flst = [ fl for fl in os.listdir("./" + stats_folder) if fl.startswith(".ipynb") != True and fl.endswith("_merged.coverage") == merged]
	
	files = []
	coverage = []
	percentiles = []
	
	for fl in flst:
		with open("./" + stats_folder + "/" + fl) as fin:
			sample = fl.rstrip(".coverage")
			lines = [ int(line.strip().split()[2]) for line in fin ]
			if sample not in files:
				files.append(sample)
				coverage.append(np.array(lines))
			else:
				sindex = files.index(sample)
				coverage[sindex] += np.array(lines)
	for i, file in enumerate(files):
		plt.plot(coverage[i], label=file)
		try:
			percentile = np.percentile(coverage[i], [0, 5, 10, 15, 20, 25, 50 ,75, 100])
			percentiles.append(list(percentile))
		except IndexError:
			continue

	plt.xlabel("Genomic position")
	plt.ylabel("Coverage")
	plt.title("Coverage profiles")
	plt.legend(ncol=4, loc="best")

	if xlim != None:
		xlim = [float(i) for i in xlim.split(",")]
		plt.xlim(xlim[0], xlim[1])
	if ylim != None:
		ylim = [float(i) for i in ylim.split(",")]
		plt.ylim(ylim[0],ylim[1])
	if logscale != "false":
		plt.yscale("log")

	plt.savefig(prefix + "-coverage.pdf")
	plt.savefig(prefix + "-coverage.png", dpi=100)

	plt.clf()

	percentiles = list(zip(*percentiles))

	plt.boxplot(percentiles)
	plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ["0", "5", "10", "15", "20", "25", "50", "75", "100"])
	plt.xlabel("Percentiles")
	plt.savefig(prefix + "-covPerc.pdf")
	plt.savefig(prefix + "-covPerc.png", dpi=100)

	plt.clf()

def main(args=None):
	args = parse_args(args)
	draw_coverage_profiles(args.stats_folder, args.prefix + "-sep", args.xlim, args.ylim, args.logscale, merged=False)
	if args.runmerged == "true":
		draw_coverage_profiles(args.stats_folder, args.prefix + "-merge", args.xlim, args.ylim, args.logscale, merged=True)

if __name__ == '__main__':
	sys.exit(main())
