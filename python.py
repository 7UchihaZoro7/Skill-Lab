import keyword
print(keyword.kwlist)

a=None

print(a)

print(type(a))

print(bool(a))

print(bool(0.0))

print(bool(1.8))

print(int())

a=3j+5

print(a)

a="Happy Father's Day"

print(a)

print(a[6])

a=10

print(a)

a={10,2,3,5j,False,'hi',(1,2)}

print(a)

'''a={'a':[10,20,30],'b':40}
print(a['a'][-2])'''

a="Good Morning"

print(a[5:12])

print(a[-8:-2])

print(a[1:7:2])

print(a[1:5+1:2])

print(a[8:6:-1])

a=eval(input("Enter a number: "))
print(a,type(a))

if a%2==0:
    
    print("Even")
else:
    print("Odd")

l=eval(input("Enter the list: "))

if len(l)==5:
    print("yep")
else:
    print("nope")

ch=input("Enter a character: ")

if "A"<=ch<="Z":
    print("Uppercase Alphabet")
elif "a"<=ch<="z":
    print("Lowercase Alphabet")
else:
    print("Not an Alphabet")

un=input("Enter username: ")
pwd=input("Enter password: ")
if un=="Zoro":
    print("Username is correct")
else:
    print("Username is incorrect")
    if pwd=="Zoro@123":
        print("Password is correct")
    else:
        print("Password is incorrect")

i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1

n=int(input("Enter a number: "))
rev=0

while n>0:
    ld=n%10
    n=n//10

    print(rev)

    s=input("Enter:")
    rev=''
    for i in s:
        rev=i+rev

    print(rev)

    for i in range(1,6):
        for j in range(1,i+1):
            if i==j:
                print(i,end=' ')
            else:
                print(j,end=' ')
        print()

a='Happy Birthday'
print(a[-4:-7:-1])

def convert(s,out):
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
            print(out)
            return out
        print(convert())
        class college:
            def __init__(self):
                self.usn=self.usn
                def display(self):
                    print(self.name,self.phno,self.usn)

                    s1=college('Amit','1234567890','1RV17CS001')
                    s2=college('Rohit','0987654321','1RV17CS002')
                    s1.display()
                    s2.display()