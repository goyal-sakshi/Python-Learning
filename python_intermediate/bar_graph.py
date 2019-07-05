#!/usr/bin env python

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import argparse

def display_graph(df, tog):

	print df
	if tog == 'v': 
		plot = df.plot(kind='bar', rot=0)
	elif tog == 'h':
                plot = df.plot(kind='barh')
	else:
                print 'Invalid type input'
	        sys.exit(1)

	path = os.getcwd()
        fig = plot.get_figure()
	fig.savefig(path + '/bar.png')
        img = Image.open(path + '/bar.png')
        img.show()

def set_coordinates(*args):

	all_series = []
	if len(args) == 3:
		tog = args[2]
		X = map(float, args[0].split(','))
		Y = map(float, args[1].split(','))
		df = pd.DataFrame(Y, index=X)
		display_graph(df, tog)
		
	else:	
		tog = args[1]
		items = args[0].split(';')
		for i in items:
			column_name, col_val = i.split(':')
			column_values = map(float, col_val.split(','))
			all_series.append(pd.Series(column_values))
	
		df = pd.DataFrame(all_series)
		display_graph(df, tog)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-x', '--xAxis',help='X coordinates')
	parser.add_argument('-y', '--yAxis',help='Y coordinates')
	parser.add_argument('-tog', '--type_of_graph',help='Type of graph', required=True)
	parser.add_argument('-df', '--data_frame',help='Data Frame')
	args = parser.parse_args()	

	if args.data_frame:
		set_coordinates(args.data_frame, args.type_of_graph)
	else:
		set_coordinates(args.xAxis, args.yAxis, args.type_of_graph)

if __name__ == '__main__':
	main()
