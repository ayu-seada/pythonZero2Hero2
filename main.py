#Lists
li = [1,2,3,4,4,4,5,6,6,6]
li2= ['a','b','c','d']
li3 = [1,2,'a',True]
amazon_cart = ['notebooks','sunglasses','videogames','toys','grapes']
#printed_number=input('introduce a number from 0 to 2')
#print(amazon_cart[int(printed_number)])
print(amazon_cart[2])

#List Slicing
amazon_cart[0]='laptop'
print(amazon_cart[0::2])

#Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print( matrix[1][2])

##List Methods
basket= [1,2,3,4,5]
print(len(basket))
##new_list = basket.append(100)
##print(new_list)
print(basket)
#############################
#basket.insert(0,100)
#print(basket)
#basket.extend([100,101])
#print(basket)
# basket.pop(3)
# basket.remove(3)
# basket.clear()
# print(basket)
print(basket.index(2))
print(1 in basket)
print(basket.count(1))
basket_2= ['a','x','c','h','o','2']
basket_2.sort()
print(f'{basket_2}')
basket_2.reverse()
print(basket_2)
# print(list(range(1,100)))
sentence=' '
new_sentence=sentence.join(['hi','my','name','is','goku'])
print(new_sentence)
##List Unpacking
a,b,c, *other,d=[1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)
print(other)
print(d)
##Dictionary
dictionary = {
    'a': 1,
    'b': 2
}
print(dictionary['b'])
my_list =[
    {
    'a': [1,2,3],
    'b': ['a','b','c'],
    'c': [6,7,8]
}, {
    'a': [1,2,3],
    'b': ['a','h','t'],
    'c': [9,0,4]
 }
]

print(my_list[0].get('o'))
print(my_list[1]['b'][2])
print('g' in my_list[0])
user = dict(name = 'Jhon')
print(user)
user_2={
    'basket':[1,2,3],
    'greet': 'hello',
    'age' : 20
}
print('hello' in user_2.values())
print('age' in user_2.keys())
print(user_2.items())
print(user_2.update({'age': 55}))
print(user_2)
# Tuple ---> list that doesn't change
my_tuple = (1,2,3,4,5,6)
# my_tuple[1]='z'
##print(int(input('write what u want')) in my_tuple)
print(my_tuple.count(2))
print(my_tuple.index(2))
print(len(my_tuple))
#Set
my_set = {1,2,3,4,5}
my_set2={6,2,4,5,0}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# print(set(li))
# print(my_set.difference(my_set2))
# my_set.discard(2)
# print(my_set)
# my_set.difference_update(my_set2)
# print(my_set)
# print(my_set.intersection(my_set2))
#print(my_set & my_set2)
# print(my_set.isdisjoint(my_set2))
# print(my_set.union(my_set2))
# print(my_set | my_set2)
#issubset
#issuperset