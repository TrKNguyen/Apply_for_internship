import numpy
import pandas as pd
import array as arr

cnt = []
cntnw = 0
t = 0  
while(t<30):
   cnt.append(0) 
   t+=1

def add(x):
   x=ord(x)-ord('a')
   global cntnw
   cnt[x+1]+=1
   if (cnt[x+1]==1): 
      cntnw+=1

def ers(x):
   x=ord(x)-ord('a')
   global cntnw
   cnt[x+1]-=1
   if (cnt[x+1]==0): 
      cntnw-=1


s= input()
k= input()
k= ord(k) - ord('0')
n = len(s)


i = 1
lf = 0
while (lf < n and cntnw<=k ):
   add(s[lf])
   print(cntnw)
   lf+=1

res = lf - 1
while (i<n) :
   ers(s[i-1])
   while (lf<n and cntnw <=k):
      add(s[lf])
      lf+=1
   res = max(res,lf-2-i+1)
   i+=1

print (res) 


   
   



