#dictionaries 
d={'name':"lakshmi",'age':"26"}
print(type(d))
#adding into dictionreies
d={'a':45,'b':67}
d['c']=90#adding
d['b']=86#update
d.pop('a')#delete
#2 nd approchrr=[1,2,3,4,5,5,6,6,9,8,7,7]
d={}
for item in arr:
    id(d.get(item)):
    d[item]+=1
else:
    d[item]=1
    unique_values=[]
    duplicate_values=[]
    for each in d:
        if(d[each]==1):
            unique_values.append(each)
        else: 
            duplicate_values.append(each)
d.get('a')#values to get
d.update({'d':98,'e':56})#update
print(d.keys())
print(d.values())
print(d.items())
print(d)



# unique values ^ duplicate values
arr=[1,1,2,3,4,4,5,5,]
d={}
for item in arr:
    if(d.get(item)):
    d[item]+=1
else:
    d[item]=1
    unique_values=[]
    duplicate_values=[]
    for each in d:
        if(d[each]==1):
            unique_values.append(each)
        else: 
            duplicate_values.append(each) 

#tuples      

a=(1,2,3,4,5)
num=a.count(2)
print(num)
id=a.index(3)
print(id)