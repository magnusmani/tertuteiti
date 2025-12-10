import csv
import itertools
from collections import Counter

# stafrófið
alph = ["a", "á", "b", "c", "d", "ð", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "v", "w", "x", "y", "ý", "z", "þ", "æ", "ö"]

# allar mögulega samsetningar af tveimur og þremur stöfum
two_combos = [''.join(p) for p in itertools.product(alph, repeat=2)]
three_combos = [''.join(p) for p in itertools.product(alph, repeat=3)]

# öll orð úr skrá
with open("wordlist.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# talning
counts = Counter()

for combo in two_combos:
    counts[combo] = text.count(combo)

for combo in three_combos:
    counts[combo] = text.count(combo)

# skrifum í csv skrá
with open("samsetningar.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["samsetning", "fjöldi"])  
    for combo, cnt in counts.items():
        writer.writerow([combo, cnt])


