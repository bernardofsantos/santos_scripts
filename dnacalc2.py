#!/usr/bin/env python

DNASeq = raw_input("Enter a DNA sequence:")
#DNASeq = 'ATGTCTCATTCAAAGCA'
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace (" ", "")

print 'Sequence', DNASeq

SeqLength = float(len(DNASeq))
print 'Sequence Length:', SeqLength

BaseList = list(set(DNASeq))
if len(BaseList) == 4:
#tttwcaggaatgtcgggtgtttgtcttttgtattgctgttgttggggtgtccgttgttcaa
	for Base in BaseList:
		#if Base == 'A' or 'C' or 'G' or 'T'
			Percent = 100 * DNASeq.count(Base) / SeqLength
			print "%s: %4.1f" % (Base, Percent)

	CGcontent= 100*((DNASeq.count("C")+DNASeq.count("G"))/SeqLength)

	#Calculate overall CG content; only works for sequences without gaps, and doesn't count IUPAC symbols other than ACTGT
	print "CG content", "%.1f%%" % CGcontent

	#Calculating primer melting points with different formulas by length

	TotalStrong = DNASeq.count("C")+DNASeq.count("G")
	TotalWeak = DNASeq.count("A")+DNASeq.count("T")

	if SeqLength >= 14:
		#formula for sequences 14 or more nucleotides long
		MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
		print "Melting Temp (>14): %.1f C" % (MeltTempLong)

	else:
		MeltTemp = (4 * TotalStrong) + (2 * TotalWeak)
		print "Melting Temp: %.1f C" % MeltTemp

else:
	print "Error: not all bases are A, C, G or T. Please enter a sequence that contains only ACGT characters"
