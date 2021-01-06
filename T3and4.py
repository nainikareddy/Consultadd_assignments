from functools import reduce

#1
list1 = ["one", 1.0, 7, 1+2j, 8.7, "twenty", 2, 4+3j, 5.6, "seventy two"]
#2
list2 = [1,2,3,4,5]
print(list2[1:3])

#3
print(sum(list2))
mutltipied = reduce(lambda x,y: x*y, list2)
print(mutltipied)
#4
print(min(list2))
print(max(list2))
#5
list3 = []
for elem in list2:
    if elem%2 == 1:
        list3.append(elem)
print(list3)
#6
list4 = []
for i in range(1,31):
    if i < 6 or i > 24:
        list4.append(i*i)
print(list4)
#7
list4[-1:] = list3
print(list4)
#8
a = {'a':10, 'b':20,}
b = {'c':6, 'd':3}
c = {**a,**b}
print(c)
#9
d = {k : k*k for k in range(1,6)}
print(d)
#L = [x for x in input("Enter multiple values\n").split(',')]
#print(L)
#print(tuple(L))
#T41
txt = "Hi there"
print(txt[::-1])
#2
#input_word = input("Type word here:")
#print("Number of Capital letters", sum(1 for c in input_word if c.isupper()),
 #                                      "Number of small letters:",sum(1 for c in input_word if c.islower()))

#3
def unique_list_elems(list):
    new_list = []
    for elem in list:
        if elem not in new_list:
            new_list.append(elem)
    print(new_list)
unique_list_elems([1,2,3,3,4,4,4,5])
#4
#Hyphen_sep = [x for x in input("Enter multiple hyphen separated strings\n").split('-')]
#Hyphen_sep.sort()
#print('-'.join(Hyphen_sep))
#5
string_input = input("Enter a string:")
print(string_input.upper())
#6
def sum_of_two():
    x = input("Enter number:")
    y = input("Enter number:")
    z = int(x)+int(y)
    print(z)
#sum_of_two()
#7
def max_len_string():
    x = input("Enter string 1:")
    y = input("Enter string 2:")
    if len(x)==len(y):
        print(x+'\n'+ y)
    else:
        print(max(x, y, key=len))


max_len_string()
def generate_tuples():
    t= [(x,x*x) for x in range(1,21)]
    print(t)
generate_tuples()
#9
def showNumbers(z):
    for i in range(z+1):
        if i%2 == 0:
            print(i,"EVEN")
        else:
            print(i, "ODD")
#showNumbers(4)
#10
result = list(filter(lambda x:x%2==0,range(1,21)))
#print(result)
#11
even_list = list(filter(lambda x:x%2==0,range(1,11)))
squared_list = list(map(lambda x: x*x , even_list))
print(squared_list)
#12
def divide_by(x,y):
    try:
        print(int(x)/int(y))
    except ZeroDivisionError:
        print("You cannot divide a number by 0")

#divide_by(4,9)
#13
tolist = [1,2,3,4,5]
print(str(tolist))
gd = reduce(lambda i,j:str(i)+str(j), tolist[:])
print(gd)

number_list = list(filter(lambda x: x%7==0 and x%3 != 0,range(1,40)))
#print(number_list)
#15
def toy(n):
    result = 1
    result = n*n
    return result

op = list(map(toy, [1,2,3,3,4]))
print(op)
#16 Returns 2 because the variable finally stores 2 in it
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
# F is not defined
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')