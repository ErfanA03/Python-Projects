#Functions Video
"""
mySentence = 'loves the color'


color_list = ['red','blue','green','pink','teal','black']

def getColor(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst


def getName():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name.lower() == 'sally':
            print('Welcome Sally, this is your personal ai assistant!')
        else:
            go = False
    lst = getColor(name)
    for i in lst:
        print(i)

        
getName()
"""


#Functions Challenge
"""
def getProduct(x,y):
    print(x * y)


getProduct(2,100)
"""


#Array Challenge
"""
myArr = [1,2,3,4,5]

for i in myArr:
    print(i)

Arr_of_twos = (1,2,2,6,2,9,1)
count_of_twos = Arr_of_twos.count(2)
print("Count of 2's:", count_of_twos)


disorg_Arr = [5,3,4,1,2]
disorg_Arr.sort()
print(disorg_Arr)
"""


#LAMBDA
"""
x = lambda a : a + 10

y = lambda x: x * x * x

print(x(5))
print(y(20))
"""


#String Format() Function
"""
fName = 'Erfan'
lName = 'Arsin'
print('Hello {} {}, ready to begin your training?'.format(fName,lName))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

x = format(8, 'b')
print(x)

print('binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}'.format(4))
"""

#Python Variables
"""
def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

getSum(2,4)

myAdd = getSum

myAdd(2,4)
"""
