import nltk, re, pprint
#nltk.download('all')
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

tokens = word_tokenize(s)
words = [w.lower() for w in tokens]
vocab = sorted(words)
list1 = [x for x in vocab if x not in st]
counts = Counter(list1)
list2 = []
for k,v in  counts.most_common():
	list2.append(v)
c1 = Counter(list2)

list3 = []
list4 = []
for k1,v1 in  c1.most_common():
	list3.append(k1)
	list4.append(v1)
a = sum(list4)
list4 = [i/float(a) for i in list4]

#print(math.log(3))
#list3 = [math.log(i) for i in list3]
#list4 = [math.log(i) for i in list4]
#print(len(list3))
pl = plt.gca()
pl.plot(list3,list4,'o')
pl.set_yscale('log')
pl.set_xscale('log')
plt.show()
