from random import randint

products = ['milk','bread','tomato','cucumber','salt']
dict = {'milk':[70,4], 'bread':[80,2], 'tomato':[120,5], 'cucumber':[130,5], 'salt':[60,1]}
print(dict)
product = products[randint(0, len(products)-1)]
print(product)
dict.pop(product)
print (dict)
