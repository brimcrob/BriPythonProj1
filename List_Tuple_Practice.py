'''''
fruits = ['apple', 'pear']
print(fruits)
fruits.append('strawberry')
print(fruits)
'''
'''''
fruits = ['apple', 'pear', 'strawberry']
fruits[1] = 'blueberry'
print(fruits)
'''''


'''
for fruit in fruits:
    print(fruit)
'''
#below is good way to find something in list if you know the object and the size of the list
fruits = ['apples', 'pears', 'strawberry', 3, 8, 10]
for x in range(0, 6):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')




