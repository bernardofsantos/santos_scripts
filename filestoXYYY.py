#!/usr/bin/env python

Usage = '''
filestoXYYY.py - version 1.0
Example file for PCfB Chapter 11
Convert a series of X Y tab-delimited files to X Y Y Y format and print them to the screen.
Usage:
	filestoXYY.py *txt >combinedfile.dat
'''

import sys

if len(sys.argv)<2:
	print Usage
else:
	FileList=sys.argv[1:]
	#for InfileName in FileList:
	#print InfileName
	Header = 'lambda'
	LinestoSkip=1
	
	#change this to comma-delimited files
	Delimiter ='\t'
	MasterList=[]
	FileNum=0
	for InfileName in FileList:
	#use the name of the file as the column Header
		Header += '\t' + InfileName
		Infile = open (InfileName, 'r')
		LineNumber = 0 #reset for each file
		RecordNum=0
	
		for Line in Infile:
		#skipe firstr line and blanks
			if LineNumber > (LinesToSkip-1) and len(Line)>3:
				Line=Line.strip('\n')
				if FileNum==0:
					MasterList.append(Line)
				else:
					ElementList=Line.split(Delimiter)
					if len(ElementList)>1:
						MasterList[RecordNum] += '\t' + ElementList[1]
						RecordNum+=1
					else:
						sys.stderr.write("Line %d not XY format in file %s\n" % (LineNumber, InfileName)
			LineNumber += 1
		FileNum += 1
		Infile.close()

	print Header
	for Item in MasterList
		print Item
	
	sys.stderr.write("Converted %d file(s)\n" % FileNum)