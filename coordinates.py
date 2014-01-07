#!/usr/bin/env python

InFileName = raw_input("What is the input file? ")
OutFileName = InFileName + '.kml'
WriteOutFile = True
TaxName = raw_input("What is the taxon name? ")

InFile = open(InFileName, 'r')
Headstring='''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
<Document>'''

if WriteOutFile:
	OutFile = open(OutFileName, 'w')
	OutFile.write(Headstring)

LineNumber = 0

# Loop through each line in the file
for Line in InFile:
	if LineNumber > 0:
		#remove the line-ending characters
		Line = Line.strip('\n')
		ElementList = Line.split('\t')
		Place = ElementList[0]
		LatDegrees = float(ElementList[1])
		LonDegrees = float(ElementList[2])
		PlaceMarkString = '''
<Placemark>
	<name> %s - %s</name>
	<description>%s</description>
	<Point>
		<coordinates>%f, %f </coordinates>
	</Point>
</Placemark>'''% (TaxName, Place, Place, LonDegrees, LatDegrees)
		if WriteOutFile:
			OutFile.write(PlaceMarkString)
		else:
			print PlacemarkString
	LineNumber += 1

InFile.close()
if WriteOutFile:
	print "Saved", LineNumber, "records from", InFileName, "as", OutFileName
	OutFile.write('\n</Document>\n</kml>\n')
	OutFile.close()
else:
	print '\n</Document>\n</kml>\n'