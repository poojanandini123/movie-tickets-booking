#map function
#perform multiple operations
#short code,clear
a=[1,2,2,3]
def name(values):
    return values*2
print(list(map(name,a)))

#functions  are two types
#normal functions
def add(a,b):
 return a+b
result=add(10,20)
print(result)
#void functions
def sri():
   print("i am sri")
sri()

# string comression


data="aabbbcccddaae" 
data_compression="" #to store results
d={}                  #to know current frequency
n=len(data)
for i in range(len(data)):
    key=data[i] #current character
    if(d.get(key)):
       d[key]+=1
    else:
       if(i!=0): 
           data_compression+=data[i-1]+str(d[data[i-1]])
       d={}
       d[key]=1
data_compression+=data[n-1]+str(d[data[n-1]])
print(data_compression)


#patterns
for i in range (5):
    starts=""
    for j in range (5):
        starts=starts+ "* "
    print(starts)


# selection sort 
arr=[4,2,3,1,0,9,8]
n=len(arr)
print(n)
for i in range(0,n-1):
   for j in range(i+1,n):
      if(arr[i]>arr[j]):
         arr[i],arr[j]=arr[j],arr[i]
print(arr)         

a=[1,2,3,9,8,7]
a.sort()
print(a)

#bubble sort
age=[24,19,3,22,18,13,4,11,2,5]
n=len(age)
is_swap=True
while(is_swap):
   is_swap=False
   for i in range(n-1):
      if(age[i]>age[i+1]):
         is_swap=True
         age[i],age[i+1]=age[i+1],age[i]
print(age)

#generator function
def generater():
   for i in range(1,5):
      yield i
gen=generater()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))