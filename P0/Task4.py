"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def num_of_records(texts):
    text_list =set()
    for call in texts:
        text_list.add(call[0])
        text_list.add(call[1])
    return text_list

num_in_texts = num_of_records(texts)
num_in_calls = num_of_records(calls)
total_records = num_in_texts.union(num_in_calls)

records_dict = dict(zip(total_records, [1]*len(total_records)))
# print(records_dict)

for record in texts:
    if record[1] in records_dict:
        records_dict[record[1]] = 0
for record in calls:
    if record[1] in records_dict:
        records_dict[record[1]] = 0

telemarketers = set()
for each in records_dict:
    if records_dict[each] == 1:
        telemarketers.add(each)
    
telemarketers_f = sorted(telemarketers)


print ("These numbers could be telemarketers: ")
for ele in telemarketers_f:
    print(ele)

    

