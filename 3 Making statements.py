
#Q1
#writing Lists
print('Q1: writing Lists')
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print('1. Displaying the month name according to the number')
print('\tFirst Month: ',month[0])
print('\tsixth Month: ',month[5])
print('\ttwelvth Month: ',month[11])
# a multi-dimensional list of two elements, which themselves are lists of three elements each containing integer values
print('2. A multi-dimensional list of two elements, which themselves are lists of three elements each containing integer values and in 3D list display the values contained in two specific inner list elements')
XYZ_coords=[[1,2,3],[4,5,6],[7,8,9]]
# display the values contained in two specific inner list elements
print('\ttop left 0,0:\t\t', XYZ_coords[0][0])
print('\tcenter 1,1:\t\t', XYZ_coords[1][1])
print('\telement 1,2:\t\t', XYZ_coords[1][2])
print('\tbottom right 2,2:\t', XYZ_coords[2][2])
print('\ty,z coordinates of 1st point:\t\t', XYZ_coords[0][1:])
print('\tx, y, z coordinates of 1st point:\t', XYZ_coords[0])
# display just one character of a string value
print('3. Display just one character of a string values as month names in the list \'month\'')
print('\t3rd letter of 12th month: ',month[12-1],'- ',month[12-1][3-1])
print('\t1st letter of 5th month: ',month[5-1],'- ',month[5-1][1-1])
print('\n\n\n\n\n')







#Q2
#Manipulating Lists
print('Q2: Manipulating Lists\n Below is the list of 12 months.')
month1=['Jan','Feb','Mar','Apr','May','Jun']
month2='Jul','Aug','Sep','Oct','Nov','Dec'
num=[5,7,2,8,10]
print(month1)
print(month2)
print('No. of elements in month1 list: ',len(month1))
print('No. of elements in month2 list: ',len(month2))
print('No. of elements in 3rd month Mar list',len(month1[3-1]))
print('Number of times the \'Apr\' has come in list month1: ',month1.count('Apr'))
print('Number of times the \'Oct\' has come in list month2: ',month2.count('Oct'))
print(month1.index('Apr'))
month1.remove('Apr') #removing an object from the list
print(month1)
print(month2)
print('Index number of Jun: ',month1.index('Jun')) #knowing out an index number of an object from the list
month1.pop() #poping out a last object from the list
print(month1)
print(month2)
month1.insert(3,'Apr') #inserting an object in the list at a specified index
print(month1)
print(month2)
month1.append('Jun') #appending an object in the list at last
print(month1)
print(month2)
month2=list(month2) #converting a tuple into a list
month=month1+month2 # adding two lists
print('After adding two lists month1 and month2:',month,len(month))
print(month.index('Mar')) #finding out an index of an object
print(month[2]) # displaying an element presentat the index position 2
mun=num
print(mun)
mun.sort() #sorting out a numeric list
print(mun)
mun.reverse()
num.extend(mun)
print(num,mun,sep='*')
month1.append(month2) #appending list month2 to the list month1.
print('After appending two lists month2 to month1:',month1,len(month1))
print(month1)
print(month2)
print(month.count('Aug'))#counting the objects
print(month1.count('Aug'))
print(month1.count('Feb'))
print('\n\n\n\n\n')







#Q3
#Restricting Lists / TUPLES
print('Q3: Restricting Lists / TUPLES/ SETS')
tup1=('app','ball','cat')
tup2=('dog','ele')
alp=('A','B','C','D','E')
tup=tup1+tup2
print('1. Tuple is: ',tup, len(tup), type(tup))
tup=list(tup) #converting a tuple to a list
tup.remove('dog') #removing an item from a list or converted tuple
print('\t',tup)
tup=tuple(tup)
print('\t',tup)
print('\t',tup[0])#checking if the tuple displays for the wanted index and its value
set1={'app','ball','cat',10} #SET
set2={'cat','ele'}
print('2. Set1 is: ',set1,'\tSet1 length is:', len(set1), type(set1))
print('   Set2 is: ',set2,'\t\tSet2 length is:', len(set2), type(set2))
set1.add('dog')
set2.add('fro')
print('\t',set1,'\tSet1 length is:', len(set1), type(set1))
print('\t',set2,'\t\tSet2 length is:', len(set2), type(set2))
print('\tprint(set[0]) --> TypeError: \'set\' object is not subscriptable')
#print(set[0])--> print(set[0]) --> TypeError: 'set' object is not subscriptable
#add statements to seek two values in the set ie. checking is the search elements are present in the set or not
print('3. Check for \'cat\' in set1: ','cat'in set1)
print('   Check for \'cat\' in set2: ','cat'in set2)
print('   Check for \'ball\' in set1: ','ball'in set1)
print('   Check for \'ball\' in set2: ','ball'in set2)
# all common values found in both sets and other operations
print('4. Common To Both Sets:',set1.intersection(set2))
print('   Difference:set1-set2: ',set1.difference(set2))
print('   Difference:set2-set1: ',set2.difference(set1))
set2.discard('fro')
print('   Discarding element \'fro\' from set2:',set2)
set2.update('ice','joy')
set1.update('fro','kit')
print('   Adding some elements to set1',set1)
print('   Adding some elements to set2:',set2)
o=input('5. Enter a word: ')
def check(x):
    if x in set1:
       print('   in set1')
    elif x in set2:
       print('   in set2')
    else:
       print('   answer not detected thus wrong')
check(o)
print('\n\n\n\n\n')







#Q4
#Associating lists/ dictiionary
print('Q4: Associating lists/ dictionary')
dicti={2:'two',1:'one',3:'three','F':'four'}
print('dictiionary is: ',dicti)
# display a single value referenced by its key
print('1. Value corresponding to key-\'F\': ',dicti['F'])
#display all keys within the dictiionary
print('2. ',dicti.keys())
#Delete one pair from the dictiionary and add a replacement pair then display the new key:value contents
del dicti['F']
dicti[5]='five'
dicti[4]='four'
print('Edited dictiionary: ',dicti)
#search the dictiionary for a specific key and display the result of the search
print('3. Value corresponding to key-5: ',dicti[5])
#checking for some keys in dicti
print('4. checking for some keys in dicti')
print('   5 in dicti: ',5 in dicti)
print('  \'five\' in dicti','five' in dicti)
dicti1=dicti.copy() #copying the dictiionary using copy() method
dicti=dicti.clear() #clearing all the elements in the dictiionary named dicti
print(dicti)
del dicti #deleted dicti dictionary
print(dicti1)
skey=dicti1.keys()
sorted(skey)
print(dicti1)
print('\n\n\n\n\n')







#Q5
#If/ If Else/ Else if/ Elif Statement
print('Q5: If/ If Else/ Else if/ Elif Statement')
# initializing a variable with user input of an integer value
get=float(input('Enter obtained percentage to check grades(%): '))
def Grade(get):
   if get>80:
      print('Grade: A\tExcellent')
   elif get>60:
      print('Grade: B\tVery Good')
   elif get>40:
      print('Grade: C\tGood')
   elif get>20:
      print('Grade: D\tBad')
   else:
      print('Grade: E\tVery Bad')
   # test the variable again using two expressions and display a response only upon success
def remark(get):
   if get==100:
      print('Award')
   elif get==0:
      print('Fail')
   else:
      print('Pass')
Grade(get)
remark(get)
print('\n\n\n\n\n')







#Q6
#While Loop Fibonacci Series
print('Q6: While Loop')
print('Fabonacci Series: ')
a=0
b=1
def met1(a,b):
   print('   ',a)
   while b<200:
      print('   ',b)
      c=b
      b+=a
      a=c
print('1. c=b\n   b+=a\n   a=c')
met1(a,b)
def met2(a,b):
   print('   ',a)
   while b<100:
      print('   ',b)
      a, b=b, a+b
print('2. a, b=b, a+b\tOne-Liner')
met2(a,b)
print('\n\n\n\n\n')







#Q7
#Nested While Loop: Tables of 2
print('Q7: Nested While Loop- Inner loop in Outer loop: ')
#initializing a “counter” variable and define an outer loop using that variable in its test expression
print('   initialize a “counter” variable and define an outer loop using that variable in its test expression')
i=1
while i<6:
   print('   Outer loop iteration: ',i)
   i+=1
   j=1
   while j<4:
      print('\t  Inner Loop Iteration: ',j)
      j += 1
print('4. Table of 2 for numbers below 100: :')
i=0
for i in range(10):
   j=0
   while  j<10:
      if (i*10+j)%2==0:
         print('   ',i*10+j)
      j+=1
   pass
   i+=1
print('5. Table of n for numbers below 100: :')
n=int(input('   Table of: '))
i=0
for i in range(10):
   j=0
   while  j<10:
      if (i*10+j)%n==0:
         print('   ',i*10+j)
      j+=1
   pass
   i+=1
print('\n\n\n\n\n')







#Q8
#For Loop: Looping over items
print('Q8: For Loop- Looping over items')
#initialize a list, a tuple, and a dictionary
char_list=['A','B','C']
fruit_tuple=('Apple','Banana','Cherry')
animal_set={'Ant','Bunny','Cat','Dog'}
dic={'name':'Mike','ref':'Python','sys':'Win'}
# display all list element values
print('1. ',char_list,'\n   Elements in char_list: ')
for x in char_list:
   print('   ',x)
#display list elements with their relative index number using enumerate()
print('2. Enumerated Elements in char_list: ')
for y in enumerate(char_list):
   print('   ',y)
#display all list and tuple elements using zip()
print('3. Zipped Elements in char_list and fruit_tuple simultaneously: \n   Tuple is: ',fruit_tuple)
for z in zip(char_list,fruit_tuple):
   print('   ',z)
print('4. Zipped Elements in char_list, fruit_tuple and animal_set simultaneously: \n   Tuple is: ',fruit_tuple,'\n   Set is: ',animal_set)
for z in zip(char_list,fruit_tuple,animal_set):
   print('   ',z)
# display all dictionary key names and associated element values
print('5. Dictionary is:',dic,'\n   Paired dictionary key names and associated element values:')
print('   ',dic.items())
for key, value in dic.items():
   print('   ',key,'=',value)
print('6. Only keys in dictionary: ')
for x in dic.keys():
   print('   ',x)
print('7. Only values in dictionary: ')
for x in dic.keys():
   print('   ',dic[x])
   print('\n\n\n\n\n')







#Q9
#For Loop: Breaking out of loops
print('Q9: For Loop- Breaking out of loops')
#statement creating a loop that iterates three times
for aa in range(3):
   for bb in range(3):
      print('Counter for outer loop (aa)= ',aa,'\tCounter for inner loop (bb)= ',bb)
      if aa==1 and bb==1:
         print('break at aa=1 and bb=1. Thus the next statement for \'Hi\' will not be executed')
         break
      print('Hi')
