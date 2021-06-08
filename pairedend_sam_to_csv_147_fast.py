import csv
import sys

align1 = open(sys.argv[1], 'r')
#sam file used entered via user input
dyad = []
for line in align1:
    if line [0] != '@':
        diclist = line.split('\t')
        if int(diclist[8]) in range(136,159):
            dyad.append((int(diclist[8])/2)+int(diclist[3]))
# generating the dyad score
nucpos = []
for i in dyad:
    nucpos.append(range(i-73, i+74))
#getting the nucleosome position
nucposstr = []
for i in nucpos:
    liststr = []
    for val in i:
        liststr.append(str(val))
    nucposstr.append(liststr)
#convert back to strings
nuc_pos_cat = []
for i in nucposstr:
    for val in i:
        nuc_pos_cat.append(val)
#concatenate liststr
nuc_pos_cat_int = []
adj_score = int(sys.argv[2])
adj_nuc_pos = []
for i in nuc_pos_cat:
    nuc_pos_cat_int.append(int(i))
for i in nuc_pos_cat_int:
    adj_nuc_pos.append(i - adj_score)
#shift to center
count_dictionary = {}
for i in nucposstr:
    for val in i:
        if val in count_dictionary.keys():
            count_dictionary[val] += 1
        else:
            count_dictionary[val] = 1
#count accurances of numbers
countdictionary = str(sys.argv[3])+"_countdictionary.csv"
with open(countdictionary, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in count_dictionary.items():
        writer.writerow([key,value])
# write count_dictionary to csv file named by user
rawlist=str(sys.argv[3])+'_rawlist.csv'
with open(rawlist, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for val in adj_nuc_pos:
        writer.writerow([val])
#write raw list of positions
dyadlist=str(sys.argv[3])+'_dyad.csv'
with open(dyadlist, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    for val in dyad:
        writer.writerow([val])
#list of dyad scores
count_dictionary_int = []
range = []
for i in count_dictionary.keys():
    count_dictionary_int.append(int(i))
for i in count_dictionary_int:
    range.append(i - adj_score)
rangelist = str(sys.argv[3])+'_range.txt'
f = open(rangelist, 'w')
f.write(str(sorted(range)))
f.close()
# write range of dictionary to csv file in single row

# print 'dictionary_c'
# print dictionary_c
# print 'List of values'
# print listofvalues
# print 'dyad'
# print dyad
# # print 'Nucleosome position'
# # print nucpos
# print 'Nucleosome position string'
# print nucposs
# print 'the whole list'
# print nuc_pos_cat
# print "count dictionary"
# print count_dictionary
