import csv
from collections import defaultdict

def isKanji(ch):
    res = False
    o = ord(ch)
    if (o >= 0x4e00) and (o <= 0x9faf):
        res = True
    #print (ch, ":",  res)
    return res

f = open("GJVL.txt")
fields = ["English", "Japanese", "Reading", "Story", "Picture"]
cf = csv.DictReader(f, fieldnames=fields, delimiter="\t")
all = defaultdict(int)
stories = defaultdict(int)
for row in cf:
    words = row["Japanese"]
    story = row["Story"]
    for ch in words:
        if isKanji(ch): 
            all[ch] +=1
    for ch in story:
        if isKanji(ch):
            stories[ch] +=1

nonuniq = 0
print ("Total", len(all))
for key in all:
    if all[key] > 1:
        nonuniq += 1
        # print(key)

print("Non unique", nonuniq)

print("With stories")

all |= stories
nonuniq = 0
print ("Total", len(all))
for key in all:
    if all[key] > 1:
        nonuniq += 1

print("Non unique", nonuniq)



# use ord to get number from kanji
# check between 4e00 and 9faf