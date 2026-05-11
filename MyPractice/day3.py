# x  = 7#0111
# x ^= 3#0011
# print(x)
# a=5+12j
# b=3+4j
# print(a*b)
# print(len('solve')>len('forksrgg'))

# print('z' in 'Asabeneh')
# print('coding' in 'coding for all')
# print(4 is 2*2)

#exercises
#1
age=23
#2
height=5.5
#3
s=3+4j
#4
b=float(input("Enter base: "))
h=float(input("Enter height: "))
area=0.5*h*b
print("area of circle:", area)
#5
a=(float)(input("Enter side, a:"))
b=(float)(input("Enter side, b:"))
c=(float)(input("Enter side, c:"))
perim=2*(a+b+c)
print("Perimeter:",perim)
#6
a=(float)(input("Enter side, length:"))
b=(float)(input("Enter side, height:"))
perim=2*(a+b)
print("Perimeter:",perim)
#7
r=(float)(input("Enter radius:"))
pi=3.1416
area=pi*(r**2)
print("area is:",area)
#8
x1, x2 = 3, 4
y1, y2 = 2*x1-2, 2*x2-2
m = (y2-y1) / (x2-x1)
print("slope:",m)
#9
x1, x2 = 2, 6
y1, y2 = 2, 10
m = (y2-y1) / (x2-x1)
ed= ((x1-x2)**2+(y1-y2)**2) ** 0.5
print("slope:",m)
print("ed:",ed)
#10---->slopes are same
#11--->boring
#12
print(len('python')>len('dragon'))
#13
print("on is in both python and dragon:", 'on' in 'python' and 'on' in 'dragon')
#14
sentence= "I hope this course is not full of jargon"
print("Use in operator to check if jargon is in the sentence.",'jargon' in sentence)
#15--->go home
#16
length=len('python')
l1=(float)(length)
print("float length:",l1)
l2=(str)(length)
print("str length:",l2)
#17
x=(int)(input("Enter number:"))
even= x%2 is 0
odd= x%2 is 1
print("x is odd:",odd)
print("x is even",even)
#18
print(7 // 3 is (int)(2.7))
#19
print(type('10') is type(10))
#20
print((int)(9.8) == 10)
#21
hours=(int)(input("Enter hours:"))
r=(int)(input("Enter rate per hour:"))
print("Your weekly earning is:",hours*r)
#22
y=(int)(input("Enter number of years you have lived:"))
s=31536000*y
print("You have lived for",s,"years")
#23
x=0
x+=1
print(x, x**0, x**1, x**2, x**3)
x+=1
print(x, x**0, x**1, x**2, x**3)
x+=1
print(x, x**0, x**1, x**2, x**3)
x+=1
print(x, x**0, x**1, x**2, x**3)
x+=1
print(x, x**0, x**1, x**2, x**3)