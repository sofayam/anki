import csv
from collections import defaultdict
f = open("../../GJVL.txt")
fields = ["English", "Japanese", "Reading", "Story", "Picture"]
cf = csv.DictReader(f, fieldnames=fields, delimiter="\t")
all = defaultdict(int)
for row in cf:
    words = row["Japanese"]
    for ch in words: 
        all[ch] +=1

nonuniq = 0
print ("Total", len(all))
for key in all:
    if all[key] > 1:
        nonuniq += 1
        # print(key)

print("Non unique", nonuniq)


# use ord to get number from kanji
# check between 4e00 and 9faf