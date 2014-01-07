#! /usr/bin/env python


InFileName = 'Marrus_claudanielis.txt'

InFile = open(InFileName, 'r')

LineNumber = 0


OutFileName=InFileName + ".kml"

OutFile=open(OutFileName,'w') # You can append instead with 'a'


for Line in InFile:
	if LineNumber > 0:
		Line=Line.strip('\n')
 		
 		ElementList=Line.split('\t')
 		
		OutputString = "Depth: %s\tLat: %s\t Lon:%s" % \
		   (ElementList[4], ElementList[2], ElementList[3])
		   
		print OutputString
		
		OutFile.write(OutputString+"\n")  
		
	LineNumber = LineNumber + 1


InFile.close()
OutFile.close()
