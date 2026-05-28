
#scond largest program
a=[1,2,3,4]
maximum=0
sec_max=0
for item in a:
    if(item>maximum):
        sec_max=maximum
        maximum=item
    elif(item>sec_max):
        sec_max=item
print(maximum,sec_max)

#prime number
n=10
is_prime=True
for i in range(2,n):
    if(n%i==0):
       is_prime=False
    if(is_prime):
        print("this is prime")
    else:
        print("this is not prime")

#secon approch
def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
            return True
res=is_prime(96)
if(res):
    print("this is prime")
else:
    print("this is not prime")


#third approch
def is_prime(n):
    for i in range(2,n//2):# or fourth is    [ for i in range(2, int(math.sqrt(n)))]
        if(n%i==0):
            return False
            return True
res=is_prime(96)
if(res):
    print("this is prime")
else:
    print("this is not prime")

#palindrome program
text="pooja"
if text==text[::-1]:
    print("this is palindrome")
else:
    print("this is not palindrome")

#even or odd
    num=9
    if(num%2==0):
        print("this is even")
    else:
        print("this is not even")


#factorial program
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
print(factorial(8))


#armstrong 
num=121
temp=num
rev=0
while(num>0):
    rev=rev+(num%10)**(len(str(temp)))
    num=num//10
if(rev==temp):
    print("amstrong")
else:
    print("not amstrong")


#largest number
a=[1,2,3,45]
maximum=0
for item in a:
    if(item>maximum):
        maximum=item
print(maximum)


#leap  year
year=2005
if(year%400==0)or(year%4==0 and year%100!=0):
    print("this is leaf year" )
else:
    print("this is not leaf year")

#fibnocci program
array=[0,1,2,3]
def fibonacci(n):
    if(n==10):
        return 
    a.append(array[n-1]+array[n-2])
    fibonacci(n+1)
    print(array)


# find out the unique values
a=[1,2,3,3,3]
res=0
for each in a:
    res==each
print(each)


# reverse problem
N=123455
rev=" "
while (N>0):
 rev=rev+str(N%10)
N=N//10
print(rev)


#count,sum problem
N=12346587
sum=0
count=0
while(N>0):
     sum=sum+N%10
     count=count+1
     print(sum)
     print(count)

# nested for loop
for i in range (2,8,1):
     for j in range (11,9,-1):
          print(i,j)  
# single loop
for i in range(18,8,-2):
     print(i)             


#Reversed string    
s="sri pasupuleti"
print("reversed string is:",s[::-1])

#count vowels
s="ahsjadhihjdedsao"
count=0
for ch in s:
  if ch in "aeiouAEIOU":
    count += 1
print("vowels is:",count)

#palindrome
s="madam"
if s==s[::-1]:
  print("palindrome")
else:
  print("not a palindrome")

#spaces removing
s="sri vidya pasupuleti"
result=s.replace(" ","")
print("after removing spaces:",result)

#count uppercase and lowercase words
s="Sri VIdya pasuPuleti"
upper=0
lower=0
for ch in s:
    if ch.isupper():
        upper +=1
    elif ch.islower():
        lower +=1
print("uppercase:",upper)
print("lowercase:",lower)

#count words in a string
s="I am searching for a job"
words=s.split()
print("total words:",len(words))

#reverse the words in a sentence#
s="hii this is sri"
words=s.split()
for word in words:
    print(word[::-1],end=" ")