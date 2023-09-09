# String Challenges
"""
fname = 'Erfan';
print(fname);

multi_line = \"""This is a multiline string
and it allows you to break lines without having to use an escape character.
All you gotta do is use triple quotation marks (single or double) at the
beginning and end of your strings.\""";
print(multi_line);

list = [0,1,2,3,4,5,6,7,8,9,10];
my_slice = slice(2, 10, 2);
result = list[my_slice];
print(result);

list_length = len(list);
print(list_length);

fullname = '       Erfan Arsin           ';
print(fullname.strip());

lowercase = 'abcdefg';
uppercase = lowercase.upper();
print(uppercase);

text = "Hello, World!";
print('W' in text);
print('w' in text);

greeting1 = 'Hello';
greeting2 = 'World!';
greeting3 = greeting1 + ' ' + greeting2;
print(greeting3);

print("Hello\nWorld");
print("Hello\tWorld");
"""

# Operator Challenges
"""
sum = 1 + 1;

sum += 3;
print(sum);

print(sum != 5);

print(True and False);

x = [1,2];
y = [1,2];
z = x;
print(x is y);
print(x is z);

list1 = [1,2,3,4,5];
print(4 in list1);

a = 5;  # Binary: 0101
b = 3;  # Binary: 0011
result = a & b;  # Binary: 0001
print(result);
"""

#Tuples
"""
animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox')

listofAnimals = list(animal)
print(listofAnimals)

listofAnimals.append("honey badger")
print(listofAnimals)

myString = "Python is such a cool language!"
newString = list(myString)
print(newString)

newString = myString.split(" ")
print(newString)
"""

#Lists Challenge
"""
myList = [5,4,3,2,1]

for i in myList:
    print(i)

myList.append(0)

copiedList = myList.copy()
print(copiedList)

#List concatenation
list1 = [1,2,3]
list2 = [4,5,6]
concatenatedList = list1 + list2
print(concatenatedList)

#The list extend() method appends the elements of one list to another list:
list3 = [7,8,9]
list4 = [10,11,12]
list3.extend(list4)
print(list3)

my_list = [1,2,3,4,5]
my_list.reverse()
print(my_list)
"""

#Tuples Challenge
"""
myTuple = (1,2,3,2,4,5,2)
print(myTuple)

for x in myTuple:
    print(x)

countofElement = myTuple.count(2)
print(countofElement)
"""

#Sets Challenge
"""
myPets = {'dog', 'cat', 'hamster', 'cat', 'parrot'}

myPets.add('monkey')
myPets.remove('cat')
print(myPets)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
difference_set = set1.difference(set2)

print("Elements present in set1 but not in set2:", difference_set)
"""

#Dictionary Video
"""
myDictionary = {'index': 1, 'index2': 2, 'index3': 3}
print(myDictionary)

print(myDictionary['index2'])

dic_users = {'em_123': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'},
             'em_456': {'fname': 'Mary', 'lname': 'Jones', 'phone': '098-765-4321'}}

print(dic_users['em_123'])

print(dic_users['em_456']['phone'])

print('User: {} {}\nPhone: {}'.format(dic_users['em_456']['fname'],
                                      dic_users['em_456']['lname'],
                                      dic_users['em_456']['phone']))
"""

#Dictionary Challenge
"""
myDictionary = {"fname": "Erfan", "lname": "Arsin", "phone": "123-456-7890"}
print(myDictionary)

myPhoneNum = myDictionary.get('fname')
print(myPhoneNum)

myDictionary['fname'] = 'Bob'
print(myDictionary['fname'])

myDictionary['email'] = 'BobArsin@gmail.com'
print(myDictionary)

Employees = {'emp_1': {'fname': 'Darrell', 'lname': 'Morgan', 'phone': '801-382-2831'},
             'emp_2': {'fname': 'Emily', 'lname': 'Bingham', 'phone': '918-283-3019'} }

keys = ['key1', 'key2', 'key3']
default_value = 0

my_dict = dict.fromkeys(keys, default_value)

print(my_dict)
"""

fruits = ['banana', 'apple', 'orange', 'grapes']
