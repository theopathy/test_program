#INIT#
import os
language={}
with open(os.path.dirname(os.path.realpath(__file__))+r'\strings.txt', 'r') as f:
	x = f.readlines()
	for val in x :
		a,b = val.split("\t")
		a = a.replace('"', '')
		b = b.replace('"', '')
		b = b.strip("\n") 
		language[a]=bytes(b, "utf-8").decode("unicode_escape")