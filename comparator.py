#!/usr/bin/python
###AUTHOR: Gabriel Ursu
###The following script compares 2 SAP profiles showing as output:
### - Parameters present in both profiles with the same value
### - Parameters present in both profiles with different value
### - Parameters present in System1 but not in System2
### - Parameters present in System2 but not in System1
###
### The usage is the following:
### python ./comparator.py /dir/to/profile1 /dir/to/profile2
### the SIDs are taken from the parameter SAPSYSTEMNAME

import sys

f1 = [];
f2 = [];

#file1 and file2 opening
with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip();
		f1.append(line);

with open(sys.argv[2], 'r') as ff:
	for line in ff: 
		line = line.rstrip();
		f2.append(line);

#stripping comments and emptylines
for line in f1[:]:
	if line.startswith('#') or len(line)==0:
		f1.remove(line);

for line in f2[:]:
	if line.startswith('#') or len(line)==0:
		f2.remove(line);

#building a dictionary with entries of the type  param:value
params1={};
params2={};

for line in f1:
	coppia=line.split(' = ');
	params1.update({coppia[0] : coppia[1]});

for line in f2:
	coppia=line.split(' = ');
	params2.update({coppia[0] : coppia[1]});

#capturing the System Ids from parameters
sid1 = params1['SAPSYSTEMNAME'];
sid2 = params2['SAPSYSTEMNAME'];

#starting the output
print '###parameters present in '+sid1+' and '+sid2+' with the same value:\n';
for key1 in params1:
	for key2 in params2:
		if key1 == key2:
			if params1[key1] == params2[key2]:
				print key1+' = '+params1[key1];

print ('\n\n###parameters present in '+sid1+' and '+sid2+' with different values:\n');
for key1 in params1:
	for key2 in params2:
		if key1 == key2:
			if params1[key1] != params2[key2]:
				print 'value of '+key1+':';
				print sid1+' = '+params1[key1];
				print sid2+' = '+params2[key2]+'\n';
				

found = 0;
print ('\n\n###parameters present in '+sid1+' but not in '+sid2);
for key1 in params1:
	for key2 in params2:
		if key1 == key2:
			found = 1;
	if found == 0:
		print key1+' >>> '+params1[key1];
	found = 0;

found = 0;
print('\n\n###parameters present in '+sid2+' but not in '+sid1);
for key2 in params2:
	for key1 in params1:
		if key2 == key1:
			found = 1;
	if found == 0:
		print key2+' >>> '+params2[key2];
	found=0;

