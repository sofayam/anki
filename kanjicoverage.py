import csv
from collections import defaultdict
from keywords import keywords


def isKanji(ch):
    res = False
    o = ord(ch)
    if (o >= 0x4e00) and (o <= 0x9faf):
        res = True
    #print (ch, ":",  res)
    return res


def readField(name, fields, field):
    f = open(name)
    cf = csv.DictReader(f, fieldnames=fields, delimiter="\t")
    all = defaultdict(int)
    for row in cf:
        text = row[field]
        for ch in text:
            if isKanji(ch):
                all[ch] +=1
    return all





fieldnames = ["English", "Japanese", "Reading", "Story", "Picture"]


words = readField("GJVL.txt", fieldnames, "Japanese")

stories = readField("GJVL.txt", fieldnames, "Story")

nonuniq = 0
print ("Total", len(words))
for key in words:
    if words[key] > 1:
        nonuniq += 1
        # print(key)

print("Non unique", nonuniq)

print("With stories")

all = words | stories

nonuniq = 0
print ("Total", len(all))
for key in all:
    if all[key] > 1:
        nonuniq += 1

print("Non unique", nonuniq)

fivek = readField("core5k.txt", ["1"], "1")

print("5k kanjis")
print(len(fivek))

# print (sorted(fivek.items(), key=lambda x:x[1]))

missing = defaultdict(int)

index = 0
limit = 2000
for keyword in keywords:
    index +=1
    if index > limit:
        break 
    k = keyword[0]
    if k not in fivek.keys():
        missing[k] = index

print(missing)
print("Missing", len(missing))

