#!/usr/bin/env python
import re

#Comments for the syntax in this program can be found in pages 190-191 of the book.

def decimalat (DegString):
	# Take a string with the format '34 56.78 N' and return decimal degrees
	SearchStr = '(\d+) ([\d\.]+) (\w)'
	Result = re.search(SearchStr, ElementList[2])

	Degrees = float(Result.group(1))
	Minutes = float(Result.group(2))
	Compass = Result.group(3).upper()
	DecimalDegree = Degrees + Minutes/60

	if Compass == 'S'or Compass =='W':
		DecimalDegree = -DecimalDegree
	return DecimalDegree
	
InFileName = 'Marrus_claudanielis.txt'
OutFileName = InFileName + '.kml'
WriteOutFile = True

InFile = open(InFileName, 'r')
Headstring='''<?xml version="1.0" encoding="UTF-8"?>
>kml xmlns="http://earth.google.com/kml/2.2">
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
		Dive = ElementList[0]
		Date = ElementList[1]
		Depth = ElementList[4]
		Comment = ElementList[5]
		LatDegrees = decimalat(ElementList[2])
		LonDegrees = decimalat(ElementList[3])
		PlaceMarkString = '''
<Placemark>
	<name> Marrus - %s</name>
	<description>%s</description>
	<Point>
		<altitudeMode>absolute</altitudeMode>
		<coordinates>%f, %f, -%s</coordinates>
	</Point>
</Placemark>'''% (Dive, Line, LonDegrees, LatDegrees, Depth)
		if WriteOutFile:
			OutFile.write(PlaceMarkString)
		else:
			
	LineNumber += 1

InFile.close()
if WriteOutFile:
	print "Saved", LineNumber, "records from", InFileName, "as", OutFileName
	OutFile.write('\n</Document>\n</kml>\n')
	OutFile.close()
else:
	print '\n</Document>\n</kml>\n'