print("P\tV\tn\tR\tT")
print("______________________________________")
P,V,n,R,T=2,8.314,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s"%(P,V,n,R,T)
print(tmpstr)
P,V,n,R,T=8.314,2,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s"%(P,V,n,R,T)
print(tmpstr)
P,V,n,R,T=1,16.628,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s\n"%(P,V,n,R,T)
P,V,n,R,T=2,8.314,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s"%(P,V,n,R,T)
print(tmpstr)
P,V,n,R,T=8.314,2,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s"%(P,V,n,R,T)
print(tmpstr)
P,V,n,R,T=1,16.628,0.141,8.314,14.142
tmpstr="%s\t%s\t%s\t%s\t%s\n"%(P,V,n,R,T)
print(tmpstr)
print("Ihfaz, print \"Hello world\".")
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

first_name='Fish'#input("Enter first name:")
last_name='Cakes'#input("Enter last name:")
formatted_str="You are %s %s."%(first_name,last_name)


#strnums
r=15548
pi=3.14159265358
area=pi*r**2
formatted_str="The area of circle with a radius %d is %4.4f."%(r,area)
fmstr="The area of circle with a radius {} is {:.4f}.".format(r,area) 
#its better to deal with strings in need of formatting, such as padded text or decimals, using .format or %s
fstr=f"The area of circle with a radius {r} is {area}."
print(formatted_str)
print(fmstr)
print(fstr)
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)

ryzen="cake"
fmt = "babes i want %s for breakfast"%(ryzen)
print(fmt)

a, b=40.000000, 3.000000
print(f"babe it's {a/b:.1f} degress outside")

language='Python'
a,s,d,f,g,h=language
a=language[-6]
print(a)
a=language[-5]
print(a)
a=language[-4]
print(a)
a=language[-3]
print(a)
a=language[-2]
print(a)
a=language[-1]
print(a)
challenge="this is a test"
print(challenge[3::-1].capitalize())

str=input("tell me a non-numeric fact: ")
if str.isnumeric():
    print("not cool dude")
else:
    print(f"feels nice to know that {str}")
challenge = '010'
print(challenge.isdigit())   # True


#1
print('Thirty', 'Days', 'Of', 'Python')
#2 lol
#6
a='sfd'
print(a.upper())
#8
str='Coding For All'
print(str.capitalize())
print(str.title())
#9
a=str.index(' ')
print(str[:a:1])
#10
str2='Coding'
i=str.find('Coding')
j=len(str2)
print(str[i:j:1])
##11
print(str.replace(str[i:j:1],'Python'))
#12
str3='Python for Everyone'
print(str3.replace(' Everyone', ''),'All')
#13
print(str.split(' '))
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
#15
print(str[0])
#16,17
#18,19
str297='Python For Everyone'.title()
a='a'
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
a=chr(ord(a)+1)
str297=str297.replace(a,'')
str297=str297.replace(' ','')
print(str297)
#20
#24
sntnc='You cannot end a sentence with because because is a conjunction'
print(sntnc.rindex('because'))
#25
sntnc='You cannot end a sentence with because because because is not a conjunction'
target='because because because'
list_t=target.split()
i=sntnc.index(list_t[0])
last=list_t[len(list_t)-1]
j=sntnc.rindex(last)
j+=len(last)
print(sntnc[i:j:])
#26
print(sntnc.index('because'))
#28,29
print('Coding For All'.find('Coding')==0)
print('Coding For All'.find('coding')==0)
#30
sat='   Coding For All      '
print(' '.join(sat.split()))
#31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
#32
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print('Name    \tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
#35
radius = 10
r_prompt='radius = {}'.format(radius)
area = 3.14*radius**2
area_prompt='area = 3.14 * radius ** 2'
print(r_prompt)
print(area_prompt)
print('The area of a circle with radius {} is {} meters square.'.format(radius, (int)(area)))
#36
a,b=8,6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,(a/b)))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))