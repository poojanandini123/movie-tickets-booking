d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
s="MXVII"
res=0
lastdigit=0
for ch in s[::-1]:
    if(d[ch]>=lastdigit):
       res+= d[ch]
       lastdigit=d[ch]
    else:
        res-=d[ch]
print(res)           

d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
s="MXVII"
res=0
lastdigit=0
for ch in s:
    if(d[ch]<=lastdigit):
       res+= d[ch]
       lastdigit=d[ch]
    else:
        res-=lastdigit
        res+=d[ch]-lastdigit
print(res)           


d={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
s="MCXLIII"
res=0
lastdigit=10000
for ch in s:
    if(d[ch]<=lastdigit):
       res+= d[ch]
       lastdigit=d[ch]
    else:
        res-=lastdigit
        res+=d[ch]-lastdigit
print(res)           