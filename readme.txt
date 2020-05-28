A simple comparator for SAP Profiles written in python.

AUTHOR: Gabriel Ursu
The script compares 2 SAP profiles showing as output:
 - Parameters present in both profiles with the same value
 - Parameters present in both profiles with different value
 - Parameters present in System1 but not in System2
 - Parameters present in System2 but not in System1

 The usage is the following:
 python ./comparator.py /path/to/profile1 /path/to/profile2

 the SIDs are taken from the parameter SAPSYSTEMNAME
