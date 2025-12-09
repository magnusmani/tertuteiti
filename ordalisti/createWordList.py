import xml.etree.ElementTree as ET
import re

wordlist = open('wordlist.txt','w')

tree = ET.parse('islensk_nutimamalsordabok.xml')
root = tree.getroot()

prefix = re.match(r'\{(.*)\}', root.tag).group(1)

ns = {'ns': prefix}

lemmas = root.iterfind('.//ns:Lemma', ns)
phrases = map(lambda lemma: lemma.find('./ns:feat', ns).get('val'), lemmas)
atoms = map(lambda phrase: phrase.split(' ')[0], phrases)
words = filter(lambda atom: atom[0].isalpha(), atoms)
unique_words = sorted(set(words))

for word in unique_words:
    wordlist.write(word+'\n')
