import nltk, re, pprint

from nltk import word_tokenize
import string
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import math
import matplotlib.pyplot as plt
#f = open('speech.txt')
f = open('blog.txt')
s = f.read()
st= [line.rstrip('\r\n') for line in open('stoplist.txt')]
'''
raw = ''.join([i for i in s if not i.isdigit()])
raw = " ".join("".join([" " if ch in string.punctuation else ch for ch in raw]).split())
tokenizer = nltk.RegexpTokenizer(r'\w+')
tokens=tokenizer.tokenize(raw)
'''
tokens = word_tokenize(s)
num_char = sum(len(x) for x in tokens)
total_num = len(tokens)
avg_char = float(num_char)/len(tokens) #avgper word
print ("d. average number of char per word", avg_char)
summ = 0
for x in tokens:
	for i in x:
		if i.isupper():
			summ = summ + 1
print("c. number of capital letter", summ) #upperletter


words = [w.lower() for w in tokens]
vocab = sorted(words)
u1 = sorted(set(words)) #number of unique words
print ("a. vocabulary size", len(u1))
list1 = [x for x in vocab if x not in st]
stopword_fre = len(vocab)-len(list1) #stopwords frequency
print ("b. frequency of stopwords", float(stopword_fre)/total_num)
list2 = nltk.pos_tag(list1)
c2 = Counter(tag for word, tag in list2)
'''
c3= Counter(word for word, tag in list2 if tag == "VB" or tag == "VBG" or tag == "VBZ" or tag == "VBD" or tag == "VBN" or tag == "VBP")

c3= Counter(word for word, tag in list2 if tag == "NN" or tag == "NNS")
'''
c4= Counter(tag for word, tag in list2 if word == "i")
N=2
list3 = []

