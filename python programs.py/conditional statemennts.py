#conditional statements:
#if,else,elif,match(switch)
age=18
if age>=18:
    print("your are eligible to vote")


num=9
if num % 2==0:
    print("even number")
else:
    print("odd number")


x=1
if x>5:
    print("equal")
else:
    print("not equal")

marks=9
if marks>=9:
    print("pass a")
elif marks>=8:
    print("pass b")
elif marks>=6: 
    print("pass c")  
else:
    print("fail")  

day=3
match day:
    case 1:
        print("mon")
    case 2:
        print("tue")
    case 3:
        print("wed")
    case 7:
        print("invalid")


