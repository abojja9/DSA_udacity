"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_time = {}

for record in calls:
    for x in [0,1]:
        telephone_time[record[x]] = telephone_time.get(record[x], 0) + int(record[-1])

max_val = max(telephone_time.values())

for key in telephone_time:
    if telephone_time[key] == max_val:
        telephone_num = key
        break

print (f"{telephone_num} spent the longest time, {max_val} seconds, on the phone during September 2016.")


   

