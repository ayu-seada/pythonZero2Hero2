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
basket.insert(5,100)
print(basket)