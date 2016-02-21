import csv
import math
import itertools
from collections import Counter

#Item-based collaborative filtering with Adjusted cosine similarity

num_jokes=100
num_users=24983
#24983

userLines=None
with open('./jester-data-2.csv', 'r') as f:
    reader=csv.reader(f)
    userLines=list(reader)

jokesscore={}
userscore={}
usermean={}
for i in xrange(0,num_users):
    userscore[i]=map(float, userLines[i])
    sums=0
    notnull=0
    for j in xrange(1,1+num_jokes):
        print [i,j]
        if userscore[i][j]!=99:
            sums+=userscore[i][j]
            notnull+=1
    usermean[i]=sums/notnull
vectorMagnitudes = {}
for j in xrange(1,1+num_jokes):
    jokesscore[j]=[]
    for i in xrange(0,num_users):
        jokesscore[j].append(float(userLines[i][j])-usermean[i])
    temp=[x **2 if x!=99 else 0 for x in jokesscore[j]]
    vectorMagnitudes[j]=math.sqrt(sum(temp))

with open('./joke_similarities.csv', 'wb') as f:
    writer=csv.writer(f)
    #writer.writerow(['jokeA', 'jokeB', 'similarity'])
    jokes=list(jokesscore)
    for i, jokeA in enumerate(jokes):
        for jokeB in jokes[i+1:]:
            vectorA=jokesscore[jokeA]
            vectorB=jokesscore[jokeB]
            similarity=sum([a * b  if a!=99 and b!=99 else 0 for a, b in zip(vectorA, vectorB)])
            similarity/=vectorMagnitudes[jokeA] * vectorMagnitudes[jokeB]
            writer.writerow([jokeA, jokeB, '%.4f'%similarity])
            
