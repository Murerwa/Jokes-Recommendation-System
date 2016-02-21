#!/usr/bin/env python

import csv
import math
import itertools
from collections import Counter
import cgi


print "Content-type: text/html\n\n"
arg=[0]*10

form = cgi.FieldStorage()
arg[0] = int(form.getvalue('rate1'))
arg[1] = int(form.getvalue('rate2'))
arg[2] = int(form.getvalue('rate3'))
arg[3] = int(form.getvalue('rate4'))
arg[4] = int(form.getvalue('rate5'))
arg[5] = int(form.getvalue('rate6'))
arg[6] = int(form.getvalue('rate7'))
arg[7] = int(form.getvalue('rate8'))
arg[8] = int(form.getvalue('rate9'))
arg[9] = int(form.getvalue('rate10'))


num_jokes=100

userscore=[99]*101
for i in xrange(1,11):
    userscore[i]=arg[i-1]
jid=0
jscore=0

#while True:
#    jid, jscore = raw_input("Enter the joke id and your rating here (Enter q q to stop): ").split()
#    if jid=='q':
#        break
#    else:
#        userscore[int(jid)]=int(jscore)

with open('./joke_similarities.csv', 'r') as f:
    reader=csv.reader(f)
    joke_simi=[tuple(float(n) for n in line.split(",")) for line in f]
    length=len(joke_simi)

userLines=None
with open('./jester-data-2.csv', 'r') as f:
    reader=csv.reader(f)
    userLines=list(reader)


predition={}
for j in xrange(1,1+num_jokes):
    if userscore[j]==99:
        simi_sum=1
        weighted_sum=0
        predit=0
        for k in xrange(0,length):
            if joke_simi[k][0]==j:
                if userscore[int(joke_simi[k][1])]!=99:
                    simi_sum+=abs(joke_simi[k][2])
                    weighted_sum+=joke_simi[k][2]*userscore[int(joke_simi[k][1])]
            elif joke_simi[k][1]==j:
                if userscore[int(joke_simi[k][0])]!=99:
                    simi_sum+=abs(joke_simi[k][2])
                    weighted_sum+=joke_simi[k][2]*userscore[int(joke_simi[k][0])]
        predit=weighted_sum/simi_sum
        predition[j]=float('%.4f'%predit)
predition=sorted(predition.items(), key = lambda x : x[1], reverse=True) 
pre=[]
for i in xrange(0,20):
    if len(pre)==10:
        break
    if predition[i][0] not in xrange(1,11):
        pre.append(predition[i][0])
predition=pre


print "<html>"
print "<head>"
print "<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />"
print "<meta name='description' content='Jokes Recommendation System'>"
print "<meta name='keywords' content='HTML,CSS,Python,JavaScript'>
print "<meta name='author' content='Yi-Nung Yeh'>"
print "<title>Jokes Recommendation App</title>"
print "<link href='https://fonts.googleapis.com/css?family=Lobster|Patua+One|Fredericka+the+Great' rel='stylesheet' type='text/css'>"
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css'>"
print "<link href='https://fonts.googleapis.com/css?family=Walter+Turncoat|Source+Sans+Pro' rel='stylesheet' type='text/css'>"
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css'>"
print "<style>"
print "#Header{"
print "width:100%;"
print "height:20%;"
print "text-align:center;"
print "line-height:280%;"
print "font-family: 'Lobster', cursive;"
print "font-size:200%;"
print "color:#fffaf3;"
print "font-weight:bold;"
print "background-color:#55a7ca;"
print "text-shadow: 5px 5px 0 #55a7ca, 7px 7px 0 #fffaf3;"
print "}"
print "#body{"
print "width:100%;"
print "height:50%;"
print "text-align:center;"
print "font-family: 'Source Sans Pro', sans-serif;"
print "font-size:80%;"
print "color:#000000;"
print "background-color:#fddf84;"
print "}"
print "#Footer{"
print "width:100%;"
print "height:10%;"
print "text-align:center;"
print "line-height:10%;"
print "font-size:100%;"
print "color:#fffaf3;"
print "font-weight:bold;"
print "background-color:#9cafb7;"
print "}"
print ".button {"
print "display: inline-block;"
print "background-color: #cac555; /* Green */"
print "border: none;"
print "color: white;"
print "padding: 1% 2%;"
print "width:5.075%;"
print "font-family: 'Source Sans Pro', sans-serif;"
print "text-align: center;"
print "text-decoration: none;"
print "font-weight:bold;"
print "display: inline-block;"
print "font-size: 100%;"
print "cursor: pointer;"
print "float: left;"
print "}"
print ".button:hover {    background-color: #979112;}"
print ".nonglory{color:white; font-weight:900; text-shadow: 5px 5px 0 #55a7ca, 7px 7px 0px #ffffff;}"
print ".glory{filter: glow(color:#ffffff, strength=1); color:white; font-weight:900; text-shadow: 1px 1px 5px #ffffff;}"
print ".glory2{filter: glow(color:#ffffff, strength=2); color:white; font-weight:900; text-shadow: 1px 1px 10px #ffffff;}"
print ".glory3{filter: glow(color:#ffffff, strength=3); color:white; font-weight:900; text-shadow: 1px 1px 15px #ffffff;}"
print ".glory4{filter: glow(color:#ffffff, strength=4); color:white; font-weight:900; text-shadow: 1px 1px 20px #ffffff;}"
print ".glory5{filter: glow(color:#ffffff, strength=5); color:white; font-weight:900; text-shadow: 1px 1px 25px #ffffff;}"
print ".glory6{filter: glow(color:#ffffff, strength=6); color:white; font-weight:900; text-shadow: 1px 1px 30px #ffffff;}"
print ".glory7{filter: glow(color:#ffffff, strength=7); color:white; font-weight:900; text-shadow: 1px 1px 35px #ffffff;}"
print ".glory8{filter: glow(color:#ffffff, strength=8); color:white; font-weight:900; text-shadow: 1px 1px 40px #ffffff;}"
print ".glory9{filter: glow(color:#ffffff, strength=9); color:white; font-weight:900; text-shadow: 1px 1px 45px #ffffff;}"
print "</style>"
print "<script language='javascript'>"
print "function reSize(){"
print "parent.document.all.frameid.height=0.7*document.body.scrollHeight;}" 
print "window.onload=reSize;"
print "</script>" 
print "</head>"
print "<body>"
print "<div id='Header'> <h1 id='title' class='nonglory'>Jokes Recommendation App</h1> </div>"
print "<div id='Body'>"
print "<a class='button' href='./index.html'>Index</a><a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[0])+".html' target='abc'>Joke 1</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[1])+".html' target='abc'>Joke 2</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[2])+".html' target='abc'>Joke 3</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[3])+".html' target='abc'>Joke 4</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[4])+".html' target='abc'>Joke 5</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[5])+".html' target='abc'>Joke 6</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[6])+".html' target='abc'>Joke 7</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[7])+".html' target='abc'>Joke 8</a> <a class='button' onclick='myFunction()' href='./jokes/init"+str(predition[8])+".html' target='abc'>Joke 9</a> <a class='button' onclick='myFunction()'  href='./jokes/init"+str(predition[9])+".html' target='abc'>Joke 10</a>"
print "<iframe frameborder='0' width='100%' src='./ind2.html' name='abc' id='frameid'></iframe>"
print "</div>"
print "<script language='javascript'>"
print "count=0;"
print "var myFunction=function(){"
print "console.log(count);"
print "count++;"
print "if(count==1) document.getElementById('title').className = 'glory';"
print "else if(count==2) document.getElementById('title').className = 'glory2';"
print "else if(count==3) document.getElementById('title').className = 'glory3';"
print "else if(count==4) document.getElementById('title').className = 'glory4';"
print "else if(count==5) document.getElementById('title').className = 'glory5';"
print "else if(count==6) document.getElementById('title').className = 'glory6';"
print "else if(count==7) document.getElementById('title').className = 'glory7';"
print "else if(count==8) document.getElementById('title').className = 'glory8';"
print "else document.getElementById('title').className = 'glory9';};"
print "</script>"
print "</body>"


