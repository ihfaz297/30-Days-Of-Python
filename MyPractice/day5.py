# fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
# animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
# web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
# countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# # Print the lists and its length
# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print('Vegetables:', vegetables)
# print('Number of vegetables:', len(vegetables))
# print('Animal products:',animal_products)
# print('Number of animal products:', len(animal_products))
# print('Web technologies:', web_techs)
# print('Number of web technologies:', len(web_techs))
# print('Countries:', countries)
# print('Number of countries:', len(countries))

# lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]
# print(lst[3]['country'])

# port=['lazy', 'asbestos', 'soccer']
# a,b,c=port
# print(a,b,c)
# first_item, *rest = port
# print(rest)

# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr) 
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)
# print(countries[-3:])
# print('Germany' in countries)
# countries.append('England')
# print(countries)

# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[1]
# print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
# del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
# print(fruits)       # ['orange', 'lime']
# del fruits
# #print(fruits)       # This should give: NameError: name 'fruits' is not defined

# negnum, zero, posnum=[-3,-2,-1], [0], [1,2,3]
# negnum.extend(zero)
# negnum.extend(posnum)
# print(negnum)
# negnum.pop()
# negnum.pop()
# negnum.pop()
# negnum.pop()
# negnum.pop()
# negnum.pop()
# negnum.pop()
# negnum.append('-3')
# negnum.pop()
# negnum.append(-3)
# negnum.append(-2)
# print(negnum)
#LEVEL1
#1
emptylist=list()
#2
lst=[3,3,22,5,1]
#3
print(len(lst))
#4
first_item, *middle, last_item=lst
#5
#6,7,8,9
str='Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon'
str=str.replace(' and',',')
it_companies=str.split(', ')
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[len(it_companies)-1])
#10,11
it_companies[0]='Meta'
print(it_companies)
#12
it_companies.append('Netflix')
it_companies.insert(len(it_companies)//2,'Netflix')
#13
str1=it_companies[0]
str1=str1.capitalize()
a=str1[0]
str1=str1.swapcase()
str1=a+str1[1:]
it_companies[0]=str1
print(it_companies[0])
#14
print('#;&nbsp; '.join(it_companies))
#15
print('Amazon' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
it_companies.reverse()
print(it_companies[0:3])
#19
print(it_companies[-3:])
#20
print(it_companies[(len(it_companies)-1)//2:(len(it_companies)+2)//2])
#21
del it_companies[0]
print(it_companies)
#22
del it_companies[len(it_companies)//2]
print(it_companies)
#23
del it_companies[len(it_companies)-1]
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#print(it_companies)
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
#27
full_stack=front_end.copy()
print(full_stack)
a=full_stack.index('Redux')
full_stack.insert(a+1, 'Python')
full_stack.insert(a+2, 'SQL')
print(full_stack)

#LEVEL2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age=ages[0]
max_age=ages[len(ages)-1]
ages.append(min_age)
ages.append(max_age)
ages.sort()  # ensure list is sorted after appending min and max
print(ages)
median=(ages[(len(ages)-1)//2]+ages[len(ages)//2])/2
print(median)
sum_ages=sum(ages)
avg_age=sum_ages/len(ages)
print(avg_age)
print('Range of ages:',max_age-min_age)
min_diff=abs(min_age-avg_age)
max_diff=abs(max_age-avg_age)
print('Average age is far from maximum age:', max_diff>min_diff)
print('Average age is far from minimum age:', min_diff>max_diff)
#1
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print(countries[(len(countries)-1)//2:(len(countries)+2)//2])
#2
l1=countries[0:(len(countries)+1)//2]
l2=countries[(len(countries)+1)//2:]
print(l1)
print(l2)
#3
asian, soviet, west, *scandic= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic)