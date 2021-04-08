#Lists
li = [1,2,3,4]
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
my_list = [
{
    'a': [1,2,3],
    'b': ['a','b','c'],
    'c': [6,7,8]
},
{
    'a': [1,2,3],
    'b': ['a','h','t'],
    'c': [9,0,4]
}
    ]
print(my_list[1]['b'][2])
print(my_list.get('a'))
