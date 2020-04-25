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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
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

print (f"There are {len(total_records)} different telephone numbers in the records.")

