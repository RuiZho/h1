import nltk, re, pprint
from nltk import word_tokenize
import string
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import math
import matplotlib.pyplot as plt
import operator
f = open('blog.txt')
f1 = open('speech.txt')
s = f.read()
s1 = f1.read()
st= [line.rstrip('\r\n') for line in open('stoplist.txt')]
tokens = word_tokenize(s)
tokens1 = word_tokenize(s1)
words = [w.lower() for w in tokens]
vocab = sorted(words)
words1 = [w1.lower() for w1 in tokens1]
vocab1 = sorted(words1)
list0 = [x for x in vocab if x not in st]
list1 = [x1 for x1 in vocab1 if x1 not in st]
total_0 = float(len(list0))
total_1 = float(len(list1))
counts = Counter(list0)
counts1 = Counter(list1)
list_most = []
list_most1 = []
for word, tag in  counts.most_common():
	if word in list1:
		y = math.log(1+tag/total_0)*(1+math.log(1))
		list_most.append((word,y))
	if word not in list1:
		list_most.append((word, math.log(1+tag/total_0)*(1+math.log(2))))
for word, tag in  counts1.most_common():
	if word in list0:
		list_most1.append((word, math.log(1+tag/total_1)*(1+math.log(1))))
	else:
		list_most1.append((word, math.log(1+tag/total_1)*(1+math.log(2))))
list_most1.sort(key = operator.itemgetter(1), reverse = True)
print(list_most1[0:30])
